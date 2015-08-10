"""
frame_grabber.py

>>> python frame_grabber.py [from dir] [to dir] [frame capture rate]

"""
import hpidol as hp
import cv2, sys, shutil
import numpy as np
import scipy.misc, os
import pandas as pd
from collections import Counter



def post_img(image):
	return hp.recognize_logos(image)

def get_logos(job_id):
	return hp.get_logos_result(job_id)

def do_videos(from_dir, to_dir, save_time = 1):
	for video_name in os.listdir(from_dir):
		csv_file = to_dir + "/" + video_name[:-4] + ".csv"
		if not os.path.isfile(csv_file):
			f = open(csv_file, 'w')
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

def get_logos_matrix(from_dir, to_file):
	row_names = []
	for csv in from_dir:
		row_names.append(csv[:-4])

	master_frame = pd.DataFrame(index = row_names)
	for csv in from_dir:
		csv_file = from_dir + "/" + csv
		df = pd.read_csv(csv_file)
		found_logos = []
		for item in df["job_id"]:
			found_logos.append(get_logos(item)[0])
		for item in found_logos:
			if item not in master_frame:
				master_frame[item] = 0
			master_frame[item][csv[:-4]] = int(master_frame[item][csv[:-4]]) + 1

	pd.master_frame.to_csv(to_file)
