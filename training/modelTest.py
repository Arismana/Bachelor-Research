import pandas as pd
import numpy as np
from snownlp import SnowNLP


data_test = pd.read_csv('testData.csv')


s = []
for c in data_test['review']:
    score = SnowNLP(c).sentiments
    if score>=0.5:
        s.append(1)
    else:
        s.append(0)
count = np.sum((s == data_test['label']))
print('准确率为：',count/len(data_test))