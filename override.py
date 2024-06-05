'''class sample:
    def display(self):
        print("class sample")
class sam(sample):
    def display(self):
        print("class sam")
object=sam()
object.display()        


class sample:
    def display(self):
        print("class sample")
class sam(sample):
    def display(self):
        super().display()
        print("class sam")
object=sam()
object.display()    '''    


class sample:
    def __init__(self):
        print("class sample")
class sam(sample):
    def __init__(self):
        super().__init__()
        print("class sam")
object=sam()
