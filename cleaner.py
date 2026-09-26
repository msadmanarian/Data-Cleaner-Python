def sanitize_list(items):
    """Removes leading/trailing whitespace and filters out duplicates."""
    seen = set()
    cleaned = []
    for item in items:
        stripped = str(item).strip()
        if stripped and stripped not in seen:
            seen.add(stripped)
            cleaned.append(stripped)
    return cleaned

if __name__ == "__main__":
    raw_data = ["  apple ", "banana", "apple", "  orange  ", ""]
    print("Original:", raw_data)
    print("Cleaned:", sanitize_list(raw_data))