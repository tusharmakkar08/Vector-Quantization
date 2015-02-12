'''
Helper class for making test cases 
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 12.02.2015
'''

import random

def makeTestCases (rangeOfFeatures , numberOfFeatures, numberOfTestCases):
    '''
    Returns the matrix of Test Cases
    Args:
        rangeOfFeatures : The numerical range of features [min, max]
        numberOfFeatures : Total number of Features per feature vector
        numberOfTestCases : Total Number of Test Cases we want
    Returns:
        testCases : The Test Cases matrix matrix
    '''
    testCases = []
    for testCase in xrange(numberOfTestCases):
        tempTestCase = []
        for feature in xrange(numberOfFeatures):
            tempTestCase.append(random.randint(rangeOfFeatures[0], rangeOfFeatures[1]))
        testCases.append(tempTestCase)
    return testCases

if __name__ == '__main__':
    print makeTestCases([1,5], 3, 4)
