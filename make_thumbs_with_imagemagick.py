#a little interface for image magick with python, cause...why not?
#james munsch
#use this how you wanna
#1-26-13

import os
import argparse
parser = argparse.ArgumentParser(description="This little program will thumbnail images in python as long as imagemagick is installed in linux....works on ubuntu 12.04 64bit, haven't tried it on anything else. Specify input and it outputs that to a directory named dir_thumbed_pics")


#probably would be easier to just use bash but hey why not use some python stuff... but what about PIL... don't know it yet. i guess? 

parser.add_argument('-f','--folder_in', type=str, help="Path to folders with images")
parser.add_argument('-w','--width', type=str, help="Width of thumbed images")

args = parser.parse_args()


directory_in = "/de-app-work/" + args.folder_in + "/"
print "directory:" + directory_in
width = args.width
def make_thumbs():
  #make thumbs in directory
	os.system("cd "+directory_in)
	#make the thumbs dir
	os.system("mkdir dir_thumbed_pics")
	list_dir = []
	for line in os.listdir(directory_in):
		if "jpg" or "JPG" in line:
			list_dir.append(line)
		if "png" or "PNG" in line:
			list_dir.append(line)
		#add a line like above to append the file format
	#use image magick's "convert" to resize the image
	for files in list_dir:
		cmd = "convert "+directory_in+files+" -resize "+width+" thumbed_"+files
		print("command:" + cmd)
		os.system(cmd)

	#mv thumbs to thumbs_path
	os.system('mv thumb* dir_thumbed_pics')

make_thumbs()