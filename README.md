# GoIT Algo HW 02

This repository contains solutions for Homework #2 of the GoIT Algorithms course. It includes:

- `exercise1.py`: Simulates a request queue generator and processor using Python’s `queue` module.
- `exercise2.py`: Checks whether an input string is a palindrome using a double-ended queue (`collections.deque`).

## Requirements

- Python 3.6 or higher

## Installation

```bash
git clone https://github.com/<your-username>/goit-algo-hw-02.git
cd goit-algo-hw-02
```

## Usage

### exercise1.py

```bash
python3 exercise1.py
```

This script continuously generates random requests and processes them. Note: for real concurrency, you’d run generator and processor in separate threads or processes.

### exercise2.py

```bash
python3 exercise2.py
```

This script tests the palindrome function on a sample string. To test your own string, modify the `test_str` variable or import the function into a REPL.

## File Descriptions

- **exercise1.py**

  - `generate_request()`: Creates random integer requests and enqueues them.
  - `process_request()`: Dequeues and processes requests, simulating work with delays.
  - Main loop runs both functions sequentially (note: they block; for real-time you’d use threading).

- **exercise2.py**
  - `is_palindrome(input_string)`: Returns `True` if the input string is a palindrome (ignoring case and spaces), else `False`.
  - Example usage in the `__main__` block prints result for `"A man a plan a canal Panama"`.

## Customization

- Adapt `exercise1.py` to use threading: wrap `generate_request()` and `process_request()` each in separate `threading.Thread`.
- Extend `is_palindrome` to ignore punctuation by adding `replace` calls or regex filtering.
