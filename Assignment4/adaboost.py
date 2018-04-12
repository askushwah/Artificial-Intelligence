#!/usr/bin/env python

'''
Adaboost:
My approach was to use many weak classifiers(decision stumps),which just compares
randomly selected pixels and makes a decision.Each weak classifier(hypothesis) is
assigned a weight,which signifies the importance(accuracy) of the decision stump
on the given dataset.
First,I segregated the features into 3 parts:R,G,B.Each part represented the
features for a particular color of the image.Then,I randomly selected two pixel
positions and a color,which will be used in the decision stump.Also,I randomly
selected a subset of the training dataset based on the probability distribution
acquired through the weights of each datapoint.Then,I ran each decision stump
(classifier) on the selected subset of the data.I repeated this process for
multiple iterations & created a model file for adaboost.
The model file contains the following parameters for each weak classifier:
1) Randomly selected 2 pixel positions.
2) Randomly selected color.
3) Weight of the hypothesis(weak classifier)

The following table depicts the classification accuracy for different number of
weak classifiers:

    Number of weak classifier(c) ||  Classification Accuracy(%)
   ------------------------------||----------------------------------
1)              10               ||           50.4771
2)              25               ||           59.4931
3)              50               ||           59.7049
4)              100              ||           63.3086
5)             >=120             ||           64.6267

The basic intuition was to generate a large number of random samples from the entire
dataset,so that it represents most of the features of the training datapoints.

The following table depicts the classification accuracy for different sample
size of the training dataset:

    Sample size of the dataset   ||  Classification Accuracy(%)
   ------------------------------||----------------------------------
1)             30                ||           56.2036
2)             100               ||           61.9301
3)             300               ||           63.2025
4)             3000              ||           63.5207
5)             30000             ||           65.3235
'''

import numpy as np
import sys
import math
import random
import csv

output=[0,90,180,270]
c=120  #Number of weak classifiers for a particular class

def train_weak_classifier(parameter,inst_weight,class_label,feature,bool_label):
    size=int(math.ceil(0.9*len(inst_weight)))   #Size of the subsample
    [p1,p2]=random.sample(range(0,63),2)  #Randomly selecting two features
    color=random.randint(0,2)   #Randomly selecting color
    #Randomly selecting the subsample
    index=np.unique(np.random.choice(len(feature[0]),size,list(inst_weight)))
    #Cases where the condition of decision stump is satisfied
    trueCase=index[np.where(feature[color][index,p1]>feature[color][index,p2])]
    #Cases where the condition of decision stump is not satisfied
    falseCase=index[np.where(feature[color][index,p1]<=feature[color][index,p2])]
    trueLabel=np.argmax(np.bincount(bool_label[trueCase]))
    falseCorrectIndex=falseCase[np.where(bool_label[falseCase]==(trueLabel+1)%2)]
    trueCorrectIndex=trueCase[np.where(bool_label[trueCase]==trueLabel)]
    #Computing the error
    error=1-float(len(falseCorrectIndex)+len(trueCorrectIndex))/len(index)
    #Updating(decreasing) the weight of the correctly classified training datapoints
    inst_weight[falseCorrectIndex]*=error/(1-error)
    inst_weight[trueCorrectIndex]*=error/(1-error)
    #Normalizing the weights
    inst_weight=inst_weight/float(np.sum(inst_weight))
    #Computing the weight of the weak classifier(hypothesis)
    hypo_weight=0.5*math.log((1-error)/error)
    #Rolling the parameters of the weak classifier
    parameter+=[[p1,p2,color,class_label,hypo_weight]]
    return parameter,inst_weight

def train_adaboost(train_file_name,model_file):
    train_file_name='train-data.txt'
    train_file=open(train_file_name,'r')
    data=[[],[],[]]
    concept=[]
    for row in train_file:
        data[0]+=[[int(line) for line in row.split()[2::3]]]
        data[1]+=[[int(line) for line in row.split()[3::3]]]
        data[2]+=[[int(line) for line in row.split()[4::3]]]
        concept+=[int(row.split()[1])]
    feature=np.array((data))
    feature[0]=np.array(data[0])
    feature[1]=np.array(data[1])
    feature[2]=np.array(data[2])
    label=np.array(concept)
    parameter=[]
    #Initializing the weight of the training datapoints
    inst_weight=1.0/len(feature[0])*np.ones((len(feature[0])))
    for j in range(len(output)):
        i=0
        bool_label=label==output[j]
        while i<=c:
            [parameter,inst_weight]=train_weak_classifier(parameter,inst_weight\
                                                ,output[j],feature,bool_label)
            i+=1
    model_file='adaboost_model.txt'
    with open(model_file,'w') as m_name:
        for row in parameter:
            m_name.write('%s\n'%row)

def test_adaboost(test_file_name,model_file_name):
    test_file_name='test-data.txt'
    test_file=open(test_file_name,'r')
    model_file_name='adaboost_model.txt'
    parameter=[]
    with open(model_file_name,'r') as model_file:
        parameter=[eval(line.rstrip('\n')) for line in model_file]
    test=[[],[],[]]
    actual_op=[]
    image_name=[]
    for row in test_file:
        test[0]+=[[int(line) for line in row.split()[2::3]]]
        test[1]+=[[int(line) for line in row.split()[3::3]]]
        test[2]+=[[int(line) for line in row.split()[4::3]]]
        actual_op+=[int(row.split()[1])]
        image_name+=[row.split()[0]]
    count=0
    expected=[]
    for i in range(len(test[0])):
        final=np.zeros((4))
        for j in range(c):
            for k in range(4):
                if test[parameter[j+c*k][2]][i][parameter[j+c*k][0]]>\
                   test[parameter[j+c*k][2]][i][parameter[j+c*k][1]]:
                    final[k]-=parameter[j+c*k][4]
                else:
                    final[k]+=parameter[j+c*k][4]
        #Predicted output by taking a weighted vote of all the weak classifiers
        expected.append(output[np.argmax(final)])  
        if expected[i]==actual_op[i]:
            count+=1
    with open('adaboost_output.txt','w') as f:
        for i in range(len(expected)):
            f.write('%s %s\n'%(image_name[i],expected[i]))
    print 'Accuracy: ',float(count)*100/len(test[0])
