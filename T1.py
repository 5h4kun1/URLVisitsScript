import webbrowser

def visit_url(url, num_visits):
    for _ in range(num_visits):
        webbrowser.open(url)

def main():
    url = input("Enter the URL you want to visit: ")
    num_visits = int(input("Enter the number of times to visit the URL: "))
    visit_url(url, num_visits)

if __name__ == '__main__':
    main()
