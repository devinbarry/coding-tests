# Assemble letters from Google Docs Sheet

This problem involves parsing a Google Doc which contains an HTML table mapping characters to x and y co-ordinates.
Here is a simple example:
https://docs.google.com/document/u/0/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub?pli=1

If this link ever dies, here is what the table looks like

| x-coordinate | Character | y-coordinate |
|--------------|-----------|--------------|
| 0            | █         | 0            |
| 0            | █         | 1            |
| 0            | █         | 2            |
| 1            | ▀         | 1            |
| 1            | ▀         | 2            |
| 2            | ▀         | 1            |
| 2            | ▀         | 2            |
| 3            | ▀         | 2            |

When you put each character into the correct place in the grid, it spells out a single letter.

The final problem involves using a much larger list of characters to spell out the secret code:
https://docs.google.com/document/d/e/2PACX-1vShuWova56o7XS1S3LwEIzkYJA8pBQENja01DNnVDorDVXbWakDT4NioAScvP1OCX6eeKSqRyzUW_qJ/pub

When you run my `solution.py` using the URL above you get the following output:

```
██░     ██░ ████████░      ██░     ██░        ███████░  ███░    ███░ ████████░    ██████████░
██░     ██░ ██░     ██░   ████░   ████░     ███░    ██░   ██░  ██░   ██░     ██░  ██░        
██░     ██░ ██░     ██░   ██░██░ ██░██░    ███░            ██░██░    ██░      ██░ ██░        
██████████░ ████████░    ███░ ██░██░ ██░   ██░              ███░     ██░      ██░ ████████░  
██░     ██░ ██░     ██░  ██░  █████░ ███░  ███░            ██░██░    ██░      ██░ ██░        
██░     ██░ ██░     ██░ ███░   ███░   ██░   ███░    ██░   ██░  ██░   ██░     ██░  ██░        
██░     ██░ ████████░   ██░           ███░    ███████░  ███░    ███░ ████████░    ██████████░
```
