import requests

if __name__ == "__main__":
	print(requests.__version__)

	response = requests.get("http://google.com/")
	print(response.status_code)
	print(response.text)
