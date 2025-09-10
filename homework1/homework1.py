#File: homework1.py
# --- Variables and Data Types ---
a = 10
print(a)
print(type(a))# a is an integer, a whole number
b = 1.5
print(b)
print(type(b))# b is a float, a decimal number
c = 3j
print(c)
print(type(c))# c is complex, a number with a letter which makes it imaginary
d = "hello"
print(d)
print(type(d))# d is a string, a word
e = [1, 2, 3]
print(e)
print(type(e))# e is a list, a changable assortment of values
f = {"name" : "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))# f is a dict, which is information where each data piece has a specific label
g = (1, 2)
print(g)
print(type(g)) # g is a tuple, an unchangable assortment of values
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list
i = True
print(i)
print(type(i)) # i is a boolean, a true or false value
j = None
print(j)
print(type(j)) # j is a NoneType, represents an absense of a value
k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list
l = str(14)
print(l)
print(type(l)) # l is a string, only outputs whats in the parenthases, not the str
m = 1e4
print(m)
print(type(m)) # m is a float, e representing an exponent
# 1. I found 9 different data types
# 2. Float, String, Complex, Boolean, Integer, List, Nonetype, tuple, dict
# 3. List and tuple have the same data types except tuples are unchangable
# 4. The datatype of l was a string, this was because numbers are able to be a string if the command str(#) is before it
n = colors = {"red", "blue"}
print(n)
print(type(n)) # n is a set, an unordered unique collection
print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 doesnt equal 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # true, because its a non empty value
print(bool(123)) # True because its non empty
print(bool(["apple", "cherry", "banana"])) # true because its non empty
print(bool(True)) # True because thats what I told it to output
print(bool(False)) # True because thats what I told it to output
print(bool(0)) # False, it treats 0 as an empty value
print(bool("")) #False because its empty
print(bool(" ")) #True because it treats the space as something
print(bool(())) #False because nothing in the parenthesis
print(bool([])) # False because nothing is in the brackets
print(bool({})) # False because nothing is in the brackets
print(bool(True and False)) # False, I guess picks false
print(bool(True and True)) # When given two true options picks true
print(bool(False and False)) # False, I guess 2 falses create a false
print(bool(True or False)) # True because it chooses true if between true and false
print(bool(True or True)) # True because it was choosing between two trues
print(bool(False or False)) # False becayse it was choosing between two falses 
print(bool(not(False))) # True because its the opposite of false
print(bool(not(True))) # False because its the opposite of 
# 1. If there is something in the parentheses itll pick true if its not a question
# 2. I thought (false and false) would be true
print(bool(23))# true because there is something in the parenthises
print(bool(1>2)) # False because 1<2

print(10+5) # 15 Performs addition
print(10-5) # 5 performs subtraction
print(2*4) # 8 performs multiplication
print(6/3) # 2 performs division
print(5%2) # 1 gives the remainder
print(3 ** 2) # 9 squares it by that number
print(15 // 2) # 7 divides and gives you the nearest whole number(the floor)
print(5==2) # False just tells you if its true or not
print(10 != 10) #False != means not equal to 
print(2<5) # True because 2 is greater than 5
print(12>5) # True because 12 is greater than 5
print(5<=6) # True because 6>=5
print(1>=10) # False because 1 is not >= 10

x = 5 
x += 5
x -= 4
x *= 3

# 1. It checks whether both are true
print(bool((2 < 4) and (3 == 3)))
print(bool((3>1) and (5<2)))
# 2. Or checks if either one is true
print(bool((3 == 3) or (4<2)))
print(bool((3 == 5) or (4>9)))
# 3. Reverses the truth value of whatever you get it
print(bool(not False))
print(bool(not True))

# 1. / is dividing with the decimal and // is dividing to the nearest whole number(floor)
# 2. % gives the remainder and // is dividing to the nearest whole number
# 3. I would use %, for example 5%2 would give 1
# 4. They are shortcuts for updating variables

my_string = "hello"
print(my_string) #prints hello
print(my_string[0]) # prints the first letter
print(my_string[1]) #prints second letter
print(my_string[2]) # prints third letter
print(my_string[3]) # prints 4th letter
print(my_string[4]) # prints 5th letter
print(my_string[-1]) # prints last letter
print(my_string[1:3]) # prints the second and fourth letter
print(my_string[0:5:2]) # Prints the first, fifth, and third letter but in order
print(len(my_string)) # prints the number of letters in the string
print(my_string + "goodbye") # adds the word goodbye to the end of the string
print(my_string * 7) # writes the string 7 times

# 1. Slicing means adding a command to start and stop at certain points, we did this in line 118 and 119
# 2. 
name = "Oski"
print("Hello, my name is", name) # just adds the name to the string
print(f"Hello, my name is {name}") # does the same thing
# 4. f strings are easier to insert variables into sentences

# cd
# Changes directories. Use it to move from one folder to another
# Example cd Cameron

# 2. ls
#  Lists all of the contents of a directory
# ls Cameron

# 3. ls -a
# Lists all of the contents including hidden files
# ls -a Cameron

# 4. mkdir
# makes a new directory
# mikdir folder_name

# 5. cat
# shows the content of the file you chose
# cat Cameron

# 6. pwd
# Tells you what directory youre in
# pwd 

# 7. cd .. 
# goes up one level into the parent directory
# cd ..

# 8. cd .
# keeps you in your same directory
# cd .

# 9. cd ~
# takes you to your home directory
# cd ~

# 10. cp
# copies files from one destination to another
# cp homework1 /Users/cameronearls/python_decal_fa25

# 11. mv
# used to moves files from one location to another, different than cp in that cp makes a copy to another file and mv moves it
# mv homework1 /Users/cameronearls/python_decal_fa25

# 12. rm
# removes files or directories
# rm homework1

# 13. clear
# clears all text from the terminal screen
# clear

# 14. grep
# Searches for terms within files
# grep "search_term" filename

# 15. touch
# Quickly makes a new file without making an editor
# touch file1.txt

# 16. nano
# allows you to create or edit text files directly from the command line
# nano

# 17. history
# Shows all of the commands youve type in previously
# history

# ls lists all flies in that directory and ls -a lists all files plus hidden files
# a hidden file is one not shown by default in your directory
#ls -l shows a long listing format with permisions, owner, size, ect
# cp -i asks before overwriting files
# rm -v shows which files are being deleted


