import pandas as pd

def remove_duplicates(file_path):
    """
    The remove_duplicates funciton removes duplicates in each csv file from a given repository.

    Args:
        file_path: File repository where csv files for each langauge is located
    """
    try:
        # Read the TSV file into a DataFrame without header, specifying encoding
        df = pd.read_csv(file_path, sep=',', header=None, encoding='utf-8')

        # Drop duplicates based on the first column (index 0)
        df = df.drop_duplicates(subset=0, keep='first')

        # Save the updated DataFrame back to the original TSV file, specifying encoding
        df.to_csv(file_path, sep=',', index=False, header=False, encoding='utf-8')
    except pd.errors.EmptyDataError as e:
        pass