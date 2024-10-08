import requests
from collections import Counter

# Function to categorize response


def categorize_response(response_text):
    if 'canary' in response_text.lower():
        return 'canary'
    elif 'production' in response_text.lower():
        return 'production'
    else:
        return 'unknown'

# Function to send requests and count responses


def send_requests_and_count(url, num_requests=100):
    result_count = Counter()

    for i in range(num_requests):
        try:
            response = requests.get(url)
            category = categorize_response(response.text)
            result_count[category] += 1
            print(f"Request {i + 1}: {category}")
        except Exception as e:
            print(f"Request {i + 1} failed: {e}")
            result_count['failed'] += 1

    return result_count


# URL to send requests to
url = "http://demo-canary.invideo.io"

# Send requests and get the result count
response_counts = send_requests_and_count(url)

# Output the result
print("\nFinal counts:")
for category, count in response_counts.items():
    print(f"{category}: {count}")
