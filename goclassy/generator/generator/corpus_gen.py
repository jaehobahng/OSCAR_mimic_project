import csv
import io
import re
from generator.utils.warcread import read

class classify:
    """
    Args:
        input: directory of folder with wet files
        output: directory of folder to output csv files
        lang: Languages that we wish to create corpus(input in list form)
            ex) ['kor','eng']
        n: Number of minimum characters a text must have to be included in the output text corpus

    Output: Separate csv files of all the langauges the user chooses to output
    """
    def __init__(self, input, output, lang=[], n=100):
        self.input = input
        self.lang = lang
        self.output = output
        self.n = n
        
    def classify_files(self):
        try:
            with open(self.input, "rb") as infile:
                buf_in = io.BufferedReader(infile)
                a = read(buf_in)

                for record in iter(lambda: a.read_warc_record(), {"header": "", "body": b""}):
                    input_string = record['header']
                    # Use regular expression to extract the value after "Identified-Content-Language:"
                    match = re.search(r'WARC-Identified-Content-Language:\s*(\w+)', input_string)

                    if match:
                        identified_language = match.group(1)
                        # First match that appears after the identified-content-language text
                        
                        # Output all languages into csv files if lang argument is a blank list
                        if self.lang == []:
                            with open(self.output+identified_language+'.csv', 'a', newline='',encoding='utf-8-sig') as csvfile:
                                csvwriter = csv.writer(csvfile, delimiter=',')
                                for line in str(record['body']).split('\n'):
                                    if len(line) > int(self.n):
                                        csvwriter.writerow([line, record['header']])
                        
                        # If 'lang' is not a blank list, only output langauges that were given as an input for the lang variable
                        else:
                            for i in self.lang:
                                if identified_language == i:
                                    with open(self.output+identified_language+'.csv', 'a', newline='',encoding='utf-8-sig') as csvfile:
                                        
                                        csvwriter = csv.writer(csvfile, delimiter=',')
                                        for line in str(record['body']).split('\n'):
                                            if len(line) > int(self.n):
                                                csvwriter.writerow([line, record['header']])
                    else:
                        pass

                    # Move the buffer position to read next header in wet file
                    buf_in.readline()
                    buf_in.readline()

        except ValueError as e:
            print("End of file")
