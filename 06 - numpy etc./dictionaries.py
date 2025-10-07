# dictionaries.py  Dictionaries

# 1. creating dictionaries

# most common methods
expt = {'subject' : 'jfk', 'time' : '14-Jan-1960 16:00', 'condition' : 'validcue'}
expt = dict(subject='jfk', time='14-Jan-1960 16:00', condition='validcue')

# 2. basic dictionary operations

expt['subject']          # get entry corresponding to key 'subject'
expt['subject'] = 'lbj'  # assign entry corresponding to key 'subject'
expt['rt'] = 0.145       # key doesn't have to already exist

del expt['rt']           # delete entry corresponding to key 'rt'
expt['rt']               # error ("raises an exception"; KeyError)

len(expt)                # number of entries

# - dictionaries are mappings (not sequences)
# - values are stored under a *key*
# - key can be any immutable type, e.g., number, string, tuple
# - keys are unique; values do not need to be
# - (key, value) pairs have no particular order in the dictionary

# 3. dictionary methods

# get values
expt = {'subject' : 'jfk', 'time' : '14-Jan-1960 16:00', 'condition' : 'validcue'}
x = expt.get('rt')         # returns a value corresponding to key 'rt'; if no such key,
                           # returns None, whereas expt['rt'] raises an exception
x = expt.get('rt',0.0)     # as above, but returns default value 0.0 if key doesn't exist
x = expt.pop('time')       # returns value for key 'time', and removes the entry from the dictionary
x, y = expt.popitem()      # returns an arbitrary (k,v) entry, and removes it from the dictionary
