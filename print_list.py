import sys, os
import essentia
from operator import itemgetter
from ConfigParser import SafeConfigParser
from essentia.standard import MetadataReader
import pyechonest.config as echo_conf
import pyechonest.track as echo_track
import time

parser = SafeConfigParser()
parser.read('config.ini')

api_key = parser.get('echonest', 'apikey')
echo_conf.ECHO_NEST_API_KEY = api_key
path = sys.argv[1]
output_file = sys.argv[2]

files = []

# find files that need to be analyzed
for dirpath, dirnames, filenames in os.walk(path):
	for filename in [f for f in filenames if f.endswith(".mp3")]:
		files.append(os.path.join(dirpath, filename))

all_files = []
count = 0

for filename in files:
	metadata_reader = MetadataReader(filename = filename) 
	metadata = metadata_reader()
	track_title = metadata[0]
	track_artist = metadata[1]
	track_year = metadata[6]
	while True:
		try:
			pytrack = echo_track.track_from_filename(filename)
			pytrack.get_analysis()
			break
		except:
			print "Error encountered"
			time.sleep(60)
	echonest_id = pytrack.id
	count +=1 
	print "Files analyzed: ", count
	echonest_id = echonest_id.decode('utf-8')
	all_files.append({"title": track_title, "artist": track_artist, "year": track_year, "echonest_id": echonest_id})

all_files.sort(key=itemgetter('artist', 'year', 'title'))

# echonest_example = echo_track.track_from_filename(files[0])
# echonest_example.get_analysis()
# for key in echonest.keys():
# 	print key

f = open(output_file, 'w')
for file_ in all_files:
	track_title = file_["title"]
	track_artist = file_["artist"]
	track_year = file_["year"]
	echonest_id = file_["echonest_id"].encode('ascii','ignore')
	track_title = track_title.replace("&", "\&")
	track_artist = track_artist.replace("&", "\&")
	track_year = track_year.replace("&", "\&")
	output_str = track_title + " & " + track_artist + " & " + track_year + " & " + echonest_id + " \\\\ \hline \n"
	f.write(output_str)
f.close() 