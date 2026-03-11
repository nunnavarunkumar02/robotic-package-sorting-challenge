from sorter import sort

def test_cases():
    cases = [
        (10, 10, 10, 5, "STANDARD"),
        (200, 10, 10, 5, "SPECIAL"),
        (100, 100, 100, 10, "SPECIAL"),
        (100, 100, 100, 25, "REJECTED"),
        (10, 10, 10, 25, "SPECIAL"),
    ]

    for width, height, length, mass, expected in cases:
        result = sort(width, height, length, mass)
        assert result == expected, f"Expected {expected}, got {result}"

    print("All tests passed!")

if __name__ == "__main__":
    test_cases()
