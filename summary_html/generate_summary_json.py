
#!/usr/bin/python3
import os
import datetime
import sys
import json
import re

#Path to enumerate CVEs from
dir = "../"
CVE_list = []


#fetch all the years
years = os.listdir(dir)
#remove non numeric years
years = [year for year in years if year.isdigit()]
#sort descending (we want the latest at the top)
years.sort(reverse=True)

#clean up the text blocks
def clean_text(description):
    
    #remove the '-' at the beginning of each line
    description_lines = description.split('\n')
    description_lines = [line.lstrip('- ') for line in description_lines]

    #change urls with <a> links with regular expression
    description_lines = [re.sub(r'(https?:\/\/[^\s]+)', r'<a target="_blank" href="\1">\1</a>', line) for line in description_lines]
    
    #add <br/> for each line
    description = '<br/>'.join(description_lines)
    return description



#generate JSON for each CVE
for year in years:
    
    yearDir = os.path.join(dir, year)
    for CVE_filename in os.listdir(yearDir):

        #open CVE file
        CVE_file = open(os.path.join(yearDir, CVE_filename), 'r')
        #read CVE file
        CVE_file_content = CVE_file.read()

        #extract CVE description, references and github
        CVE_description = CVE_file_content.split('### Description')[1].split('###')[0].strip()
        CVE_references = CVE_file_content.split('### Reference')[1].split('###')[0].strip()
        CVE_github = CVE_file_content.split('### Github')[1].split('###')[0].strip()
        
        #TODO: extract imageshield label attributes
        
        CVE_Name = CVE_filename.split('.')[0]
        
        CVE_description = clean_text(CVE_description)
        CVE_github = clean_text(CVE_github)
        CVE_references = clean_text(CVE_references)

        thisCVE = [year,CVE_Name, CVE_description, CVE_github,CVE_references]
        CVE_list.append(thisCVE)

CVE_output = f"dataTable_data = {json.dumps(CVE_list)}"

#save CVE list to JSON file
with open('CVE_list.json', 'w') as outfile:
    outfile.write(CVE_output)