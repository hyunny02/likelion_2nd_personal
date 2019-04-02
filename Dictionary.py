# =========================================================
# 필요한 모듈은 이곳에 importing 합니다.
import re
# 필요한 모듈은 이곳에 importing 합니다.
# =========================================================


# =========================================================
# 이곳에 함수를 작성합니다.
def example():
    return "함수를 작성하는 부분입니다."
# 이곳에 함수를 작성합니다.

# 두 수의 합을 구하는 메소드
def sum(num1, num2):
    num = num1 + num2
    return num
# 두 수의 차를 구하는 메소드_절대값
def dif(num1, num2):
    num = abs(num1 - num2)
    return num
# 두 수의 곱셈을 리턴하는 메소드
def mul(num1, num2):
    num = num1*num2
    return num
# 두 수의 나눗셈의 몫을 리턴하는 메소드
def div(num1, num2):
    num = num1 // num2
    return num
# 두 수의 나눗셈 나머지를 리턴하는 메소드
def lef(num1, num2):
    num = num1 // num2
    return num

# 1부터 입력값 까지의 합계를 리턴하는 메소드
def summ(num1):
    sum = 0
    for i in range(1, num1+1):
       sum += i
    return sum
# 입력한 리스트 중에서 가장 큰 수를 찾아 리턴하는 메소드
def big(arr):
    count = arr[0]
    for i in arr:
        if i >= count:
            count = i
    return count

#두 리스트의 교집합을 리턴하는 메소드
def intersaction( arr1, arr2):
    arr = []
    for i in arr1:
        for j in arr2:
            if i == j:
                arr.append(i)
    return arr

#두 집합의 합집합을 리턴하는 메소드
def union( arr1, arr2):
    arr = []
    ar=arr1+arr2
    for i in arr1:
        for j in arr2:
            if i == j:
                arr.append(i)
    for i in arr:
        ar.remove(i)
    return ar

#두 집합의 차집합을 구하는 메소드 , 첫번째 집합에서 교집합을 제거
def union( arr1, arr2):
    arr = []
    for i in arr1:
        for j in arr2:
            if i == j:
                arr.append(i)
    for i in arr:
        arr1.remove(i)
    return arr1


# 1부터 입력값까지의 범위 안에서 두번째입력값의 배수의 갯수를 리턴하는 메소드
def multiple(num1, num2):
    count = 0
    for i in range(1, num1+1):
        if (i % num2 == 0 ):
            count += 1
    return count


# 배열의 길이를 리턴하는 메소드
def lengthArray(arr):
    count=0
    for i in arr:
        if i is not None:
            count+=1
        else: break
    return count

# string의 길이를 리턴하는 메소드
def lengthString(str):
    count = 0
    for i in str:
        if i is not None:
            count += 1
        else:
            break
    return count

#입력한 문자가 string값에서 몇번째 인덱스인지 리턴하는 메소드
def find(str, Input):
    count=0
    for i in str:
       if i == Input:
           break
       count+=1
    return count

# 문자열값을 거꾸로 출력하는 메소드
def ReversePrint(str):
    str=str[ : : -1 ]
    print(str)

#list배열을 뒤집는 메소드
def reverse(arr):
    arr1 = arr
    count = 0
    for i in reversed(arr1):
        arr[count] = i
        count+=1
    return arr
#list배열에서 필요한 원소를 꺼내오는 메소드
def pop_(arr, num):
    arr1 = arr
    count = 0
    for i in arr:
        if i == num:
            break
        else: count+=1
    if count <= len(arr)-1:
        for i in range(count,len(arr)-1):
            arr[i] = arr[i+1]
        del arr[len(arr)-1]
        print(arr1[count])

# 문자열의 모든 공백을 없애는 메소드
def DeleteSpace(str):
    str1 = ""
    for i in  range(len(str)):
        if str[i] != " ":
            str1+=str[i]
    return str1

# 문자열 왼쪽 공백을 없애는 메소드
def DeleteLeftSpace(str):
    count = 0
    for i in str:
        if i == " ":
            count+=1
        else: break
    str = str[count:]
    return str


# 문자열 오른쪽 공백을 없애는 메소드
def DeleteRightSpace(str):
    count = 0
    for i in reversed(str):
        if i == " ":
            count+=1
        else: break
    str = str[:len(str)-count]
    return str

# 리스트의 각 요소와 인덱스를 동시에 출력하는 메소드
def printIndexFactor(arr):
    for i in range(len(arr)):
        print(i, arr[i])

# 입력값을 절대값으로 반환하는 메소드
def abs_(num):
    if num < 0:
        num = -num
    return num
# 첫번째 값을 두번쨰 값만큼 제곱한 결과를 리턴하는 메소드
def pow_(num1, num2):
    num = num1
    for i in  range(num2-1):
        num1 *= num
    return num1

# 입력한 배열을 크기순서대로 sorting하여 리턴하는 메소드
def bubblesort(arr):
    for i in reversed(range(len(arr))):
        for j in range(i):
            if arr[j] > arr[j+1]:
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
    return arr


# 입력한 배열을 내림차순으로 리턴하는 메소드
def bubblesort(arr):
    for i in reversed(range(len(arr))):
        for j in range(i):
            if arr[j] > arr[j+1]:
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
    return reversed(arr)

# 입력한 문자가 리스트의 몇번째 크기인지 인덱스를 리턴하는 메소드
def order(arr, num):
    count = 0
    for i in arr:
        if arr >= num:
            break
        else: count+=1

# 입력한 값의 인덱스값을 리턴하는 메소드
def index_(arr, num):
    count = 0
    for i in arr:
        if i != num:
            count+=1
        else: break
    if  count != len(arr):
        return count
    else: return "값이 리스트에 존재하지 않습니다."

# 배열에서 입력값과 값이 같은 요소 갯수를 리턴하는 메소드
def countInput(arr , input):
    count = 0
    for i in arr:
        if i == input:
            count+=1
    return count

# 배열에서 가장 작은 숫자를 리턴하는 메소드
def smallerList(arr):
    count = arr[0]
    for i in arr:
        if i <= count:
            count = i
    return count
# 입력한 숫자를 이진수로 바꾸어 string값으로 리턴
def bi(num):
    arr=[]
    str1=""
    while(1):
        if(num%2 == 1):
            arr.append(1)
        else: arr.append(0)
        num = num//2
        if(num == 0): break
    arr.reverse()
    for i in range (len(arr)):
        str1 += str(arr[i])

    return str1

# =========================================================


# =========================================================
# 따로 설정할 필요 없습니다.

def main():
    print("함수 사전 목록을 불러옵니다.")


if __name__ == "__main__":
    main()
    func_list = []

    for i in dir():
        if re.search('[__]+', i) or i == "i" or i == "re" or i == "main":
            pass
        else:
            func_list.append(i)

    for num, func in enumerate(func_list, start=1):
        print("{0}: {1}".format(num, func))

# 따로 설정할 필요 없습니다.
# =========================================================
