
import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.lines as mlines
import sys
from mpl_toolkits.mplot3d import Axes3D

def visualize_3d(df, lin_reg_weights=[1,1,1], feat1=0, feat2=1, labels=2,
                 xlim=(-2, 2), ylim=(-2, 4), zlim=(-2, 3),
                 alpha=0., xlabel='age', ylabel='weight', zlabel='height',
                 title=''):
    """ 
    3D surface plot. 
    Main args:
      - df: dataframe with feat1, feat2, and labels
      - feat1: int/string column name of first feature
      - feat2: int/string column name of second feature
      - labels: int/string column name of labels
      - lin_reg_weights: [b_0, b_1 , b_2] list of float weights in order
    Optional args:
      - x,y,zlim: axes boundaries. Default to -1 to 1 normalized feature values.
      - alpha: step size of this model, for title only
      - x,y,z labels: for display only
      - title: title of plot
    """

    # Setup 3D figure
    #ax = plt.figure().gca(projection='3d')
    #plt.hold(True)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Add scatter plot
    ax.scatter(df[1], df[2], df[3])

    # Set axes spacings for age, weight, height
    axes1 = np.arange(xlim[0], xlim[1], step=.05)  # age
    axes2 = np.arange(xlim[0], ylim[1], step=.05)  # weight
    axes1, axes2 = np.meshgrid(axes1, axes2)
    axes3 = np.array( [lin_reg_weights[0] +
                       lin_reg_weights[1]*f1 +
                       lin_reg_weights[2]*f2  # height
                       for f1, f2 in zip(axes1, axes2)] )
    plane = ax.plot_surface(axes1, axes2, axes3, cmap=cm.Spectral,
                            antialiased=False, rstride=1, cstride=1)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_xlim3d(xlim)
    ax.set_ylim3d(ylim)
    ax.set_zlim3d(zlim)

    if title == '':
        title = 'LinReg Height with Alpha %f' % alpha
    ax.set_title(title)

    plt.show()


def main():
    """
    YOUR CODE GOES HERE
    Implement Linear Regression using Gradient Descent, with varying alpha values and numbers of iterations.
    Write to an output csv file the outcome betas for each (alpha, iteration #) setting.
    Please run the file as follows: python3 lr.py data2.csv, results2.csv
    """
    data_set = sys.argv[1]
    result = sys.argv[2]

    data = pd.read_csv(data_set, header=None)
    #print(data)
    data.columns =[1, 2, 3]
    #print(data)   
    ones = []
    r, c = data.shape
    for i in range(r):
        ones.append(1)
    data.insert(0, 0, ones, True)
    #print(data)
    one, age_std, weight_std, height_std = data.std()
    one, age_m, weight_m, height_m = data.mean()
    
    data[1] = data[1].apply(lambda x: (x-age_m)/age_std)
    data[2] = data[2].apply(lambda x: (x-weight_m)/weight_std)
    
     
    #print(data)

    def grad_dec(data):
        beta = [0,0,0]
        total_results = [ ]
        inter_results = ['','' ,'','','']
        alphas = [0.001,0.005,0.01,0.05,0.1,0.5,1, 5, 10, .8]
        #alphas = [.8, 0.05,.08, 0.1,0.3, 0.5, 0.6, 0.7,.9, 1] 
        for a in alphas:
            iter = 100
            r, c = data.shape
            beta = [0,0,0]
            inter_results[0] = a
            inter_results[1] = iter
            
            for i in range(iter):
                beta_copy= copy.copy(beta)
                for j in range(len(beta)):
                    #bi = bi - a/n* sum(b0 + b1x1 + b2x2 - Y)* xi
                    beta[j] = beta_copy[j] - (a*(1/r) *\
                        sum((beta_copy[0]*data[0] + beta_copy[1] * data[1] + beta_copy[2] * data[2] - data[3]) * data[j]))
            inter_results[2]= beta[0]
            inter_results[3]= beta[1]
            inter_results[4]= beta[2]
            #print(beta)
            #visualize_3d(data, lin_reg_weights=beta, feat1=0, feat2=1, labels=2,
                #xlim=(-2, 2), ylim=(-2, 4), zlim=(-2, 3),
                #alpha=a, xlabel='age', ylabel='weight', zlabel='height',
                #title='')
            total_results.append(inter_results.copy()) 
            #print((1/(2*len(data[0]))) * sum((beta[0]*data[0] + beta[1] * data[1] + beta[2] * data[2] - data[3])**2))
        result= pd.DataFrame(total_results)
        return result
              
    
    results = grad_dec(data)

    #print(res)
    
    # Write results to file
    out_filename = result
    results.to_csv(result, header = False, index = False)


if __name__ == "__main__":
    main()