#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = None
    for k in a_dictionary:
        if best_score < a_dictionary[k]:
            best_score = a_dictionary[k]
            best_key = k
            return best_key


