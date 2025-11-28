# PySide6 Expense Tracker

This is a Python implementation of an Expense Tracker application using PySide6 (Qt for Python).

## Application Description

The Expense Tracker allows you to:
- Add expenses with date, name, amount, and category
- Remove selected expenses
- Filter expenses by any column
- Sort expenses by clicking column headers
- Automatically save/load data to/from a text file

## Project Structure

- **expense.py**: Defines the Expense class that represents a single expense with properties and signals
- **expensemodel.py**: Implements the data model for expenses using QAbstractTableModel
- **expenseproxymodel.py**: Provides sorting and filtering functionality
- **widget.py**: Main UI logic
- **main.py**: Application entry point
- **widget.ui**: UI design file

## Requirements

- Python 3.6 or higher
- PySide6

## Installation

1. Install PySide6:
```
pip install PySide6
```

## Running the Application

Run the main.py script to start the application:
```
python main.py
```

## Usage

- **Add Expense**: Click "Add Expense" and fill in the item name, amount, and category in the dialogs.
- **Remove Expense**: Select an expense and click "Remove Expense".
- **Filter Expenses**: Use the filter box at the top. Select which column to filter by in the dropdown.
- **Sort Expenses**: Click on any column header to sort by that column.

## Data Storage

The application stores data in a text file at "data/expenses.txt". The file is automatically created if it doesn't exist.

## Implementation Details

1. **MVC Architecture**:
   - **Model**: ExpenseModel class
   - **View**: Widget class with UI elements
   - **Controller**: Logic in the Widget class and application signals/slots

2. **Data Persistence**:
   - Data is saved to a tab-separated text file in the "data" folder
   - The application automatically loads and saves data when needed

3. **Filtering and Sorting**:
   - Uses a proxy model for efficient sorting and filtering
   - Real-time filtering as you type in the filter box

## Converting from C++

This is a direct port of a C++ Qt implementation to Python using PySide6. The code structure and functionality are kept as similar as possible while following Python conventions.
