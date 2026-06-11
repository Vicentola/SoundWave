class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0  # saber o  tamnho da lista sem precisar percorrar ela inteira


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
        
    def __repr__(self):
        parts = []
        current = self.head
        while current:
            parts.append(repr(current.value))
            current = current.next
        return f"LinkedList({', '.join(parts) if parts else 'None'})"
    

    def pop_front(self):
        if self.head is None:
            raise IndexError("Pop de uma lista vazia")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value
    
    def __len__(self):
        return self.size
    
    
class Stack:
    def __init__(self, max_size=100):
        self._data = []
        self.max_size = max_size
        
    def push(self, value):
        
        """
        verifica se a pilha ja atingiu o tamanho maximo,
        caso tenha atingido o max_size, apaere a mensagem de erro 
        caso contrario, o valor é adicionado a pilha.
        
        """
        
        if len(self._data) >= self.max_size:
            self._data.pop(0)  # Remove o elemento mais antigo (primeiro da lista)
        
        self._data.append(value)
            
            
    def pop(self):
        if not self._data:
            raise IndexError("Pop de uma pilha vazia")
        else:
            return self._data.pop()
        
    def peek(self):
        if not self._data:
            return None
        
        return self._data [-1] # retorna o ultimo elemento da pilha sem remove-lo
        
        
    def __len__(self):
        return len(self._data)
    

class Hashtable:
    
    """
    detabela hash com encadeamento externo que resolve as colisoes
    usa uma lista de buckts on eles guardam pares de (chave e valor)
    
    a funcao set guarda ou atualiza um valor associado a uma chave 
    
    a funcao get busca e retorna o valor de uma chave, ou retorna default se  nao encontar
    """
    
    def __init__(self, capacity = 64):
        self.capacity = capacity
        self._buckets = [[] for _ in range(capacity)]
        
    def set(self, key, value):
        idx= hash(key) % self.capacity
        bucket = self._buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Atualiza o valor existente
                return 
        bucket.append((key, value))  # Adiciona um novo par chave-valor

    def get(self, key, default=None):
        ids = hash (key) % self.capacity
        bucket = self._buckets[ids]
        for k, v in bucket:
            if k == key:
                return v
        return default
    
    def __len__(self):
        return sum(len(bucket) for bucket in self._buckets)
        
        
     
     
     
class BST_Node:
    def __init__(self,key,value):
        
        self.key = key
        self.values = [value]
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
        
    def _insert(self,node, key, value):
        
        if key == node.key:
            
            #a chave já exite so add valor na lista
            
            node.values.append(value)
        
        elif key < node.key:
            
            if node.left is None:
                node.left = BST_Node(key, value) 
            else:
                self._insert(node.left, key, value)
                """logica de arvore se, se for menor 
                que o no atual vai pra esquerda"""
        
        else:
            if node.right is None:
                node.right = BST_Node(key, value)
            else:
                self._insert(node.right, key, value)
                
                
    def insert(self, key, value):
        if self.root is None:
            self.root = BST_Node(key, value)
        else:
            self._insert(self.root, key, value)
            
            
    def search(self, key):
        
        current = self.root
        
        while current is not None:
            if key == current.key:
                return current.values
            elif key < current.key:
                current = current.left
            else:
                    current = current.right
        return []
                      
                
        
        
        
            

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print(ll)  # LinkedList(10, 20, 30)
    print(f"Size of linked list: {ll.size}")  # Size of linked list: 3
    st = Stack(max_size=3)
    st.push("Bohemian Rhapsody")
    st.push("Hotel California")
    st.push("Billie Jean")
    st.push("Superstition")  # deve descartar o mais antigo
    print(st.peek())
    print(len(st))
    ht = Hashtable()
    ht.set("Rock", ["Bohemian Rhapsody", "Stairway to Heaven"])
    ht.set("Pop", ["Billie Jean"])
    print(ht.get("Rock"))
    print(ht.get("Jazz", "não encontrado"))
    print(len(ht))
    bst = BinarySearchTree()
    bst.insert("Queen", "Bohemian Rhapsody")
    bst.insert("Radiohead", "Creep")
    bst.insert("Queen", "We Will Rock You")
    print(bst.search("Queen"))
    print(bst.search("Radiohead"))
    print(bst.search("Beatles"))