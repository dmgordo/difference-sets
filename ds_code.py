import pandas as pd
import numpy as np
import json

f = open('ds.json','r')
diffsets = json.load(f)
f.close()

print(f'read {len(diffsets.keys())} data items\n')

# diffsets is a python dictionary; each entry is the "name" of a set of parameters, e.g. "DS(11,5,2,[11])"
# the dictionary entries contain 
#          "status": either "All", "Yes", "Open" or "No", (all known, exist, open, or known not to exist),
#          "comment": information about how the status is known,
#          "sets": a list of each known difference set
#          "G_rep": the representation of the group elements in the sets, if not given by the invariant factors

# these functions help to access the dictionary



#status of parameters
def get_status(D):
    if 'status' in diffsets[D]:
        return diffsets[D]['status']
    return None

# comment about the type of difference set, or reason for its nonexistence
def get_comment(D):
    if 'comment' in diffsets[D]:
        return diffsets[D]['comment']

# number of sets known for these parameters
def num_sets(D):
    if 'sets' not in D:
        return 0

    return len(D['sets'])

# pull parameters out from name D
def get_v(D):
    S = D.split(',')
    return int(S[0].split('(')[1])

def get_k(D):
    S = D.split(',')
    return int(S[1])

def get_lam(D):
    S = D.split(',')
    return int(S[2])

def get_G(D):
    S = D.split('[')[1].split(']')[0].split(',')
    G = []
    for i in range(len(S)):
        component = S[i]
        G += [int(component)]
    return G

# get the representation group for difference set elements (possibly different than get_G())
def get_Grep(D):
    if 'G_rep' not in diffsets[D]:
        return get_G(D)

    S = diffsets[D]['G_rep']
    G = []
    for i in range(len(S)):
        component = S[i]
        G += [int(component)]
    return G

#get the ith set as a list
def get_set(D,i):
    if 'sets' not in diffsets[D] or (len(diffsets[D]['sets']) <= i):
        print('error: no such set')
        return
    return diffsets[D]['sets'][i]



# get ith (v,k,lam)-difference set in G in this database
def get_ds(v,k,lam,G,i):
    dsname = f'DS({v},{k},{lam},{G})'.replace(' ','')
    if dsname not in diffsets:
        print(f'{dsname} not in database')
        return

    D = diffsets[dsname]
    if 'sets' not in D:
        print(f'no {dsname} difference sets in database')
        return

    if len(D['sets'])<=i:
        print(f'only {len(D["sets"])} {dsname} difference sets in database')
        return

    # if the representation of this group for the difference sets is different
    # than the invariant factors, use that
    if 'G_rep' in D:
        G = D['G_rep']

    return [v,k,lam,G,D['sets'][i]]

# print out information about a given DS
def get_ds_data(v,k,lam,G):
    dsname = f'DS({v},{k},{lam},{G})'.replace(' ','')
    if dsname not in diffsets:
        print(f'{dsname} not in database')
        return

    D = diffsets[dsname]
    if D['status']=="All":
        if num_sets(D)>1:
            print(f'There are exactly {num_sets(D)} DS({v},{k},{lam}) in group {G}')
        else:
            print(f'There is exactly {num_sets(D)} DS({v},{k},{lam}) in group {G}')

    if D['status']=="Yes":
        if num_sets(D)>1:
            print(f'There are at least {num_sets(D)} DS({v},{k},{lam}) in group {G}')
        else:
            if num_sets(D)>0:
                print(f'There is at least {num_sets(D)} DS({v},{k},{lam}) in group {G}')
            else:
                print(f'There is at least one DS({v},{k},{lam}) in group {G}, but it is not in this dataset')

    if D['status']=="No":
            print(f'No DS({v},{k},{lam}) exists in group {G}')

    if 'comment' in D:
        print(f'Reference: {D["comment"]}\n')

    if 'G_rep' in D:
        print(f'DS given as elements of {D["G_rep"]}')

    for i in range(num_sets(D)):
        ds = D['sets'][i]
        if num_sets(D) > 1:
            print(f'{i}:\t',end='')
        for j in range(len(ds)):
            print(f'{ds[j]} ',end='')
        print('')


# find all (v,k,lambda) difference sets for any group
def get_ds_allgroups(v,k,lam):
    dsname = f'DS({v},{k},{lam}'
    dslen = len(dsname)
    for d in diffsets:
        if d[:dslen]==dsname:
            G = d[dslen+1:-1]
            get_ds_data(v,k,lam,G)
            print('')

# code to create tables for showing a list of difference sets
def init_tab():
    T = {}
    T['v'] = []
    T['k'] = []
    T['lambda'] = []
    T['n'] = []
    T['status'] = []
    T['comment'] = []
    return T

def add_tab_entry(T,D):
    v = int(D.split(',')[0].split('(')[1])
    k = int(D.split(',')[1])
    lam = int(D.split(',')[2].split(')')[0])
    n = k-lam
    T['v'] += [v]
    T['k'] += [k]
    T['lambda'] += [lam]
    T['n'] += [n]
    T['status'] += [diffsets[D]['status']]
    T['comment'] += [diffsets[D]['comment']]

def show_tab(T):
    df = pd.DataFrame(T)
    df = df.style.hide(axis='index')
    return df

# simple-minded test to verify that D is a difference set
# there are much nicer ways to do it in Sage, but I'm keeping this
# repo to only minimal python code
def is_ds(D):

    v = D[0]
    k = D[1]
    lam = D[2]
    G = D[3]
    lG = len(G)
    s = (0)*lG
    ds = D[4]

    AC = {}   # autocorrelation of D

    for s1 in ds:
        for s2 in ds:
            if len(G)==1:
                s = ((s1-s2) % G[0],)
            else:
                s = ()
                for i in range(len(G)):
                    s += ((s1[i]-s2[i]) % G[i],)
            if s in AC:
                AC[s] += 1
            else:
                AC[s] = 1
    for g in AC:
        if AC[g] != lam  and g.count(0) != lG:
            return False
    return True


    
    



