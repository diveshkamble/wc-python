<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>wc-python</h1>
<h3>◦ print newline, word, and byte counts for a file</h3>
<h3>◦ Developed with the software and tools below.</h3>

---

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
  - [🤖 Running wc-python](#-running-wc-python)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)

---

## 📍 Overview

Print newline, word, and byte counts for a FILE. A word is a non-zero-length sequence
of characters delimited by white space.

```
python wc-python [OPTION]... [FILE]
```

---

## 🚀 Getting Started

### 🔧 Installation

1. Clone the wc-python repository:

```sh
git clone https://github.com/diveshkamble/wc-python.git
```

2. Change to the project directory:

```sh
cd wc-python
```

### 🤖 Running wc-python

```sh
python wc-python test.txt
```

```sh
python wc-python -l test.txt
```

```sh
python wc-python -c test.txt
```

```sh
python wc-python -w test.txt
```

---

## 🛣 Roadmap

> - [x] `ℹ️  Task 1: Implement line count`
> - [x] `ℹ️  Task 2: Implement word count`
> - [x] `ℹ️  Task 3: Implement bytes count`
> - [ ] `ℹ️  Task 4: Support to read from standard input if no filename is specified`

---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:

1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).

```sh
git checkout -b new-feature-branch
```

4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.

```sh
git commit -m 'Implemented new feature.'
```

6. Push your changes to your forked repository on GitHub using the following command

```sh
git push origin new-feature-branch
```

7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
   The project maintainers will review your changes and provide feedback or merge them into the main branch.

---
