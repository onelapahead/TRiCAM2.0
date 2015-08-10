"""
frame_grabber.py

>>> python frame_grabber.py [from dir] [to dir] [frame capture rate]

"""
import hpidol as hp
import cv2, sys, shutil
import numpy as np
import scipy.misc, os



def post_img(image):
	return hp.recognize_logos(image)

def do_videos(from_dir, to_dir, save_time = 1):
	for video_name in os.listdir(from_dir):
		csv_file = to_dir + "/" + video_name[:-4] + ".csv"
		if csv_file.exists():
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

