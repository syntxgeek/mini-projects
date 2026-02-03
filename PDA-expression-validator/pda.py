
import re
import os
import sys

# Function to validate the middle arithmetic expression part
def validate_expression_535(expr):
    expr_body = re.sub(r'^a+', '', expr)
    expr_body = re.sub(r'a+$', '', expr_body)

    if not expr_body:
        return False

    valid_chars = set('0123456789+-*/().a')

    if not all(c in valid_chars for c in expr):
        return False

    if expr_body[0] in '+*/' or expr_body[-1] in '+-*/':
        return False

    stack = []
    for ch in expr_body:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()
    if stack:
        return False

    if re.search(r'\(\s*\)', expr_body):
        return False
    if re.search(r'[+\-*/]\.[+\-*/]', expr_body):
        return False
    if re.search(r'\.\d*\.', expr_body):
        return False
    if re.search(r'\)[\d\.]', expr_body):
        return False

    lex_pattern = re.compile(r'^(?:\d+\.\d*|\.\d+|\d+|\(|\)|[+\-*/])+$')
    if not lex_pattern.match(expr_body):
        return False

    return True


# Class to simulate the PDA
class ExprPDA_nc535:
    def __init__(self):
        self.stack_memory = []
        self.current_state = 'q'
        self.final_state = 'q_accept'

    def initialize_535(self):
        self.stack_memory = ['ϵ']
        self.current_state = 'q'

        print("\n--- PDA Initialization ---")
        print(f"Current PDA State → {self.current_state}")
        print("Input symbol → ε")
        print("Top of Stack → ϵ")
        print("Popped from Stack → ϵ")
        print("Pushed onto Stack → z0")
        print("Moves to State → q0\n")

        self.stack_memory.pop()
        self.stack_memory.append('z0')
        self.current_state = 'q0'

    def run_pda_535(self, input_str):
        print(f"\n--- Now processing: \"{input_str}\" ---")
        self.initialize_535()

        i = 0
        n = len(input_str)
        k_count = 0

        if i < n and input_str[i] == 'a':
            top = self.stack_memory[-1] if self.stack_memory else 'ϵ'
            print_transition(self.current_state, input_str[i], top, 'ϵ', 'a', 'q1')
            self.stack_memory.append('a')
            self.current_state = 'q1'
            i += 1
        else:
            return False, "String must start with 'a'."

        while i < n and input_str[i] == 'b':
            top = self.stack_memory[-1] if self.stack_memory else 'ϵ'
            print_transition(self.current_state, input_str[i], top, 'ε', 'b', 'q1')
            self.stack_memory.append('b')
            k_count += 1
            i += 1

        if i < n and input_str[i] == 'a':
            top = self.stack_memory[-1] if self.stack_memory else 'ϵ'
            print_transition('q1', input_str[i], top, 'ε', 'a', 'q2')
            self.stack_memory.append('a')
            self.current_state = 'q2'
            i += 1
        else:
            return False, "Second 'a' missing after b's."

        expr = ''
        while i < n and input_str[i] != 'a':
            symbol = input_str[i]
            expr += symbol
            top = self.stack_memory[-1] if self.stack_memory else 'ϵ'

            print(f"\nCurrent PDA State → {self.current_state}")
            print(f"Input symbol → {symbol}")
            print(f"Top of Stack → {top}")

            if symbol == '(':
                print("Pushed onto Stack → (")
                self.stack_memory.append('(')
            elif symbol == ')':
                if self.stack_memory and self.stack_memory[-1] == '(':
                    print("Popped from Stack → (")
                    self.stack_memory.pop()
                else:
                    return False, f"Unmatched ')' at position {i}"
            else:
                print("No push or pop for this symbol.")

            i += 1

        if not validate_expression_535(expr):
            return False, f"Invalid middle expression: {expr}"

        if i < n and input_str[i] == 'a':
            top = self.stack_memory[-1] if self.stack_memory else 'ϵ'
            print_transition(self.current_state, input_str[i], top, 'ε', 'none', 'q3')
            self.stack_memory.append('a')
            self.current_state = 'q3'
            i += 1
        else:
            return False, "Missing 'a' after expression."

        remaining_b = 0
        while i < n and input_str[i] == 'b':
            top = self.stack_memory[-1] if self.stack_memory else 'ϵ'
            print_transition(self.current_state, input_str[i], top, 'ε', 'none', 'q3')
            self.stack_memory.append('b')
            remaining_b += 1
            i += 1

        if remaining_b != k_count:
            return False, f"Mismatch in b counts: expected {k_count}, got {remaining_b}"

        if i < n and input_str[i] == 'a':
            top = self.stack_memory[-1] if self.stack_memory else 'ϵ'
            print_transition(self.current_state, input_str[i], top, 'ε', 'none', 'q_accept')
            self.stack_memory.append('a')
            self.current_state = self.final_state
            i += 1
        else:
            return False, "Final 'a' missing at the end."

        if i != len(input_str):
            return False, "Extra input symbols found."

        print(f"\nFinal PDA State Reached → {self.current_state}")
        return True, ""


def print_transition(curr, symbol, top, popped, pushed, next_state):
    print(f"\nCurrent PDA State → {curr}")
    print(f"Input symbol → {symbol}")
    print(f"Top of Stack → {top}")
    print(f"Popped from Stack → {popped}")
    print(f"Pushed onto Stack → {pushed}")
    print(f"Moves to State → {next_state}")


def main_driver_535():
    # Redirect output to file
    sys.stdout = open('program_output.txt', 'w')

    print("\n==== Project 2 for CS 341 ====")
    print("Section number: 002")
    print("Semester: SPRING 2025")
    print("Written by: Nathaly Kos, nc535")
    print("Instructor: Arashdeep Kaur, ak3257@njit.edu\n")

    pda = ExprPDA_nc535()
    test_cases = []

    if os.path.exists('test_inputs.txt'):
        with open('test_inputs.txt', 'r') as file:
            test_cases = [line.strip() for line in file.readlines()]
        n = len(test_cases)
        print(f"Loaded {n} test cases from 'test_inputs.txt'.\n")
    else:
        n = int(input("Enter number of strings to process (n ≥ 0): "))
        print(f"\nReceived: {n} strings to process.\n")

        for i in range(1, n + 1):
            user_input = input(f"Enter string {i} of {n}: ")
            test_cases.append(user_input)

    if n == 0:
        print("Program terminates now.")
        return

    for idx, input_str in enumerate(test_cases, start=1):
        print(f"\nProcessing string {idx} of {n}:")
        accepted, reason = pda.run_pda_535(input_str)

        if accepted:
            print(f'\nInput w = "{input_str}" is ACCEPTED.\n')
        else:
            print(f'\nInput w = "{input_str}" is REJECTED because:\n{reason}\n')

    sys.stdout.close()


if __name__ == "__main__":
    main_driver_535()