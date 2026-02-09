import argparse
import readline
from pathlib import Path

import hnswlib
from sentence_transformers import SentenceTransformer


def load_words(word_list_path: Path) -> list[str]:
    lines = word_list_path.read_text(encoding="utf-8").splitlines()
    words = [line.strip() for line in lines if line.strip()]
    return words


def build_index(words: list[str], model_name: str) -> tuple[hnswlib.Index, list[str]]:
    model = SentenceTransformer(model_name)
    embeddings = model.encode(words, normalize_embeddings=True, show_progress_bar=True)

    dimension = embeddings.shape[1]
    index = hnswlib.Index(space="cosine", dim=dimension)
    index.init_index(max_elements=len(words), ef_construction=200, M=16)
    index.add_items(embeddings)
    index.set_ef(50)

    return index, words


def search_loop(
    index: hnswlib.Index, words: list[str], model_name: str, top_k: int
) -> None:
    model = SentenceTransformer(model_name)
    quit_words = {
        "exit",
        "halt",
        "quit",
    }
    print(
        "Ready to find that word. Enter semantic search term(s) or a command prefixed with '/'"
    )

    while True:
        try:
            query = input("> ").strip()
        except EOFError:
            break
        if not query:
            continue
        is_command = query.startswith("/")
        if is_command:
            query = query[1:]

        query_embedding = model.encode([query], normalize_embeddings=True)
        count = min(top_k, len(words))
        labels, distances = index.knn_query(query_embedding, k=count)

        results = [words[label] for label in labels[0]]
        if is_command:
            has_quit_word = any(
                result_word.lower() in quit_words for result_word in results
            )
            if has_quit_word:
                break
            print(f"I don't know how to {query}.")
        else:
            print("\n".join(results))


def configure_readline() -> None:
    readline.set_auto_history(True)
    readline.set_history_length(1000)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Semantic word lookup")
    parser.add_argument(
        "word_list_path", type=Path, help="Path to word list (one per line)"
    )
    parser.add_argument(
        "--top-k", type=int, default=10, help="Number of results to return"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="all-MiniLM-L6-v2",
        help="Sentence-transformers model name",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    words = load_words(args.word_list_path)
    if not words:
        raise ValueError("Word list is empty")

    configure_readline()
    index, words = build_index(words, args.model)
    search_loop(index, words, args.model, args.top_k)


if __name__ == "__main__":
    main()
