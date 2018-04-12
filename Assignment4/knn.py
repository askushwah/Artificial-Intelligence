#!/usr/bin/env python


#One of the design decisions about the paramete K in KNN was to select K as an odd number to avoid a tie.
#Also choosing K was based on trial and error by looking at the accuracy for various values of K.
#Another design decision was to choose the distance measure between two image pixels. Here I have chosen the Euclidean distance as the measure of distance.

#The following table shows the accuracies of various K parameters according to my program:

#K Parameter        Accuracy
#   3                     68.71
#   7                     69.56
#   11                    71.15
#   15                    70.20
#   19                    69.77
#   23                    70.94
#   27                    70.94
#   31                    69.88
#   35                    70.41
#   39                    71.26
#   43                    71.68
#   47                    71.36
#   51                    70.83
#   55                    71.36
#   59                    71.58
#   63                    70.94
#   67                    71.36
#   71                    70.30
#   75                    70.51
#   77                    70.51
#   81                    69.88
#   85                    70.62   
#   89                    70.41
#   91                    71.15
#   95                    70.09
#   99                    70.20
#   103                   70.94
        



import sys
import numpy as np
import string
import math
from numpy import linalg as LA





def distance(mat,test):
    file = open("knn_output.txt",'w')
    euclid_dist = []
    correct = 0
    count = 0
    mat = mat.astype(np.int)
    for p in test:
        count += 1
        euclid_dist = []
        initial = p.strip('\n').split(None,1)
        test_id = initial[0]
        val = initial[1].split(" ")
        test_orient = val[0]
        x_test = np.matrix(val[1:]).astype(np.int)
        for i in range(len(mat)):
            orient = mat[i][0]
            dist = LA.norm(mat[i][1:] - x_test)
            euclid_dist.append([dist,orient])
        euclid_dist = sorted(euclid_dist)
        pred_orient = vote_func(euclid_dist)
        file.write(test_id+" "+str(pred_orient)+'\n')
        if pred_orient == int(test_orient):
            correct += 1
    print "Accuracy  = ",float(correct)/count*100

def vote_func(dist_mat):
    votes = {}
    for i in dist_mat[0:43]:
        o = i[1]
        if votes.has_key(o):
            votes[o] = votes.get(o)+1
        else:
            votes[o] = 1
    max_val = max(votes, key=votes.get)
    return max_val


def knn_train(train_file,model_file):
    count = 0
    file = open("nearest_model.txt",'w')
    print "Training !!!!!"
    with open(train_file) as f:
        for i in f:
            str1 = ' '.join(i.strip('\n').split(None,1)[1].split(" "))
            file.write(str1+'\n')
            count += 1

orient = {}
test_orient = {}


def knn_test(phase_file,model_file):
    print "Testing"
    h = np.loadtxt(model_file)
    with open(phase_file) as f:
    	distance(h,f)
        
