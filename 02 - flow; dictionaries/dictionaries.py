# dictionaries.py  Dictionaries

# - dictionaries are mappings (not sequences)
# - values are stored under a key
# - key can be any immutable type, e.g., number, string, tuple
# - keys are unique; values do not need to be
# - (key, value) pairs have no particular order in the dictionary

# 1. creating dictionaries

# most common methods
expt = dict(subject='jfk', time='14-Jan-1960 16:00', condition='validcue')
expt = {'subject' : 'jfk', 'time' : '14-Jan-1960 16:00', 'condition' : 'validcue'}

# additional methods
expt = dict([('subject', 'jfk'), ('time', '14-Jan-1960 16:00'), ('condition', 'validcue')])
expt = dict()
expt = dict.fromkeys(['subject', 'time', 'condition'])     # create a new dictionary with these keys
expt = dict.fromkeys(['subject', 'time', 'condition'], '') # last argument is default value

# 2. basic dictionary operations

expt['subject']          # get entry corresponding to key 'subject'
expt['subject'] = 'lbj'  # assign entry corresponding to key 'subject'
expt['rt'] = 0.145       # key doesn't have to already exist

del expt['rt']           # delete entry corresponding to key 'rt'
expt['rt']               # error ("raises an exception"; KeyError)

len(expt)                # number of entries

# 3. dictionary methods

# set values
x = expt.setdefault('pcorrect',0.75)  # sets value for key 'pcorrect' if none exists;
                                      # returns final value corresponding to key

newdata = dict(condition='invalidcue', cuepos='left')
expt.update(newdata)  # updates dictionary expt with entries of newdata;
                      # adds new entries, and replaces existing entries

# get values
x = expt.get('rt')         # returns a value corresponding to key 'rt'; if no such key,
                           # returns None, whereas expt['rt'] raises an exception
x = expt.get('rt',0.0)     # as above, but returns default value 0.0 if key doesn't exist
x = expt.pop('rt')         # returns value for key 'rt', and removes the entry from the dictionary
x, y = expt.popitem()      # returns an arbitrary (k,v) entry, and removes it from the dictionary

# shallow copy
expt2 = expt.copy()        # values are the same, not copies; see example on pp. 64-65

# deep copy
from copy import deepcopy
expt2 = deepcopy(expt)

# clear
expt.clear()               # clears all entries

