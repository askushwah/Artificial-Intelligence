################# Neural Network/ Best Eplination ##########################
# Activation function used: Sigmoid
# Learning rate (alpha) used :0.1
# Backpropogation Method : Stochastic Gradient Decent
# Training data is iter three times using reshuffling the training data
# Input Layer: 192 Features
# Hidden layers : 20 - 25
# Output layers : 4

# There are 192 input variable with each image feature and 20 hidden nodes and then 4 output nodes

# Hidden Nodes      Time Taken        Accuracy
#   20                    260             71.3%
#   20                    240             72.2%
#   23                    301             71.0%  
#   22                    315             74.2%  
#   20                    230             72.0%
#   20                    200             71.32%
#   20                    222             70%
#   20                    220             72.2%
#   25                    380             74.6%
#   25                    370             72.29%

# Neural Network is found to be the best algorithmn as it gives the best efficiency.
# Model file - Model file will be created with the name that will be used while training.
#             The same name should be used when testing the data. Model file will contain the 
#             weights that are generated and the feature vector of the test file.close

# nnet.txt - This file contains all the corresponding output of the orientation that was achieved 
#             after performing the neural network onto it.

# The heightest efficiency that was achieved throught this training data was 74.6%. And because
# this algorithm gives the heightest efficiency, this is also used for the best algorithm


import random
import math
import numpy as np
import os

class readfile:
    train = []
    test = []
    feature_training = []
    training_data = []
    hidden_node = 20
    weight1 = []
    weight2 = []

    def read_data(self, file_name, type_of_file, model_file):
        
        list_features = []
        vectors = []
        file = open(file_name, 'r')
        for line in file:
            line = line.split()
            if type_of_file == "test":
                 readfile.training_data.append(line[1])
            inner_vector = []
            for x in line[2:]:
                inner_vector.append(int(x))

            list_features += [[line[0], line[1], inner_vector]]
            vectors.append(inner_vector)
        if type_of_file == "test":
            temp = []
            readfile.test = list_features
            with open(model_file, 'r') as op:
                parameter=[eval(line.rstrip('\n')) for line in op]
            readfile.weight1 = parameter[0:192]
            readfile.weight2 = parameter[192:212]
            readfile.train+=parameter[212:]

        else:
            readfile.train = list_features
            readfile.feature_training = vectors
            temp = []
            self.weight1 = [[random.uniform(-0.01,0.01) for i in range(readfile.hidden_node)] for j in range(192)]
            self.weight2 = [[random.uniform(-0.01,0.01) for i in range(4)] for j in range(readfile.hidden_node)]
            with open(model_file, 'w') as op:
                for row in self.weight1:
                    op.write('%s\n'%row)
                for row2 in self.weight2:
                    op.write('%s\n'%row2)
                for row3 in readfile.train:
                    op.write('%s\n'%row3)

class nnet:
    def __init__(self, input, output):
        self.input = input 
        self.output = output  

    def apply_sigmoid(self):
        self.output = self.sigmoid(self.input)

    def sigmoid(self, value):
        return 1 / (1 + math.exp(-value))

    def derivative_sigmoid(self, value):
        return self.sigmoid(value) * (1 - self.sigmoid(value))

    def calculate_derivative_sigmoid_sigmoid(self):
        return self.sigmoid(self.input) * (1 - self.sigmoid(self.input))

    def calculate_derivative_sigmoid(self):
        return self.calculate_derivative_sigmoid_sigmoid()


class Neural_Network:
    def __init__(self):
        self.orientation = ['0', '90', '180', '270']
        self.expected = [0 for i in range(4)]
        self.alpha = 0.1
        self.input_nodes = 192
        self.output_nodes = 4
        self.hidden_node = int(readfile.hidden_node)
        # 192 input nodes
        self.input = [nnet(0, 0) for i in range(self.input_nodes)]
        # random weights
        self.hidden = [nnet(0, 0) for i in range(self.hidden_node)]
        # output nodes
        self.output = [nnet(0, 0) for i in range(self.output_nodes)]

    def feed_forward(self, input_image):
        #print(input_image)        
        for i in range(self.input_nodes):
            self.input[i].input = self.input[i].output = input_image[i] / 255.0

        for i in range(self.hidden_node):
            total = 0.0
            for j in range(self.input_nodes):
                total += self.input[j].output * readfile.weight1[j][i]

            self.hidden[i].input = total
            self.hidden[i].apply_sigmoid()

        for i in range(self.output_nodes):
            total = 0.0
            for j in range(self.hidden_node):
                total += self.hidden[j].output * readfile.weight2[j][i]

            self.output[i].input = total
            self.output[i].apply_sigmoid()
            if self.output[i].output >= 0.7:
                self.output[i].output = 1.0
            elif self.output[i].output <= 0.4:
                self.output[i].output = 0.0

        return self.output

    def back_propogation(self, target_label):

        delta = [0.0 for i in range(self.output_nodes)]

        actual_output = target_label

        for i in range(self.output_nodes):
            delta[i] = (actual_output[i] - self.output[i].output) * self.output[i].calculate_derivative_sigmoid()

        delta_hidden = [0.0 for i in range(self.hidden_node)]

        for i in range(self.hidden_node):
            error_value = 0.0
            for k in range(self.output_nodes):
                error_value += delta[k] * readfile.weight2[i][k]

            delta_hidden[i] = error_value * self.hidden[i].output * self.hidden[i].calculate_derivative_sigmoid()

        for i in range(self.hidden_node):
            for k in range(self.output_nodes):
                readfile.weight2[i][k] += delta[k] * self.hidden[i].output * self.alpha

        for i in range(self.input_nodes):
            for k in range(self.hidden_node):
                readfile.weight1[i][k] += delta_hidden[k] * self.input[i].output * self.alpha

        error_value = 0.0
        for i in range(self.output_nodes):
            error_value += math.pow(actual_output[i] - self.output[i].output, 2)

        return math.sqrt(error_value)

    def test_model(self):
        final_outcome = []
        label = 0
        for image in readfile.test:
            outcome = []
            nodes = self.feed_forward(image[2])  
            self.expected = [0.0 for k in range(4)]
            self.expected[self.orientation.index(image[1])] = 1.0
            for i in range(len(self.orientation)):
                outcome.append(nodes[i].output)
            label = self.orientation[outcome.index(max(outcome))]
            final_outcome.append(label)
        return final_outcome

    def classify_model(self):
        op = open('nnet.txt', 'w')
        condition = False
        iterations = 3
        count = 0
        # print(readfile.train)
        print "Please Wait!!"
        while not condition and iterations > 0:
            iterations -= 1
            random.shuffle(readfile.train)
            error_value = 0.0
            for i in range(len(readfile.train)):
                self.feed_forward(readfile.train[i][2])
                self.expected_outcome = [0.0 for k in range(4)]
                self.expected_outcome[self.orientation.index(readfile.train[i][1])] = 1.0
                error_value = error_value + self.back_propogation(self.expected_outcome)
            if error_value <= 1000:
                condition = True

        computed_output = self.test_model()
        for i in range(len(computed_output)):
            if computed_output[i] == readfile.training_data[i]:
                count+=1
            op.write(readfile.test[i][0] + ' ' + computed_output[i] + '\n')
        op.close()
        return (count/float(len(readfile.training_data)))*100

read_file = readfile()
# os.chdir("/Users/adityakushwah/Python/Neural_Network_A4")
# read_file.read_data("train-data.txt","train","a.txt")
# read_file.read_data("test-data.txt","test","a.txt")
# nn = Neural_Network()
# print("The accuracy of the output is: ", nn.classify_model(),"%")
