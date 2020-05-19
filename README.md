# ATIP-OCR
It is perennial problem in Canada that municipal, provincial, and federal government agencies disclose records by default in a non-machine readable (image) format. Excel files, for instance, are often printed and scanned by access coordinators before they are released to the requester. In some cases, coordinators may be willing to release the data in a "raw" format, however, this is not always the case. Fortunately, there is a free and open-source solution to this problem using the Tesseract Optical Character Recognition (OCR) engine, widely considered one of the best OCR engines available.

## Limitations
The Tesseract OCR engine is highly effective, but not perfect. ATI/FOI disclosures are scanned copies of records. Depending on the quality of the scan, not all characters may be properly recognized. Moreover, ATI/FOI disclosures generally contain redactions, usually in the form of white, grey, or black boxes covering undisclosed portions of the text. This can also produce some issues for the OCR engine. As a result, depending on the quality and format of the ATI/FOI records, it is likely that some degree of document "cleaning" will be required after processing them.

## Code (MacOS)

The goal of this tutorial is to walk you through how to render your scanned, image format ATI/FOI disclosures machine readable in a txt format. For learning purposes, we recommend following the steps using one of the sample ATI disclosures provided in the repository. 

### Step one: download the repository
Download the repository, unzip the folder, and save it locally on your computer's harddrive. 

### Step two: open your computer's command prompt
Open your computer's command prompt. On MacOS, this is called the Terminal. To open the Terminal, simply press Command + Space and enter the word "Terminal" in the search bar. Double click the Terminal application listed under Top Hit to open it.

### Step three: install Homebrew
*If you already have Homebrew installed on your computer, skip this step.

Download Homebrew by entering the following command into your computer's Terminal:
```
mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
```

### Step four: install Ghostscript using Homebrew
*If you already have Ghostscript installed on your computer, skip this step.

Download Ghostscript using Homebrew by entering the following command into your computer's Terminal:
```
brew install ghostscript
```

### Step five: install Tesseract using Homebrew
*If you already have Tesseractc installed on your computer, skip this step.
```
brew install tesseract
```

### Step six: copy the pathname of the folder you downloaded, unzipped, and saved in step one
We need to obtain the full directory pathname of the folder that you downloaded, unzipped, and saved in step one. This is a copy of the repistory and contains the sample ATI disclosures and scripts we will need to run the Tesseract OCR engine. To obtain the exact pathname to this folder, simply open the folder on your computer, click the gear wheel at the top, and select the "copy <folder name> as Pathname" option from the list. This will copy the name of the pathname to your clipboard.
	
### Step seven: change your working directory in the Terminal
Change your working directory using the pathname you just copied to your clipboard in step six. To do this, we will return to the Terminal, first writing "cd" followed by the pathname we just copied (pasted into the Terminal using command + V). The end result will look something like this:
```
cd <path/name>
```
To be more exact, if your name was Jane, and you saved the folder on your desktop, it would look like this:
```
cd /Users/jane/Desktop/ATIP-OCR-master
```
To double check that you are in the correct directory, you can enter the following into your Terminal, which will tell you the name of your current directory and print off the name of the files contained in it:
```
ls
```

### Step eight: create an output subfolder
To process our ATIP disclosure file rendering it machine readable, we are going to be first parsing the file into individual page elements, running each of these page elements through the Tesseract OCR engine, and recompiling the .txt files generated from each individual page item into a single .txt file that we can then analyze. Throughout these processing stages, a lot individual .png and .txt files are going to be generated, and these need to be stored somewhere.

Inside the ATIP-OCR-master folder, our working directory, create a new subfolder. You can call this folder whatever you like. If you are using one of the sample ATI disclosures in the Sample-ATI-Disclosures folder, you might name the folder after the sample record you are processing, for example "A-2017-00078". 

To check that this has worked, return to your Terminal and enter the following command (which we learned earlier):
```
ls
```
You should now see the name of your new subfolder listed with the other files in your working directory.

### Step nine: run the script
We are now ready to process our ATIP disclosure file using Ghostcript (to parse the file into individual page elements) and Tesseract (OCR engine). This stage can take several minutes (or hours) depending on the size of the file.

To do this, we are going to be running a simple Python script (in you working directory, this is the OCR-converter.py file). All we need do is obtain the correct pathname for our input file (the ATIP disclosure file) and the correct pathname for our ouput file (the subfolder we created in step eight) and we are ready to go.

The basic formula is:
```
python OCR-converter.py -i <input/file/pathname> -o <output/folder/pathname>
```
So, let's say we are going to run the script on the A-2017-00078.pdf file in the Sample-ATI-Disclosures subfolder, and we are going to store the results in the subfolder we created in step eight called A-2017-00078. The result would look like this:
```
python OCR-converter.py -i Sample-ATI-Disclosures/A-2017-00078.pdf -o A-2017-00078
```
