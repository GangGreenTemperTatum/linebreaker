# Burp Linebreaker

<div align="center">

<img
  src="assets/burp-linebreaker.webp"
  alt="Logo"
  align="center"
  width="144px"
  height="144px"
/>

## A Burp Suite extension that renders escaped newlines (`\n`) as actual line breaks

_... making it easier to read and modify request/response data_ 🔋

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/GangGreenTemperTatum/burp-linebreaker)](https://github.com/GangGreenTemperTatum/burp-linebreaker/releases)
[![GitHub stars](https://img.shields.io/github/stars/GangGreenTemperTatum/burp-linebreaker?style=social)](https://github.com/GangGreenTemperTatum/burp-linebreaker/stargazers)
[![BApp Store](https://img.shields.io/badge/BApp%20Store-Submission%20In%20Progress-yellow)](https://portswigger.net/bappstore)
[![License](https://img.shields.io/github/license/GangGreenTemperTatum/burp-linebreaker?branch=main)](https://github.com/GangGreenTemperTatum/burp-linebreaker/blob/main/LICENSE)

[Report Bug](https://github.com/GangGreenTemperTatum/burp-linebreaker/issues) •
[Request Feature](https://github.com/GangGreenTemperTatum/burp-linebreaker/issues)

</div>

- [Burp Linebreaker](#burp-linebreaker)
  - [A Burp Suite extension that renders escaped newlines (`\n`) as actual line breaks](#a-burp-suite-extension-that-renders-escaped-newlines-n-as-actual-line-breaks)
  - [Features](#features)
  - [🚀 Quick Start Installation](#-quick-start-installation)
  - [Usage](#usage)
  - [📁 Project Structure](#-project-structure)
  - [🤝 Contributing](#-contributing)
  - [📄 License](#-license)
  - [🔐 Security](#-security)
  - [⭐ Star History](#-star-history)

## Features

- Adds a new tab "Newline View" to Burp's message editor
- Automatically converts `\n` sequences to actual line breaks
- Supports both viewing and editing of request/response data
- Maintains original message integrity when not modified

## 🚀 Quick Start Installation

1. Download and install [Burp Suite](https://portswigger.net/burp/communitydownload)
2. Go to Burp Suite → Extender → Extensions
3. Click "Add"
4. Set Extension Type to "Python"
5. Select the `burp-linebreaker.py` file
6. Click "Next" to load the extension

## Usage

1. The extension adds a new "Newline View" tab in any message editor within Burp Suite
2. When viewing requests or responses containing escaped newlines (`\n`), switch to the "Newline View" tab
3. The content will be displayed with proper line breaks
4. You can edit the content if needed, and changes will be preserved

## 📁 Project Structure

- Burp Suite (Free or Pro)
- Jython 2.7+ (required for Python extensions in Burp)

## 🤝 Contributing

Contributions are welcome! Please see the [Contributing Guide](docs/contributing.md).

## 📄 License

This project is licensed under the MIT - see the
[LICENSE](LICENSE) file for details.

## 🔐 Security

See the [Security Policy](SECURITY.md) for reporting vulnerabilities.

## ⭐ Star History

[![GitHub stars](https://img.shields.io/github/stars/GangGreenTemperTatum/burp-linebreaker?style=social)](https://github.com/GangGreenTemperTatum/burp-linebreaker/stargazers)

By watching the repo, you can also be notified of any upcoming releases.

[![Star history graph](https://api.star-history.com/svg?repos=GangGreenTemperTatum/burp-linebreaker&type=Date)](https://star-history.com/#GangGreenTemperTatum/burp-linebreaker&Date)
