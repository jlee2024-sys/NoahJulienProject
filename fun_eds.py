import pandas as pd

def import_get_var(path_name, var_name):
    '''Imports a data file and returns the data from one variable in the data.

    Arguments:
    path -- the name of the path to the file we want to import, a string.
    name -- the name of the file we want to import, a string.
    var_name -- the header of the data we want to extract, a stirng.
        Must match the header in the file exactly.
    
    Outputs:
    var_data -- the data we want to get out of the dataset;
        the points in the variable var_name.
    '''
    df = pd.read_csv(path_name)
    var_data = df[var_name]
    return var_data

