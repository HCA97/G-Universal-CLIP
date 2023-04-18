# [Visual Product Recognition Challenge](https://www.aicrowd.com/challenges/visual-product-recognition-challenge-2023)

This is my implementation for Aicrowd Visual Product Recognition Challenge. The goal is doing a visual search over e-commerce products.

The training and most of the hyper parameters are taken from [paper](https://arxiv.org/abs/2210.11141) which is the authors of the repo i fork too.

## Structure

- main branch is where all of my experiments are if you are interested some of my ideas you can check on it however they are not documented so you need to play ground.

- aicrowd branch is my final solution.

- [training on produck-10k and h&m](aicrowd-products-10k-h%26m-clip-training-v2-vit-h.ipynb)

We use code and pre-trained models from the amazing repo **[open_clip](https://github.com/mlfoundations/open_clip)** !

- [soup.ipynb](/soup.ipynb) model soups script. Idea from mlfoundation [WiSE-FT](https://github.com/mlfoundations/wise-ft) and [Robust fine-tuning of zero-shot models](https://arxiv.org/abs/2109.01903)

- [train_vit_h_224.ipynb](train_vit_h_224.ipynb) - Train ViT-H/14 pre-trained on LAION-2B

- [train_vit_l_336.ipynb](train_vit_l_336.ipynb) - Train ViT-L/14 pre-trained on LAION-2B

- [utilities.py](utilities.py) - General utilities!

- Models are available at this link : https://www.kaggle.com/datasets/ivanaerlic/guiemodels

## Setup

### 1. Get Data

### 2. Setup Env

### 3. Run the Experiments

### 4. Ensemble the Experiements



## Contact

Feel free to contact us if you have suggestions/inquiries about this work: [marcos.conde-osorio@uni-wuerzburg.de](mailto:marcos.conde-osorio@uni-wuerzburg.de)  and [ivanaer@outlook.com](mailto:ivanaer@outlook.com) Please add "google challenge" in the email subject.
