count = 0
file = open('mbox.txt', 'r')
for line in file:
    if line.startswith("From:"):
        parts = line.split()
        if len(parts) > 1:
                email = parts[1]
                host = email.split('@')[1]
                print(host)
                count += 1
print("Number of hosts:", count)
