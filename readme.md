# 🔐 Password Generator

A small Python study project for generating random PINs, passwords, and URL-safe random strings.

The main goal of this project is **learning**, not creating a professional password manager.

## 📚 What I learned

This project was made while I was getting back into programming.

I built the project by reading Python documentation and examples. I did **not use AI to build the code**. I used documentation to understand how the modules and methods worked, then wrote and adapted the code myself.

The main things I practiced were:

- `while` loops
- `if`, `elif`, and `else`
- `input()`
- `int()`
- `.isdigit()`
- Lists and strings
- `string.digits`
- `string.ascii_letters`
- `secrets.choice()`
- `secrets.token_urlsafe()`
- `''.join()`
- `any()`
- `sum()`
- `time.sleep()`
- Using external Python packages
- Copying generated text to the clipboard

## 🎯 Project idea

The idea is simple:

> Generate different kinds of random passwords from a terminal menu and copy the result directly to the clipboard.

I did not want to use `print(password)` as the main way to show the generated password.

The reason is simple: if a password is printed in the terminal, someone looking at the screen can see it.

Instead, the program copies the generated password to the clipboard:

```python
clip.copy(password)
```

This makes the program more practical for temporary passwords or other situations where I only need to generate a random value and paste it somewhere.

## 🔒 Why `secrets` instead of `random`?

One of the main things I learned from the Python documentation was the `secrets` module.

Python's `random` module is useful for normal randomization, simulations, games, and similar situations.

For security-related random values, Python provides `secrets`.

For example:

```python
secrets.choice(string.digits)
```

This chooses a random digit using the `secrets` module.

The project also uses:

```python
secrets.token_urlsafe(16)
```

which generates a random URL-safe text string.

## 🧩 How the generator works

One of the most important pieces of the project is:

```python
''.join(secrets.choice(alphabet) for _ in range(value))
```

I found this general pattern through the documentation/examples and used it in my project.

I understand it as several small operations working together:

```text
range(value)
    ↓
for
    ↓
secrets.choice(alphabet)
    ↓
choose one character
    ↓
join()
    ↓
put all characters together
```

For example, if `value` is `6`, the loop generates six characters and `join()` combines them into one string.

Without `join()`, the loop can still run, but the characters would be produced separately instead of being combined into one password string.

## 🔢 Available options

The program currently has six generation options.

### 1. Four-digit PIN

```text
PIN - 1234 - only numbers
```

It uses:

```python
string.digits
```

and generates four random digits.

### 2. Six-digit PIN

Same idea, but with six digits.

### 3. Custom numeric password

The user chooses how many digits should be generated.

For example:

```text
Choose how many numbers it will have. 12
```

The program then generates a 12-digit random string.

### 4. Ten-character password

This option generates a 10-character password using letters and numbers.

It checks that the result contains:

- at least one lowercase letter
- at least one uppercase letter
- at least three numbers

The check uses:

```python
any(c.islower() for c in password)
any(c.isupper() for c in password)
sum(c.isdigit() for c in password) >= 3
```

If the generated password does not satisfy the requirements, the program generates another one.

### 5. URL-safe random string

This option uses:

```python
secrets.token_urlsafe(16)
```

The Python documentation describes this as returning a random URL-safe text string containing random bytes.

### 6. Custom alphanumeric password

The user chooses the desired length.

The program then generates a password using:

```python
string.ascii_letters + string.digits
```

This means the result can contain uppercase letters, lowercase letters, and numbers.

## 📋 Clipboard

The project uses the external package `pyperclip`.

The import is:

```python
import pyperclip as clip
```

Then:

```python
clip.copy(password)
```

copies the generated value to the clipboard.

### Installation

Python is required.

`pyperclip` must also be installed:

```bash
pip install pyperclip
```

After installation, the program can use the clipboard functionality provided by `pyperclip`.

## 📖 Documentation

The project was developed mainly by reading Python documentation.

Useful documentation:

- Python `secrets` module:
  https://docs.python.org/3/library/secrets.html
- Python `string` module:
  https://docs.python.org/3/library/string.html
- Python `tkinter` clipboard documentation:
  https://docs.python.org/pt-br/3.14/library/tkinter.html#tkinter.Misc.clipboard_append
- `pyperclip`:
  https://pypi.org/project/pyperclip/

The Tkinter documentation was useful for understanding the general Python clipboard functionality, while this project itself uses `pyperclip` to make copying simpler.

## ⚠️ Important note

This is a **learning project**, not a professional password manager.

I do not recommend using this exact program as a complete security solution for important real-world accounts.

The main purpose is to practice Python and understand how secure random generation, strings, loops, conditions, and external packages can work together.

## 🚧 Future ideas

There are several things I may experiment with later:

- Add special characters
- Allow the user to choose which character types are included
- Improve the password generation rules
- Create a graphical interface
- Improve input validation
- Add more password formats
- Create a system that accepts a word or name as input and transforms it into a generated string
- Study better ways of handling generated credentials
- Experiment with saving data locally

Some of these ideas are intentionally left for later because the main goal right now is learning the fundamentals.

## 🧠 Why I made this

This is one of my small projects while returning to programming.

I wanted to take something I found in the documentation and turn it into something practical instead of only reading the example.

The project is simple, but it helped me practice turning documentation into a working program.

---

**Study project — Python 🔐🐍**
