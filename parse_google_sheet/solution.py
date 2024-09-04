import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vShuWova56o7XS1S3LwEIzkYJA8pBQENja01DNnVDorDVXbWakDT4NioAScvP1OCX6eeKSqRyzUW_qJ/pub"


def read_table_from_google_doc(url):
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')

        rows = []
        for row in table.find_all('tr'):
            cols = row.find_all('td')
            # Get the text from each column and strip any extra whitespace
            cols = [col.get_text(strip=True) for col in cols]
            rows.append(cols)

        return rows
    return []


def print_table_data(rows):
    # There is nothing dynamic here. I am assuming its always like this. Anything else is an error
    assert rows[0] == ['x-coordinate', 'Character', 'y-coordinate']

    coordinate_map = {}
    for row in rows[1:]:
        x = int(row[0])
        y = int(row[2])
        char = row[1]
        coordinate_map[(x, y)] = char

    # Find the maximum x and y of the grid
    max_x = max(x for x, y in coordinate_map.keys())
    max_y = max(y for x, y in coordinate_map.keys())

    # Print the characters at their given coordinates (0,0) is bottom left.
    for y in range(max_y, -1, -1):  # Start from max_y down to 0
        line = ''
        for x in range(max_x + 1):
            if (x, y) in coordinate_map:
                line += coordinate_map[(x, y)]
            else:
                # If we don't find a character add a space
                line += ' '
        print(line)


def code_solution(url):
    rows = read_table_from_google_doc(url)
    print_table_data(rows)


code_solution(url)
