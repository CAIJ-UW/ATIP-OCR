# ATIP-OCR (IN PROGRESS...)
It is perennial problem in Canada that municipal, provincial, and federal government agencies disclose records by default in a non-machine readable (image) format. Excel files, for instance, are often printed and scanned by access coordinators before they are released to the requester. In some cases, coordinators may be willing to release the data in a "raw" format, however, this is not always the case. Fortunately, there is a free and open-source solution to this problem using the Tesseract Optical Character Recognition (OCR) engine.

# Sample ATI Disclosures
We provide two sample Access to Information (ATI) Act disclosures. 

1. A-2017-00078: A 251-page, non-machine readable PDF copy of internal correspondence in the Canadian federal government concerning its relationship with the controversial, private American software company known as Palantir.

2. A201700785_2019-05-13_11-33-38: A declassified, 57-page, non-machine readable PDF copy of the Canadian federal government's August 14th briefing on Deferred Prosecution Agreements.

# Code

We recommend first breaking the PDF up into smaller image batches before processing using Tesseract OCR. To process the two example files in this repo, we divided each into single image files. The first was thus converted 251 individual image-page items, the second into 57.
