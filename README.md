# Project Title

PDF Metadata Application

## Description

Metadata Fields:  Title, Author, Subject, Keywords, PDF Producer, CreatorTool, PDF Version, Fastweb view
Metadata values should provide in the "meta.ini" file, tool will read this ini file and apply the values in the PDF file.

## Getting Started

### Dependencies

* Windows 7

### Installing

* pip install pikepdf

### Executing program

* Run the program
* Tool will ask to enter the path of the input pdf file
* Tool execute the pdf files and create the output split pdf in the "Output" folder of the same input file  path

##Help

* Enter the Metadata values in the meta.ini file
* Values should enter the within the respective tags, example: <Subject>... Subject Content ...</Subject>.
* If any field not required leave this field as empty tag, example: <Subject></Subject>.
* If any special character present in the meta.ini, then file format should be in "UTF-8"


## Version History

* 0.1
    * Initial Release
