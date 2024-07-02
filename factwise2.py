
def func(cp,l,h,k):
    points = 0
    for i in range(1,k+1):
        if cardpoints[l] > cardpoints[h]:
            points += cardpoints[l]
            l += 1
        elif cardpoints[l] < cardpoints[h]: 
            points += cardpoints[h]
            h -= 1
        else:
            points += cardpoints[0]
            return points + max(func(cp,l+1,h,k-1),func(cp,l,h-1,k-1))
    return points
    
cardpoints = list(map(int,input("Enter the list:").strip().split()))
k = int(input("Enter k:"))
l = 0
h = len(cardpoints) - 1
points = func(cardpoints,l,h,k)
print(points)
