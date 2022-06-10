import os
import re
from pikepdf import Pdf
from datetime import datetime

print("\n PDF Metadata Tool \n")
print("\n Metadata Fields:  Title, Author, Subject, Keywords, \n PDF Producer, CreatorTool, PDF Version \n")
print("\n Developed by A Rajasekaran\n")
print("\n Date: 01 June 2022 \n\n")

'''
- Metadata Information should capture in the "meta.ini" file, within the respective tags
- meta.ini file should be in UTF-8 format
- Tool will get the value from meta ini file and update in the PDF output
- Metadata fields: Title, Author, Subject, Keywords, PDF Producer, CreatorTool, PDF Version
'''

filepath1 = input(" Enter the File path: ")

filepath = filepath1 + "\\"

filelist = os.path.isdir(filepath)

directory = "Output"

Out = filepath + directory

meta = "meta.ini"  # All metadata values should update in the INI file.

if os.path.exists(meta): # check the password.ini file present
    pass
else:
    print("\n meta.ini file is missing")

if os.path.exists(Out):
    pass
else:
    os.mkdir(Out)


fo = open(meta, "r+", encoding="utf-8")
str1 = fo.readlines()

aut = re.search(r"<Author>(.*)</Author>", str(str1))
author = aut.group(1)

tit = re.search(r"<Title>(.*)</Title>", str(str1))
title = tit.group(1)

sub = re.search(r"<Subject>(.*)</Subject>", str(str1))
subject = sub.group(1)

key = re.search(r"<Keywords>(.*)</Keywords>", str(str1))
keyd = key.group(1)

pro = re.search(r"<Producer>(.*)</Producer>", str(str1))
producer = pro.group(1)

ver = re.search(r"<Version>(.*)</Version>", str(str1))
version = ver.group(1)

cret = re.search(r"<CreatorTool>(.*)</CreatorTool>", str(str1))
creatortool = cret.group(1)

fo.close()


for fname in os.listdir(filepath):
	if not fname.endswith(".pdf"):
		continue
	print(fname)
	pdf_file = filepath + fname
	with Pdf.open(pdf_file) as pdf:
		final = Out + "\\" + fname
		with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:         # set_pikepdf_as_editor=False for applying the Producer value
			meta["dc:title"] = title
			meta["dc:creator"] = author
			meta["dc:description"] = subject
			meta["pdf:Keywords"] = keyd
			meta["pdf:Producer"] = producer
			meta["xmp:CreatorTool"] = creatortool
			meta["xmp:CreateDate"] = datetime.now(datetime.utcnow().astimezone().tzinfo).isoformat()   # Current date of file saving date
			meta["xmp:ModifyDate"] = datetime.now(datetime.utcnow().astimezone().tzinfo).isoformat()
		pdf.save(final, linearize=True, force_version=version)	 #	force_version for assigning the PDF version & linearize for assigning the Fastweb view
		pdf.close()
		


