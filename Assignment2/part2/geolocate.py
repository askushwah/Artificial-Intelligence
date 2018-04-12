
#!/usr/bin/env python
# Build a naive bayes classifier for geolocating tweets.

#geolocate.py train_file test_file output_file

#read a tweet data file and return a list of pairs where each pair is location and words (list(location, (words, words,....)))

import os
import sys

def read_tweetfile(filename):
    result = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            token_list = line.split(' ')
            result += [(token_list[0], token_list[1:]),]
    return result

# Classify_tweet: take words of a tweet and predict the location, also takes a hash, p_loc, mapping locations to prior probaibility
# and hash of hash p_word_loc, mapping words and locations to P(word|location)

def classify_tweet(words, P_loc, P_word_loc):
    #from bayes law: max P(location|words) = max P(words|location) P(location) / P(words) = max P(words|location)P(location)
    # = max P(word1 | location) * P(word2 | location) ... P(location) ----- due to naive bayes assumption
    (max_loc, max_prob) = ("",0)
    
    for loc in P_loc.keys():
        p_of_loc_given_tweet = P_loc[loc]
        for word in words:
            if word in P_word_loc[loc]:
                p_of_loc_given_tweet *= P_word_loc[loc][word]
            else:
                p_of_loc_given_tweet *= 0.00001
        if p_of_loc_given_tweet > max_prob:
            (max_loc, max_prob) = (loc,p_of_loc_given_tweet)
    return max_loc

# To point to the current directory
#os.chdir("/Users/adityakushwah/Python/Naive_Bayes")

# Training Phase
print(sys.argv[1:])
(train_fname, test_fname, output_fname) = sys.argv[1:]
train_Data = read_tweetfile(train_fname)
#print(train_Data)
# Hash for P(location), maps city names to probability
P_loc = {}
#hash for p(word| location), map city names to a map of words to probability
P_word_loc = {}
P_word = {}
for tweet in train_Data:
    gt_location = tweet[0]
    words = tweet[1]
    if gt_location in P_loc:
        P_loc[gt_location] += 1
    else:
        P_loc[gt_location] = 1
        P_word_loc[gt_location] = {}
    
    for word in words:
        if word in P_word:
            P_word[word] +=1
        else:
            P_word[word] = 1

        if word in P_word_loc[gt_location]:
            P_word_loc[gt_location][word] += 1
        else:
            P_word_loc[gt_location][word] = 1
#normalize the count into the probability

for loc in P_loc:
    P_loc[loc] /= float(len(train_Data))
    for word in P_word_loc[loc]:
        P_word_loc[loc][word] /= float(len(P_word_loc[loc]))

# display for each location the 10 words that maximize P(loc|word)
# P(loc|word) = P(word|loc) P(loc) / P(word)
for loc in P_loc:
    posterior_probs = sorted([ (w, P_word_loc[loc][w] * P_loc[loc] / P_word[w]) if P_word[w] > 10 else (w,0) for w in P_word_loc[loc] ], key = lambda x: x[1])
    print loc, "  ".join([l[0] for l in posterior_probs[-10:]])

#Testing Phase
test_Data = read_tweetfile(test_fname)
correct_count = 0
for tweet in test_Data:
    gt_location = tweet[0]
    estimated_location = classify_tweet(tweet[1], P_loc, P_word_loc)
    correct_count += 1 if estimated_location == gt_location else 0

print("We got ", correct_count," of ", len(test_Data),"tweets correct, ", (correct_count)/float(len(test_Data))*100, "%")