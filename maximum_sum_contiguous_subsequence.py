def max_sum1(A,n):

	curr_max=max_so_far=A[0]

	for i in range(1,n):
		curr_max=max(curr_max+A[i], A[i])
		max_so_far=max(max_so_far,curr_max)

	return max_so_far

def max_sum2(A,n):

	curr_max=max_so_far=A[0]
	temp_start=temp_end=0
	start=end=0

	for i in range(1,n):
		if curr_max+A[i] > A[i]:
			temp_end=i
			curr_max+=A[i]
		else:
			temp_start=temp_end=i
			curr_max=A[i]

		if max_so_far < curr_max:
			start=temp_start
			end=temp_end
			max_so_far=curr_max

	return [max_so_far, start, end]

A=[-5,-4,20,-3,11,-4,-1,30]

print(A)
print(max_sum1(A,len(A)))
print(max_sum2(A,len(A)))

