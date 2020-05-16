# coding: utf-8
# Developer: Deiner Zapata Silva.
# Date: 13/05/2020
# Last Update: 13/05/2020
# Description: Algoritms for sorting.
# https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/02.08-Sorting.ipynb#scrollTo=y93ROhjEpvsB
#########################################################################################

import numpy as np

# Sorting arrays
def selection_sort(x):
    for i in range (len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x

def make_dataframe(cols,ind):
    """Quickly make a Dataframe"""
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.Dataframe(data,ind)

class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)
    

if __name__ == "__main__":
    x = np.array([2,1,4,3,5])
    print("x = {0}".format(x))

    print("selection_sort")
    print("{0}".format(selection_sort(x)))

    print("bogosort")
    print("{0}".format(bogosort(x)))

    print("np.sort(x)")
    x = np.array([2,1,4,3,5])
    print("{0}".format(np.sort(x)))

    print("np.argsort(x)")
    x = np.array([2,1,4,3,5])
    print("{0}".format(np.argsort(x)))

    print("Sorting along rows or columns...")
    rand = np.random.RandomState(42)
    X = rand.randint(0,10,(4,6))
    print(X)

    print("sort each column of X")
    print("np.sort(X, axis=0)\n{0}".format(np.sort(X, axis=0)))
    
    print("sort each row of X")
    print("np.sort(X, axis=1)\n{0}".format(np.sort(X, axis=1)))
    
    print("Partial Sorts: Partitioning")
    x = np.array([7,2,3,1,6,5,4])
    print("np.partition(x,3) = {0}".format(np.partition(x,3)))

    np.partition(X, 2, axis=1)
    #np.argpartition()

    # Ploting Sorting
    import matplotlib.pyplot as plt
    import seaborn
    seaborn.set()
    plt.scatter(X[:,0], X[:,1], s=100)
    plt.show()
    
    # Compute the distance between each pair of point. 
    # Recall square-distance between two points is the sum of the square differences in each dimensions; using the efficient broadcasting 
    dist_sq = np.num( (X[:, np.newaxis, :] - X[np.newaxis, :,:] ) ** 2, axis=-1)
    
    # for each pair of points, compute differences in their coordinates
    differences = X[:, np.newaxis, :] - X[np.newaxis, :,:]
    differences.shape

    # square the coordinate differences
    sq_differences = differences ** 2
    print("sq_differences = {0}".format( sq_differences.shape ) )

    # sum the coordinate differences to get the squared distance
    dist_sq = sq_differences.sum(-1)
    print("dist_sq = {0}".format(dist_sq) )

    # The set of distances between each point and itself, is all zero
    print("diagonal = {0}".format( dist_sq.diagonal() ) )

    # We can now use np.argsort to sort along each row.
    # The leftmost columns will then give the indices of the nearest neigbors:
    nearest = np.argsort( dist_sq, axis=1 )

    print("nearest = {0}".format(nearest) ) 
    # The first column the numbers 0 through 9 in order: this is due to the fact that each point's closest neighbor is itself, as we would expect.
    # By using a full sort here, we've actually done more work than we need to in this case.
    # If we're simply interested in the nearest K neighbors, all we need is to partition each row so that the smallest K+1 square distances come first,
    # with larger distances filling the remaining positions of the array. We can do this with the np.argpartition funtion.
    # https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/02.08-Sorting.ipynb#scrollTo=Q1XCuEDKv6XT

    K = 2
    nearest_partition = np.argpartition( dist_sq , K+1, axis=1 )

    plt.scatter(X[:,0], X[:,1], s=100)
    #draw lines from each point to its two nearest neigbors
    for i in range(X.shape[0]):
        for j in nearest_partition[i, K+1]:
            # plot a line from X[i] to X[j]
            # use some zip magic to make it happen:
            plt.plot(*zip(X[j], X[i]), color='black')

    # Creating a dataframes
    x = make_dataframe('AB', [0,1])
    y = make_dataframe('BC', [2,3])

    y.index = x.index # creating duplicates index
    print("x:\n{0}".format(x))
    print("y:\n{0}".format(x))
    
    x_y = pd.concat( [x,y] )
    print("pd.concat( [x,y] )=\n{0}".format(x_y))

    #Catching the repeats index as an error
    try:
        pd.concat( [x,y], verify_integrity=True)
    except ValueError as e:
        print("Index duplicated | Value Error: {0}".format(e))
        print("Try executing: pd.concat([x,y], ignore_index=True)")
    
    pass

