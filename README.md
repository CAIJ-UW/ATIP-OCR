# ATIP-OCR
It is perennial problem in Canada that municipal, provincial, and federal government agencies disclose records by default in a non-machine readable (image) format. Excel files, for instance, are often printed and scanned by access coordinators before they are released to the requester. In some cases, coordinators may be willing to release the data in a "raw" format, however, this is not always the case. Fortunately, there is a free and open-source solution to this problem using the Tesseract Optical Character Recognition (OCR) engine, widely considered one of the best OCR engines available.

## Limitations
The Tesseract OCR engine is highly effective, but not perfect. ATI/FOI disclosures are scanned copies of records. Depending on the quality of the scan, not all characters may be properly recognized. Moreover, ATI/FOI disclosures generally contain redactions, usually in the form of white, grey, or black boxes covering undisclosed portions of the text. This can also produce some issues for the OCR engine. As a result, depending on the quality and format of the ATI/FOI records, it is likely that some degree of document "cleaning" will be required after processing them.

## Code (MacOS)

### Step one
Create a new folder on your computer's Desktop called "Sample-ATI-Disclosure". 

Inside of this folder, create two additional folders that we will also need at later steps. Call first the "page-imgs", and the second "page-txt".

Download the sample disclosure PDF file from this GitHub repository and save it in the Sample-ATI-Disclosure folder you just created on your desktop. Note: for the example code to work, you need to keep the file name the same. It should be saved as "A-2017-00078.pdf".

You should now have a folder called "Sample-ATI-Disclosure" saved on your Desktop. Insider of this folder you should see a file called A-2017-00078.pdf and two empty folders called "page-imgs" and "page-txt".

### Step three
We recommend parsing each PDF file into smaller batches before processing using Tesseract OCR. To achieve this, we will be using Ghoscript, which we will download using Homebrew. As not everyone may have Homebrew installed on their computers, we will need to first download Homebrew, which we will then use to download Ghostscript.

Downloading these two applications requires entering only two simple lines of code into your computer's Terminal.

To open your computer's Terminal, press command + space, and search "Terminal". Double click the Terminal application listed under Top Hit to open it. In your Terminal's command line, first install Homebrew by entering the following:
```
mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
```
Next, use homebrew to install ghostscript by entering:
```
brew install ghostscript
```
You should now have successfully downloaded homebrew and ghostcript on your computer and are ready to begin parsing the PDF.

### Step four
Before we can proceed any further, we need to set our working directory. The same as above, we will do this in the Terminal.

Your working directory should be the folder that contains the PDF file you wish to convert into machine-readable format. If you have followed the instructions above, this is the Sample-ATI-Disclosure folder that you created on your computer's Desktop and saved the sample disclosure file in. 

To set your working directory, you will need to furst obtain the name of the directory. On a Mac, this is very easy. Simply open the Sample-ATI-Disclosure folder on your desktop, click the gear wheel at the top, and select the option "Copy "Sample-ATI-Disclosure" as Path Name" from the list. 

Now, in the Terminal command line, change your working directory to this folder, by entering:
```
cd paste/copied/pathway/name/here
```
In place of "paste/copied/pathway/name/here", paste the pathway that you copied in the previous step. The end result should look something like:
```
cd /Users/yourname/Desktop/Sample-ATI-Disclosure
```

### Step five
Using Ghostscript, we will now convert the sample PDF disclosure file to individual page PNG files by typing a variation of the following into your Terminal's command line:
```
gs -dNOPAUSE -sDEVICE=png16m -r256 -sOutputFile=page%03d.png input.pdf
```
Where,
```python
"-sDEVICE=png16m" specifies the file conversion format, 
"-r256" specifies the pixel dimensions of your PNG files, 
"-sOutputFile=page%03d.png" specifies how each individual page output will be named on your local harddrive, and 
"input.pdf" specifies the name of the PDF file you want to convert
```
For this code to work, we will need to tailor it to our specific purposes by changing two of the parameters. 

Depending on how many pages are in your PDF file, you will need to the edit the "%03d" section of the "-sOutputFile=page%page03d.png" parameter.  If your file has <10 pages, change this to "%01d" (1 digit), if your file has <100 pages, change this to "%02d" (two digits), if your file has >100 pages but less than <1000, it can be left at "%03d" (three digits), if your file has >1000 pages but less than <10000, it should be changed to "%04d" (four digits), and so on. 

The "input.pdf" parameter should be replaced with the exact name of the file you wish to convert. 

Therefore, to process the sample PDF disclosure file saved in our Sample-ATI-Disclosure folder, we will adapt it as follows:
```
gs -dNOPAUSE -sDEVICE=png16m -r256 -sOutputFile=page-imgs/page%03d.png A-2017-00078.pdf
```
As there are 251 pages in this file, this may take a few minutes. When it is finished, you should see 251 individual .png files in your Sample-ATI-Disclosure folder.

You should now exit Ghostscript interpreter by typing "quit" into the command line.

### Step six
We are now going to install Tesseract. In the Termiinal command line, type:
```
brew install tesseract
```
Now we are ready to run each of these individual .png files through Tesseract's OCR engine. To do this, we use Python. 

Since Python is installed on MacOS computers by default, there is no need to install anything. Simply type the following into your Terminal's command line and press Enter twice:

```Python
Python
import os
for page in [x.split('.')[0] for x in os.listdir('page-imgs/')]: os.system(f'tesseract page-imgs/{page}.png page-txt/{page}')
```
As there are 251 individual PNG files to process, this can take some time. 

### Step seven

Finally, since we probably don't want the output to be 251 individual machine-reacable txt files, we need to recompile these. We can do this by running the following Python script, again in the Terminal:

```Python
import os

in_dir = 'page-txt'
out_f  = 'compiled.txt'

open(out_f, 'w').write('')
for i in range(1, len(os.listdir(in_dir)) + 1): 
	if i < 10: i = f'00{i}'
	elif i < 100: i = f'0{i}'
	else: pass
	cmd = f'cat {in_dir}/page{i}.txt >> {out_f}'
	print(cmd)
	os.system(cmd)
```

