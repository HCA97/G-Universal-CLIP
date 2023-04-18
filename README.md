# [Visual Product Recognition Challenge](https://www.aicrowd.com/challenges/visual-product-recognition-challenge-2023)

This is my implementation for Aicrowd Visual Product Recognition Challenge. The goal is doing a visual search over e-commerce products.

The training and most of the hyper parameters are taken from [paper](https://arxiv.org/abs/2210.11141) which is the authors of the repo I fork too.

## Structure

- `main` branch is where all of my experiments are if you are interested some of my ideas you can check on it however they are not documented so you need to play ground.

- `aicrowd` branch is my final solution.

## Setup

### 1. Setup Env

* Install CUDA. 
    
    ***Note:** VIT-H is a huge model you need at least 24GB VRAM to run the experiments.*
* `pip install -r requirements.txt`

### 2. Get Data

* Product-10k [link](https://products-10k.github.io/)
* H&M [link](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data)
* Amazon Dataset [link](https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/)
* Shopee [link](https://www.kaggle.com/competitions/shopee-product-matching/data)
* Test Data from aicrowd team (Optional) [link](https://www.aicrowd.com/challenges/visual-product-recognition-challenge-2023/dataset_files)

Download the datasets and unzip them into their respected folders. 

To install the amazan dataset first;
```bash
cd amazon_dataset_1
python download_meta_data.py
python download_images.py
```
***Note:** You might need to run the scripts multiple times*

### 3. Run the Experiments

* EX1: [training on produck-10k and h&m](experiments/aicrowd-p10k-h&m-amazon-clip-training-v2.1-vit-h.ipynb)
* EX2: [training on product-10k + h&m + amazon (15k)](experiments/aicrowd-p10k-h&m-amazon-clip-training-v2.1-vit-h.ipynb)
* EX3: [training on product-10k + h&m + amazon (15k) + shopee](experiments/aicrowd-p10k-h&m-shopee-amazon-clip-training-v2.1-vit-h)
* EX4: [training on product-10k + h&m + shopee](experiments/aicrowd-p10k-h&m-shopee-clip-training-v2.1-vit-h)

### 4. Ensemble the Experiements

* `model 1`: weight ensemble of `EX1` results
* `model 2`: weight ensemble of `model 1` + `EX2` results
* `model 3`: weight ensemble of `EX3` + `EX4` results

To run the weight ensemble see [link](experiments/weight_ensembele.ipynb)





