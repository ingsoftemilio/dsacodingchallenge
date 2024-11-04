from pprint import pprint

dict1={
    "value":"11"
}

dict2=dict1

#Se modifica tanto dict1 y dict2 porque apuntan al mismo lugar de memoria
dict2['value']="22"

print(id(dict1))
print(id(dict2))

print(dict1)
print(dict2)