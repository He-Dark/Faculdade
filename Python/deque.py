# myStack = []
# myStack.append(1)
# print(myStack)
# myStack.append(2)
# print(myStack)
# myStack.append(3)
# print(myStack)
# myStack.pop()
# print(myStack)
# myStack.pop()
# print(myStack)
# myStack.pop()
# print(myStack)
# myStack.append('Ana')
# myStack.append('Pedro')
# myStack.append('Roberto')
# myStack.append('Joana')
# print(myStack)
# myStack.pop(0)
# print(myStack)
# myStack.pop(0)
# print(myStack)

# Programa em Python para
# Demonstrar a implementação de pilha
# Utilizando a coleção .deque

from collections import deque

stack = deque()

# função .append() para inserir
# elementos na pilha

stack.append('a')
stack.append('b')
stack.append('c')
print('Pilha Inicial:')
print(stack)

# função .pop() para remover
# elementos da pilha
# na ordem LIFO => Last In First Out

print('\nElementos removidos da pilha:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nPilha após retirada dos elementos:')
print(stack)

# O uso de print (stack.pop())
# causará o erro IndexError
# devido à pilha estar vazia agora.
