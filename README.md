# Predicting Domain Generation Algorithms using LSTMs
This repo contains very simple code for classifying domains as DGA or benign.  This
code demonstrates our results in our arxiv paper here: https://arxiv.org/abs/1611.00791.
One difference is the datasets.  Both the paper and this repo use 
the Alexa top 1 million as benign, but this repo generates its own domains for simplicity.

We also only implement the LSTM and bigram classifier from the paper.  These are the two best 
classifiers and are simple to implement in Keras.

## Running the code

`python run.py` will download and generate all the data, train and evaluate the classifier, and save a PNG to disk (the ROC curve). 
It defaults to 1 fold to speed things up.  This code will run on your local machine or on a machine with a GPU (GPU will of course
be much faster).

## DGA Algorithms
We have 11 DGA algorithms in our repo.  Some are from the https://github.com/baderj/domain_generation_algorithms
repo.  We noted these in each file and kept the same GNU license.  However, we made some small edits
such as allowing for no TLD and varying the size for some algorithms.  
