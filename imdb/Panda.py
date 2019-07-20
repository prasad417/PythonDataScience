import re


with open("title.ratings.tsv", 'r') as myfile:
    with open("title.ratings.csv", 'w') as csv_file:
        for line in myfile:
            fileContent = re.sub("\t", "\t", line)
            csv_file.write(fileContent)
