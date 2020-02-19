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




# 2. Spam Filter
