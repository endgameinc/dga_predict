"""Run experiments and create figs"""
import itertools
import os
import pickle
#import matplotlib
#matplotlib.use('Agg')
import numpy as np

import src.dga_classifier.bigram as bigram
import src.dga_classifier.lstm as lstm

from scipy import interp
from sklearn.metrics import roc_curve, auc

RESULT_FILE = 'results.pkl'

def run_experiments(isbigram=True, islstm=True, nfolds=10):
    """Runs all experiments"""
    bigram_results = None
    lstm_results = None

    if isbigram:
        bigram_results = bigram.run(nfolds=nfolds)

    if islstm:
        lstm_results = lstm.run(nfolds=nfolds)

    return bigram_results, lstm_results

def create_figs(isbigram=True, islstm=True, nfolds=10, force=False):
    """Create figures"""
    # Generate results if needed
    if force or (not os.path.isfile(RESULT_FILE)):
        bigram_results, lstm_results = run_experiments(isbigram, islstm, nfolds)

        results = {'bigram': bigram_results, 'lstm': lstm_results}

        pickle.dump(results, open(RESULT_FILE, 'w'))
    else:
        results = pickle.load(open(RESULT_FILE))

    # Extract and calculate bigram ROC
    if results['bigram']:
        bigram_results = results['bigram']
        fpr = []
        tpr = []
        for bigram_result in bigram_results:
            t_fpr, t_tpr, _ = roc_curve(bigram_result['y'], bigram_result['probs'])
            fpr.append(t_fpr)
            tpr.append(t_tpr)
        bigram_binary_fpr, bigram_binary_tpr, bigram_binary_auc = calc_macro_roc(fpr, tpr)

    # xtract and calculate LSTM ROC
    if results['lstm']:
        lstm_results = results['lstm']
        fpr = []
        tpr = []
        for lstm_result in lstm_results:
            t_fpr, t_tpr, _ = roc_curve(lstm_result['y'], lstm_result['probs'])
            fpr.append(t_fpr)
            tpr.append(t_tpr)
        lstm_binary_fpr, lstm_binary_tpr, lstm_binary_auc = calc_macro_roc(fpr, tpr)

    # Save figure

    """
    from matplotlib import pyplot as plt
    with plt.style.context('bmh'):
        plt.plot(lstm_binary_fpr, lstm_binary_tpr,
                 label='LSTM (AUC = %.4f)' % (lstm_binary_auc, ), rasterized=True)
        plt.plot(bigram_binary_fpr, bigram_binary_tpr,
                 label='Bigrams (AUC = %.4f)' % (bigram_binary_auc, ), rasterized=True)

        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate', fontsize=22)
        plt.ylabel('True Positive Rate', fontsize=22)
        plt.title('ROC - Binary Classification', fontsize=26)
        plt.legend(loc="lower right", fontsize=22)

        plt.tick_params(axis='both', labelsize=22)
        plt.savefig('results.png')
    """

def calc_macro_roc(fpr, tpr):
    """Calcs macro ROC on log scale"""
    # Create log scale domain
    all_fpr = sorted(itertools.chain(*fpr))

    # Then interpolate all ROC curves at this points
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(len(tpr)):
        mean_tpr += interp(all_fpr, fpr[i], tpr[i])

    return all_fpr, mean_tpr / len(tpr), auc(all_fpr, mean_tpr) / len(tpr)

if __name__ == "__main__":
    create_figs(nfolds=1) # Run with 1 to make it fast
