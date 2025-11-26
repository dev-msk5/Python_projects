def square_root_bisection(num, tol=0.01, max_iter=10):
    if num < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if num == 0 or num == 1:
        print(f"The square root of {num} is {num}")
        return num

    low = 0.0
    high = num if num >= 1.0 else 1.0

    for i in range(max_iter):
        mid = (low + high) / 2
        mid_sq = mid * mid

        if mid_sq == num:
            print(f"The square root of {num} is approximately {mid}")
            return mid

        if mid_sq < num:
            low = mid
        else:
            high = mid

        if (high - low) <= tol:
            print(f"The square root of {num} is approximately {mid}")
            return mid

    print(f"Failed to converge within {max_iter} iterations")
    return None
