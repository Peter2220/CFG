# Import necessary libraries
import nltk
import codecs

# Load Grammar file
load_grammar = nltk.data.load('file:Grammar.cfg')
input_file = codecs.open('InputText.txt', 'r')

for sentence in input_file:
    wrong_syntax = 1
    sent_split = sentence.split()
    print("\n\n"+ sentence)
    rd_parser = nltk.RecursiveDescentParser(load_grammar)
    
    """
    Loop through each tree structure in the loaded grammar.cfg file
    If the input text is a correct sentence (correct grammar), 
    append the sentence and Tree structure to a file named CorrectGrammar.txt
    """
    
    for tree_structure in rd_parser.parse(sent_split):
        s = tree_structure
        wrong_syntax = 0
        print("\n Correct Grammar! \n")
        print(str(s))
        f = open("CorrectGrammar.txt", "a")
        f.write(str(sentence) + "" + "Correct Grammar! \n \n")
        f.write(str(s) + "\n \n \n \n")
        f.close()
# Otherwise (Incorrect sentence), append it to a file named IncorrectGrammar.txt        
    if wrong_syntax == 1:
        print("\n Wrong Grammar! \n")
        f = open("IncorrectGrammar.txt", "a")
        f.write(str(sentence) + "" + "\n \n")
        f.close()
