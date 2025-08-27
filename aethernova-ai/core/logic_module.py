# aethernova-ai/core/logic_module.py (Simplified Mock)

MOCK_KB = {
    "father": [("john", "pete"), ("john", "ann")],
    "mother": [("mary", "pete"), ("mary", "ann")]
}

def query(query_string):
    """
    Simulates a Prolog query on the mock knowledge base.
    This is a simplified mock that handles specific hardcoded queries.
    """
    print(f"Executing mock logic query: '{query_string}'")
    if query_string == "father(john, Child)":
        return [{"Child": name} for parent, name in MOCK_KB["father"] if parent == "john"]
    elif query_string == "parent(Parent, pete)":
        solutions = []
        for parent, child in MOCK_KB["father"]:
            if child == "pete":
                solutions.append({"Parent": parent})
        for parent, child in MOCK_KB["mother"]:
            if child == "pete":
                solutions.append({"Parent": parent})
        return solutions
    else:
        return []

def main():
    """
    Main function to demonstrate the logic module's functionality.
    """
    print("--- Demonstrating Mock Symbolic Logic Module ---")

    query1 = "father(john, Child)"
    solutions1 = query(query1)
    print(f"Solutions for '{query1}': {solutions1}")

    query2 = "parent(Parent, pete)"
    solutions2 = query(query2)
    print(f"Solutions for '{query2}': {solutions2}")

    print("\n--- Mock Logic Module Demonstration Complete ---")

if __name__ == "__main__":
    main()
