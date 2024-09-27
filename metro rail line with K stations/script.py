def solution(start, dest, limit):
    number_of_rides = len(start)
    large_station_number = 0
    fees = 0
    for n in range(number_of_rides):
        fees+=1 + abs(dest[n]-start[n])*2
        large_station_number = max(large_station_number,start[n],dest[n])
    return min(fees, limit[large_station_number])