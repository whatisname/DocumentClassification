# DocumentClassification
Performance of various ML algorithms on Document Classification

# 1. [Build Naïve Bayes Model for Document Tagging](https://github.com/whatisname/DocumentClassification/tree/master/multipleTags)

## Introduction

The main task of this project is to design a program that accept a training dataset of labeled documents to train a Naïve Bayes classifier to classify new documents with satisficing accuracy. The program implements Naïve Bayes algorithm to perform probabilistic prediction on its input. Thus in this program, the assumption is that each word is individual from each other in training and testing datasets. The algorithm is totally implemented in Python language, by which I could build several different modules for the purpose of scalability and reusability. Code of three modules are in Attachment.

## Algorithm Demonstration

The main learning algorithm functions are listed below. The program uses VocTable first to read training data and generate vocabulary set and counting array, then calculates the probabilities of each word. Next, pass VocTable to Processor, which loop up and calculate probability of new words and overall probabilities regarding each category. Select the largest one as its predicted label and save to a 2d array too. (Equation showed in Figure1) At last, Processor generate confusion matrix and plot on the screen. Every probability is natural log transformed to preserve precision.

![Classifier Image](multipleTags/backup/img/1.png)

Figure1: The classifier this program uses to calculate the probabilities that a new document belongs to which class.

![algorithm](multipleTags/backup/img/2.png)

Figure2: Learning algorithm used in the program

Besides the main function, the two modules also provide some other functions. They all provide functions to save middle calculation results, for example, counting result, vocabulary set and probability table, result of prediction (table), statistics of prediction table (confusion matrix), save and reread in CSV format.   

They also provide different plot function. VocTable can plot top table of given number of most frequent word in each category or given categories (not implemented for now). Processor provides functions to plot confusion matrix/heatmap and bar plot of the category count of the training/testing set. Plots are included in later section.

During development, there is also other modules produced for data process: DocumentProcessor module (transfer another dataset to proper form for program input), plot support (plot module), diction look function (Dictionary module), word stemming function (PorterStemmer module).  Some of them are not all written by myself, the link will be listed in reference.

Main entrance is file “fileprocess.py”.

Table 1 Important modules/functions demonstration

+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Main algorithms/modules                                                                            | Description                                                                         |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| VocTable                                                                                           | Module                                                                              |
|                                                                                                    | for reading training data, counting, calculating probability, generating vocabulary |
|                                                                                                    | count table (2d array), read/save middle data.                                      |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| VocTable.read(fileName, min_word_length, max_word_length, avoid_stopword, dictionary_lookup, skip) | For training. Accept the file name of training                                      |
|                                                                                                    |   dataset file, minimum word length, maximum word length to skip add into           |
|                                                                                                    |   vocabulary set, flags of whether to avoid stopword, whether to look if a word     |
|                                                                                                    |   is English word, customize word list for the user to skip for the user.           |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| VocTable                                                                                           | After                                                                               |
| .__caculate__()                                                                                    | reading, it calls this method automatically to calculate word count, category       |
|                                                                                                    | count and generate a 2-dementional array.                                           |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Predictor                                                                                          | Provided function to prediction testing set, plot of category                       |
|                                                                                                    |   counting, confusion matrix/heatmap,                                               |
|                                                                                                    |                                                                                     |
|                                                                                                    |  read/save middle data.                                                             |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Predictor.read(fileName)                                                                           | Read testing data file and call count().                                            |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Predictor.count()                                                                                  | Count probabilities of new words and decide which                                   |
|                                                                                                    |   category one new document belongs to.                                             |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Predictor.plot(cellLable, fileName)                                                                | Plot for confusion matrix/heatmap for                                               |
|                                                                                                    |   visualization. cellLable indicate whether the plot has sample size on each        |
|                                                                                                    |   cell. filename indicate the name of file to save to file system.                  |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Predictor.plotCategryCount(fileName)                                                               | Plot category count to bar plot.                                                    |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Dictionary                                                                                         | The module                                                                          |
|                                                                                                    |   for dictionary lookup. Dictionary is a json file download from GitHub. [2]        |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| plot                                                                                               | The module for plotting.                                                            |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| PorterStemmer                                                                                      | The module for wording stemming.                                                    |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| DocumentProcessor                                                                                  | The module for format second data source to proper form for program                 |
|                                                                                                    |   input.                                                                            |
+----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

## Data Structure and Algorithm Logic 

The program uses 2d array to store word count, vocabulary probabilities and confusion matrix. Main document process logic does not use external library because of the performance was slow when I use third library (1 hour to process training data). I read the file in byte stream, separate word one by one and look if it already exists in vocabulary list. One of the main reasons that the program execution can be scaled down from more than 1 hour to about 30 second is that I used binary search each time I try to find in vocabulary set (it is implemented in all list and array retrieval). 

## Experiment Result and Compare

### 1 Experimental Version of Third library

First version is not completed. It uses “pandas” package data frame structure to store vocabulary. It is very slow because the logic in Figure2 is not efficient. Time spent: 1.2 hour (only the total time of reading training dataset).




# 2. Spam Filter
