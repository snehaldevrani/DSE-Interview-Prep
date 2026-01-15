s= "abcdefghijklmnopqrstuvwqyz"

def reversee(s):
    return s[::-1]

def check_palindrome(s):
    a=s.lower().replace(" ","")
    return a==a[::-1]

def count_vowels(s):
    vowels ="aeiouAEIOU"
    # return sum(1 for char in s if char in vowels)

    cnt=0
    for i in s:
        if i in s:
            cnt+=1
    return cnt

print (reversee(s))
print (check_palindrome(s))
print (count_vowels(s))

# # ===== DAY 1: STRING PARSING =====



# def reverse_string(s):
#     # Task 1: Reverse the string
#     # Hint: s[::-1] OR loop from end
#     return s[::-1]  # ← WRITE THIS LINE

# def is_palindrome(s):
#     # Task 2: Check if palindrome (ignore case)
#     # Steps:
#     # 1. Convert to lowercase
#     # 2. Compare s == s[::-1]
#     s = s.lower()          # ← ADD THIS
#     return s == s[::-1]    # ← ADD THIS

# def tiny_lingomath(expression):
#     # Task 3: Simple LingoMath (already written for you)
#     word_to_digit = {"one": "1", "zero": "0"}
    
#     expr = expression.replace("plus", " plus ")
#     tokens = expr.split()
    
#     numbers = []
#     for token in tokens:
#         if token in word_to_digit:
#             numbers.append(word_to_digit[token])
#         else:
#             numbers.append(token)
    
#     expr_str = "".join(numbers)
#     try:
#         result = eval(expr_str)
#         return f"{result:.2f}"
#     except:
#         return "Error"

# # ===== TESTS =====
# if __name__ == "__main__":
#     print("1. Reverse:", reverse_string("hello"))           # olleh
#     print("2. Palindrome:", is_palindrome("Racecar"))       # True
#     print("3. LingoMath:", tiny_lingomath("oneplusone"))    # 2.00
#     print("4. LingoMath:", tiny_lingomath("onepluszero"))   # 1.00
