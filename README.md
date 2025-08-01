# Inventory CLI Tool

Small command-line tool to browse stock, search & order items, and list inventory by warehouse with simple user authentication.

## Features
- List items by warehouse
- Search an item, view availability, and place an order
- Browse inventory by category
- Recursive personnel lookup with password check

## Project Structure
- `methods.py` — core logic (loading stock, searching, ordering, auth)
- `query.py` — entry point / CLI orchestration
- `data/` — expected to contain `personnel` and `stock` definitions (imported by `methods.py`)

## Requirements
- Python 3.8+
- `datetime` and `collections` (standard library)

## Setup & Run
- Clone the repository:
  - git clone <repo-url>
  - cd <repo-directory>

- Ensure your data module is available and properly populated
- Run the CLI:
  - python query.py

- Follow the interactive prompts:
  - Enter your name
  - Choose an operation (1–4)
  - Authenticate if placing an order
