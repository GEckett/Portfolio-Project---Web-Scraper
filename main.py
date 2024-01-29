import requests
from bs4 import BeautifulSoup
import csv


def scrape_website_and_save_to_csv(url, csv_filename, selected_tags):
    # Make a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract information based on user-selected tags
        data_to_write = []
        for tag in selected_tags:
            elements = soup.find_all(tag)
            column_data = [element.text for element in elements]
            data_to_write.append(column_data)

        # Transpose the data to align columns properly
        transposed_data = list(map(list, zip(*data_to_write)))

        # Save the data to a CSV file
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write header
            csv_writer.writerow(selected_tags)

            # Write data to CSV
            csv_writer.writerows(transposed_data)

        print(f"Data saved to {csv_filename}")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Example usage
url_to_scrape = input("Enter the URL to scrape. ")
file_name = input("Please name the output file. ")
csv_filename = f'{file_name}.csv'

# Prompt the user for selected HTML tags (columns)
selected_tags = input("Enter HTML tags (comma-separated) for columns: ").split(',')

scrape_website_and_save_to_csv(url_to_scrape, csv_filename, selected_tags)
