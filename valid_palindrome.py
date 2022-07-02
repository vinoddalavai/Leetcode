class ValidPalindrome:

    def is_valid(self, char1: str, char2: str) -> bool:
        return char1.lower() == char2.lower()

    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif not self.is_valid(s[left], s[right]):
                return False
            else:
                left += 1
                right -= 1
        return True


sentence1 = "A man, a plan, a canal: Panama"
print("Is sentence1 a valid Palindrome? : " +
      str(ValidPalindrome().is_palindrome(sentence1)))
