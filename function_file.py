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

#%%
