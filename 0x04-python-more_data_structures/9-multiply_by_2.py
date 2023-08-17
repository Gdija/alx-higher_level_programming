#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dic = {}
    for i in a_dictionary:
        n_dic[i] = a_dictionary[i] * 2
    return n_dic
