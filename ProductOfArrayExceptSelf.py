def product_except_self(nums):
    n = len(nums)
    left_products = [1]*n
    right_products = [1]*n

    left_product =1
    for i in range(n):
        left_products[i] = left_product
        left_product = left_product*nums[i]

    right_product=1
    for i in range(n-1,-1,-1):
        right_products[i] = right_product
        right_product = right_product*nums[i]

    result = [1]*n
    for i in range(n):
        result[i] = left_products[i]*right_products[i]

    return result




output_array = product_except_self([1,2,3,4])
print(output_array)  # Output: [24, 12, 8, 6]