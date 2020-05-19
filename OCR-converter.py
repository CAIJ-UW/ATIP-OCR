""" OCR-converter.py
Author: Kevin Dick
Date: 2020-05-18
---
Description: Optical Character Recognition (OCR) script
that takes in a scanned PDF document, splits it into individual
PNG pages, applies the Tesseract OCR to each, and compiles together
the result in a machine-readable and searchable text-document.
"""
import os, sys
import locale
import ghostscript
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-i', '--input_pdf', required=True,
                    help='path to the scanned PDF document')
parser.add_argument('-o', '--output_dir', required=True,
                    help='the directory where the output will be saved')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='increase verbosity')
args = parser.parse_args()

# EXAMPLE: python3 OCR-converter.py -i /path/to/the/scanned/pdf-file.pdf -o /path/to/the/directory/where/files/will/be/saved/ -v

# Subdirectories for the individual pages
PAGE_IMG = 'page-img'
PAGE_TXT = 'page-txt'

def check_paths():
	""" check_paths
	    This function will verify that the PDF exists and that the output paths are correctly formatted.
	    If the sub-directories for the pages are not present, they will be made.
	    Input:  None
	    Output: <str, None>, error message if input file or output dir don't exist. None, if everything ok.
	"""
	if args.verbose: print('Checking validity of input and creating subdirectories..')
	if not os.path.exists(args.input_pdf):  return f"Error: File {args.input_pdf} doesn't exist."
	if not os.path.exists(args.output_dir): return f"Error: Directory {args.output_dir} doesn't exist."

	# If the page image directory exists, remove everything inside & remake it
	if os.path.exists(os.path.join(args.output_dir, PAGE_IMG)): os.system(f'rm -rf {os.path.join(args.output_dir, PAGE_IMG)}')
	os.mkdir(os.path.join(args.output_dir, PAGE_IMG))

	# If the page text directory exists, remove everything inside and remake it
	if os.path.exists(os.path.join(args.output_dir, PAGE_TXT)): os.system(f'rm -rf {os.path.join(args.output_dir, PAGE_TXT)}')
	os.mkdir(os.path.join(args.output_dir, PAGE_TXT))

def main():
	""" main function """
	# Step 0: We must ensure that the PDF and directory specified exist and the subdirectories for individual pages exist.
	#         We make the subirectories if they dont already exist.
	setup = check_paths()
	if setup != None: 
		# If we get an error message, we print it and exit
		print(setup)
		sys.exit(0)
	
	# These are the two locations where individual files will be saved as well as where the output txt will be saved
	png_dir = os.path.join(os.path.abspath(args.output_dir), PAGE_IMG)
	txt_dir = os.path.join(os.path.abspath(args.output_dir), PAGE_TXT)
	output_txt = os.path.join(os.path.abspath(args.output_dir), os.path.basename(args.input_pdf).replace('.pdf', '.txt'))

	# Step 1: First the PDF is split into individual pages, with one PNG image representing each page of the scanned PDF.
	#         This is achieved using Ghostscript, a suite of software capable of manipulateing and transforming the contents
	#         of PDFs. We move to the directory where Ghostscript will output the individual pages as PNG files:  png_dir.
	#         We then run the following command:
	gs_args = [arg.encode(locale.getpreferredencoding()) for arg in ['', 
									 '-dBATCH', 
									 '-dNOPAUSE', 
									 '-sDEVICE=png16m', 
									 '-r256', 
									 '-sOutputFile=page%d.png', 
									 '-f', os.path.abspath(args.input_pdf)]]
	# Equivalent to this command: gs -dBATCH -dNOPAUSE -sDEVICE=png16m -r256 -sOutputFile=page%d.png {os.path.abspath(args.input_pdf)}
	os.chdir(png_dir)
	ghostscript.Ghostscript(*gs_args)
	#if args.verbose: print(cmd)
	#os.system(cmd)
	
	# Step 2: Secondly, we run the Tesseract OCR on each PNG image and it produces the detected text-based output for each image.
	#         Since we are currently in the PNG subdirectory, we will run over all files in this directory and save them to the
	#         txt_dir.
	for page_png in os.listdir(png_dir):		     # extract all of the filenames in this directory (e.g. "page001.png") 
		if 'page' not in page_png: continue	     # skip any files that don't have 'page' in the name (e.g. .DS_Store)
		page_txt = page_png.replace('.png', '')  # convert the .png to .txt for the output file (the .txt gets added)
		cmd = f'tesseract {page_png} {os.path.join(txt_dir, page_txt)}'
		if args.verbose: print(cmd)
		os.system(cmd)
	
	# Step 3: Finally, we iterate over all txt files in sorted order to compile them into a final document of all pages.
	#         The output file name will be the same as the input file, only with .txt instead of .pdf)
	open(output_txt, 'w').write('') # Create an empty file to save txt data to
	for page_txt in sorted(os.listdir(txt_dir)):
		if 'page' not in page_txt: continue # skip any files that don't have 'page' in the name (e.g. .DS_Store)
		# the 'cat' command prints out the contents of a file
		# the '>>' operator redirects the result of the 'cat' command to the END of the file
		# together, this command simply adds the text of each page to the end of the output txt file.
		cmd = f'cat {os.path.join(txt_dir, page_txt)} >> {output_txt}'
		if args.verbose: print(cmd)
		os.system(cmd)		

if __name__ == "__main__": main()
