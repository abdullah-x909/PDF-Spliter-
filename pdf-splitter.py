#!/usr/bin/env python3

import os
import getpass
from PyPDF2 import PdfReader, PdfWriter

def list_pdfs(folder="."):
    """Return list of PDFs in the folder"""
    return [f for f in os.listdir(folder) if f.lower().endswith(".pdf")]

def split_pdf(input_file, pages_per_part=50, output_dir="output_parts"):
    """Split PDF into chunks"""
    reader = PdfReader(input_file)

    # If encrypted, ask password
    if reader.is_encrypted:
        password = getpass.getpass("Enter PDF password: ")
        if reader.decrypt(password) != 0:
            print("✅ PDF decrypted successfully.")
        else:
            print("❌ Wrong password, cannot decrypt!")
            return

    total_pages = len(reader.pages)
    os.makedirs(output_dir, exist_ok=True)

    part = 1
    for start in range(0, total_pages, pages_per_part):
        writer = PdfWriter()
        end = min(start + pages_per_part, total_pages)

        for page in range(start, end):
            writer.add_page(reader.pages[page])

        output_file = os.path.join(output_dir, f"part_{part}.pdf")
        with open(output_file, "wb") as f:
            writer.write(f)

        print(f"📄 Created: {output_file} ({end-start} pages)")
        part += 1

    print(f"\n✅ Done! {part-1} parts created in '{output_dir}'")

def main():
    print("🔍 Scanning for PDF files...\n")
    pdfs = list_pdfs(".")

    if not pdfs:
        print("❌ No PDF files found in this folder.")
        return

    # List available PDFs
    for i, pdf in enumerate(pdfs, start=1):
        print(f"{i}. {pdf}")

    choice = input("\nEnter the number of the PDF you want to split: ")
    try:
        choice = int(choice) - 1
        input_file = pdfs[choice]
    except (ValueError, IndexError):
        print("❌ Invalid choice.")
        return

    try:
        pages_per_part = int(input("Enter number of pages per split (default 50): ") or 50)
    except ValueError:
        pages_per_part = 50

    output_dir = input("Enter output folder name (default: output_parts): ") or "output_parts"

    print(f"\n🚀 Splitting '{input_file}' into parts of {pages_per_part} pages...")
    split_pdf(input_file, pages_per_part, output_dir)


if __name__ == "__main__":
    main()
