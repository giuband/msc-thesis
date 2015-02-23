import seaborn as sns
import json
import matplotlib.pyplot as plt

values = [0, 0, 2, 4, 11]
all_keys = [u'Extremely\ndifficult',
 u'Difficult',
 u'Average',
 u'Simple',
 u'Extremely\nsimple']


plt.bar(range(len(all_keys)), values, align='center')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.title(r'Was it easy to use the application?', fontsize=18)

plt.xticks(range(len(all_keys)), all_keys)

plt.show()