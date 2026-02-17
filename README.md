# Kramer-Specter Deobfuscator

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Language](https://img.shields.io/badge/language-Python-blue.svg)]()
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)]()

</div>

## 🌟 Introduction

**Kramer-Specter Deobfuscator** is a powerful utility designed to reverse the obfuscation applied by the [Kramer](https://github.com/billythegoat356/Kramer) and [Specter](https://github.com/billythegoat356/Specter) tools. It helps developers and security researchers analyze protected Python scripts by restoring them to a readable state.

## ✨ Key Features

-   **🔓 Dual Support**: Handles both Kramer and Specter obfuscation techniques.
-   **🐍 Python Bytecode Analysis**: Extracts and reconstructs code from marshal payloads.
-   **💾 Save Functionality**: Option to save the deobfuscated code or dumped marshal data.

## 🚀 Getting Started

### Prerequisites

-   Python 3.x

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/KhanhNguyen9872/kramer-specter_deobf.git
    cd kramer-specter_deobf
    ```

### Usage

1.  **Run the script**:
    ```bash
    python kramer-specter-deobf.py
    ```
2.  **Input File**: Enter the path to your Kramer or Specter obfuscated file.
3.  **Inspect**: Press Enter to view the code or the `marshal.loads` payload.
4.  **Save**: Type `save` to export the result to a file.

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## ✍️ Author

**Nguyễn Văn Khánh** (KhanhNguyen9872)

-   GitHub: [@KhanhNguyen9872](https://github.com/KhanhNguyen9872)
