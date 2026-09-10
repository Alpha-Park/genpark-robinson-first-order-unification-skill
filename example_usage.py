from client import FirstOrderUnifier

def main():
    print("=== Testing Robinson First-Order Unification ===")
    unifier = FirstOrderUnifier()
    
    # f(?X, b) = f(a, ?Y)
    t1 = ('f', '?X', 'b')
    t2 = ('f', 'a', '?Y')
    mgu = unifier.unify(t1, t2)
    print(f"Term 1: {t1}")
    print(f"Term 2: {t2}")
    print(f"Most General Unifier: {mgu}")
    assert mgu == {'?X': 'a', '?Y': 'b'}

    # Occurs-check cycle: ?X = f(?X)
    cycle = unifier.unify('?X', ('f', '?X'))
    print(f"Occurs Check Cycle Result: {cycle}")
    assert cycle is None
    print("=== Unification Verification Complete ===")

if __name__ == "__main__":
    main()
