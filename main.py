'''
Vector Quantization
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 12.02.2015
'''

from test import makeTestCases
from math import sqrt

def avgf(classData):
    '''
    Returns the codebook
    Args:
        classData : Training Data which needs to be aggregated
    Returns:
        avgData :average of the class elements
    '''
    avgData = []
    sumData = [0]*len(classData[0])
    for indSample in classData:
        startIndex = 0
        for indData in indSample:
            sumData[startIndex] += indData
            startIndex += 1
    for indSum in sumData :
        avgData.append(indSum*1.0/len(classData[0]))
    return avgData

def minf(classData):
    '''
    Returns the codebook
    Args:
        classData : Training Data which needs to be aggregated
    Returns:
        minData : Minimum of the class elements
    '''
    minData = [1000000000]*len(classData[0])
    for indSample in classData:
        startIndex = 0
        for indData in indSample:
            minData[startIndex] = min(minData[startIndex], indData)
            startIndex += 1
    return minData

def maxf(classData):
    '''
    Returns the codebook
    Args:
        classData : Training Data which needs to be aggregated
    Returns:
        maxData : Maximum of the class elements
    '''
    maxData = [-1]*len(classData[0])
    for indSample in classData:
        startIndex = 0
        for indData in indSample:
            maxData[startIndex] = max(maxData[startIndex], indData)
            startIndex += 1
    return maxData

    
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
    # [[class, code] : [training Data], .. ]
    classNo = 0 
    # Initial Class number = 0
    if (aggregation == 'a'):
        for indClass in trainingData: 
            classNo += 1
            codeBook.append({classNo: avgf(indClass)})
    elif (aggregation== 'm'):
        for indClass in trainingData: 
            classNo += 1
            codeBook.append({classNo: minf(indClass)})
    elif (aggregation == 'M'):
        for indClass in trainingData: 
            classNo += 1
            codeBook.append({classNo: maxf(indClass)})
    else: 
        raise Exception("Aggregation Type doesn't matches with the defined types")
        return 
    return codeBook

def euclidean (codeWord, testData):
    '''
    Returns the 
    Args:
        codeWord : The Word in codeBook corresponding to each class
        testData : The Data which needs to be tested
    Returns:
        distance : Euclidean Distance
    '''
    distance = 0 
    index = 0
    for feature in codeWord : 
        distance += abs((feature - testData[0][index])*(feature - testData[0][index]))
        index += 1
    return sqrt(distance)

def manhattan (codeWord, testData):
    '''
    Returns the 
    Args:
        codeWord : The Word in codeBook corresponding to each class
        testData : The Data which needs to be tested
    Returns:
        distance : Manhattan Distance
    '''
    distance = 0 
    index = 0
    for feature in codeWord : 
        distance += abs(feature - testData[0][index])
        index += 1
    return sqrt(distance)
    
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
                        our classifier.It's an array of testCases
    ''' 
    testResults = []
    if(similarityMetric == 'e'):
        for indTest in testData: 
            testRes = 0 ## No class numbered 0
            currEucl = 10000000000
            for indTrainData in codeBook: 
                tempEucl = euclidean(indTrainData[indTrainData.keys()[0]], indTest)
                if(tempEucl < currEucl):
                    testRes = indTrainData.keys()[0]
                    currEucl = tempEucl
            testResults.append(testRes)
    elif(similarityMetric == 'm'):
        for indTest in testData: 
            testRes = 0 ## No class numbered 0
            currMan = 10000000000
            for indTrainData in codeBook: 
                tempMan = manhattan(indTrainData[indTrainData.keys()[0]], indTest)
                if(tempMan < currMan):
                    testRes = indTrainData.keys()[0]
                    currMan = tempMan
            testResults.append(testRes)
    else: 
        raise Exception("Similarity metric doesn't matches with the defined types")
        return 
    return testResults

if __name__ == '__main__':
    trainingData = makeTestCases([1,5], 2, 3, 4)
    codeBook = train(trainingData, 'a')
    testData = makeTestCases([1,8], 1, 3, 2)
    print codeBook
    print testData
    print test(testData, codeBook, 'e')
