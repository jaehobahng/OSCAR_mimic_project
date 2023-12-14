###
# Hugging Face Setup

# Go to https://oscar-project.github.io/documentation/accessing/ and follow the instructions to download the OSCAR corpus.

# Once the access token is made, in Powershell (or Terminal) run the following command:

# ```huggingface-cli login```

# After running the above code, run the below code and you should have access to the OSCAR data.
###

from datasets import load_dataset
import os

class oscarDataLoader:
    """
    This class contains logic to load in an OSCAR dataset specified by the user.
    """
    def __init__(self, path):
        """
        Initialize the class with the path to the OSCAR dataset, then load in the dataset and assign it to the class.
        """
        self.path = path
        # Run huggingface-cli-login in the terminal to authenticate
        try:
            os.system("huggingface-cli login")
            self.dataset = load_dataset(self.path,
                                        use_auth_token=True, # required
                                        language="ar", 
                                        streaming=True, # optional
                                        split="train") # optional, but the dataset only has a train split
        except:
            raise RuntimeError("Unable to load dataset, please ensure that you have properly authenticated your client with huggingface.")
        
    def get_doc_record_ids(self, date_cutoff, n = 10):
        """
        Find a specified number of document IDs from the loaded dataset that are newer than a specified date.

        Args:
        n - The number of docids to return. Defaults to 10.
        date_cutoff - The date cutoff to use when finding docids. Should be in the following format: "YYYY-MM-DDTHH:MM:SSZ".
        """
        # Create an empty list to store the document ids
        docids = []

        # Create a counter to keep track of how many docids have been found
        i = 0

        # Ensure that date_cutoff is in proper format
        assert(len(date_cutoff) == 20)

        # Iterate through the dataset
        for d in self.dataset:
            if d["meta"]["warc_headers"]["warc-date"] >= date_cutoff:
                # Add the docid to the list
                docids.append(d["meta"]["warc_headers"]["warc-record-id"])
                i += 1
                if i >= n:
                    break
        
        return docids