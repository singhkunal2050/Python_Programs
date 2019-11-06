class Queue(object) :
    def __init__(self):
        self.q=[]

    def insert(self,element):
        self.q.append(element)

    def delete(self):
        self.q.pop(0)

    def show(self):
        print(self.q)

Q=Queue()
for i in range(11):
    print("Inserting..")
    Q.insert(i)
    Q.show()

for i in range(5):
    print("Deleting..")
    Q.delete()

Q.show()

