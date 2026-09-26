arr = [12,5,7,19,3,15]
n=2
m=3
arr.sort()
nth_min=arr[n-1]
mth_max=arr[-m]
sum_value=nth_min + mth_max
diff_value=mth_max - nth_min
print('min',nth_min)
print('max',mth_max)
print('sum',sum_value)
print('diff',diff_value)
