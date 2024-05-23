
### Load Packages
import pandas as pd
import numpy as np

#######################################################################################################
## Hand definition
#######################################################################################################
# the variables and process here follows the equation and variables discussed in the README
def levenshtein_distance(word1, word2):
    # Store word length of word1 in m and length of word2 in n
    m, n = len(word1), len(word2)
    # Create a matrix of all 0s with m+1 rows and n+1 columns
    matrix = np.zeros((m+1, n+1), dtype = int)
    # Initialize the first row and column with 0 through the matrix dimensions
    matrix[:, 0] = np.arange(m+1)
    matrix[0, :] = np.arange(n+1)
    # Loop over each character in word1 and word2 
    for i in range(1, m+1):
        for j in range(1, n+1):
            # If the last characters are the same, no addition is required
            if word1[i-1] == word2[j-1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            # Update the current matrix cell
            matrix[i, j] = min(
                matrix[i-1, j] + 1, # deletion
                matrix[i, j-1] + 1, # insertion
                matrix[i-1, j-1] + substitution_cost # replacement
            )
    # Get the last, bottom right cell of the matrix
    lastcell = matrix[m, n]
    # Calculate the similarity percentage by deriving the ratio of the number of edits needed to the maximum length among the words
    similarity = 1 - lastcell / max(m, n)
    similarity_percentage = similarity * 100
    return ('Levenshtein Distance = ' + str(lastcell) + \
            '   Similarity Percentage = ' + str(similarity_percentage) + '%')


## Compare Words
levenshtein_distance('Doctor', 'Dalek')

## Compare array of words
a = ['Doctor', 'River', 'Sonic']
b = ['Dalek', 'Rose', 'Screwdriver']
for i in range(len(a)):
    print("{} and {}: {}". format(a[i], b[i], levenshtein_distance(a[i], b[i])))

## Comparing Sentences
sent1 = 'Hello Sweetie'.split()
sent2 = 'Hello World'.split()
levenshtein_distance(sent1, sent2)



#######################################################################################################
## Package
#######################################################################################################

## Install package if not already
# pip install python-Levenshtein

## Load function
from Levenshtein import distance as lev

# Distance between two strings
lev('Doctor', 'Dalek')

# Distance between two strings in two arrays
a = ['Doctor', 'River', 'Sonic']
b = ['Dalek', 'Rose', 'Screwdriver']
for i in range(len(a)):
    print("Levenshtein Distance between {} and {} = {}". format(a[i], b[i], lev(a[i], b[i])))


# Distance between two sentences
a = 'Hello Sweetie'.split()
b = 'Hello World'.split()
lev(a, b)