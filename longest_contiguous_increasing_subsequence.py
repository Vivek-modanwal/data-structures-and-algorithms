def longest_sequence(A,n):
	curr_len=max_len=1
	temp_start=temp_end=0
	start=end=0

	for i in range(1,n):
		if A[i] > A[i-1]:
			temp_end=i
			curr_len+=1
		else:
			temp_start=temp_end=i
			curr_len=1

		if max_len < curr_len:
			start=temp_start
			end=temp_end
			max_len=curr_len

	return [max_len, start, end]

A=[-1,-2,-3,-4,-4,-5,-6,-8]
print(longest_sequence(A,len(A)))