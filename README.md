# ATIP-OCR (IN PROGRESS...)
It is perennial problem in Canada that municipal, provincial, and federal government agencies disclose records by default in a non-machine readable (image) format. Excel files, for instance, are often printed and scanned by access coordinators before they are released to the requester. In some cases, coordinators may be willing to release the data in a "raw" format, however, this is not always the case. Fortunately, there is a free and open-source solution to this problem using the Tesseract Optical Character Recognition (OCR) engine.

# Sample ATI Disclosures
We provide two sample Access to Information (ATI) Act disclosures. 

1. A-2017-00078: A 251-page, non-machine readable PDF copy of internal correspondence in the Canadian federal government concerning its relationship with the controversial, private American software company known as Palantir.

2. A201700785_2019-05-13_11-33-38: A declassified, 57-page, non-machine readable PDF copy of the Canadian federal government's August 14th briefing on Deferred Prosecution Agreements.

# Code (MacOS)

We recommend first parsing each PDF disclosure package into smaller batches before processing using Tesseract OCR. To process the two example files in this repo, we divided each into single page files. To achieve this, we used Ghoscript.

Install Ghostscript in your computer's terminal using Homebrew. To open your computer's terminal, first press command + space, and search "Terminal". Double click the Terminal application listed under Top Hit to open it.

Install Ghostscript on your computer by entering the following script into your command line terminal:
```
$ brew install ghostscript
```
Using Ghostscript, convert your PDF disclosure file to individual page PNG files by typing a variation of the following into your Terminal, where \textcolor{red}{red} "-sDEVICE=png16m" specifies the file conversion format, "-r256" specifies the dimensions of your PNG files, "-sOutputFile=page%03d.png" specifies how each individual page output will be named on your local harddrive, and "input.pdf" specifies the name of the PDF file you want to convert.
```
$ gs -dNOPAUSE -sDEVICE=png16m -r256 -sOutputFile=page%03d.png input.pdf
```


