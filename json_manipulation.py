import requests
import json

def get_json_from_url(url):
    """
    Fetch JSON data from a specified URL.
    :param url: str, The URL to fetch the JSON from.
    :return: dict/list, Parsed JSON data as a dictionary or list or None if there's an error.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        return response.json()  # Parse the JSON data and return it
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None  # Return None in case of any issues

def manipulate_json_data(data, key, action):
    """
    Manipulate JSON data based on the provided key and action.
    This function supports DELETE, CHANGE, and VIEW actions.
    :param data: dict/list, The original data to manipulate, can be a dictionary or list of dictionaries.
    :param key: str, The key in the JSON data to perform the action on.
    :param action: str, The action to perform - expected 'DELETE', 'CHANGE', or 'VIEW'.
    :return: dict/list/None, Updated data after performing action or None if action is invalid or data type unsupported.
    """
    if isinstance(data, dict):
        items = [data]  # Single dictionary, wrap it in a list
    elif isinstance(data, list):
        items = data  # Already a list of dictionaries
    else:
        return None  # Unsupported type

    for item in items:
        if key in item:  # Check if the key is present
            if action.upper() == "DELETE":
                del item[key]  # Delete the key-value pair
            elif action.upper() == "CHANGE":
                # Add your specific logic for what the change should be
                # For example, let's just set the value to 'null' (None in Python)
                item[key] = None
            elif action.upper() == "VIEW":
                print(item[key])  # Print the value associated with the key
            else:
                print(f"Invalid action: {action}")
                return None  # Invalid action provided
    return data if isinstance(data, dict) else items  # Return the updated data

def save_to_file(data, filename):
    """
    Save data to a file in JSON format.
    :param data: dict/list, The data to save, expected a dictionary or list of dictionaries.
    :param filename: str, The name of the file to save the data to.
    :return: bool, True if successful, False otherwise.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)  # Serialize data to a JSON formatted str and write it to a file
    except IOError as e:
        print(f"IO error: {e}")
        return False  # Return False in case of IOError
    return True  # Return True if successful

def main():
    """
    Main function to drive the script.
    """
    # User input for the operation parameters
    url = input("Enter the URL to retrieve the JSON: ")
    key = input("Enter the key you want to manipulate: ")
    action = input("Enter the action (DELETE, CHANGE, VIEW): ")

    # Step 1: Fetch the JSON data from the URL
    json_data = get_json_from_url(url)
    if json_data is None:
        print("Failed to retrieve valid JSON data.")
        return

    # Step 2: Manipulate the JSON data based on the user's choices
    updated_data = manipulate_json_data(json_data, key, action)
    if updated_data is not None:
        print("JSON data manipulated successfully.")
        if action.upper() != "VIEW":  # Skip printing the JSON data for VIEW action
            print(json.dumps(updated_data, indent=4))  # Print the updated JSON data

            # Step 3: Save the updated JSON to a new file
            if save_to_file(updated_data, 'new_file.json'):
                print("Data saved to new_file.json successfully.")
            else:
                print("Failed to save data to file.")
    else:
        print("Failed to manipulate JSON data.")

if __name__ == "__main__":
    main()  # Run the main function when script is executed
