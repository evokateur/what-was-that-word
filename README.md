# What was that word?

A terminal program that embeds a word list so you can do a semantic search over it.

## What is this for?

I have used this to great effect with the [EFF long word list](https://github.com/redacted/XKCD-password-generator/blob/master/xkcdpass/static/eff-long) to do a remember on this one word I'd forgotten in an XKCD password.

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

Note:

`*.txt` files added to the project directory are gitignored.
