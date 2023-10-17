total = 0
count = 0
while True:
    file_name = input("Enter a file name: ")
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if line.startswith("X-DSPAM-Confidence:"):
                    value = float(line.split(":")[1])
                    total += value
                    count += 1
            if count > 0:
                average = total / count
                print(f"Average spam confidence: {average}")
            else:
                print("Nothing matching the format found.")
    except FileNotFoundError:
        print(f"File cannot be opened: {file_name}")
        break
