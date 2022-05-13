time = int(input())
hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60
print(f"{hours}:{minutes}:{seconds}")
