class Node():

    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

    def __str__(self):
        return "Node-" + str(self.value)
    

class Lista():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    
    def _perc(self, index): # get_node()
        if index < 0 or index >= self.size:
            raise Exception("ÍNDICE INVÁLIDO!")
        
        node = self.head

        for i in range(index):
            node = node.next

        return node
    

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        
        self.size += 1


    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise Exception("ÍNDICE INVÁLIDO!")
        
        new_node = Node(value)
        if index == 0:
            if self.head is None:
                self.add(value)
            
            else:
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node
                self.size += 1
                
        else:
            node = self.head
            for i in range(index - 1):
                node = node.next

            _next = node.next
            new_node.previous = node
            new_node.next = _next
            node.next = new_node

            if _next is not None:
                _next.previous = new_node

            else:
                self.tail = new_node
            
            self.size += 1
        

    def set_value(self, index, value):
        if self.size == 0:
            raise Exception("LISTA VAZIA!")
        
        if index < 0 or index > self.size:
            raise Exception("ÍNDICE INVÁLIDO!")
   
   
        node = self.head
        for i in range(index):
            node = node.next
            
        node.value = value
            
   
    def get_index(self, value):
        node = self.head
        index = 0

        while node is not None:
            if node.value == value:
                return index
            node = node.next
            index += 1
        
        return -1 # NÃO ENCONTRADO


    def remove_value(self, value):
        nodeAtual = self.head

        while nodeAtual is not None:
            if nodeAtual.value == value:
                if nodeAtual == self.head: # SE O VALOR TIVER NO INÍCIO
                    self.head = nodeAtual.next
                    if self.head is not None:
                        self.head.previous = None
                    else:
                        self.tail = None # A LISTA SÓ TINHA UM NODE, AGORA TÁ VAZIA
                    
                elif nodeAtual == self.tail: # SE TIVER NO FINAL DA LISTA
                    self.tail = self.tail.previous
                    self.tail.next = None

                else: # SE TIVER NO MEIO DA LISTA
                    nodeAtual.previous.next = nodeAtual.next
                    nodeAtual.next.previous = nodeAtual.previous


                self.size -= 1
                return True

            nodeAtual = nodeAtual.next

        return False # NÃO ENCONTRADO


    def remove_index(self, index):
        if index < 0 or index >= self.size or self.size == 0:
            raise Exception("INVÁLIDO!")

        if index == 0: # SE O VALOR ESTÁ NO INÍCIO, HEAD APONTA PARA O PRÓXIMO
            nextNode = self.head.next
            self.head = nextNode
            self.size -= 1
            return True
        else:
            node = self.head
            i = 0
            while i < index:
                node = node.next
                i += 1
            
            _next = node.next
            node.previous.next = _next
            if _next is None:
                self.tail = node
                self.tail.next = None 

            self.size -= 1
            return True

            
    def slice(self, start, end):
        # Retorna uma nova lista contendo os nós entre os índices start e end

        if self.size == 0:
            raise Exception("LISTA VAZIA")
        if start < 0 or start >= self.size:
            raise Exception("ÍNDICE INVÁLIDO")

        if end < 0 or end >= self.size:
            raise Exception("ÍNDICE INVÁLIDO")
        
        if start > end:
            raise Exception("End não pode ser menor que Start")
        
        
        newList = Lista()
        node = self.head

        for i in range(start):
            node = node.next
    
        for i in range(start, end + 1): # A função Range para 1 posição antes... Logo, somamos +1
            newList.add(node.value)
            node = node.next
            
        return newList


    def sum(self):
        # Retorna a soma de todos os valores na lista

        if self.size == 0:
            return 0
        
        node = self.head
        _sum = 0
        while node is not None:
            _sum += node.value
            node = node.next

        return _sum
        

    def sum_index_par(self):
        # Retorna a soma dos valores nos índices pares

        if self.size == 0:
            return 0
        
        node = self.head
        _sum = 0
        for i in range(self.size):
            if i % 2 == 0:
                _sum += node.value
            node = node.next

        return _sum

    
    def sum_index_impar(self):
        # Retorna a soma dos valores nos índices ímpares

        if self.size == 0:
            return 0
        
        node = self.head
        _sum = 0
        for i in range(self.size):
            if i % 2 != 0:
                _sum += node.value
            node = node.next

        return _sum
    
    
    def impar_par(self):
        #Trocar os valores nos indexs par e impar
        # o index 0 vai para o 1 e o 1 para para o 0
        # 3 para o 4 e o 4 para o 3 e assim vai
        #[10, 20, 30, 40]
        #[20, 10, 40, 30]

        node = self.head
        
        while node is not None and node.next is not None:
            atual_value = node.value
            node.value = node.next.value
            node.next.value = atual_value

            node = node.next
            node = node.next


    def count(self, value):
        # Conta quantas vezes um valor aparece na lista

        if self.size == 0:
            raise Exception("LISTA VAZIA")
        
        node = self.head
        vezes = 0
        while node is not None:
            if node.value == value:
                vezes += 1
            node = node.next

        return vezes
        

    def contains(self, value):
        # Retorna True se o valor estiver na lista, False se não estiver

        if self.size == 0:
            raise Exception("LISTA VAZIA")
        
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next

        return False
        

    def find_middle(self):
        # Retorna o valor do nó que está no meio da lista

        if self.size == 0:
            raise Exception("LISTA VAZIA")
        
        
        node = self.head
        centro = self.size / 2 
        valorCentral = ''

        # Se a lista for PAR, retorna os dois centrais
        if self.size % 2 == 0: 
            
            for i in range(int(centro - 1)):
                node = node.next
            valorCentral = '[' + str(node.value) + ', ' + str(node.next.value) + ']'
            return valorCentral

        else:
            # Se a lista for IMPAR, aí sim retorna o central

            for i in range(int(centro - 1)):
                node = node.next
            
            valorCentral = '[' + str(node.value) + ']'
            return valorCentral


    def clear(self):
        # Remove todos os nós da lista

        if self.size == 0:
            return True

        
        node = self.head
        while node is not None:
            node.previous = None
            node = node.next
            
        self.head = None
        self.tail = None
        self.size = 0

        return True
    

    def invert(self):
        if self.size == 0 or self.size == 1:
            return
        
        node_final = self.tail
        new_lista = Lista()

        while node_final is not None:
            new_lista.add(node_final.value)
            node_final = node_final.previous

        self.head = new_lista.head
        self.tail = new_lista.tail


    def invert_index(self, index_a, index_b):
        
        if index_a < 0 or index_b < 0:
            raise Exception("ÍNDICE INVÁLIDO!")
        
        if index_a == index_b:
            return # SE É IGUAL, NÃO PRECISA FAZER NADA
        
        
        node_a = self._perc(index_a)
        node_b = self._perc(index_b)

        # É melhor fazer essa troca ao mesmo tempo, Atribuição Múltipla
        node_a.value, node_b.value = node_b.value, node_a.value
    

    def reverse(self):
        # Inverte a lista, o último nó se torna o primeiro
        if self.size == 0 or self.size == 1:
            return
        
        head = self.head.value
        tail = self.tail.value
        self.head.value = tail
        self.tail.value = head


    def merge(self, other_list): 
        # A lista que vai passar em other_list é uma lista do nosso tipo lista
        # Combina outra lista no final da lista atual
        
        if other_list.head is None:
            return

        if self.tail is not None:
            self.tail.next = other_list.head
            other_list.head.previous = self.tail
            self.tail = other_list.tail
        
        else:
            self.head = other_list.head
            self.tail = other_list.tail
        
        self.size += other_list.size

        
    def __len__(self):
        return self.size


    def __str__(self):
        if self.size == 0:
            return '[]'

        _list = '['
        node = self.head

        while node.next is not None:
            _list += str(node.value) + ', '
            node = node.next
        
        _list += str(node.value) + ']'
        
        return _list