import numpy as np

def gen_sub(df, col1, col2, filename=''):
    '''
    This purpose of this function is to generate an evaluation matrix in the kaggle submission format

    This function takes in a dataframe and 2 columns and returns a new dataframe with just the 2 columns selected.
    There is an optional parameter called filename where, if defined, outputs new dataframe as a csv file to file indicated by filename
    Returns a pandas dataframe with 2 columns, col1 and col2 from df.
    '''
    newDF = df[[col1,col2]]
    newDF = newDF.rename(index=str, columns={col1:'Id', col2:'SalePrice'})
    if filename != '':
        # output the new dataframe to location filename
        newDF.to_csv(filename, index=False)
    return newDF


def rmsle(y_pred, y_test):
    '''
    This function takes in a list of predicted y values and a list of ground truth y values. It then computes the 
    Root Mean Squared Logarithmic Error, or RMSLE. 
    
    This function implements this equation:
    sqrt(mean(((1+y_pred) - (1+y_test))^2))
    '''
    assert len(y_test) == len(y_pred)
    return np.sqrt(np.mean((np.log(1+y_pred) - np.log(1+y_test))**2))
