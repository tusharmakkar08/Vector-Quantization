'''
Vector Quantization
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 12.02.2015
'''

import test

def train (trainingData, aggregation):
    '''
    Returns the codebook
    Args:
        trainingData  : Training Data for our classifier
        aggregation : the aggregation philosphy used; 'a' for mean, 'm'
                        for minimum , 'M' for maximum
    Returns:
        codeBook : Code Book corresponding to the training data
    '''
    codeBook = []
    return codeBook

def test (testData, codeBook, similarityMetric):
    '''
    Returns the 
    Args:
        testData  : Testing Data for our classifier
        codeBook : Code Book correspondng to the training data
        similarityMetric : the similarity measure used; 'e' for euclidean, 
                        'm' for manhattan
    Returns:
        testResults : Results corresponding to the codeBook according to
                        our classifier
    ''' 
    testResults = []
    return testResults

if __name__ == '__main__':
    
