queue = []

# (a)
for count in range(4):
    incoming_call = input("Incoming call from: ")
    queue.append(incoming_call)
print("The queue is: " + str(queue))

# (b)
for count in range(4):
    queue.pop(0)
    print("Handled a call. Queue: " + str(queue))
