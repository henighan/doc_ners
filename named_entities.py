import argparse
import docx
import spacy


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename',
            help='docx file you would like to process', type=str)
    return parser.parse_args()


def get_named_entities_set(filename, nlp, ent_types2ignore):
    ddoc = docx.Document(filename)
    named_entities = []
    for para in ddoc.paragraphs:
        sdoc = nlp(para.text)
        named_entities += [ent.text for ent in sdoc.ents
                if ent.label_ not in ent_types2ignore]
    return sorted(list(set(named_entities)))


def main():
    args = parse_args()
    nlp = spacy.load('en')
    ent_types2ignore = set(['DATE', 'TIME', 'PERCENT', 'MONEY',
        'QUANTITY', 'ORDINAL', 'CARDINAL'])
    named_entities = get_named_entities_set(
            args.filename, nlp, ent_types2ignore)
    print('\n'.join(named_entities))


if __name__=='__main__':
    main()
