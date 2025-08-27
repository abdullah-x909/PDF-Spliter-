# 📚 PDF Splitter Tool

A simple **Python CLI tool** to split large PDF files into smaller parts.
Supports:

* 🔍 Auto-detect PDFs in current folder
* 🗂️ Lets you choose which PDF to split
* 🔐 Handles encrypted PDFs (asks password)
* ✂️ Split into custom number of pages per part
* 🗁 Custom output folder name

---

## 🚀 Features

* Works on **Linux, macOS, and Windows**
* Uses [PyPDF2](https://pypi.org/project/PyPDF2/) library
* Lightweight, no GUI required
* Perfect for splitting large documents (books, reports, scanned files)

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abdullah-x909/pdf-splitter.git
   cd pdf-splitter
   ```

2. Create a virtual environment (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install PyPDF2
   ```

---

## 📌 Usage

Place your PDF(s) in the same folder as `pdf_splitter.py`.

Run the tool:

```bash
python pdf_splitter.py
```

### Example session:

```
🔍 Scanning for PDF files...

1. mybook.pdf
2. research.pdf

Enter the number of the PDF you want to split: 1
Enter number of pages per split (default 50): 50
Enter output folder name (default: output_parts): mybook_parts

🚀 Splitting 'mybook.pdf' into parts of 50 pages...
Enter PDF password: *****

📄 Created: mybook_parts/part_1.pdf (50 pages)
📄 Created: mybook_parts/part_2.pdf (50 pages)
...
✅ Done! 17 parts created in 'mybook_parts'
```

---

## 🔐 Encrypted PDFs

If the file is password-protected, the script will ask you to enter the password.

* If correct → the file will be split.
* If wrong → the script will exit.

---

## 📜 License

MIT License — free to use, modify, and share.

---

## 👨‍💻 Author

Developed by [Abdullah](https://github.com/abdullah-x909)
Contributions welcome! 🚀
