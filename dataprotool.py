import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QTextEdit, QWidget, QVBoxLayout, QPushButton, \
    QFileDialog, QLabel


# Part 1: Define the main application class
class DataPreprocessingTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Preprocessing Tool")

        # Create a tab widget for the application
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # Part 2: Initialize Load Data Widget
        self.initialize_load_data_widget()  # TODO: Implement this

        # Part 3: Initialize Pandas Ready Widget
        self.initialize_pandas_ready_widget()  # TODO: Implement this

        # Part 4: Initialize Terminal Widget
        self.initialize_terminal_widget()  # TODO: Implement this

        self.show()

        # TODO: Initialize any data structures or variables here
        self.data = None  # To store the loaded and preprocessed data

    # Part 2: Load Data Widget Initialization
    def initialize_load_data_widget(self):
        self.load_data_widget = QWidget()
        self.load_data_layout = QVBoxLayout()
        self.load_data_button = QPushButton("Load Data to Tool")
        self.load_data_button.clicked.connect(self.load_data)
        self.load_data_layout.addWidget(self.load_data_button)
        self.load_data_widget.setLayout(self.load_data_layout)
        self.tab_widget.addTab(self.load_data_widget, "Load Data")

        # TODO: Add more UI components as needed

    # Part 3: Pandas Ready Widget Initialization
    def initialize_pandas_ready_widget(self):
        self.pandas_ready_widget = QWidget()
        self.pandas_ready_layout = QVBoxLayout()

        # Add Pandas Ready status label
        self.pandas_status_label = QLabel("Pandas Ready: No Data")
        self.pandas_ready_layout.addWidget(self.pandas_status_label)

        # Add File Loaded status label
        self.file_loaded_status_label = QLabel("File Loaded: No")
        self.pandas_ready_layout.addWidget(self.file_loaded_status_label)

        self.pandas_ready_widget.setLayout(self.pandas_ready_layout)
        self.tab_widget.addTab(self.pandas_ready_widget, "Load and Pandas Status")

        # TODO: Add more UI components as needed

    # Part 4: Terminal Widget Initialization
    def initialize_terminal_widget(self):
        self.terminal_widget = QWidget()
        self.terminal_layout = QVBoxLayout()
        self.terminal_text_edit = QTextEdit()
        self.execute_button = QPushButton("Execute")
        self.execute_button.clicked.connect(self.execute_commands)
        self.terminal_layout.addWidget(self.terminal_text_edit)
        self.terminal_layout.addWidget(self.execute_button)
        self.terminal_widget.setLayout(self.terminal_layout)
        self.tab_widget.addTab(self.terminal_widget, "Terminal")

        # TODO: Add more UI components as needed

    # Part 2: Load and preprocess data
    def load_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        filters = 'CSV Files (*.csv);;Excel Files (*.xlsx);;Text Files (*.txt)'
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select File', '', filters, options=options)

        if file_path:
            # Load and preprocess data
            self.data = self.load_and_preprocess_data(file_path)

            # Update Pandas Ready status
            if self.data is not None:
                self.pandas_status_label.setText("Pandas Ready: Yes")
            else:
                self.pandas_status_label.setText("Pandas Ready: No Data")

            # Update File Loaded status
            self.file_loaded_status_label.setText("File Loaded: Yes")  # TODO: Handle cases where data loading fails

    # Part 2: Load and preprocess data based on file type
    def load_and_preprocess_data(self, file_path):
        try:
            # TODO: Determine file type and load data accordingly
            if file_path.lower().endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.lower().endswith(('.xlsx', '.xls')):
                df = pd.read_excel(file_path)
            elif file_path.lower().endswith('.txt'):
                with open(file_path, 'r') as file:
                    file_content = file.read()
                    df = pd.DataFrame({'Text Data': [file_content]})
            else:
                print("Unsupported file format.")
                return None
            return df
        except Exception as e:
            print("Error loading and preprocessing data:", e)
            return None

    # Part 4: Execute commands in the terminal
    def execute_commands(self):
        commands = self.terminal_text_edit.toPlainText()
        if self.data is not None:
            try:
                exec(commands, {'data': self.data})
            except Exception as e:
                print("Error executing commands:", e)
        else:
            print("No data available to execute commands on.")


# Part 1: Main function to start the application
def main():
    app = QApplication(sys.argv)
    window = DataPreprocessingTool()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
