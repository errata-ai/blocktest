import spacy


def my_component(doc):  # my_component begin
    print("After tokenization, this doc has %s tokens." % len(doc))
    if len(doc) < 10:
        print("This is a pretty short document.")
    return doc

nlp = spacy.load('en')
nlp.add_pipe(my_component, name='print_info', first=True)
print(nlp.pipe_names) # ['print_info', 'tagger', 'parser', 'ner']
doc = nlp(u"This is a sentence.")  # my_component end

assert nlp.pipe_names == ['print_info', 'tagger', 'parser', 'ner']