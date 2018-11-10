

def gen_sub(df, col1, col2, filename=''):
    '''
    This purpose of this function is to generate an evaluation matrix in the kaggle submission format

    This function takes in a dataframe and 2 columns and returns a new dataframe with just the 2 columns selected.
    There is an optional parameter called filename where, if defined, outputs new dataframe as a csv file to file indicated by filename
    Returns a pandas dataframe with 2 columns, col1 and col2 from df.
    '''
    newDF = df[[col1,col2]]
    if filename != '':
        # output the new dataframe to location filename
        newDF.to_csv(filename, index=False)
    return newDF

