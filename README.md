# PySpector

**PySpector** is a beginner-friendly Python static code analyzer that inspects your Python source files to report on function characteristics such as length and documentation (docstring presence).  
It helps you improve code quality by identifying functions that may need better comments or refactoring due to length, making your code cleaner, more maintainable, and professional — skills highly valued by top tech companies like Google, Apple, and Meta.

---

## Features

- Parses Python source code using Python’s built-in Abstract Syntax Tree (AST) module
- Detects every function’s name, starting line number, length in lines, and whether it has a docstring
- Displays results in a clear, color-coded terminal table using the `rich` library
- Designed for ease of use and educational value for early-stage developers

---

## Why PySpector?

Writing clean, well-documented code is critical for collaboration and long-term maintenance in any software project. PySpector automates the detection of poorly documented or overly long functions, empowering you to improve your code proactively.

**This project showcases skills in:**

- Code parsing and analysis
- Python AST manipulation
- Command-line interface (CLI) development
- Using third-party libraries like `rich` for polished output
- Writing clear documentation and project structure

These are exactly the kinds of skills top companies look for in software engineers.

---

<h3>Example</h3>
<p>Given the following <code>sample.py</code> file:</p>

<pre><code>def greet(name):
    """Say hello to the user."""
    print(f"Hello, {name}!")

def complicated():
    # No docstring here
    total = 0
    for i in range(100):
        total += i
    return total
</code></pre>

<h3>Running:</h3>
<p><code>python main.py sample.py</code></p>

<table>
  <thead>
    <tr>
      <th>Function</th>
      <th>Line No.</th>
      <th>Length</th>
      <th>Docstring?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>greet</td>
      <td>1</td>
      <td>3</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>complicated</td>
      <td>5</td>
      <td>6</td>
      <td>No</td>
    </tr>
  </tbody>
</table>

<h3>How It Works</h3>
<ul>
  <li>The program reads your Python file and uses Python’s AST module to parse the code into a syntax tree.</li>
  <li>It walks the tree looking for function definitions.</li>
  <li>For each function, it records:
    <ul>
      <li>Name</li>
      <li>Starting line number</li>
      <li>Length (number of lines)</li>
      <li>Docstring presence</li>
    </ul>
  </li>
  <li>This information is printed in a neatly formatted table using the rich library for colorful CLI output.</li>
</ul>

<h3>Future Enhancements</h3>
<ul>
  <li>Scan entire folders recursively to analyze multiple files</li>
  <li>Perform basic natural language analysis on docstrings for quality scoring</li>
  <li>Export analysis reports in Markdown or HTML formats</li>
  <li>Add interactive command-line options for customized reports</li>
</ul>

<p>MIT License © Marc Yebra</p>

<p>Created by Marc Yebra</p>

