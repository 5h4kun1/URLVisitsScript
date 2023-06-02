import requests

def visit_url(url, num_visits):
    for _ in range(num_visits):
        response = requests.get(url)
        # You can customize the handling of the response based on your requirements
        print(f"Visited URL: {url}. Response: {response.status_code}")

def main():
    url = input("Enter the URL you want to visit: ")
    num_visits = int(input("Enter the number of times to visit the URL: "))
    visit_url(url, num_visits)

if __name__ == '__main__':
    main()
