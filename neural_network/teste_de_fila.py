from queue import PriorityQueue

fila = PriorityQueue()

fila.put((3, 2, "teste1"))
fila.put((2, 4, "teste2"))
fila.put((1, 1, "teste3"))
fila.put((1, 5, "teste4"))

print(f"Fila inteira: {fila.queue}")

print(fila.get()) # retorna o elemento com menor prioridade, no caso, o elemento com menor valor no caso (1, "teste3")
print(fila.get())
print(fila.get())
print(fila.get())

print(f"Fila inteira: {fila.queue}")

print(abs(8.5 + 1))