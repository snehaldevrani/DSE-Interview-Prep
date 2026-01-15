# # LingoMath

# ## Task
# Implement the function `evaluate_word_expression(s)` which calculates a numerical result from an arithmetic word expression. Round the result to 2 decimal places. 


# ### Problem: Evaluate Word-Encoded Arithmetic Expressions
 
# You will receive a single string that encodes an arithmetic expression using **words** instead of symbols.  
# Your task is to **parse** the string and return the **numeric result** of the expression.
 
# #### Tokens you may see
 
# - **Digits (0–9):**  `zero, one, two, three, four, five, six, seven, eight, nine`
 
# - **Operators & parentheses:**  `plus, minus, times, dividedby, leftparenthesis, rightparenthesis`
 
# #### Important details

# - Input is case-insensitive
# - Ignore everything that is not a letter
# - Numbers are single digits (0–9)
# - Use standard arithmetic rules for operator precedence
# - Round the result to 2 decimal places
# - Return None for incorrect expressions
 

# ## Input & Output 

# ### Format
# - Input: str
# - Output: str or None

# ### Examples
 
# 1. `"OnePlusZero"` → `"1.00"`  
# 2. `"leftparenthesistwominusonerightparenthesisTimesThree"` → `(2 - 1) * 3` → `"3.00"`  
# 3. `"seventimestwominusthree"` → `7 * 2 - 3` → `"11.00"`  
# 4. `"eightdividedbythree"` → `8 / 3` → `"2.67"`  
# 5. `"@@@ fourtimes ### six ???"` → `4 * 6` → `"24.00"`

# ## Note
# The task should be solved using only Python standard libraries, without requiring third-party libraries.

s=input()
a=""
for i in s:
    if i.isalpha():
        a+=i.lower()

d= {
    "zero": "0",
    "one": "1",
    "two": "2", 
    "three": "3", 
    "four": "4",
    "five": "5", 
    "six": "6", 
    "seven": "7", 
    "eight": "8", 
    "nine": "9",
    "plus": "+", 
    "minus": "-", 
    "times": "*", 
    "dividedby": "/",
    "leftparenthesis": "(", 
    "rightparenthesis": ")"
}

for k in d:
    if k in a:
        a=a.replace(k,d[k])

final=""

for i in a:
    if i in "0123456789+-()/*":
        final+=i

try:
    ans = eval(final)
    print(f"{ans:.2f}")
except:
    print(None)