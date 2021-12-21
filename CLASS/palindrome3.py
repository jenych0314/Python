class Palindrome3: # 회문 예)"기러기"

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
        return self.re(self.string)
    
    def re(self, string):
        if len(string) == 0 or len(string) == 1:
            return True
        return string[0] == string[-1] and self.re(string[1:-1])
    
    def ignoreSpaces(self):
        string = ''.join(self.string.split())
        return self.re(string)

if __name__ == '__main__':
    p1 = Palindrome3('abcd')
    print(p1.normal())
    print(p1.recursive())
    print(p1.ignoreSpaces())
    p2 = Palindrome3('bab')
    print(p2.normal())
    print(p2.recursive())
    print(p2.ignoreSpaces())
    p3 = Palindrome3('ab a')
    print(p3.normal())
    print(p3.recursive())
    print(p3.ignoreSpaces())