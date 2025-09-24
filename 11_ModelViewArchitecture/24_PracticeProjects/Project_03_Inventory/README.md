# Inventory Management System with PySide6

This project is a comprehensive desktop application built with PySide6 (Qt for Python) that demonstrates the Model-View-Delegate pattern along with practical implementations of data persistence, custom widgets, and modern Python practices. It serves as an educational resource for understanding Qt's powerful MVC architecture in a Python context.

## Architecture Overview

### Model-View-Delegate Pattern Implementation

The application implements Qt's Model-View-Delegate pattern with three distinct layers:

1. **Model Layer** (`InventoryModel`):   - Inherits from `QAbstractTableModel`
   - Manages data storage and business logic
   - Implements required methods:
     ```python
     def rowCount(self, parent=QModelIndex()):
     def columnCount(self, parent=QModelIndex()):
     def data(self, index, role=Qt.DisplayRole):
     def setData(self, index, value, role=Qt.EditRole):
     ```
   - Handles data persistence through JSON serialization
   - Provides CRUD operations for inventory items

2. **View Layer**:
   - Main window (`Widget`) with split layout
   - Table view for item listing
   - Detail panel (`ProductDetailsWidget`) for item editing
   - Search and filtering capabilities

3. **Delegate Layer** (`InventoryDelegates`):
   - Custom rendering and editing of table cells
   - Specialized delegates for:
     - Images (`ImageDelegate`)
     - Star ratings (`RatingDelegate`)
     - Supplier selection (`SupplierDelegate`)

## Features

- **Master-Detail View**: Split interface showing a table of items and detailed information
- **Product Management**:
  - Add, edit, and delete inventory items
  - Track product name, quantity, supplier, and rating
  - Add and manage product images
  - Add detailed product descriptions
- **Data Persistence**: Automatically saves data to JSON format
- **Search Functionality**: Real-time search through inventory items
- **Supplier Management**: Manage list of suppliers through a simple interface
- **Rating System**: Visual star-rating system for products
- **Image Support**: Add and manage product images with thumbnail display

## Project Structure

- `main.py`: Application entry point
- `widget.py`: Main window implementation
- `inventorymodel.py`: Data model implementation (MVC pattern)
- `inventoryitem.py`: Product item data structure
- `inventorydelegates.py`: Custom delegates for table view rendering
- `productdetailswidget.py`: Detail view implementation
- `ui_widget.py`: Auto-generated UI code from Qt Designer

## Technical Implementation

### Data Model
- Uses `QAbstractTableModel` for implementing the MVC pattern
- Data stored in JSON format (`data/inventory.json`)
- Images stored in `data/images/` directory

### User Interface
- Table view with custom delegates for:
  - Image thumbnails
  - Star ratings
  - Supplier selection
- Split view interface using `QSplitter`
- Detail panel showing comprehensive item information

### Key Components in Detail

#### 1. Inventory Model (`inventorymodel.py`)
```python
class InventoryModel(QAbstractTableModel):
    # Column enum
    ProductName = 0
    Quantity = 1
    Supplier = 2
    ProductImage = 3
    Rating = 4
    ColumnCount = 5

    def __init__(self, parent=None):
        super().__init__(parent)
        self.items = []
        self.supplierList = []
```
- Implements table model interface
- Manages data persistence
- Handles item validation and unique constraints
- Provides search and filter capabilities

#### 2. Item Structure (`inventoryitem.py`)
```python
class InventoryItem:
    def __init__(self):
        self.productName = ""
        self.quantity = 0
        self.supplier = ""
        self.imagePath = ""
        self.image = QPixmap()
        self.rating = 0  # 1-5 stars
        self.description = ""
        self.lastUpdated = QDateTime.currentDateTime()
```
- Represents individual inventory items
- Contains all item properties
- Used for data transfer and storage

#### 3. Custom Delegates (`inventorydelegates.py`)
- **ImageDelegate**: 
  - Displays thumbnails in table
  - Handles image file selection
  - Manages image scaling and caching
- **RatingDelegate**:
  - Shows interactive star rating
  - Provides click-to-rate functionality
  - Custom star rendering with antialiasing
- **SupplierDelegate**:
  - Implements dropdown selection with QComboBox
  - Manages supplier list synchronization

#### 4. Data Persistence System
- JSON-based storage:
  ```python
  # Saving example (simplified)
  def saveToFile(self, filename):
      items_data = []
      for item in self.items:
          item_dict = {
              "productName": item.productName,
              "quantity": item.quantity,
              "supplier": item.supplier,
              # ... other properties
          }
          items_data.append(item_dict)
  ```
- Automatic save/load functionality
- Image file management
- Data validation and error handling

## Building and Running the Project

### Prerequisites
- Python 3.x
- PySide6
- Qt Designer (optional, for UI editing)

### Build Steps
1. Install the required packages:
   ```bash
   pip install PySide6
   ```
2. Run the application:
   ```bash
   python main.py
   ```

The application will create necessary data directories on first run.

## Usage

1. **Adding Items**:
   - Click "Add" button
   - Enter product name
   - Fill in details in the detail panel

2. **Editing Items**:
   - Select an item in the table
   - Click "Edit" or directly edit cells
   - Modify details in the detail panel

3. **Managing Suppliers**:
   - Click "Manage Suppliers"
   - Enter comma-separated supplier names

4. **Search**:
   - Type in the search box to filter items

5. **Images**:
   - Click "Change Image" in detail panel
   - Select an image file (supports PNG, JPG)

## Data Storage

- All data is automatically saved when the application closes
- Images are copied to the data directory
- Data can be found in:
  - `data/inventory.json`: Item data
  - `data/images/`: Product images

## Implementation Details for Students

### Signal-Slot Connections
Example from `widget.py`:
```python
def setupConnections(self):
    # Button connections
    self.ui.addButton.clicked.connect(self.onAddItem)
    self.ui.editButton.clicked.connect(self.onEditItem)
    self.ui.deleteButton.clicked.connect(self.onDeleteItem)
    self.ui.manageSuppliersButton.clicked.connect(self.onManageSuppliers)
    
    # Search functionality
    self.ui.searchLineEdit.textChanged.connect(self.onSearchTextChanged)
    
    # Selection change handling
    selection_model = self.ui.inventoryTableView.selectionModel()
    selection_model.currentRowChanged.connect(self.onSelectionChanged)
    
    # Details panel connections
    self.detailsWidget.imageChanged.connect(self.onImageChanged)
    self.detailsWidget.descriptionChanged.connect(self.onDescriptionChanged)
```

### Data Loading Process
1. Application startup flow (`widget.py`):
   ```python
   def __init__(self, parent=None):
       super().__init__(parent)
       self.ui = Ui_Widget()
       self.ui.setupUi(self)

       # Set up data directory
       dataDir = QDir.current()
       if not dataDir.exists("data"):
           dataDir.mkdir("data")
       if not dataDir.exists("data/images"):
           dataDir.mkdir("data/images")
           
       self.setupModel()
       self.setupConnections()
       self.loadData()
       self.setupDelegates()
   ```

2. JSON handling (`inventorymodel.py`):
   ```python
   def loadFromFile(self, filename):
       try:
           if not os.path.exists(filename):
               return False

           with open(filename, 'r', encoding='utf-8') as f:
               data = json.load(f)

           self.beginResetModel()
           self.items.clear()

           for item_data in data.get("items", []):
               item = InventoryItem()
               item.productName = item_data["productName"]
               item.quantity = item_data["quantity"]
               item.supplier = item_data["supplier"]
               item.imagePath = item_data["imagePath"]
               if item.imagePath:
                   item.image = QPixmap(item.imagePath)
               item.rating = item_data["rating"]
               item.description = item_data["description"]
               item.lastUpdated = QDateTime.fromString(
                   item_data["lastUpdated"], Qt.ISODate
               )
               self.items.append(item)

           self.supplierList = data.get("suppliers", [])
           self.endResetModel()
           return True
       except:
           return False
   ```

### Key Learning Points
1. **Model-View-Delegate Pattern**
   - Separation of concerns using PySide6
   - Data management vs. presentation
   - Custom delegate implementation in Python

2. **Qt Best Practices in Python**
   - Signal-slot mechanism using Python decorators (@Slot)
   - Pythonic resource management
   - Event handling with Qt in Python

3. **Modern Python Features Used**
   - Type annotations and hints
   - Context managers (with statements)
   - List comprehensions
   - Lambda functions

4. **Data Persistence Patterns**
   - JSON serialization with Python's json module
   - File handling with context managers
   - Error handling with try/except

5. **UI Design Patterns**
   - Master-detail views
   - Custom delegates
   - Dynamic updates
   - Search and filtering

This project serves as a comprehensive example of professional Qt development using Python and PySide6. Study the implementation details to understand how various components work together in a real-world Python application.
