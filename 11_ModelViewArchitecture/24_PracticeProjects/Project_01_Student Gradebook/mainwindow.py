from PySide6.QtWidgets import (QMainWindow, QMessageBox, QTableWidgetItem,
                               QAbstractItemView, QHeaderView)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Store UI elements in member variables for easier access
        self.nameEdit = self.ui.nameEdit
        self.subjectEdit = self.ui.subjectEdit
        self.scoreEdit = self.ui.scoreEdit
        self.tableWidget = self.ui.tableWidget
        self.averageScoreLabel = self.ui.averageScoreLabel

        # Connect signals and slots
        self.ui.addStudentButton.clicked.connect(self.add_student)
        self.ui.clearAllButton.clicked.connect(self.clear_students)
        self.tableWidget.itemChanged.connect(self.item_changed)

        # Configure tableWidget properties
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked | 
                                       QAbstractItemView.SelectedClicked)

        # Set font for average score label
        font = self.averageScoreLabel.font()
        font.setBold(True)
        self.averageScoreLabel.setFont(font)

    def add_student(self):
        # Get input values
        name = self.nameEdit.text().strip()
        subject = self.subjectEdit.text().strip()
        score_text = self.scoreEdit.text().strip()

        # Validate inputs
        if not all([name, subject, score_text]):
            QMessageBox.warning(self, "Validation Error", "All fields must be filled in.")
            return

        # Validate score
        score = self.validate_score(score_text)
        if score is None:
            QMessageBox.warning(self, "Validation Error", 
                              "Score must be a number between 0 and 100.")
            return

        # Add new row to table
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)

        # Create and set table items
        name_item = QTableWidgetItem(name)
        subject_item = QTableWidgetItem(subject)
        score_item = QTableWidgetItem(score_text)

        # Make first two columns non-editable
        name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
        subject_item.setFlags(subject_item.flags() & ~Qt.ItemIsEditable)

        # Set items in the table
        self.tableWidget.setItem(row, 0, name_item)
        self.tableWidget.setItem(row, 1, subject_item)
        self.tableWidget.setItem(row, 2, score_item)

        # Apply background color based on score
        if score < 40.0:
            score_item.setBackground(QColor(255, 200, 200))  # Light red
        else:
            score_item.setBackground(QColor(Qt.green))  # Green

        # Clear input fields
        self.nameEdit.clear()
        self.subjectEdit.clear()
        self.scoreEdit.clear()
        self.nameEdit.setFocus()

        # Update average score
        self.update_average_score()

    def clear_students(self):
        # Ask for confirmation
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Are you sure you want to clear all student records?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # Temporarily disconnect itemChanged signal to prevent multiple updates
            self.tableWidget.itemChanged.disconnect(self.item_changed)

            # Clear all rows
            self.tableWidget.setRowCount(0)

            # Reconnect signal
            self.tableWidget.itemChanged.connect(self.item_changed)

            # Reset average score
            self.averageScoreLabel.setText("Average Score: 0.0")

    def item_changed(self, item):
        # Only process changes to the Score column (column 2)
        if item and item.column() == 2:
            score_text = item.text().strip()
            score = self.validate_score(score_text)

            # Validate the edited score
            if score is None:
                QMessageBox.warning(
                    self,
                    "Invalid Score",
                    "Score must be a number between 0 and 100.\nChanges will be reverted."
                )
                # Restore to 0
                item.setText("0")
                return

            # Update cell background based on score
            if score < 40.0:
                item.setBackground(QColor(255, 200, 200))  # Light red for failing scores
            else:
                item.setBackground(QColor(Qt.green))  # Green

            # Update average score
            self.update_average_score()

    def update_average_score(self):
        total_score = 0.0
        count = 0

        # Calculate sum of all scores
        for row in range(self.tableWidget.rowCount()):
            score_item = self.tableWidget.item(row, 2)
            if score_item:
                try:
                    score = float(score_item.text())
                    total_score += score
                    count += 1
                except ValueError:
                    pass

        # Calculate and display average
        average = total_score / count if count > 0 else 0.0
        self.averageScoreLabel.setText(f"Average Score: {average:.1f}")

    def validate_score(self, score_text):
        try:
            score = float(score_text)
            if 0.0 <= score <= 100.0:
                print(f"Score validation passed: {score_text}, score={score}")
                return score
        except ValueError:
            pass

        print(f"Score validation failed: {score_text}")
        return None
