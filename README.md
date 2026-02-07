# what-was-that-word

A terminal program that embeds a word list and does semantic search over it.

## Usage

Install dependencies (uv):

```bash
uv venv
. .venv/bin/activate
uv pip install -e .
```

Install dependencies (pip):

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .
```

Run (no venv activate):

```bash
uv run what-was-that-word /path/to/wordlist.txt
```

Run (activated venv):

```bash
what-was-that-word /path/to/wordlist.txt
```

Options:

```bash
python main.py /path/to/wordlist.txt --top-k 10 --model all-MiniLM-L6-v2
```

Exit with `:q` or `:exit`.

Note:

`*txt` files added to the project directory are gitgnored.
