## Finds the position of the first occurrence of a substring.
#  @param string a string
#  @param sub the substring to search for
#  @return the first position of sub in string, or -1 if it doesn't occur
#
'''
Suppose we want to find the position of the first occurrence of a substring in a potentially 
very long string. For example, we may want to find the first occurrence of the string 
"Cheshire cat" within the text of “Alice in Wonderland.” Let’s solve the problem with recursion.

Instructions:
1. Define a main() function
2. Rearrange the code to solve Interactive Problem 3 on page 524.
3. Write an input() with prompt ("Enter a phrase: ")
4. Write an input() with prompt ("Enter a substring: ")
5. Test the syntax using the following phrase and substring:
    phrase: All the world's a stage, and all the men and women merely players; They have their exits
    sub: and women
6. Print the result.
'''

def main():
    phrase = input('Enter a phrase: ')
    sub = input("Enter a substring: ")
    
    result = indexOf(phrase, sub)
    print("Result: ", result)

def indexOf(string, sub):
    # Case 1: Found match at the start
    if string.startswith(sub):
        return 0
    
    # Case 2: String is too short to contain the substring (Not found)
    elif len(sub) > len(string):
        return -1
    
    else:
        # Recursive Step: Try finding it in the rest of the string (string[1:])
        pos = indexOf(string[1:], sub)
        
        # Bubbling up: Check result from the recursive call
        if pos == -1:
            return -1
        else:
            # If found later, add 1 to account for the character we skipped
            return pos + 1

main()