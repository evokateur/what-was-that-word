# What was that word?

A terminal program that embeds a word list and does semantic search over it.

## Usage

Install and run (uv):

```bash
uv pip install -e .
uv run what-was-that-word /path/to/wordlist.txt
```

Install and run (pip):

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .
what-was-that-word /path/to/wordlist.txt
```

Options:

```bash
python main.py /path/to/wordlist.txt --top-k 10 --model all-MiniLM-L6-v2
```

Exit with `:q` or `:exit`.

Note:

`*.txt` files added to the project directory are gitignored.
