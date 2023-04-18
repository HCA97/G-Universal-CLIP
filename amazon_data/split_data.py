import pandas as pd

# df = pd.read_csv('amazon_data_set_sample_500.csv')
# df_g = df.groupby('id', group_keys=True).apply(lambda x: x)


# gallery = []
# query = []
# for i, group in enumerate(set(df_g['id'])):
#     paths = list(df_g.path[df_g['id'] == group])
#     if len(paths) >= 3:
#         query.append({'id': i, 'path': paths[0]})
#         query.append({'id': i, 'path': paths[1]})
#         for p in paths[2:]:
#             gallery.append({'id': i, 'path': p})

# print(len(gallery), len(query))

# pd.DataFrame(gallery).to_csv('gallery.csv')
# pd.DataFrame(query).to_csv('query.csv')

df1 = pd.read_csv('amazon_data_set_sample_10000.csv')
df2 = pd.read_csv('amazon_data_set_sample_5000.csv')
df = pd.concat([df1, df2])
df = df.drop_duplicates(subset='path', keep="last")
df.to_csv('amazon_data_set_sample_15000_2.csv', index=False)