# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 00:59:24 2019

@author: XX

Reference
---------
https://realpython.com/python-matplotlib-guide/#why-can-matplotlib-be-confusing
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def confusion_matrix(cm,
                          target_names,
                          title='Confusion matrix',
                          cmap=None,
                          normalize=True,
                          cell_label=True,
                          filepath = ''):
    """
    given a sklearn confusion matrix (cm), make a nice plot

    Arguments
    ---------
    cm:           confusion matrix from sklearn.metrics.confusion_matrix

    target_names: given classification classes such as [0, 1, 2]
                  the class names, for example: ['high', 'medium', 'low']

    title:        the text to display at the top of the matrix

    cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
                  see http://matplotlib.org/examples/color/colormaps_reference.html
                  plt.get_cmap('jet') or plt.cm.Blues

    normalize:    If False, plot the raw numbers
                  If True, plot the proportions
    filepath:     If length of filepath is not 0, save figure to file. (only suport .png)
                          
    cell_label:   If set True, each cell will shows its value in the center. 
                  If False, do not show number in cell.

    Usage
    -----
    plot_confusion_matrix(cm           = cm,                  # confusion matrix created by
                                                              # sklearn.metrics.confusion_matrix
                          normalize    = True,                # show proportions
                          target_names = y_labels_vals,       # list of names of the classes
                          title        = best_estimator_name  # title of graph
                          filepath     = 'confusion.png')     # filepath of figure output (only suport .png)    
    plot_confusion_matrix(cm           = np.array([[ 1098,  1934,   807],
                                              [  604,  4392,  6233],
                                              [  162,  2362, 31760]]), 
                          normalize    = False,
                          target_names = ['high', 'medium', 'low'],
                          title        = "Confusion Matrix")

    plot_confusion_matrix(cm           = np.array([[ 1098,  1934,   807],
                                                  [  604,  4392,  6233],
                                                  [  162,  2362, 31760]]), 
                          normalize    = True,
                          target_names = ['high', 'medium', 'low'],
                          title        = "Confusion Matrix, Normalized")
    Citiation
    ---------
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
    
    Reference
    ---------
    https://www.kaggle.com/grfiv4/plot-a-confusion-matrix
    """
    import itertools

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if cell_label:
            if normalize:
                plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")
            else:
                plt.text(j, i, "{:,}".format(cm[i, j]),
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, '',
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")


#    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.show()
    if len(filepath) != 0:
        plt.savefig(filepath, format='png') # TODO: not working
        
def toptable(data, row_label, column_label, filepath = ''):
    fig, axs =plt.subplots(2,1)
    clust_data = np.random.random((10,3))
    collabel=("col 1", "col 2", "col 3")
    axs[0].axis('tight')
    axs[0].axis('off')
    the_table = axs[0].table(cellText=clust_data,colLabels=collabel,loc='center')
    
    axs[1].plot(clust_data[:,0],clust_data[:,1])
    plt.show()
    if len(filepath) != 0:
        plt.savefig(filepath, format='png') # TODO: not working
        
def toptable1(data, row_label, column_label, filepath = ''):
    data = [[ 66386, 174296,  75131, 577908,  32015],
    [ 58230, 381139,  78045,  99308, 160454],
    [ 89135,  80552, 152558, 497981, 603535],
    [ 78415,  81858, 150656, 193263,  69638],
    [139361, 331509, 343164, 781380,  52269]]

    columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
    rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
    
    values = np.arange(0, 2500, 500)
    value_increment = 1000
    
    # Get some pastel shades for the colors
    colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
    n_rows = len(data)
    
    index = np.arange(len(columns)) + 0.3
    bar_width = 0.4
    
    # Initialize the vertical-offset for the stacked bar chart.
    y_offset = np.zeros(len(columns))
    
    # Plot bars and create text labels for the table
    cell_text = []
    for row in range(n_rows):
        plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
        y_offset = y_offset + data[row]
        cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
    # Reverse colors and text labels to display the last value at the top.
    colors = colors[::-1]
    cell_text.reverse()
    
    # Add a table at the bottom of the axes
    the_table = plt.table(cellText=cell_text,
                          rowLabels=rows,
                          rowColours=colors,
                          colLabels=columns,
                          loc='bottom')
    
    # Adjust layout to make room for the table:
    plt.subplots_adjust(left=0.2, bottom=0.2)
    
    plt.ylabel("Loss in ${0}'s".format(value_increment))
    plt.yticks(values * value_increment, ['%d' % val for val in values])
    plt.xticks([])
    plt.title('Loss by Disaster')
    
    plt.show()
    
def bar(labels, values, filepath = ''):
    "https://matplotlib.org/gallery/ticks_and_spines/custom_ticker1.html#sphx-glr-gallery-ticks-and-spines-custom-ticker1-py"
    from matplotlib.ticker import FuncFormatter
    x = np.arange(len(labels))
    
    def millions(x, pos):
        'The two args are the value and tick position'
        return '%1.1f' % (x)
    
    formatter = FuncFormatter(millions)
    
    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)
    plt.bar(x, values)
    plt.xticks(x, labels)
    plt.show()
    if len(filepath) != 0:
        plt.savefig(filepath, format='png') # TODO: not working

if __name__ == '__main__':
    toptable(data=[], row_label=[], column_label=[])
#    bar(['a', 'b', 'c'], [10, 20, 30])
    
        
    
    
    
