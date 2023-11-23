import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.lines as mlines
import sys


def visualize_scatter(df, feat1 = 0, feat2=1, labels=2, weights=[-1, -1, 1],
                      title=''):
    """
        Scatter plot feat1 vs feat2.
        Assumes +/- binary labels.
        Plots first and second columns by default.
        Args:
          - df: dataframe with feat1, feat2, and labels
          - feat1: column name of first feature
          - feat2: column name of second feature
          - labels: column name of labels
          - weights: [w1, w2, b] 
    """

    # Draw color-coded scatter plot
    colors = pd.Series(['r' if label > 0 else 'b' for label in df[labels]])
    ax = df.plot(x=feat1, y=feat2, kind='scatter', c=colors)

    # Get scatter plot boundaries to define line boundaries
    xmin, xmax = ax.get_xlim()

    # Compute and draw line. ax + by + c = 0  =>  y = -a/b*x - c/b
    a = weights[0]
    b = weights[1]
    c = weights[2]

    def y(x):
        return (-a/b)*x - c/b

    line_start = (xmin, xmax)
    line_end = (y(xmin), y(xmax))
    line = mlines.Line2D(line_start, line_end, color='red')
    ax.add_line(line)


    if title == '':
        title = 'Scatter of feature %s vs %s' %(str(feat1), str(feat2))
    ax.set_title(title)

    plt.show()



def perceptron(data):
    w = np.array([0,0,0]) #list of weights w1,w2,b
    iter = [[0,0,0]]
    converge = False
    r, c = data.shape
    while(converge!=True):
        converge = True
        for index, row in data.iterrows():
            f = w[0]*row[0] + w[1]*row[1] + w[2]
            if f * row[2] <= 0:
                converge = False
                for i in range (len(w)-1):
                    w[i] += 1*row[2] *row[i]
                w[2] += 1*row[2]
        iter.append(w.copy())
        #print(w)        
        
    
    all_weights= pd.DataFrame(iter)
    return all_weights
                    


def main():
    '''YOUR CODE GOES HERE'''
# Import input1.csv, without headers for easier indexing
    data_set = sys.argv[1]
    result = sys.argv[2]

    data = pd.read_csv(data_set, header=None)
    visualize_scatter(data, feat1 = 0, feat2=1, labels=2, weights=[-5, -2, 39],
                      title='')
    results = perceptron(data)

    # Write results to file
    out_filename = result
    results.to_csv(result, header = False, index = False)



if __name__ == "__main__":
    """DO NOT MODIFY"""
    main()