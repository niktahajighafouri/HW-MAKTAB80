import sys

if __name__ == '__main__':
    sum=0
    for i in range(1,len(sys.argv)):
        sum+=float(sys.argv[i])
    avg=sum/(len(sys.argv)-1)
    print(f'average is : {avg}')
