'''
Vector Quantization
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 12.02.2015
'''

from test import makeTestCases

def avg(classData):
    '''
    Returns the codebook
    Args:
        classData : Training Data which needs to be aggregated
    Returns:
        average of the class elements
    '''
    return sum(classData)*1.0/len(classData)
    
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
            codeBook.append({(classNo, avg(indClass)) : indClass})
    elif (aggregation== 'm'):
        for indClass in trainingData: 
            classNo += 1
            codeBook.append({(classNo, min(indClass)) : indClass})
    elif (aggregation == 'M'):
        for indClass in trainingData: 
            classNo += 1
            codeBook.append({(classNo, max(indClass)) : indClass})
    else: 
        raise Exception("Aggregation Type doesn't matches with the defined types")
        return 
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
    trainingData = makeTestCases([1,5], 3, 4)
    print train(trainingData, 'm')
