# 📁 JPG File Organizer – Python Task Automation

## 📌 Project Overview

The JPG File Organizer is a simple Python automation project developed as part of the **CodeAlpha Python Programming Internship**. It automatically moves JPG images from a source folder to a destination folder, helping users organize files efficiently.

## ✨ Features

- Automatically identifies JPG image files.
- Supports both `.jpg` and `.JPG` extensions.
- Moves images to the specified destination folder.
- Skips files when a file with the same name already exists in the destination.
- Keeps other file types unchanged.
- Displays a summary of moved and skipped files.
- Handles common folder and file errors.

## 🛠️ Technologies Used

- **Python 3**
- `os` – File and directory operations.
- `shutil` – Moving files between folders.

## 📂 Project Structure

```text
CodeAlpha_TaskAutomation/
├── file_organizer.py
└── README.md
```

## 🚀 How to Run the Project

### Step 1: Install Python

Install Python 3 from [python.org](https://www.python.org/downloads/) if it is not already installed.

### Step 2: Clone the Repository

```bash
git clone https://github.com/chatzz06/CodeAlpha_TaskAutomation.git
```

### Step 3: Open the Project Folder

```bash
cd CodeAlpha_TaskAutomation
```

### Step 4: Run the Program

```bash
python file_organizer.py
```

On Windows, you can also use:

```bash
py file_organizer.py
```

### Step 5: Enter Folder Paths

Enter the source folder path containing your images and the destination folder path where you want to move them.

## 💻 Example

**Source folder before execution:**

```text
TestFiles/
├── photo1.jpg
├── photo2.JPG
├── notes.txt
└── document.pdf
```

**Destination folder after execution:**

```text
OrganizedImages/
├── photo1.jpg
└── photo2.JPG
```

The other files remain in the source folder.

### Sample Output

```text
========================================
       JPG FILE ORGANIZER
========================================
Enter the source folder path: TestFiles
Enter the destination folder path: OrganizedImages

Moved: photo1.jpg
Moved: photo2.JPG

========================================
       FILE ORGANIZATION SUMMARY
========================================
Files moved:   2
Files skipped: 0
Destination:   OrganizedImages
Task completed!
```

*Note: The displayed paths and output are examples; actual output depends on your files and folder locations.*

## 🎯 Concepts Learned

- Python functions
- File handling and directory management
- `os` and `shutil` modules
- Conditional statements and loops
- Exception handling
- Automation of repetitive tasks

## ⚠️ Important Note

This program **moves files rather than copying them**. Test it with sample images first and choose a destination outside the source folder. Existing destination files with matching names are skipped to avoid overwriting them.

## 👨‍💻 Author

**GitHub:** [chatzz06](https://github.com/chatzz06)

## 📜 Internship

Developed as part of the **CodeAlpha Python Programming Internship**.

---

⭐ If you find this project useful, feel free to explore the repository!
