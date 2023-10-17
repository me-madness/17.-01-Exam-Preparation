days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0

for day in range(1, days + 1):
    total_plunder += daily_plunder
    
    if day % 3 == 0:
        total_plunder