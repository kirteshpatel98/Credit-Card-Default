#%% md
# FUNCTIONS
#%% md
### Change to Binary
#%%
def change_to_bi(col,col_nam):
    old=list(col[col_nam].unique())
    new=[0,1]
    col[col_nam]=col[col_nam].replace(old,new)
    return col
#%% md
### Change to numeric classification
#%%
def change_to_num(col,col_nam):
    col[col_nam]=col[col_nam].replace(list(col[col_nam].unique()),list(range(0,len(col[col_nam].unique()))))
    return col
#%%
def change_to_bi_check(feature_check,col_name,check_data):
    old=feature_check
    new=[0,1]
    check_data[col_name]=check_data[col_name].replace(old,new)
    return check_data
#%%
def change_to_bi_check_misc(feature_check,col_name,check_data):
    old=feature_check
    new=[1,0]
    check_data[col_name]=check_data[col_name].replace(old,new)
    return check_data
#%%
def change_to_num_check(feature_check,col_nam,check_data):
    check_data[col_nam]=check_data[col_nam].replace(list(feature_check),list(range(0,len(feature_check))))
    return check_data