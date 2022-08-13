import priority_queue as pq

p = pq.PriorityQueue()
p.enqueue("Cat", 13)
p.enqueue("Bat", 2)
p.enqueue("Rat", 1)
p.enqueue("Ant", 26)
p.enqueue("Lion", 25)

p.print_queue()
val = p.dequeue()
print(val)
p.print_queue()

