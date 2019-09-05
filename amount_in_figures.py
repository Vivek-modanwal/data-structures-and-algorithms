def convert_to_figures(num):
	Map={
			1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
			11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',
			18:'Eighteen',19:'Nineteen',20:'Twenty',30:'Thirty',40:'Fourty',50:'Fifty',60:'Sixty',
			70:'Seventy',80:'Eighty',90:'Ninety',100:'Hundred',1000:'Thousand',100000:'Lakh',10000000:'Crore'
		}
	print(figures(num,Map))


def convert_slice(num,Map):
	st=''
	if num//100 in Map:
		st=st+f'{Map[num//100]} {Map[100]} '
		num%=100
	if num in Map:
		st=st+f'{Map[num]} '
	else:
		temp=(num//10)*10
		if temp in Map:
			st=st+f'{Map[temp]} '
		if num%10 in Map:
			st=st+f'{Map[num%10]} '
	return st

def figures(num,Map):
	if num==0:
		return 'Zero'
	total=''
	total=convert_slice(num%1000,Map)
	num=num//1000
	place_value=1000
	while num>0:
		if num%100!=0:
			total=f'{convert_slice(num%100,Map)}{Map[place_value]} '+total
		num=num//100
		place_value*=100
	return total


for i in range(100000):
	8convert_to_figures(i)





