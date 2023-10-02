import requests

def get_user_ip():
    try:
        #gets IP from API
        response = requests.get("http://ip-api.com/json/")

        # Makes sure the request was succesful
        if response.status_code == 200:
            user_info = response.json()
            user_ip = user_info["query"]
            return user_ip
        else:
            print(f"Error: Unable to fetch IP address (HTTP Status Code: {response.status_code})")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

#prints it
if __name__ == "__main__":
    user_ip = get_user_ip()
    if user_ip:
        print(f"Your IP address is: {user_ip}")

