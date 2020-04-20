import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Dr2iaJFHvjiiyhGBGVLA", "isbns": "TIVxGRXnyrMIWvkWjfUv78d52tjGplD9levpRCs"})
print(res.json())