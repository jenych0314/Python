class Palindrome1: # 회문 예)"기러기"

    def __init__(self, user_input):
        self.string = user_input
    
    def normal(self):
        left = 0
        right = len(self.string) - 1
        is_palindrome = False

        while left < right:
            if self.string[left] != self.string[right]:
                break
            left += 1
            right -= 1
        else:
            is_palindrome = True
            
        return is_palindrome
    
    def recursive(self):
        return self.recursive_string(self.string)
    
    def recursive_string(self, user_input):
        return user_input[0] == user_input[-1] and self.recursive_string(user_input[1:-1])

if __name__ == '__main__':
    p1 = Palindrome1('abcd')
    print(p1.normal())
    p2 = Palindrome1('abcdedcba')
    print(p2.normal())