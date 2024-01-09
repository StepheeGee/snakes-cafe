# LAB - Class 01

## Project: Snakes Cafe

**Author:** Stephanie G. Johnson

### Links and Resources

- [Code](snakes_cafe.py)

### Setup

#### I. Environment Requirements

- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db

#### II. Initialization/Running the Application

To start the application, run the following command:

```bash
python app.py
```

#### III. How to use your library (where applicable)

There's no specific library usage for this application.

#### IV. Tests

- To run tests, use the following command:

  pytest

- Notable Tests

  Currently, no notable tests exist.

- Incomplete/Skipped Tests

  There are no skipped tests at this stage.


#### Notes I need

- .strip() method is used to remove leading and trailing whitespace characters.

- python for loop

``` python
for key, value in some_dictionary.items():
    # Code block to execute for each key-value pair
    print(key)
    for item in value:
        print(item)
```
- python while loop

``` python
while condition_is_true:
    # Code block to execute repeatedly
    user_input = input("Enter something: ")
    if user_input == "quit":
        break  # To exit the loop
```