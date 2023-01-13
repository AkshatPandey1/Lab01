import requests

if __name__ == "__main__":
	print(requests.__version__)

	response = requests.get("http://google.com/")
	print(response.status_code)
	print(response.text)

	# Download https://raw.githubusercontent.com/AkshatPandey1/Lab01/main/version.py from github and print the source code
	response = requests.get("https://raw.githubusercontent.com/AkshatPandey1/Lab01/main/version.py")
	print(response.text)

