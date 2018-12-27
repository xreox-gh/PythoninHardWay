"""ex12: Prompt users"""
print "*" * 6,
print "\\Prompt users\\",
print "*" * 6

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So, you'ar %r old, %r tall and %r heavy." %(age, height, weight)




"""ex11: Question
print "*" * 6,
print "\\Question\\",
print "*" * 6

print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weight?"
weight = raw_input()

print 'So you are %r old, %r tall and %r heavy.' %(age, height, weight)
"""


"""ex10: What's that?
print "*" * 6,
print "ex10: What's that?",
print "*" * 6

# escape sequences
# using \ back-slash and \\ double back-slash

print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

# tripple-quotes
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
#I'll do a list:
#\t* Cat food
#\t* Fishes
#\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

"""

"""ex9: Print, Print and Print
print "*" * 6,
print "ex9: Print, Print and Print",
print "*" * 6

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days # add a comma, things are different.
print "Here are the months: ", months

print """
# There's something going on here.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.
"""

print "days: %s" % days
print "months: %s" % months

Weeks = 52

print "there are ", Weeks, "weeks in one year." # this is to print string, int and string continuously
print "there are %d" % Weeks, "weeks in one year." # this is to print int into string first, then print second string
print Weeks
"""

"""ex8: Print and Print

# Re-write title with loop
print "*" * 6,
print "ex8: Print and Print",
print "*"*6

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",  # since there is a ', output will show "
    "So I said goodnight."
)

test_quote = "Is there a quote"

s = "%r" %("Is there a quote?") # %r will print out all the things including quote
ss = "%s" %(test_quote)  # %s will print the string only
print s
print ss
"""



"""ex7: More print
print "*****ex7: More print*****"

print "Mary had a little lamb." # print a string
print "Its fleece was white as %s." %'snow'  # need '' to print a string
print "And everywhere that Mary went."
print "." * 10 # print . recursively

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,  # comma plays as a space and link two strings into one sentence
print end7 + end8 + end9 + end10 + end11 + end12

a = 'ss'
b = 'kk'
c = "tt",  # what's this??
d = 'i am ok'

print a,
print b
print c
print d

"""

"""ex6: String and text
print "*****ex6: String and text*****"

x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)  # string in string

print x
print y

print "I said: %r." %x # string in string
print "I also said: '%s'." %y  # string in string

hilarious = False

joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious  # not string in string

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
"""

"""ex5: More variable and print

print "*****ex5: More variable and print.*****"

my_name = "Zed A. Shaw"
my_age = 35 #not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = "Blue"
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." %my_name
print "He's %d inches tall." %my_height
print "He's %d pounds heavy." %my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age+my_height+my_weight)

# try more standard output format
# %[(name)][flags][width].[precision]typecode
tst_float0 = 3.141592654
tst_float1 = -5.36

print "output some floats: %+8.3f, %8.3f." %(tst_float0, tst_float1)
s1 = "i am %s, i am %d years old" %('jeck', 26)
# s2 = "i am %(name)s, i am %(age)d years old, i am %(heiht).2f." %('name':'jeck', 'age':48, 'height':1.715)
s2 = "i am %(name)+10s, i am %(age)d years old, i am %(height).2f" % {'name':'jeck','age':26,'height':1.7512}
# for dict/key, it has to use {}, NOT ()!!!
s3 = "Original value: %d, Science e format: %.3e, Science E format: %.4E" %(1000000, 1000000, 1000000)
s4 = "Try r output: Int %r, Str %r." %(22,'tst_string2')

print(s1)
print(s2)
print(s3)
print(s4)

# format
f1 = "i am {0}, i am {1} years old.".format('Jeck',26)
f2 = "i am {name}, i am {age} years old".format(**{'name':'jeck','age':26}) # pls note: ** for key
f3 = "--{name:*^10s}--   =={age:<10.2f}==".format(name='jeckonly', age=27) # as name and age inside of {}, they are keys
f4 = "Original value:{:d} binary:{:#b}, oct:{:#o}, hex:{:#X}".format(15,15,15,15)
f5 = "Original value:{:2F}, % value:{:.2%}, auto split:{:,}.".format(0.75, 0.7584, 1000000)


print(f1)
print(f2)
print(f3)
print(f4)
print(f5)

"""

"""ex4: Variable

print "*****ex4: Variable.*****"
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars availbale."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We need to put about", average_passengers_per_car, "in each car."
"""


"""ex3: Math.

print "*****ex3: Math.*****"

print "I will not count my chickens:"
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
print "Now I will count the eggs:"
print 3+2+1-5+4%2-1/4+6

print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3+2
print "What is 5 - 7?", 5-7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print "using float."
print "Now I will count the eggs:"
print 3.0+2.0+1.0-5.0+4.0%2.0-1.0/4.0+6.0
print "But the result is weird!!!"

"""

"""ex2: Comment and #

print "*****ex2: Comment and #.*****"
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print "*****ex2: Comment and #.*****"
print "I could have code like this." # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:

# print "This wont run."
"""

"""ex1: print.

print "*****ex1: print.*****"
print "Hello World!"
#print "Hello Again."
#print "I like typing this."
#print "This is fun."
print "Yay! Printing."
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'
print "This line is added by myself."
print 'This line is to test "single quote".'

"""