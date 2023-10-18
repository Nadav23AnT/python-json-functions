# Python JSON Functions - Json_manipulation.py

This repository contains a Python script that performs various manipulations on JSON data fetched from a specified URL. It allows users to DELETE, CHANGE, or VIEW specific keys within the loaded JSON data and save the resulting data to a file.

![json_m_photo](https://github.com/Nadav23AnT/python-json-functions/assets/71144691/69ac6780-e656-40e1-a007-e8307b9439ee)

## Features

- Fetch JSON data from a URL.
- Perform actions like DELETE, CHANGE, or VIEW on specific keys in the JSON data.
- Save the updated JSON data to a new file.

## Requirements

- Python 3
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

## Usage

Run the script in your terminal:

```bash
python main.py
```

You will be prompted to enter:

- `URL`: The URL from where the JSON will be fetched.
- `key`: The specific key in the JSON data you want to manipulate.
- `action`: The operation you want to perform on the key - available options are DELETE, CHANGE, or VIEW.
- 
Based on the input, the script will fetch the JSON data, and perform the specified action, and if the action is not VIEW, it will save the updated JSON data to `new_file.json`.

## Functions

- `get_json_from_url(url)`: This function takes a URL as an argument, sends a GET request to it, and returns the response as JSON. It handles any potential errors that might occur during the request and alerts the user accordingly.

- `manipulate_json_data(data, key, action)`: This function accepts the JSON data, a key to look for in the data, and an action (DELETE, CHANGE, or VIEW). Depending on the action specified, the function will either delete the key-value pair, change the value, or print out the value associated with the provided key.

- `save_to_file(data, filename)`: This function saves the provided data into a file with the given filename. It writes the data in JSON format and handles any IO errors, printing an error message if one occurs.

- `main()`: The main driver function of the script. It prompts the user for the necessary inputs, calls the other functions to fetch, manipulate, and potentially save the JSON data, and prints out messages to the console regarding the success or failure of these operations.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
