import sift
import os
import Image
import time
import math
import heapq
f = open('resultlog','w')
f.write('Initializing \n')
def chunks(l,n):
    return [l[i:i+n] for i in range(0,len(l),n)]
def eucledian_distance(sift_vector_1,sift_vector_2):
	distance = 0
	for i in range(128):
		distance = distance + (sift_vector_1[i]-sift_vector_2[i])**2
	distance = math.sqrt(distance)
	return distance
def eucledian_matcher(image1,image2):
	#print len(image1)
	#print len(image2)
	no_of_matches = 0
	distances = []
	for sift_vector_1 in image1:
		distances = []
		for sift_vector_2 in image2:
			distance = eucledian_distance(sift_vector_1,sift_vector_2)
			distances.append(distance)
		distances.sort()
		if distances[0]/distances[1] < 0.7:
			no_of_matches = no_of_matches + 1
	return no_of_matches
# -------------------------------------------------- SAD FEATURES ----------------------------------------------------------------
directory = './sad'
tempdir = directory.split('/')
dirlength = len(tempdir)
f = open('siftfeatures','w')
siftfeatures_sad = []
picturenames = []
for dirname, dirnames, filenames in os.walk(directory):
# print path to all subdirectories first.
    for filename in filenames:
        #print os.path.join(dirname, filename)
        picturenames.append(filename)
print picturenames
imagenumber = 0
for picture in picturenames[:5]:
	imagenumber = imagenumber + 1
	print 'IMAGE NUMBER' + str(imagenumber)
	print '----------------------------------------'
	os.system('convert ' + 'sad/' + picture + ' processed_picture.pgm')
	sift.process_image('processed_picture.pgm','processed_picture.key')
	locs,descriptors = sift.read_features_from_file('processed_picture.key')
	siftfeatures_sad.append(descriptors)

# --------------------------------------------------- FEAR FEATURES ----------------------------------------------------------------
directory = './fear'
tempdir = directory.split('/')
dirlength = len(tempdir)
f = open('siftfeatures','w')
siftfeatures_fear = []
picturenames = []
for dirname, dirnames, filenames in os.walk(directory):
# print path to all subdirectories first.
    for filename in filenames:
        #print os.path.join(dirname, filename)
        picturenames.append(filename)
print picturenames
imagenumber = 0
for picture in picturenames[:5]:
	imagenumber = imagenumber + 1
	print 'IMAGE NUMBER' + str(imagenumber)
	print '----------------------------------------'
	os.system('convert ' + 'fear/' + picture + ' processed_picture.pgm')
	sift.process_image('processed_picture.pgm','processed_picture.key')
	locs,descriptors = sift.read_features_from_file('processed_picture.key')
	siftfeatures_fear.append(descriptors)

# -------------------------------------------------- HAPPY FEATURES ------------------------------------------------------------------

directory = './smile'
tempdir = directory.split('/')
dirlength = len(tempdir)
f = open('siftfeatures','w')
picturenames = []
siftfeatures_happy = []
for dirname, dirnames, filenames in os.walk(directory):
# print path to all subdirectories first.
    for filename in filenames:
        #print os.path.join(dirname, filename)
        picturenames.append(filename)
print picturenames
imagenumber = 0
for picture in picturenames[:5]:
	imagenumber = imagenumber + 1
	print 'IMAGE NUMBER' + str(imagenumber)
	print '----------------------------------------'
	os.system('convert ' + 'smile/' + picture + ' processed_picture.pgm')
	sift.process_image('processed_picture.pgm','processed_picture.key')
	locs,descriptors = sift.read_features_from_file('processed_picture.key')
	siftfeatures_happy.append(descriptors)

print len(siftfeatures_happy)
# ------------------------------------------------ ANGRY FEATURES ------------------------------------------------------------------------

directory = './anger'
tempdir = directory.split('/')
dirlength = len(tempdir)
siftfeatures_angry = []
picturenames = []
for dirname, dirnames, filenames in os.walk(directory):
# print path to all subdirectories first.
    for filename in filenames:
        #print os.path.join(dirname, filename)
        picturenames.append(filename)
print picturenames
imagenumber = 0
for picture in picturenames[:5]:
	imagenumber = imagenumber + 1
	print 'IMAGE NUMBER' + str(imagenumber)
	print '----------------------------------------'
	os.system('convert ' + 'anger/' + picture + ' processed_picture.pgm')
	sift.process_image('processed_picture.pgm','processed_picture.key')
	locs,descriptors = sift.read_features_from_file('processed_picture.key')
	siftfeatures_angry.append(descriptors)

# ------------------------------------------------- SURPRISED FEATURES -----------------------------------------------------------------------

directory = './surprise'
tempdir = directory.split('/')
dirlength = len(tempdir)
siftfeatures_surprise = []
picturenames = []
for dirname, dirnames, filenames in os.walk(directory):
# print path to all subdirectories first.
    for filename in filenames:
        #print os.path.join(dirname, filename)
        picturenames.append(filename)
print picturenames
imagenumber = 0
for picture in picturenames[:5]:
	imagenumber = imagenumber + 1
	print 'IMAGE NUMBER' + str(imagenumber)
	print '----------------------------------------'
	os.system('convert ' + 'surprise/' + picture + ' processed_picture.pgm')
	sift.process_image('processed_picture.pgm','processed_picture.key')
	locs,descriptors = sift.read_features_from_file('processed_picture.key')
	siftfeatures_surprise.append(descriptors)
# ------------------------------------------------ NEUTRAL FEATURES ----------------------------------------------------------------------------
directory = './neutral'
tempdir = directory.split('/')
dirlength = len(tempdir)
siftfeatures_neutral = []
picturenames = []
for dirname, dirnames, filenames in os.walk(directory):
# print path to all subdirectories first.
    for filename in filenames:
        #print os.path.join(dirname, filename)
        picturenames.append(filename)
print picturenames
imagenumber = 0
for picture in picturenames[:5]:
	imagenumber = imagenumber + 1
	print 'IMAGE NUMBER' + str(imagenumber)
	print '----------------------------------------'
	os.system('convert ' + 'neutral/' + picture + ' processed_picture.pgm')
	sift.process_image('processed_picture.pgm','processed_picture.key')
	locs,descriptors = sift.read_features_from_file('processed_picture.key')
	siftfeatures_neutral.append(descriptors)
# --------------------------------------------- CONTEMPT FEATURES --------------------------------------------------------------------------
directory = './contempt'
tempdir = directory.split('/')
dirlength = len(tempdir)
siftfeatures_contempt = []
picturenames = []
for dirname, dirnames, filenames in os.walk(directory):
# print path to all subdirectories first.
    for filename in filenames:
        #print os.path.join(dirname, filename)
        picturenames.append(filename)
print picturenames
imagenumber = 0
for picture in picturenames[:5]:
	imagenumber = imagenumber + 1
	print 'IMAGE NUMBER' + str(imagenumber)
	print '----------------------------------------'
	os.system('convert ' + 'contempt/' + picture + ' processed_picture.pgm')
	sift.process_image('processed_picture.pgm','processed_picture.key')
	locs,descriptors = sift.read_features_from_file('processed_picture.key')
	siftfeatures_contempt.append(descriptors)

directory = './test_trials_sad'
tempdir = directory.split('/')
dirlength = len(tempdir)
siftfeatures_test = []
picturenames = []
for dirname, dirnames, filenames in os.walk(directory):
# print path to all subdirectories first.
    for filename in filenames:
        #print os.path.join(dirname, filename)
        picturenames.append(filename)
#print picturenames
i = 0
picturenames = chunks(picturenames,5)
new_picturenames = [item[0] for item in picturenames]
picturenames = new_picturenames
print len(picturenames)
time.sleep(2)
imagenumber = 0
for picture in picturenames:
	imagenumber = imagenumber + 1
	print 'IMAGE NUMBER' + str(imagenumber)
	print '----------------------------------------'
	os.system('convert ' + 'test_trials_sad/' + picture + ' processed_picture.pgm')
	sift.process_image('processed_picture.pgm','processed_picture.key')
	locs,descriptors = sift.read_features_from_file('processed_picture.key')
	siftfeatures_test.append(descriptors)
scores = []
for test_vector in siftfeatures_test:
	print '-------------------------------------------------'
	print 'Happy', eucledian_matcher(test_vector[:70],siftfeatures_happy[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_happy[1][:70])
	print 'Sad', eucledian_matcher(test_vector[:70],siftfeatures_sad[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_sad[1][:70])
	print 'Surprise', eucledian_matcher(test_vector[:70],siftfeatures_surprise[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_surprise[1][:70])
	print 'Contempt', eucledian_matcher(test_vector[:70],siftfeatures_contempt[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_contempt[1][:70])
	print 'Neutral', eucledian_matcher(test_vector[:70],siftfeatures_neutral[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_neutral[1][:70])
	print 'Angry', eucledian_matcher(test_vector[:70],siftfeatures_angry[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_neutral[1][:70])
	print 'Fear', eucledian_matcher(test_vector[:70],siftfeatures_fear[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_fear[1][:70])
	scores.append((eucledian_matcher(test_vector[:70],siftfeatures_happy[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_happy[1][:70])))
	scores.append((eucledian_matcher(test_vector[:70],siftfeatures_sad[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_sad[1][:70])))
	scores.append(eucledian_matcher(test_vector[:70],siftfeatures_surprise[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_surprise[1][:70]))
	scores.append(eucledian_matcher(test_vector[:70],siftfeatures_contempt[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_contempt[1][:70]))
	scores.append((eucledian_matcher(test_vector[:70],siftfeatures_neutral[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_neutral[1][:70])))
	scores.append((eucledian_matcher(test_vector[:70],siftfeatures_angry[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_neutral[1][:70])))
	scores.append((eucledian_matcher(test_vector[:70],siftfeatures_fear[0][:70]) + eucledian_matcher(test_vector[:70],siftfeatures_fear[1][:70])))
	print '--------------------------------------------------'
scores = chunks(scores,7)
optimal_sequence = []
for score in scores:
	two_highest = heapq.nlargest(2,score)
	highest_item = two_highest[0]
	second_highest_item = two_highest[1]
	highest_index = score.index(highest_item)
	second_highest_index = score.index(second_highest_item)
	confidence_estimate = float(highest_item)/float(second_highest_item)
	if highest_index == 0:
		optimal_sequence.append(['Happy',confidence_estimate])
		print 'HAPPY'
		f.write('Happy' + '\n')
	if highest_index == 1:
		optimal_sequence.append(['Sad',confidence_estimate])
		print 'SAD'
		f.write('Sad' + '\n')
	if highest_index == 2:
		optimal_sequence.append(['Surprised',confidence_estimate])
		print 'SURPRISED'
		f.write('Surprised' + '\n')
	if highest_index == 3:
		optimal_sequence.append(['Contempt',confidence_estimate])
		print 'CONTEMPT'
		f.write('Contempt' + '\n')
	if highest_index == 4:
		optimal_sequence.append(['Neutral',confidence_estimate])
		print 'NEUTRAL'
		f.write('Neutral' + '\n')
	if highest_index == 5:
		optimal_sequence.append(['Angry',confidence_estimate])
		print 'ANGRY'
		f.write('Angry' + '\n')
	if highest_index == 6:
		optimal_sequence.append(['Fear',confidence_estimate])
		print 'Fear'
		f.write('Fear' + '\n')
optimal_score = 0
prev_item = 'Somethingelse'
for item in optimal_sequence:
	if item[0] == 'Happy' or item[0] == 'Surprised' or item[0] == 'Neutral':
		if item[0] == prev_item:
			optimal_score = optimal_score + item[1]*1.5
		else:
			optimal_score = optimal_score + item[1]
	elif item[0] == 'Sad' or item[0] == 'Angry' or item[0] == 'Fear':
		if item[0] == prev_item:
			optimal_score = optimal_score + (item[1]*-1)*1.5
		else:
			optimal_score = optimal_score + (item[1]*-1)
	print optimal_score
	prev_item = item[0]
if optimal_score < 0:
	print 'There is a good chance he might have depression',optimal_score
	f.write('Verdict : There is a good chance he might have depression. The confidence estimate is : ' + str(optimal_score))
else:
	print 'No apparent signs of depression',optimal_score
	f.write('Verdict : There were no apparent signs of depression. The confidence estimate is : ' + str(optimal_score)) 