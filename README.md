First push: 01.11.2018
Sebastjan Leskovar - [sebastjan.leskovar@gmail.com](mailto:sebastjan.leskovar@gmail.com) - [github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

# PDF Detective

A small Python program for analysing PDF files. The program analyses a large number of PDF files for a specific word.

[https://github.com/SebastjanLeskovar/pdf_detective](https://github.com/SebastjanLeskovar/pdf_detective)

## Getting Started

### Prerequisites

As of version V1.0, the following prerequisites are necessary to run this program:
- Python 3.x
- PyPDF2 1.26.0

Please check the 'requirements.txt' file for an up-to-date list of prerequisites.

### Installation

1. Download the ZIP of the repository.
Click the green button 'Clone or download' and 'Download ZIP'.

2. Extract the ZIP contents on your computer.

### How to use

1. Copy all the PDF files you want to analyse into 'pdf_folder', located at the root of ZIP.
If there is no 'pdf_folder', PDF-Detective will create one at launch.

2. Open the Command Prompt and navigate to the root folder (e.g. cd ...\pdf_detective).
Launch the program with the followind command:
```bash
  > python pdf_detective.py
```

3. The program will ask you to enter a word you would like to search for. Please type in any word.

4. PDF analysis will start, displaying all instances of the word found.

## Versioning

### V4.0

* Implement Tkinter GUI.

### V3.0

* Implement classes.

### V2.0

* Create main() function with logic to launch other functions if needed.
This will remove Bug #1.

#### V1.1

* Bug fixes in file README.md.
* Added files requrements.txt and LICENSE.

### V1.0

* Basic functionality: find PDF files and analyse them.
* Case-insensitive search.
* Check if 'pdf_folder' exists. If it does not, create one.
* Add word counter for each separate PDF.

## Bugs and Issues

1. (Detected 01.11.2018, V1.0) All functions are always called, even if there is no need for them. E.g., if the program detects there is no 'pdf_folder' folder, calling the function 'analyse_pdf_files()' is unnecessary.
Should be removed in V2.0.

2. (Deteched 31.10.2018, V1.0) For some PDF files, the following error is raised:
```bash
 "PdfReadWarning: Xref table not zero-indexed. ID numbers for objects will be corrected. [pdf.py:1736]".
 ```
 The error stopped the program from analysing whole files, but was limited to pages only with try/except method.

3. Search does not yield any results in some example files, although the word is there.
Adding utf-8 encoding might solve this.

## Authors

Sebastjan Leskovar - [sebastjan.leskovar@gmail.com](mailto:sebastjan.leskovar@gmail.com) - [github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

## License

This project is licensed under the MIT License - see the LICENSE file for more details.
