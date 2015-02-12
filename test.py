'''
Helper class for making test cases 
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 12.02.2015
'''

import random

def makeTestCases (rangeOfFeatures ,numberOfSamples, numberOfFeatures, numberOfTestCases):
    '''
    Returns the matrix of Test Cases
    Args:
        rangeOfFeatures : The numerical range of features [min, max]
        numberOfSamples : Total number of Sample in a matrix
        numberOfFeatures : Total number of Features per feature vector
        numberOfTestCases : Total Number of Test Cases we want
    Returns:
        testCases : The Test Cases matrix matrix
    '''
    testCases = []
    for testCase in xrange(numberOfTestCases):
        tempTestCase = []
        for sample in xrange(numberOfSamples): 
            tempSample = []
            for feature in xrange(numberOfFeatures):
                tempSample.append(random.randint(rangeOfFeatures[0], rangeOfFeatures[1]))
            tempTestCase.append(tempSample)
        testCases.append(tempTestCase)
    return testCases

if __name__ == '__main__':
    print makeTestCases([1,5], 2, 3, 4)
