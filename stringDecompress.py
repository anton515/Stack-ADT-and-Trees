

from dataStructures import Stack
import check

## decompressFile(txt) returns a string of the originial file text (txt), 
## where txt is a string type representing the compressed file.
## Effects: Given a original file text (txt) in the pattern k{text_string},
## returns a decompressed Str where the text_string inside the curly
## brackets is being repeated exactly k times.
## decompressFile: Str -> Str
## Requires: Compress text file to be in a repeated pattern: k{text_string},
## where the text_string inside the curly brackets is being repeated 
## exactly k times.
## Examples:
## txt = "2{a}3{bc}", decompressFile(txt) -> "aabcbcbc"
## txt = "2{a3{c}}", decompressFile(txt) -> "acccaccc"
## txt = "3{abc}2{cd}ef", decompressFile(txt) -> "abcabcabccdcdef" 

def decompressFile(txt):
    final = []
    lst = []
    mystack = Stack()
    for token in txt:
        mystack.push(token)
    while not mystack.isEmpty():
        item = mystack.pop()
        lst.insert(0,item)
    for i in range(len(lst)):
        if lst[i] == "{":
            lst[i] = '*!('
        elif lst[i] == "}":
            lst[i] = ')!$'
    lst = str(lst)
    lst = lst.replace("'","")
    lst = lst.replace(",","")
    lst = lst.replace(" ","")
    lst = lst.replace("[","")
    lst = lst.replace("]","")
    lst = lst.replace("!","'")
    lst = lst.replace("(","")
    lst = lst.replace(")","")
    lst = lst.split("$")
    for i in range(len(lst)):
        if "*" in lst[i]:
            final.append(eval(lst[i]))
        else:
            final.append(lst[i])
    final = str(final)
    final = final.replace("[","")
    final = final.replace("]","")
    final = final.replace("'","")
    final = final.replace(",","")
    final = final.replace(" ","") 
    return final

    
## Tests
    
txt1 = "2{a}3{bc}"
check.expect("Q3T1",decompressFile(txt1),"aabcbcbc")
txt3 = "3{abc}2{cd}ef"
check.expect("Q3T3",decompressFile(txt3),"abcabcabccdcdef")
txt4 = "10{a}abc"
check.expect("Q3T4",decompressFile(txt4),"aaaaaaaaaaabc")