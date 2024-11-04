import sys
from pprint import pprint

#CREO MI NODO BASE
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

#CREO MI CLASE LinkedList
class LinkedList:
    def __init__(self,value):
        #CREO UN NODO CON EL VALOR QUE LE DETERMINE
        oNewNode = Node(value)
        #CREO EL HEAD APUNTANDO AL NODO
        self.head = oNewNode
        #CREO EL TAIL APUNTANDO AL NODO
        self.tail = oNewNode
        #DECLARO MI LENGTH INICIAL
        self.length = 1

    #Metodo para imprimir lista de nodos
    def print_list(self):
        
        #Empiezo desde el head
        nodoEnCurso=self.head
        while nodoEnCurso is not None:
            #Imprimo mi valor
            print("Value: ",nodoEnCurso.value)
            #Me asigno al siguiente nodo
            nodoEnCurso = nodoEnCurso.next
        
        self.printLength()
        print("************")

    def printLength(self):
        print("Size linked list: ",self.length)

    #Metodo para append al final de mi linkedList
    def append(self,value):
        #Crear el nuevo nodo para append
        oNewNode = Node(value)

        #Edge case, si el head no tiene valor es porque esta vacia my linkedList
        if self.head is None:
            self.head = oNewNode
            self.tail = oNewNode
        else:
            #El ultimo nodo (tail contiene esta info) que estaba en la lista apuntarlo al nuevo nodo
            self.tail.next = oNewNode
            self.tail = oNewNode

        #Aumento el length
        self.length+=1

        #Opcional para evaluar
        return True
    
    #Metodo para pop del final de mi linkedList
    def pop(self):
        #Cuando no tengo ningun elemento
        #self.printLength()
        if self.length == 0:
            return None
        temp=self.head
        pre=self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        
        return temp.value
    
    #Metodo para agregar un nuevo nodo al primer elemento
    def prepend(self,value):

        #Nuevo nodo
        oNewNode = Node(value)

        #Si la lista esta vacia, head y tail se convierten en este nodo
        if self.length==0:
            self.head=oNewNode
            self.tail=oNewNode
        else:
            #El nuevo nodo va a puntar a lo que es actualmente la cabeza
            oNewNode.next = self.head
            #La cabeza va a ser el nuevo nodo
            self.head = oNewNode
        
        #Aumento el length de la lista
        self.length+=1

        return True
    
    #Metodo para hacer pop_first, eliminar el primer elemento
    def pop_first(self):

        #Cuando no hay elementos, no hago nada
        if self.length==0:
            return None
        #Cuando hay 1 elemento, vacio los elementos:
        elif self.length==1:
            self.head=None
            self.tail=None
        #Cuando hay +1 elemento
        else:
            #La cabeza sera igual al apuntador de la cabeza actual
            #en teoria esta bien y no porque sigue existiendo el primer nodo
            #solo que no esta asignado a nada
            #self.head=self.head.next

            #Para corregir esto, necesitamos un temporal del head
            tmpHead = self.head
            #La cabeza sera igual al apuntador de la cabeza actual
            self.head = self.head.next
            #Remuevo el next del temporal que traia el head anterior para que no apunte a nada
            tmpHead.next=None
            tmpHead=None

        #Decremento my length
        self.length-=1

        return True

    #Retornar el nodo en el indice indicado
    def get(self, index):

        #Edge case
        if index < 0 or index >=self.length:
            return None

        #Itero sobre los elementos el underscore sirve cuando no tenemos una
        #variable que usar
        tmpNodoEnCurso = self.head
        for _ in range(index):
            #Asigno el tmp el nuevo next
            tmpNodoEnCurso=tmpNodoEnCurso.next

            return tmpNodoEnCurso

    #Insertar elemento
    def insert(self,index,value):

        #Edga case
        if index < 0 or index>self.length:
            return False
                    
        if index == 0:#Si es el primer nodo hago prepend
            return self.prepend(value)
        if index == self.length-1:#Si es el ultimo nodo hago el append
            return self.append(value)
        
        #Puede que este en cualquier elemento en medio
        #Obtengo el elemento anterior al indice porque es el que tiene al apuntador
        tmpNodeAnterior=self.get(index-1)
        #Creo un nodo nuevo
        oNewNode = Node(value)
        #El nuevo nodo va apuntar al siguiente nodo del nodo anterior
        oNewNode.next=tmpNodeAnterior.next
        #El nodo anterior ahora va a apuntar al nuevo nodo
        tmpNodeAnterior.next=oNewNode
        #Aumento el length
        self.length+=1
        return True


            
            



my_linked_list = LinkedList(0)
my_linked_list.append(2)

#Hacer prepend
my_linked_list.prepend(4)

# #Eliminar primero
# my_linked_list.pop_first()
# my_linked_list.pop_first()
# my_linked_list.pop_first()
# my_linked_list.pop_first()

my_linked_list.print_list()

#Obtener el nodo con base al indice
print(my_linked_list.get(0).value)

sys.exit(0)

#(2) items - returns 2 nodes
print(f"Value eliminado: {my_linked_list.pop()}")
#(1) items - returns 1 nodes
print(f"Value eliminado: {my_linked_list.pop()}")
#(0) items - returns None
print(f"Value eliminado: {my_linked_list.pop()}")

my_linked_list.prepend(33)
my_linked_list.prepend(65)
my_linked_list.prepend(13)

my_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    