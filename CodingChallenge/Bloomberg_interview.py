"""'''
Below is a description of a problem about alphabet ordering. This question will involve an exercise
using sample data, and eventually writing a program implementing an algorithm.


If you sampled random words out of the english dictionary and kept them in order, you might get a
list something like this

a
able
ace
aces
but
cat
...

a<b
b<c


This is a simple sorted list of words. Words are sorted in a very particular way, ordered by first
letter, then second letter, etc. A casual reader can see this list and say that it's sorted just by
looking at it, because english speakers know the alphabet order

a b c d e f g ...

It turns out, given a sorted list of words, you can *derive* this alphabet order, even if you don't
know it. As an example of one step of this process, these two words in this order prove that b
comes before c.

able
ace

Below is a sample dataset, sorted with a non-english alphabet order.

Please solve this dataset by hand so we can discuss it. This dataset uses 4 english letters,
(g m t v) ordered in an unusual way.

tmgg
tvm
tvmt
gt
gm
gmvt
vtg
vtgmt
vvmg
vvgm


t=1 m=2 g=3 v=4 ?
1. t<g (t, g)
2. g<v
3. m<v
4. m<g

[(t, g), (g, v), (m,,v) ()]
t m g v



What is the alphabet order used above ? _ _ _ _
'''

'''
['g'=>'t','v'=>'g','v'=>'m','g'=>'m']


#Starting from second word
    Iterate each character and compare it to the index char of my previous word
    If it is equal I will go the next char
    else:
        create the list
        then:
            add previous char in my list_order
        else:
            add current char in my list order
 tmgg
tvm       
'''




def find_order(arr_words):
    
    list_order=[]
    
    # Traverse the array words
    for i,word in enumerate(arr_words):
        # I start on the second word
        if i>0:
            for j,current_char in enumerate(word):
                # Get previoues word
                previous_ch=word[i-1][j]
                if previous_ch==current_char:
                    # Wont do anything
                    pass
                else:
                    # Previous character goes before me, add it to the previous
                    list_order.push(previous_ch)  m v  --> list_order=[m]
                
            
        
    
    return list_order

def addNumbers(a,b):
    sum = a + b
    return sum

num1 = int(input())
num2 = int(input())

print("The sum is", addNumbers(num1, num2))
"""