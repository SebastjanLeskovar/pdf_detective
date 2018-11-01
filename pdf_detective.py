import os
import PyPDF2

print("##### Started program PDF-Detective #####")

# Check if 'pdf_folder' exists. If not, create one.
if os.path.isdir("pdf_folder") == False:
    os.mkdir("pdf_folder")
    print("There was no 'pdf_folder', but it was just created. Copy the PDF files into 'pdf_folder' and restart the program.")

# search_input = "the"
search_input = input("What word would you like to search for? ")

# Dictionary to contain file name and file location
dictionary_of_pdf_files = {}

# Find all PDF files and store them in a dictionary.
def find_pdf_files(folder_location):
    print("===== Searching through files in 'pdf_folder' =====")

    for foldername, subfolders, filenames in os.walk(folder_location):
        for filename in filenames:
            if filename.endswith('.pdf'):
                print("Found PDF file: %s" % filename)

                # Add the PDF file to 'dictionary_of_pdf_files'.
                file_location = os.path.join(foldername, filename)
                dictionary_of_pdf_files[filename] = file_location
            else:
                print("Found non-PDF file: %s, it will be ignored." % filename)


        if len(dictionary_of_pdf_files) == 0:
            print("There are no PDF files in 'pdf_folder'. Copy some  files there and restart the program.")
        # else:
            # print("Dictionary of PDF files: %s" % dictionary_of_pdf_files)

    return(dictionary_of_pdf_files)


def analyse_pdf_files(search_word):
    print("===== Analysing PDF files =====")

    # Iterate through every file in the dictionary.
    for filename, file_location in dictionary_of_pdf_files.items():
        print("=== Analysing file: %s. ===" % filename)
        counter = 0
        pdfFileObj = open(file_location, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # Iterate through every page.
        for pageNum in range(pdfReader.numPages):
            try:
                # print("Analysing page %s..." % (pageNum + 1))
                pageObj = pdfReader.getPage(pageNum)
                pageText = pageObj.extractText()

                # Search each page for 'search_word'. Search should be case-insensitive.
                if search_word.lower() in pageText.lower():
                    print("Found '%s' on page %s." % (search_word, pageNum + 1))
                    counter += 1
            except:
                print("Error: could not analyse page %s." % (pageNum + 1))

        pdfFileObj.close()
        if counter == 0:
            print("No search words found in this PDF.")
        else:
            print("Found %s instances of word '%s'." % (counter, search_word))


# TODO: No need to always call all functions. E.g., if the program detects there is no 'pdf_folder', it does not need to call function 'analyse_pdf_files()'.
find_pdf_files("pdf_folder")

print("Tocka 1", dictionary_of_pdf_files)

analyse_pdf_files(search_input)

print("##### Analysis completed. Please find the results above. #####")

# TODO: Check if search works with two or more words seperated by a space.
