import pyshorteners

url = input("Enter URL: ")

if not url:
    print("Please enter a URL to shorten.")
else:
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        print("Shortened URL:", short_url)
    except pyshorteners.exceptions.BadURLException:
        print("Invalid URL. Please enter a valid URL.")
    except pyshorteners.exceptions.ShorteningErrorException:
        print("Error while shortening URL. Please try again later.")