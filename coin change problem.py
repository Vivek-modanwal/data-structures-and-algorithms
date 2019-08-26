import time
def total_coin_change1(coin,total):
	return coin_change(coin,total,len(coin)-1)

def coin_change(coin,total,index):
	if total==0:
		return 1
	if index<0:
		return 0
	if total < coin[index]:
		return coin_change(coin,total,index-1)
	return coin_change(coin,total,index-1) + coin_change(coin,total-coin[index],index)

def total_coin_change2(coin,total):
	A=[]
	B=[0]*(total+1)
	l=len(coin)
	for i in range(l):
		A.append(B.copy())
		A[i][0]=1	
	for i in range(coin[0],total+1):
		if i%coin[0]==0:
			A[0][i]=1
	for i in range(1,l):
		for j in range(1,total+1):
			if coin[i]>j:
				A[i][j]=A[i-1][j]
			else:
				 A[i][j]=A[i-1][j]+A[i][j-coin[i]]
	return A[-1][-1]


print(' '*20,end='')
print('COIN CHANGE PROBLEM')
coin=[2,3,5,6]
total=800
print(f'coins : {coin}')
print(f'total money : {total}')
print('USING RECURSION : ')
print()
start=time.time()
print(f'total ways : {total_coin_change1(coin,total)}')
end=time.time()
print(f'total time taken = {end-start} sec')
print()
print('-'*50)
print('USING DYNAMIC PROGRAMMING : ')
print()
start=time.time()
print(f'total ways : {total_coin_change2(coin,total)}')
end=time.time()
print(f'total time taken = {end-start} sec') 