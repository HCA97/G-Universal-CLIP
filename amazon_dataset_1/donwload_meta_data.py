import os
import json
import gzip
import csv
from multiprocessing import Pool

from tqdm import tqdm



def create_duplicated_products(duplicated_products_txt: str) -> dict:
    print('Processing the duplicated products...')
    duplicated_products = {}
    with open(duplicated_products_txt) as f:
        for line in  tqdm(f):
            product_ids = line.strip().split(' ')
            for id in product_ids:
                duplicated_products[id] = product_ids[0]
    return duplicated_products


raw_data_folder = 'amazon_categories'
clean_data_folder = 'amazon_categories_clean'
duplicated_products = create_duplicated_products('duplicates.txt')
threshold = 4

def download_metadata(amazon_category: str):
    amazon_category = amazon_category.replace(' ', '_')

    save_path = f'{raw_data_folder}/meta_{amazon_category}.json.gz'
    metadata_url = f'https://jmcauley.ucsd.edu/data/amazon_v2/metaFiles2/meta_{amazon_category}.json.gz'
    if not os.path.exists(save_path):
        os.makedirs(raw_data_folder, exist_ok=True)
        os.system(f'wget {metadata_url} -O {save_path} --no-check-certificate')


def clean_data(amazon_category: str) -> None:
    print(f'Starting to clean {amazon_category}...')
    
    amazon_category = amazon_category.replace(' ', '_')
    save_path = f'{clean_data_folder}/{amazon_category}.csv'

    if not os.path.exists(save_path):
        os.makedirs(clean_data_folder, exist_ok=True)
        data = {}
        count = 0

        try:
            with gzip.open(f'{raw_data_folder}/meta_{amazon_category}.json.gz') as f:
                for line in f:
                    try:
                        row = json.loads(line.strip())
                        # product must have high res images and product id
                        if row.get('imageURLHighRes', []) and \
                            row.get('asin', '') and \
                            'getTime' not in row.get('title', 'getTime'): # filter those unformatted rows

                            p_id =  duplicated_products.get(row['asin'], row['asin'])
                            img_urls = data.get(p_id, [])
                            data[p_id] = img_urls + row['imageURLHighRes']
                    except Exception as e:
                        print(f'Error occured when processing {amazon_category} skipping the line...')
                        count += 1
        except Exception as e:
            print(f'{amazon_category} failed {e}')

        if data:
            print(f'In total {len(data)} rows exists and {count} failed to process for {amazon_category}...')
            with open(save_path, 'w', encoding='utf8', newline='') as f:
                dict_writer = csv.DictWriter(f, ['id', 'img_urls'])
                dict_writer.writeheader()
                to_csv = [
                     {'id': key, 'img_urls': ' '.join(set(value))}
                     for key, value in data.items()
                     if len(set(value)) >= threshold
                ]
                dict_writer.writerows(to_csv)




def process(amazon_category: str) -> None:
    print(f'Start processing {amazon_category}...')
    download_metadata(amazon_category)
    print(f'Downloading is finished for {amazon_category}...')
    clean_data(amazon_category)

if __name__ == '__main__':
    # i manually remove the categories that might not be needed.
    amazon_categories = [
        'Cell_Phones_and_Accessories.csv',
        'Office_Products.csv',
        'All_Beauty.csv',
        'Clothing_Shoes_and_Jewelry.csv',
        'AMAZON_FASHION.csv',
        'Luxury_Beauty.csv',
        'Sports_and_Outdoors.csv'
    ]

    # download duplicated files
    os.system(f'wget https://jmcauley.ucsd.edu/data/amazon_v2/metaFiles/duplicates.txt -O duplicates.txt --no-check-certificate')

    # download meta datas
    with Pool(5) as p:
        p.map(process, amazon_categories)