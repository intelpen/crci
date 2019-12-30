# 3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linked list data structure.

# We can have 2 queues but we need to keep the "arrival times" as the data element
from c3_stacks_and_queues.myqueue import MyQueue

class AnimalShelter(object):
    def __init__(self):
        self.cats = MyQueue()
        self.dogs = MyQueue()
        self.last_time = 0

    def enqueue(self,animal):
        if animal == "cat":
            self.cats.add(self.last_time)
        else:
            self.dogs.add(self.last_time)
        self.last_time +=1

    def dequeue_dog(self):
        return ("dog",self.dogs.remove())

    def dequeue_cat(self):
        return ("cat",self.cats.remove())

    def is_empty(self):
        return self.dogs.is_empty() and self.cats.is_empty()

    def dequeue_any(self):
        if self.is_empty():
            raise Exception("NoCatsNeitherDogs")
        if not self.dogs.is_empty() and not self.cats.is_empty():
            # we have cats and dogs
            if self.dogs.peek() < self.cats.peek():
                return self.dequeue_dog()
            else:
                return self.dequeue_cat()
        else:
            if not self.dogs.is_empty():
                # just dogs
                return self.dequeue_dog()
            else:
                # just cats
                return self.dequeue_cat()


ash = AnimalShelter()
ash.enqueue("dog")
ash.enqueue("dog")
ash.enqueue("dog")
print(ash.dequeue_any())
ash.enqueue("cat")
ash.enqueue("cat")
ash.enqueue("dog")
#print(ash.dequeue_dog())
while not ash.is_empty():
    print(ash.dequeue_any())
