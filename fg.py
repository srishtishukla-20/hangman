def test(dictionary):
    for key in dictionary:
        dictionary[key].clear()
    return dictionary

dictionary = { 
               'C1' : [10,20,30], 
               'C2' : [20,30,40],
               'C3' : [12,34]
             }
print("\nClear the list values in the said dictionary:")
print(test(dictionary)) 
