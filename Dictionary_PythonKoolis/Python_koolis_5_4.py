#import Python_koolis_5_1 as dictionary

#if 'headaega' not in dictionary.english:
#    dictionary.english['headaega'] = "goodbye"
#if 'headaega' not in dictionary.italian:
#    dictionary.italian['headaega'] = "arrivederci"

#if 'pott' not in dictionary.english:
#    dictionary.english['pott'] = "pot"
#if 'pott' not in dictionary.italian:
#    dictionary.italian['pott'] = "pentola"

#if 'sõnastik' not in dictionary.english:
#    dictionary.english['sõnastik'] = "dizionario"
#if 'sõnastik' not in dictionary.italian:
#    dictionary.italian['sõnastik'] = "dizionario"

#print(dictionary.english, dictionary.italian)

from Python_koolis_5_3 import second
from Python_koolis_5_3 import e_english, e_italian

def add_new_word(estonian, english, italian):
    second.dictionary.english[estonian] = english
    second.dictionary.italian[estonian] = italian
    e_english[italian] = estonian
    e_italian[english] = estonian

add_new_word("headaega", "goodbye", "arrivederci")
add_new_word("pott", "pot", "pentola")
add_new_word("sõnastik", "dictionary", "dizionario")

#if 'headaega' not in e_english:
    #e_english['headaega'] = "goodbye"
#if 'goodbye' not in e_english:
    #e_english['goodbye'] = "headaega"
#if 'headaega' not in e_italian:
    #e_italian['headaega'] = "arrivederci"
#if 'arrivederci' not in e_italian:
    #e_italian['arrivederci'] = "headaega"

if __name__ == '__main__':
    print(second.dictionary.english)
    print(second.dictionary.italian)
    print(e_english)
    print(e_italian)
    print(f"üks -> itaalia = {second.dictionary.italian['üks']}")
    print(f"ciao -> eesti = {e_italian['ciao']}")
    print(f"dog -> itaalia = {second.dictionary.italian[e_english['dog']]}")
    print(f"pentola -> inglise = {second.dictionary.italian[e_italian['pentola']]}")
    