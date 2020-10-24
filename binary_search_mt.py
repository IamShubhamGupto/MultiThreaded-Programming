import threading
DEBUG = 0
MAX_THREAD = 8
array = []
key = -1
found = False
position = -1
part = 0
def binary_search():
    global array,key,found,position,part
    if found:
        return
    thread_part = part
    part+=1
    low = thread_part*(len(array)//MAX_THREAD)
    high = (thread_part+1)*(len(array)//MAX_THREAD)
    if DEBUG:
        print(array[low:high+1])
        print(key)
        print(part)
    while(low <= high):
        mid = low + (high-low)//2
        #print(mid)
        if array[mid] == key:
            found = True
            position = mid
            break
        elif array[mid] > key:
            high = mid-1
        else:
            low = mid+1

def main():
    global array,key,found,position
    threads = []
    array = list(map(int,input("Enter sorted array ").split()))
    key = int(input("Enter key "))
    for i in range(MAX_THREAD):
        threads.append(threading.Thread(target=binary_search,args=()))
        threads[i].start()
    for i in range(MAX_THREAD):
        threads[i].join()
    if found:
        print(key,"was found at position",position)
    else:
        print(key,"is not present in the array")   

if __name__=='__main__':
    main() 