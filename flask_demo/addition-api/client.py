# client.py
import requests

BASE_URL = 'http://localhost:8080'


def add_numbers(a, b):
    """Call the addition API and return the result."""
    response = requests.post(f'{BASE_URL}/add', json={'a': a, 'b': b})

    if response.status_code == 200:
        return response.json()['result']
    else:
        raise Exception(f"API error: {response.json().get('error', 'Unknown error')}")


def get_numbers():
    """Get the current list of numbers from the API."""
    response = requests.get(f'{BASE_URL}/numbers')
    return response.json()


def add_number_to_list(number):
    """Add a number to the list via the API."""
    response = requests.post(f'{BASE_URL}/numbers', json={'number': number})

    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"API error: {response.json().get('error', 'Unknown error')}")


if __name__ == '__main__':
    # Test the /add endpoint
    print("Testing /add endpoint:")
    print(f"  5 + 3 = {add_numbers(5, 3)}")
    print(f"  10 + 20 = {add_numbers(10, 20)}")

    # Test the /numbers endpoints
    print("\nTesting /numbers endpoints:")

    # Check the initial list (should be empty)
    result = get_numbers()
    print(f"  Initial list: {result['numbers']} (count: {result['count']})")

    # Add some numbers
    add_number_to_list(42)
    add_number_to_list(3.14)
    add_number_to_list(100)

    # Check the list again
    result = get_numbers()
    print(f"  After adding numbers: {result['numbers']} (count: {result['count']})")