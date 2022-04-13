from PIL import Image

import glob
import itertools

def combination_generator():
	# Get all assets path for 
	body_paths = glob.glob("assets/body/*")
	eyes_paths = glob.glob("assets/eyes/*")
	mouth_paths = glob.glob("assets/mouth/*")

	paths_list = [body_paths, eyes_paths, mouth_paths]

	# generate unique combinations of the lists of different assets
	return list(itertools.product(*paths_list))

def composer():
	paths = combination_generator()

	# loop through the paths and combine the different assets
	for index, path in enumerate(paths):
		# load the body first since we want to make it as out canvass and put the othr assets on top of the body
		body = Image.open(path[0])
		slime_detail_1 = Image.open(path[1])
		slime_detail_2 = Image.open(path[2])

		# combine first body/part of slime to the body
		slime = Image.alpha_composite(body, slime_detail_1)

		# combine second body/part of slime to the body
		slime = Image.alpha_composite(slime, slime_detail_2)

		# save final image
		slime.save("output/slime_{}.png".format(index))

if __name__ == "__main__":
	composer()