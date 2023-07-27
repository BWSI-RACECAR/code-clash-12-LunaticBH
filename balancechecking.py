"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #12 - Braces Brackets & Bows Balance (balancechecking.py)


Author: Ali Qattan

Difficulty Level: 6/10

Prompt: In your IDEs, your code editors and sometimes Vim (for those 
unfortunate ones who use vim) your application will yell at you when you don’t
have matching closing brackets. Python does not have that problem as much as
other languages like Java and C which rely heavily on curly braces.  You need 
to write a program that allows for that functionality so that every ‘[‘ and ‘{‘ 
and ‘(‘ has a matching ‘]’  ‘}’  ‘)’. 
This problem can be solved quickly using the right data structure.

Test Cases:
Input: {[()]}  Output: True

Input: [()]  Output: True

Input:{[{}]  Output: False

"""
class Solution:
    def isBalanced(self, parenthesis): 
            #type parenthesis: string
            #return type: boolean
            dict = {"(":")", "[":"]", "{":"}"}
            length = len(parenthesis)

            if (length+2) % 2 == 0 and "[" in parenthesis or "{" in parenthesis or "(" in parenthesis:
                for i in range(length):
                    if parenthesis[i] in dict:
                        print(parenthesis[i])
                        for j in range(i,length):
                            if parenthesis[j] == dict[parenthesis[i]]:
                                break
                            elif j == length-1:
                                return False
                            else:
                                pass
                            print(f"found one {i}")
                    else:
                        pass
                return True
            else:
                return False

def main():
    str1=input()
    tc1= Solution()
    ans=tc1.isBalanced(str1)
    print(ans)

if __name__ == "__main__":
    main()
