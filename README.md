# [4th place solution - Google Universal Image Embedding Kaggle Challenge @ ECCV 2022](https://www.kaggle.com/competitions/google-universal-image-embedding/)
## [Instance-Level Recognition workshop](https://ilr-workshop.github.io/ECCVW2022/)  [ <a href="https://www.kaggle.com/competitions/google-universal-image-embedding/"><img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Kaggle_logo.png?20140912155123" alt="kaggle logo" width=50></a>](https://www.kaggle.com/competitions/google-universal-image-embedding/)


[Marcos V. Conde](https://scholar.google.com/citations?user=NtB1kjYAAAAJ&hl=en), [Ivan Aerlic](https://www.kaggle.com/ivanaerlic), [Simon Jégou](https://www.kaggle.com/simjeg)

------------------

**News 🚀🚀**

- [10/2022] The paper will be available by 17th October
- [10/2022] 4th place solution! setting up this repo

------------------

<img src="media/guie-lb.png " alt="guie lb" width="600" border="0">

## Structure

We use code and pre-trained models from the amazing repo **[open_clip](https://github.com/mlfoundations/open_clip)** !

- [soup.ipynb](/soup.ipynb) model soups script. Idea from mlfoundation [WiSE-FT](https://github.com/mlfoundations/wise-ft) and [Robust fine-tuning of zero-shot models](https://arxiv.org/abs/2109.01903)

- [train_vit_h_224.ipynb](train_vit_h_224.ipynb) - Train ViT-H/14 pre-trained on LAION-2B

- [train_vit_l_336.ipynb](train_vit_l_336.ipynb) - Train ViT-L/14 pre-trained on LAION-2B

- [utilities.py](utilities.py) - General utilities!

------------------

## Contact

Feel free to contact us if you have suggestions/inquiries about this work: [marcos.conde-osorio@uni-wuerzburg.de](mailto:marcos.conde-osorio@uni-wuerzburg.de)  and [ivanaer@outlook.com](mailto:ivanaer@outlook.com) Please add "google challenge" in the email subject.