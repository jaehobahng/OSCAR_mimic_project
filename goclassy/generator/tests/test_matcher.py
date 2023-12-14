from generator.corpus_gen import classify
from generator.utils import other
from generator.utils import duplicate

def test_numfile():
    filenames = other.get_filenames('./tests/data/input/')
    for i in filenames: 
        a = classify('./tests/data/input/' + i, './tests/data/output/', lang = ['kor'], n = 1)
        a.classify_files()

    out_names = other.get_filenames('./tests/data/output/')
    assert (len(out_names) == 1)