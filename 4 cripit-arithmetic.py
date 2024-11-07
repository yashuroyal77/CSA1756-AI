import itertools

def solve_cryptarithmetic():
    # Define the letters in the puzzle
    letters = 'SENDMORY'
    # Generate all possible digit assignments (0-9) for the 8 unique letters
    for perm in itertools.permutations(range(10), len(letters)):
        # Map each letter to a digit
        s, e, n, d, m, o, r, y = perm
        
        # Ensure that S and M are non-zero (since they are the leading digits in SEND and MONEY)
        if s == 0 or m == 0:
            continue
        
        # Calculate SEND, MORE, and MONEY as integers based on current permutation
        send = s * 1000 + e * 100 + n * 10 + d
        more = m * 1000 + o * 100 + r * 10 + e
        money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
        
        # Check if SEND + MORE == MONEY
        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            print(f"Solution: S={s}, E={e}, N={n}, D={d}, M={m}, O={o}, R={r}, Y={y}")
            return  # Stop at the first solution

    print("No solution found.")

# Run the function to solve the puzzle
solve_cryptarithmetic()
