
n=int(input("한변의 크기를 입력하세요: "))

arr1=[]
arr2=[]
print("첫번째 배열의 값을 차례대로 입력하세요.")
for i in range(n):
    arr1.append(int(input()))

print("두번째 배열의 값을 차례대로 입력하세요.")
for i in range(n):
    arr2.append(int(input()))

# 행 혹은 열의 길이와 숫자를 넣어서 이진수 만들기.
def bi(length, num):
    arr = [0]*length
    for i in range(length):
        if(num%2 == 1):
            arr[length-i-1] = 1
        num = num//2
        if(num == 0): break

    return arr
# 1차원 리스트에 각 원소를 이진수로 바꾸어 다시 이차원리스트에 저장
for i in range(n):
    arr1[i] = bi(n, arr1[i])
for i in range(n):
    arr2[i] = bi(n, arr2[i])


for i in range(n):
    ar = []
    for j in range(n):
        ar.append(arr1[i][j]+arr2[i][j])
        if(ar[j] != 0):
            print("#", end='')
        else:
            print(" ", end='')
    ar.clear()
    print()







