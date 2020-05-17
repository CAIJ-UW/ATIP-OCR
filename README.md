# ATIP-OCR (IN PROGRESS...)
It is perennial problem in Canada that municipal, provincial, and federal government agencies disclose records by default in a non-machine readable (image) format. Excel files, for instance, are often printed and scanned by access coordinators before they are released to the requester. In some cases, coordinators may be willing to release the data in a "raw" format, however, this is not always the case. Fortunately, there is a free and open-source solution to this problem using the Tesseract Optical Character Recognition (OCR) engine, widely considered one of the best OCR engines available.

# Sample ATI Disclosures
We provide two sample Access to Information (ATI) Act disclosures. 

1. A-2017-00078: A 251-page, non-machine readable PDF copy of internal correspondence in the Canadian federal government concerning its relationship with the controversial, private American software company known as Palantir.

2. A201700785_2019-05-13_11-33-38: A declassified, 57-page, non-machine readable PDF copy of the Canadian federal government's August 14th briefing on Deferred Prosecution Agreements.

# Code (MacOS)

We recommend first parsing each PDF disclosure package into smaller batches before processing using Tesseract OCR. To process the two example files in this repo, we divided each into single page files. To achieve this, we used Ghoscript.

1. Install Ghostscript in your computer's terminal using Homebrew. To open your computer's terminal, first press command + space, and search "Terminal". Double click the Terminal application listed under Top Hit to open it. Entering the following script into your Terminal's command line:
```
$ brew install ghostscript
```
2. Set your working directly. Your working directory should be the folder that contains the PDF file you wish to convert into machine-readable format. To identify which directory you are current in, type the following script into your Terminal's command line: 
```
pwd
```
To change your directory, type:
```
cd /Name/Of/The/Directory/Containing/Your/File
```
3. Using Ghostscript, convert your PDF disclosure file (stored in your working directory) to individual page PNG files by typing a variation of the following into your Terminal, where "-sDEVICE=png16m" specifies the file conversion format, "-r256" specifies the pixel dimensions of your PNG files, "-sOutputFile=page%03d.png" specifies how each individual page output will be named on your local harddrive, and "input.pdf" specifies the name of the PDF file you want to convert.
```
$ gs -dNOPAUSE -sDEVICE=png16m -r256 -sOutputFile=page%03d.png input.pdf
```
For this code to work, you will need to tailor it to your specific purposes by changing two of the parameters. 

Depending on how many pages are in your PDF file, you will need to the edit the "%03d" section of the "-sOutputFile=page%page03d.png" parameter.  If your file has <10 pages, change this to "%01d" (1 digit), if your file has <100 pages, change this to "%02d" (two digits), if your file has >100 pages but less than <1000, it can be left at "%03d" (three digits), if your file has >1000 pages but less than <10000, it should be changed to "%04d" (four digits), and so on. 

The "input.pdf" parameter should be replaced with the exact name of the file you wish to convert. 

The rest of the parameters can be left the same.

For a PDF file with 40 pages named ATIP.pdf, the script should look like this:
```
$ gs -dNOPAUSE -sDEVICE=png16m -r256 -sOutputFile=page%02d.png ATIP.pdf
```
4. Run each of the individual .png files through Tesseract's OCR engine using the following Python script. Python is installed on MacOS computers by default, so there is no need to install anything. Simply type the following into your Terminal's command line:
```
import os
for page in [x.split('.')[0] for x in os.listdir('page-imgs/')]: os.system(f'tesseract page-imgs/{page}.png page-txt/{page}')
```
