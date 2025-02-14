# Problem: Books - https://codeforces.com/contest/279/problem/B

number_of_books , limit_time = [int(i) for i in input().split()]
book_time = [int(i) for i in input().split()]
maximum = 0
time_track = 0
start = 0

for t in range(number_of_books):
    time_track += book_time[t] # Add new book 

    while time_track > limit_time: # if time is not enough decrement book from start
        time_track -= book_time[start]
        start += 1

    maximum = max(maximum,t-start+1) # calculate number of books and updating maximum if it is less

print(maximum)