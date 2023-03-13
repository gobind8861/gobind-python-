class Gobind:
    def fibo(self,num):
        first = 0
        second = 1
        for i in range(1,num):
            third = first + second
            first = second
            second = third
        return third  
def main():
    g = Gobind()
    n = int(input("enter the number which fibo you want to find\n"))
    print(g.fibo(n))
if __name__ == '__main__':
   main()
    