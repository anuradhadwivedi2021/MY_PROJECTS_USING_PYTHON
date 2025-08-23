hosts_path = "hosts.txt"  # demo file
redirect = "127.0.0.1"
website_list = ["facebook.com", "instagram.com"]

with open(hosts_path, "a") as file:
    for site in website_list:
        file.write(redirect + " " + site + "\n")

print("✅ Websites Blocked")