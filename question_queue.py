
class Queue:
    def __init__(self):
        self.gobindArray=[]
        
    def enqueue(self,item):
        self.gobindArray= self.gobindArray+[item]
        
    def dequeue(self):
        if not self.is_empty():
            item = self.gobindArray[0]
            self.gobindArray=self.gobindArray[1:]
            return item
    def peek(self):
        if self.is_empty():
            return none
        return self.gobindArray[0]   
       
    def is_empty(self):
        return len(self.gobindArray)==0
    
def main():
        queue1=Queue()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        print(queue1.peek())
        print(queue1.dequeue())
        print(queue1.peek())
        print(queue1.is_empty())
if __name__ == '__main__':
   main()
    
    
        