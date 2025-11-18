from PySide6.QtWidgets import QWidget, QInputDialog, QMessageBox, QFileSystemModel
from PySide6.QtCore import QDir, Slot
from ui_widget import Ui_Widget


class Widget(QWidget): 
    def __init__(self, parent = None):
        super().__init__(parent)

        # Connect to the ui form
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Create the file system model
        self.model = QFileSystemModel(self)
        self.model.setReadOnly(False)

        # Set root path to current directory
        self.model.setRootPath(QDir.currentPath())

        # Connect the view to the model
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setAlternatingRowColors(True)


        # Set the current directory as the initial location
        index = self.model.index(QDir.currentPath())
        self.ui.treeView.expand(index)
        self.ui.treeView.scrollTo(index)
        self.ui.treeView.resizeColumnToContents(0)

        # Connect button signals to slots
        self.ui.addDirButton.clicked.connect(self.add_new_dir)
        self.ui.removeButton.clicked.connect(self.remove_item)

    @Slot()
    def add_new_dir(self):
        index = self.ui.treeView.currentIndex()
        if not index.isValid():
            return 
        
        # Get directory name from user
        dir_name, ok = QInputDialog.getText(
            self, 
            "Create Directory",
            "Directory name"
        )

        if ok and dir_name:
            # Try to create the directory
            if not self.model.mkdir(index,dir_name).isValid:
                QMessageBox.information(
                    self, 
                    "Create Directory",
                    "Failed to create the directory"
                )


    @Slot()
    def remove_item(self):
        index = self.ui.treeView.currentIndex()
        if not index.isValid():
            return  
        
        # Determine if it's a directory or a file and remove accordingly
        file_info = self.model.fileInfo(index)
        ok = False

        if file_info.isDir():
            ok = self.model.rmdir(index)
        else:
            ok = self.model.remove(index)

        if not ok:
            QMessageBox.information(
                self, 
                "Delete",
                f"Failed to delete {self.model.fileName(index)}"
            ) 
