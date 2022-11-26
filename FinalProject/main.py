import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

the_dir = r'C:\Users\aradg\OneDrive - post.bgu.ac.il'
train_data = os.path.join(the_dir, 'train.csv')
train = pd.read_csv(train_data, nrows=10000000,
                   dtype={'acoustic_data': np.int16, 'time_to_failure': np.float64})
print(train.head(5))

train.rename({'acoustic_data':'signal', 'time_to_failure':'quaketime'}, axis='columns', inplace=True)
print(train.head())

fig, ax = plt.subplots(2,1, figsize=(20,12))
ax[0].plot(train.index.values, train.quaketime.values)
ax[0].set_title('Quaketime for 10,000,000 rows')
ax[0].set_xlabel('index')
ax[0].set_ylabel('Quaketime in ms')

ax[1].plot(train.index.values, train.signal.values)
ax[1].set_title('Signal for 10,000,000 rows')
ax[1].set_xlabel('index')
ax[1].set_ylabel('Acoustic signal')
plt.grid()

fig, ax = plt.subplots(3,1, figsize=(20,18))
ax[0].plot(train.index.values[0:10000], train.quaketime.values[0:10000], c='r')
ax[0].set_ylabel('quaketime')
ax[0].set_xlabel('index')
ax[0].set_title('how does the second quaketime pattern look like?')

ax[1].plot(train.index.values[0:9999], np.diff(train.quaketime.values[0:10000]), c='g')
ax[1].set_ylabel('quaketime difference')
ax[1].set_xlabel('index')
ax[1].set_title('Are the jumps always the same?')

ax[2].plot(train.index.values[0:8000], train.quaketime.values[0:8000], c='b')
ax[2].set_ylabel('quaketime')
ax[2].set_xlabel('index')
ax[2].set_title('how does the second quaketime pattern look like? closer look')
fig.tight_layout()
plt.show()