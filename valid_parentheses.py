class ValidParentheses:
    BRACKETS = {
        ']': '[',
        ')': '(',
        '}': '{'
    }

    def is_valid(self, s: str) -> bool:
        stack = []
        for char in s:
            if ((char in self.BRACKETS.keys() and not stack) or
                    (char in self.BRACKETS.keys() and stack and self.BRACKETS[char] != stack.pop())):
                return False
            elif char in self.BRACKETS.values():
                stack.append(char)
        return stack == []


string1, string2, string3 = '}{', '[()]{}', '()]]'
print("Validating parentheses for " + string1 + " : " + str(ValidParentheses().is_valid(string1)))
print("Validating parentheses for " + string2 + " : " + str(ValidParentheses().is_valid(string2)))
print("Validating parentheses for " + string3 + " : " + str(ValidParentheses().is_valid(string3)))
