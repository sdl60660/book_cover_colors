
import pandas as pd
from colorthief import ColorThief
from colormap import rgb2hex, rgb2hsv
from skimage import color
import time


start = time.time()
counter = iter(range(0, 40000))

def get_main_color(img_path):
	true_path = './data/' + img_path
	color_thief = ColorThief(true_path)
	dominant_color = color_thief.get_color(quality=1)

	print(next(counter), time.time() - start)

	return dominant_color


cover_data = pd.read_csv('data/main_dataset.csv')

cover_data['main_cover_color_rgb'] = cover_data['img_paths'].apply(lambda img_path: get_main_color(img_path))
cover_data['main_cover_color_hex'] = cover_data['main_cover_color_rgb'].apply(lambda x: rgb2hex(*x))
cover_data['main_cover_color_hsv'] = cover_data['main_cover_color_rgb'].apply(lambda x: rgb2hsv(*x, normalised=False))
cover_data['main_cover_color_lab'] = cover_data['main_cover_color_rgb'].apply(lambda x: color.rgb2lab([i / 255 for i in x]))

cover_data.to_csv('./data/main_dataset_processed_colors.csv', index=False)
