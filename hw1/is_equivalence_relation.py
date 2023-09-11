def is_equivalence_relation(set_of_items: tuple, rel: tuple) -> bool:
    for i in set_of_items:
        # checking reflexive
        if (i, i) not in rel:
            return False

    # checking symmetric
    for pair in rel:
        (x, y) = pair
        if (y, x) not in rel:
            return False

    # checking transitive
    for pair in rel:
        (x, y) = pair
        for second_pair in rel:
            (a, b) = second_pair
            if y != a:
                continue
            if (x, b) not in rel:
                return False

    return True


# Test Case 1
set_of_items_1 = (1, 2, 3)
relation_1 = ((1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1))
# This relation is reflexive, symmetric, and transitive.
assert is_equivalence_relation(set_of_items_1, relation_1) == True

# Test Case 2
set_of_items_2 = (1, 2, 3)
relation_2 = ((1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3))
# This relation is reflexive and transitive but not symmetric.
assert is_equivalence_relation(set_of_items_2, relation_2) == False

# Test Case 3
set_of_items_3 = (1, 2, 3)
relation_3 = ((1, 2), (2, 1), (2, 3), (3, 2))
# This relation is not reflexive, symmetric, and not transitive.
assert is_equivalence_relation(set_of_items_3, relation_3) == False

# Test Case 4
set_of_items_4 = (1, 2, 3)
relation_4 = ((1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2))
# This relation is reflexive and symmetric but not transitive.
assert is_equivalence_relation(set_of_items_4, relation_4) == False

# Test Case 5
set_of_items_5 = (1, 2, 3)
relation_5 = ((1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (1, 3), (3, 1))
# This relation is reflexive and transitive but not symmetric.
assert is_equivalence_relation(set_of_items_5, relation_5) == False

# Test Case 6
set_of_items_6 = ()
relation_6 = ()
# An empty set is always an equivalence relation.
assert is_equivalence_relation(set_of_items_6, relation_6) == True

# Test Case 7
set_of_items_7 = (1,)
relation_7 = ((1, 1),)
# A single-element set with a single pair is an equivalence relation.
assert is_equivalence_relation(set_of_items_7, relation_7) == True

# Test Case 8
set_of_items_8 = (1,)
relation_8 = ()
# A single-element set with an empty relation is not reflexive.
assert is_equivalence_relation(set_of_items_8, relation_8) == False

# Test Case 9
set_of_items_9 = (1, 2)
relation_9 = ((1, 1), (2, 2), (1, 2), (2, 1))
# This relation is reflexive, symmetric, and transitive.
assert is_equivalence_relation(set_of_items_9, relation_9) == True

# Test Case 10
set_of_items_10 = (1, 2, 3, 4)
relation_10 = ((1, 2), (2, 3), (1, 3), (2, 1), (3, 2), (3, 1), (1, 1), (2, 2), (3, 3))
# This relation is symmetric and transitive but not reflexive.
assert is_equivalence_relation(set_of_items_10, relation_10) == False
