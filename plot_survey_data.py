import seaborn as sns
import json
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 42

# values = [0, 0, 2, 4, 11]
# all_keys = [u'Extremely\ndifficult',
#  u'Difficult',
#  u'Average',
#  u'Simple',
#  u'Extremely\nsimple']
# plt.bar(range(len(all_keys)), values, align='center')
# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')
# plt.title(r'Was it easy to use the application?', fontsize=18)

# plt.xticks(range(len(all_keys)), all_keys)
# plt.savefig('/home/giuseppe/Thesis/Figures/easytouse.pdf')

# plt.show()

# values = [5, 14]
# all_keys = [u'Yes',
#  u'No']
# plt.bar(range(len(all_keys)), values, align='center')
# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')
# plt.title(r'Have you ever seen or interacted with a similar kind of software?', fontsize=18)
# plt.xticks(range(len(all_keys)), all_keys)
# plt.savefig('/home/giuseppe/Thesis/Figures/similarsoftware.pdf')

# The slices will be ordered and plotted counter-clockwise.
# labels = [r'I could understand all of them (42.1 %)', r'I could understand most of them (42.1 %)', 
# r'Some were clear, but others were not (10.6 %)', r"I couldn't understand most of them (5.2 %)", 
# r"I couldn't understand any of them (0 %)"]
# sizes = [42.1, 42.1, 10.6, 5.2, 0]
# colors = ['#56CDF5', '#B8F74A', '#F7F44A', '#F2862E', "#F22E2E"]
# patches, texts = plt.pie(sizes, colors=colors, startangle=90)
# plt.legend(patches, labels, loc="best")
# plt.axis('equal')
# plt.tight_layout()
# plt.title('Did you understand the meaning of the sliders?')
# plt.show()

# labels = [r'I really enjoyed the way music was mixed, it "flowed" (31.5 %)', r'Despite some minor issues, the musical experience flowed well (57.9 %)', 
# r'The music sometimes sounded disconnected and sometimes flowing (5.2 %)', r"The music sounded generally disconnected and I couldn't enjoy it (0 %)", 
# r'I found the music extremely disconnected or "jumpy" (0 %)']
# sizes = [31.5, 57.9, 10.6, 0, 0]
# colors = ['#56CDF5', '#B8F74A', '#F7F44A', '#F2862E', "#F22E2E"]
# patches, texts = plt.pie(sizes, colors=colors, startangle=90)
# plt.legend(patches, labels, loc="best")
# plt.axis('equal')
# plt.tight_layout()
# plt.title('How did you find the musical output?')
# plt.show()

# values = [5, 7, 4, 3]
# all_keys = [u'Extremely\nunfamiliar',
#  u'Unfamiliar',
#  u'Quite familiar',
#  u'Very familiar']
# plt.bar(range(len(all_keys)), values, align='center')
# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')
# plt.title(r"What's your familiarity with this kind of music?", fontsize=18)

# plt.xticks(range(len(all_keys)), all_keys)
# plt.show()

# labels = [r'I think it would make it definitely easier (47.4 %)', r'I think it would make it quite easier (47.4 %)', 
# r'Generally not, but sometimes it could be useful (5.2 %)', r"Just in rare cases (0 %)", 
# r'Not at all (0 %)']
# sizes = [47.4, 47.4, 5.2, 0, 0]
# colors = ['#56CDF5', '#B8F74A', '#F7F44A', '#F2862E', "#F22E2E"]
# patches, texts = plt.pie(sizes, colors=colors, startangle=90)
# plt.legend(patches, labels, loc="best")
# plt.axis('equal')
# plt.tight_layout()
# plt.title('Do you think that this player could make it easier to explore a huge collection of music?')
# plt.show()

labels = [r"It's definitely an improvement and I would use it all the time (5.2 %)", r'I think that I could use this player many times (57.9 %)', 
r'Generally not, but sometimes it could be useful (26.6 %)', r"Just in rare cases (5.2 %)", 
r'Not at all (5.2 %)']
sizes = [5.2, 57.9, 26.6, 5.2, 5.2]
colors = ['#56CDF5', '#B8F74A', '#F7F44A', '#F2862E', "#F22E2E"]
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.title('Is this way of listening to music an improvement over the traditional one?')
plt.show()