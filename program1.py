import threading
'''
prints the pattern:
1
1 2 
1 2 3
1 2 3 4
...n
'''
def pattern_1(n):
    print("Executing thread",threading.currentThread().name)
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
'''
prints the pattern:
1 2 ... n
2 3 ... n
... n
n 
'''
def pattern_2(n):
    print("Executing thread",threading.currentThread().name)
    for i in range(1,n+1):
        for j in range(i,n+1):
            print(j,end=" ")
        print()

def main():
    n = int(input("Enter a number "))
    t1 = threading.Thread(target=pattern_1,args = (n,))
    t1.start()
    t1.join()
    t2 = threading.Thread(target=pattern_2,args = (n,))
    t2.start()
    t2.join()

if __name__=='__main__':
    main()