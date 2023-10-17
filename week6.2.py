fname = input("Enter the file name: ")
try:
    with open(fname, 'r') as fhand:
        hosts = {}
        for line in fhand:
            if line.startswith("From:"):
                words = line.split()
                if len(words) > 1:
                    email = words[1]
                    _, host = email.split('@')
                    hosts[host] = hosts.get(host, 0) + 1
        for host in hosts.keys():
            print(f"\n{host}\n")
        total_hosts = len(hosts)
        print(f"Total {total_hosts} hosts printed.")
        
except FileNotFoundError:
    print(f"Error! File '{fname}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")