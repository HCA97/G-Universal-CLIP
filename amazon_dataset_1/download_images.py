import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import csv
import socket

import pandas as pd
import cv2
import tqdm

# timeout after 15second
socket.setdefaulttimeout(15)


# PARAMETERS
csv_root = 'amazon_categories_clean'
img_root = 'images'
n_workers = 5
n_products = 1500
save_path = f'amazon_data_set_sample_{n_products}.csv'
files = [
    'Cell_Phones_and_Accessories.csv',
    'Office_Products.csv',
    'All_Beauty.csv',
    'Clothing_Shoes_and_Jewelry.csv',
    'AMAZON_FASHION.csv',
    'Luxury_Beauty.csv',
    'Sports_and_Outdoors.csv'
]

def get_product_metadata() -> pd.DataFrame:
    df = pd.concat([pd.read_csv(os.path.join(csv_root, f)) for f in files])
    df['#imgs'] = df['img_urls'].apply(lambda x: len(x.split(' ')))

    # some values
    print(f"#products {len(df)}, #ids {df['id'].nunique()}, #img_urls {sum(df['#imgs'])}, avg img per id {sum(df['#imgs'])/df['id'].nunique()}")

    return df

def download_image(url: str) -> None:
    f_name = url.split('/')[-1]
    f_path = f'{img_root}/{f_name}'
    if not os.path.exists(f_path):
        try:
            urllib.request.urlretrieve(url, f_path)
            # check if img loadded succesfully
            img = cv2.imread(f_path)
            if img is None:
                print(f'Failed to read the {f_path} probably there was error when we are downloading. Deleting the image.')
                os.remove(f_path)
        except Exception as e:
            print(e)

def download_images(df: pd.DataFrame) -> None:
    os.makedirs(img_root, exist_ok=True)

    with ThreadPoolExecutor(n_workers) as p:
        jobs = []
        for _, row in tqdm.tqdm(df.iterrows()):
            img_urls = row['img_urls'].split(' ')
            for img_url in img_urls:
                jobs.append(p.submit(download_image, img_url))

        for job in tqdm.tqdm(jobs):
            job.result()
    
if __name__ == '__main__':


    df = get_product_metadata()
    # get 10k products images
    df_sample = df.sample(n=n_products)
    download_images(df_sample)

    # transform the df_sample so we can use it for training
    new_df = []
    for _, row in df_sample.iterrows():
        p_id = row['id']
        for img_url in row['img_urls'].split(' '):
            f_name = img_url.split('/')[-1]
            f_path = f'{img_root}/{f_name}'
            if os.path.exists(f_path):
                new_df.append({
                    'id': p_id,
                    'path': f_path
                })

    with open(save_path, 'w', encoding='utf8', newline='') as f:
        dict_writer = csv.DictWriter(f, ['id', 'path'])
        dict_writer.writeheader()
        dict_writer.writerows(new_df)