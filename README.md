* 01.11.2018

* Sebastjan Leskovar  
* [sebastjan.leskovar@gmail.com](sebastjan.leskovar@gmail.com)
* [https://github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

# PDF-Detective
[https://github.com/SebastjanLeskovar/pdf_detective](https://github.com/SebastjanLeskovar/pdf_detective)
A small Python program for analysing PDF files. The program analyses a large number of PDF files for a specific word.


## Getting Started

### Prerequisites
As of version v1.0, the following prerequisites are necessary to run this program:
- Python 3.x
- PyPDF2 1.26.0

Please also check the 'requirements.txt' file for an up-to-date list of prerequisites.

### Installation
1. Download the ZIP of the repository.
Click the green button 'Clone or download' and 'Download ZIP'.
2. Extract the ZIP contents on your computer.

### How to use
1. Copy all the PDF files you want to analyse into the folder 'pdf_folder', located at the root of ZIP.
If there is no 'pdf_folder', PDF-Detective will create one at launch.
2. Open the Command Prompt and navigate to the root folder (e.g. cd ...\pdf_detective).
Launch the program by typing in:
```bash
  > python pdf_detective.py
```
3. The program will ask you to enter a word you would like to search for. Please type in any word.
4. PDF analysis will start, displaying all instances of the word found.

## Versioning

### V4.0
* Tkinter GUI.

### V3.0
* Implement classes.

### V2.0
* Create main() function with logic to launch other functions.
This will remove Bug #1.

### V1.0
* Basic functionality: find PDF files and analyse them.
* Case-insensitive search.
* Check if 'pdf_folder' exists and if not, create one.

## Bugs and Issues
1. (Detected 01.11.2018, V1.0) All the functions always start, even if there is no need for them. E.g., if the program detects there is no 'pdf_folder' folder, starting the function 'analyse_pdf_files()' is unecessary.
Should be removed in V2.0.

## Authors
Sebastjan Leskovar - [https://github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

License
This project is licensed under the MIT License - see the LICENSE file for more details.
