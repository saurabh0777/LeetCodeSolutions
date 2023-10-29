def maxgain(arr)->int:
    ans =0
    minsofar = arr[0]
    for i in range(1,len(arr)):
        current_profit = arr[i] - minsofar
        if current_profit > ans:
            ans = current_profit

        minsofar = min(minsofar,arr[i])

    return ans



'''
        for i in range (1,len(arr)):
        current_profit = arr[i] - minsofar
        if current_profit > ans:
            ans = current_profit

        minsofar = min(minsofar,arr[i])

    return ans

'''




out = maxgain([3,2,6,5,0,3])
print("final ",out)

