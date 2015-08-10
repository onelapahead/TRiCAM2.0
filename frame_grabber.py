"""
frame_grabber.py

>>> python frame_grabber.py [from dir] [to dir] [frame capture rate]

"""
import hpidol as hp

def post_img(image):
	return hp.recognize_logos(image)


if __name__ == "__main__":
	import cv2, sys, shutil
	import numpy as np
	import scipy.misc, os

	api_key = ""

	from_dir = str(sys.argv[1])
	to_dir = str(sys.argv[2])
	
	try: save_time = float(sys.argv[3])
	except: save_time = 1
	
	print save_time

	try:
		os.makedirs(to_dir)
	except OSError:
		shutil.rmtree(to_dir)
		os.makedirs(to_dir)
	

	for video_name in os.listdir(from_dir):
		print video_name

		text_file = to_dir + "/" + video_name[:-4] + ".csv"
		f = open(text_file, 'w')
		f.write("video_time,job_id\n")

		video_file = from_dir + "/" + video_name
		cap = cv2.VideoCapture(video_file)

		seconds_from_start = 0
		
		while cap.isOpened():
			ret, frame = cap.read()
			if not ret:
				break
			
			video_time = cap.get(cv2.cv.CV_CAP_PROP_POS_MSEC)
			
			if ((video_time/1000) - seconds_from_start) > 1:
				
				frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				job_id = post_img(frame, api_key)
				f.write(str(video_time/1000) + "," + str(job_id) + "\n")
				seconds_from_start += save_time

		f.close()