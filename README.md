# Coffee Making Machine ☕

A simple console-based coffee machine simulator built in Python. It manages ingredient resources, processes drink orders, handles payments, and reports remaining resources via a command-line interface.

## Features

- Choose from multiple coffee options (e.g., espresso, latte, cappuccino).
- Tracks available resources such as water, milk, and coffee.
- Validates whether enough ingredients are available for the selected drink.
- Simulates payment handling using coins or amounts entered by the user.
- Prints a resource report showing current ingredient levels and collected money.
- Looping menu so the machine can serve multiple drinks until turned off.

## Project Structure

- `main.py`: Entry point; runs the main loop, handles user input, and orchestrates the coffee machine workflow.
- `functions.py`: Core logic functions for:
  - Checking resources
  - Processing coins / payment
  - Making the drink and updating resources
  - Printing status or error messages
- `data.py`: Defines configuration data such as:
  - Menu of drinks and their ingredient requirements
  - Initial resource levels
  - Pricing details

## Requirements

- Python 3.8 or higher (any recent 3.x version should work).
- No external libraries required; uses only the Python standard library.

## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/lakumsaicharan/coffee-making-machine.git
   cd coffee-making-machine
   ```
2. Run the main script:
   ```
   python main.py
   ```
3. Follow the on-screen prompts to:
   - Enter a drink name to order coffee.
   - Type `report` to see current resources.
   - Type `off` (or the configured command) to turn the machine off and exit.

## Example Usage

- Start the program and select a drink by typing its name (e.g., `espresso`).
- Insert coins or enter the requested amount when prompted.
- If resources and payment are sufficient, the drink is "made" and a confirmation message is shown.
- Use the report command periodically to see remaining water, milk, coffee, and total money.

## Future Improvements

- Add more drink options and customizable recipes.
- Implement error handling for invalid inputs more robustly.
- Add tests for core functions in `functions.py`.
- Extend to a GUI-based interface or a web API version in the future.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
