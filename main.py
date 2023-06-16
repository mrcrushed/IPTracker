import requests

#color codes for formatting

color_code = "\033[1;31m"
back_color_code = "\033[0m"

def beautify_program():
    global color_code, back_color_code
    print("\n\n")
    word = "MRCrushed"
    n = len(word)
    width = 2 * n + 5
    

    for i in range(n):
        blocks = " ".join([f"{color_code}▓{back_color_code}" * (2 * i + 1)] * 3)
        print(f"{blocks:^{width}}")
        
    blocks = f"{color_code}▓{back_color_code}" * width
    print(f"{blocks:^{width}}")

    for i in range(n):
        blocks = " ".join([f"{color_code}▓{back_color_code}" * (2 * (n - i - 1) + 1)] * 3)
        print(f"{blocks:^{width}}")

    print('\n\n')
    print(f"{color_code}IP Tracker by MRCrushed{back_color_code}")

def mainip():
    global color_code, back_color_code

    fields = 'status,query,country,city,region,zip,isp,mobile,district'
    # while True:
    
    user_IP = input("Please Enter ip address => ")
    api = "http://ip-api.com/json/"
    get_url = requests.get(f"{api}{user_IP}?fields={fields}")
    
    data = get_url.json()

    status = data['status']
    query = data['query']
    country = data['country']
    city = data['city']
    region = data['region']
    zip = data['zip']
    isp = data['isp']
    mobile = data['mobile']
    district = data['district']

    print(f"status : {status}")
    print(f"Query : {query}")
    print(f"Country : {country}")
    print(f"City : {city}")
    print(f"Region : {region}")
    print(f"ZIP : {zip}")
    print(f"ISP : {isp}")
    print(f"Mobile : {mobile}")
    print(f"District : {district}")



if __name__ == "__main__":
    beautify_program()
    mainip()