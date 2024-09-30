# chapter05_code.py  Strings

# 5.1 Introduction

# creating strings

result1 = 'tracking error mean: M = 1.245 mm'

result2 = "tracking error standard deviation: s = 0.212 mm"

instructions = '''This experiment will test your ability to track 
a moving target. You will see a red dot moving unpredictably
across the screen, and your goal is to use the mouse to keep
a plus-shaped cursor on top of the red dot.'''

# indices and slices
result1[0]
result1[0:8]

# length of a string
len(result1)

# concatenating strings
'mean' + ' and ' + 'standard deviation'

# 5.2 f-strings

# using an f-string
err_mean = 1.245897
message = f'The mean tracking error was {err_mean} mm.'

# doing a calculation in an f-string
err_mean = 1.245897
err_std = 0.2124194
message = f'( {err_mean - 1.96*err_std}, {err_mean + 1.96*err_std} )'

# formatting results in an f-string

message = f'( {err_mean - 1.96*err_std:.3f}, {err_mean + 1.96*err_std:.3f} )'

total_time = 384.122
message = f'The total time was {total_time:.0f} s.'

# looping over a list
response_times = [3.41222, 4.12, 12.1454]
for r in response_times:
    print(r)

# looping over two lists
participants = ['jfk', 'lj', 'rn']
response_times = [3.41222, 4.12, 12.1454]
for p, r in zip(participants, response_times):
    print(p, r)

# padding results
for p, r in zip(participants, response_times):
    print(f'{p:5s}{r:10.3f}')

# padding on the left or right, and centering
subject = 'jfk'
print(f'---{subject:<10s}---')
print(f'---{subject:>10s}---')
print(f'---{subject:^10s}---')

# creating a line of data for a text file

data = [[1, 1, 0.0161, 0, 0, 104, 210],
        [1, 2, 0.032445, 0, 2, 110, 215],
        [1, 3, 0.048, 1, 5, 115, 220]]

for d in data:
    framedata = f'{d[0]},{d[1]},{d[2]:.6f},{d[3]},{d[4]},{d[5]},{d[6]}'
    print(framedata)

# 5.3 Other ways of creating strings

message = 'The mean tracking error was ' + str(err_mean) + ' mm.'

message = 'mean %.3f mm, standard deviation %.3f mm' % (err_mean, err_std)

message = 'mean {0} mm, standard deviation {1} mm'.format(err_mean, err_std)

# 5.4 String methods

filename = 'stimulus001.tif'
filename2 = filename.replace('.tif', '.jpg')

filename[11:15] = '.jpg'  # error

filename2 = 'stimulus001.tif'.replace('.tif','.jpg')

participant_initials = 'JfK'
participant_initials.upper()
participant_initials.lower()

filename = 'ra/Desktop/experiment/data.txt'
fileparts = filename.split('/')

participant_list = ['jfk', 'lbj', 'rmn', 'grf', 'jec']
str_list = ', '.join(participant_list)

# 5.5 Escape sequences

phrase = 'It's not easy being green.'  # error
phrase = "It's not easy being green."

phrase = '"It's not easy being green," says Kermit.'  # error

phrase = 'It\'s not easy being green.'
phrase = "\"It's not easy being green,\" says Kermit."

report = 'file 1\tC:\\Users\\rfm\\Desktop\\data.txt\n\nend of list'

# 5.6 More random numbers

import random
stimulusLeft = random.choice([True, False])

p = 0.80
validCue = random.uniform(0, 1) < p

validCue = int(random.uniform(0, 1) < p)

