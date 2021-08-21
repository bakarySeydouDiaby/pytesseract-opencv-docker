import cv2
import pytesseract

def process_image(image_name, lang_code):
	return pytesseract.image_to_string(cv2.imread(image_name), lang=lang_code)

def print_data(data):
	print(data)

def output_file(filename, data):
	file = open(filename, "w+")
	file.write(data)
	file.close()

def main():
	data_eng = process_image("1_test_eng.png", "eng")
	data_fra = process_image("2_test_fra.png", "fra")
	print("******************eng**********************")
	print_data(data_eng)
	print("******************fra**********************")
	print_data(data_fra)
	output_file("1_text_eng_genere.txt", data_eng)
	output_file("2_text_fra_genere.txt", data_fra)

# programme pricipal
if  __name__ == '__main__':
	main()