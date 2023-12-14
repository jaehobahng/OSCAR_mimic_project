import argparse
from generator.corpus_gen import classify
from generator.utils import other
from generator.utils import duplicate
import logging


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Making a corpus out of Common Crawl"
    )
    parser.add_argument("-i", "--indir", required=True, help="Input data directory")
    parser.add_argument("-o", "--outdir", required=True, help="Output data directory")
    parser.add_argument("-l", "--language", nargs="+", required=False, help="language in list", default=[])
    parser.add_argument("-n", "--number", required=False, help="number of characters", default = 100)

    parser.add_argument("-p", "--print", required=False, help="print output size y/n", default = 'y')

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(),  # Output to console
            logging.FileHandler('logfile.log')  # Output to file
        ]
    )

    # Showing a message indicating that iteration has begun
    logging.info("Beginning iteration over the WET files...")
        
    j = 1
    filenames = other.get_filenames(args.indir)
    for i in filenames: 
        a = classify(args.indir + i, args.outdir, args.language, args.number)
        a.classify_files()
        logging.info(f'WET file iteration: {j}')
        j+=1

    # Showing a message indicating that iteration has finished, and that duplicates will now be removed
    logging.info("Finished iteration over the WET files.")
    logging.info("Beginning duplicate removal...")

    filenames = other.get_filenames(args.outdir)
    for filename in filenames:
        logging.info(f'Removing duplicates from {filename}...')
        duplicate.remove_duplicates(args.outdir + filename)
    
    if args.print =='y':
        folder_path = args.outdir  
        folder_size = other.get_folder_size(folder_path)
        logging.info(f'The total size of the folder "{args.outdir}" is: {other.format_size(folder_size)}')
    else:
        pass


# python main.py -i ../../data/input/ -o ../../data/output/ -n 100