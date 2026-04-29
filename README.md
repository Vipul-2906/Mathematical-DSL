# MathDSL — Visual Compiler for Mathematical Problems

MathDSL is a domain-specific language (DSL) that solves mathematical problems while showing how a compiler processes input step by step. It combines a custom compiler pipeline with a web interface for visualization.

---

## Features

- Custom DSL for writing math problems (geometry and trigonometry)
- Tokenization (Lexer output)
- Parse Tree (Concrete Syntax Tree)
- Abstract Syntax Tree (AST)
- Graphical visualization of Parse Tree and AST
- Step-by-step solution generation
- Parser trace for understanding execution flow
- Web-based interface for interactive use

---

## Tech Stack

- Python — core logic (lexer, parser, solver)
- Flask — backend server
- Graphviz — tree visualization
- HTML, CSS, JavaScript — frontend interface

---

## Project Structure

```
src/
├── app.py
├── lexer.py
├── parser.py
├── solver.py
├── parse_tree.py
├── ast_visualizer.py
├── index.html
├── static/
│   ├── ast_graph.png
│   └── parse_tree_graph.png
```

---

## Getting Started

### 1. Clone the repository

```
git clone <repo-url>
cd <repo-folder>
```

### 2. Install dependencies

```
pip install flask graphviz
```

### 3. Install Graphviz (required)

Download and install from:
https://graphviz.org/download/

Make sure Graphviz is added to your system PATH.

---

### 4. Run the application

```
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

## Example Inputs

### Pythagoras

```
solve pythagoras
where a = 3, b = 4
find c
```

### Trigonometry

```
solve sin
where angle = 30
find value
```

---

## Output Includes

- Tokens (Lexer stage)
- Parse Tree (text and graph)
- AST (text and graph)
- Parser trace
- Final result with explanation

---

## Notes

- Graph images are generated inside the `static/` folder
- UI automatically refreshes graphs after execution
- The system is modular and can be extended easily

---

## Possible Extensions

- Add more mathematical domains (algebra, calculus)
- Interactive graph visualization
- Step-by-step parsing animation
- Syntax highlighting in the editor

---

- This project focuses on combining compiler design concepts with practical problem solving in a simple and visual way.

---

## Author
Vipul Kumar
