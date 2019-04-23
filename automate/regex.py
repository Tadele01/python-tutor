import re
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')#putting r in the parenthesis makes the escape chr as raw string
user_input = input("Enter your string : ")
phone_found = phone_num_regex.search(user_input)
if phone_found == None:
    print("sorry there is no phone number inserted")
else:
    print("The phone number found is : ", phone_found.group())

#matching multiple groups with the pipe

hero = re.compile(r'Batman|Tina Fey') #| is called pipe use for to match one of many expression(is like or statement)
mo1 = hero.search('Batman and Tina Fey')
print(mo1.group())

mo2 = hero.search('Tina Fey and Batman')
print(mo2.group())


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

#optional matching with the ? 

batRegex = re.compile(r'Bat(wo)?man')
'''? implies Match zero or one of the group preceding
this question mark'''
mo1 = batRegex.search('The Adventure of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventure of Batwoman')
print(mo2.group())

#matching zero or more with the star

batRegx = re.compile(r'Bat(wo)*man')
mo1 = batRegx.search('The Adventures of the Batwoman')
print(mo1.group())
mo2 = batRegx.search('The Adventure of Batwowowowowoman')
print(mo2.group())

#matching one or more with the plus

batRegx = re.compile(r'Bat(wo)+man')
mo1 = batRegx.search('The Adventure of Batwoman')
print(mo1.group())
mo2 = batRegx.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegx.search('The Adventure of Batman')
print(mo3 == None)

#matching specific repetitions with curly brackets
haRegx = re.compile(r'(Ha){3}')
mo1 = haRegx.search('HaHaHa')
print(mo1.group())
'''if we want to specifiy the boundaries of the repetitions we can use like 
{a,b} a->initial and b is final 
{,b} -> from 0 to b 
{a,} -> from a to infinity
{a} -> exactly match the a times repetitions of a phrase 
'''
mo2 = haRegx.search('Ha')
print(mo2==None)

#Greedy and Nongreedy matching

greedyRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyRegx = re.compile(r'(Ha){3,5}?')#the quesion mark makes it nongreedy regular expression objex
mo2 = nongreedyRegx.search('HaHaHaHaHa')
print(mo2.group())
'''By default python regular expression is greedy which means that
in ambiguous situations the will match the longest string possible'''

'''The non greedy version match the shortest string possible'''

#findall method

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

'''findall() will return a list of strings as long as there are no groups
in the regular expression each string in the list is a piece of the searched
text that matched the regular expression'''

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
no_group = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(no_group)

'''if there are groups in the regular expression then findall() will return 
a list of tuples each represent a found match and its items are the matched
strings for each group in the regx'''

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
has_group = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(has_group)

#character classes
''' 
\d -> any numeric digit 0-9
\D -> any character that is not a numeric digit from 0-9
\w -> any letter, numeric digit or underscore
\W -> any character that is not a letter, numeric digit or underscore
\s -> any space tab, or newline
\S -> any character that is not a space tab, or newline
'''
xmasRegex = re.compile(r'\d+\s\w+')
xmas = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(xmas)

#making your own character classes

'''
 you can define your own character class using square brackets
 You can also include ranges of letters or numbers by using a hyphen
 inside the square brackets, the normal regular expression
symbols are not interpreted as such.
 By placing a caret character ^ just after the character class\'s opening
bracket  you can make a negative character class.
 a negative character class. A negative character class
will match all the characters that are not in the character class.  
 
'''

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowel = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(vowel)

consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonant = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(consonant)

#the caret and dollar sign characters
'''
when we use ^ at the start of a regex to indicate that  a match must occur at the beginning
when we use $ at the end f a regex to indicate that  a match must occur at the end
'''

beginsWithHello = re.compile(r'^Hello')
begin = beginsWithHello.search('Hello world!')
print(begin)
print(beginsWithHello.search('He said hello.') == None)
endsWithNumber = re.compile(r'\d$')
end = endsWithNumber.search('Your number is 42')
print(end)
print(endsWithNumber.search('Your number is forty two.') == None)
wholeStringIsNum = re.compile(r'^\d+$') #matches strings that both begin and end with one or more numeric characters
whole = wholeStringIsNum.search('1234567890')
print(whole)
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12 34567890') == None)

#the wildcard character

'''
.(dot)  will match any character except for a newline
the dot character will match just one character
'''
atRegex = re.compile(r'.at')
at = atRegex.findall('The cat in the hat sat on the flat mat.')
print(at)

#matching everything with dot-star

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Tadele Last Name: Yednkachw')
print(mo.group(1))
print(mo.group(2))

#The dot-star uses greedy mode

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

#matching newlines with the dot character

'''
By passing re.DOTALL asthe second argument to re.compile(), 
you can make the dot character match
all characters, including the newline character.
'''

noNewlineRegex = re.compile('.*')
no = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(no)
newlineRegex = re.compile('.*', re.DOTALL)
new = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(new)

#case-insensitive matching

'''
to make your regex case-insensitive,
you can pass re.IGNORECASE or re.I as a second argument to re.compile().
'''

robocop = re.compile(r'robocop', re.I)
robo = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(robo)

#substituting strings with the sub() method

'''
The sub() method for Regex objects is passed two arguments.
The first argument is a string to replace any matches.
The second is the string for the regular expression.
The sub() method returns a string with the substitutions applied.
'''

namesRegex = re.compile(r'Agent \w+')
replace = namesRegex.sub('TADE', 'Agent Alice gave the secret documents to Agent Bob.')
print(replace)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agent_censord = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that AgentEve knew Agent Bob was a double agent.')
print(agent_censord)

#managing complex regexes
'''
by passing re.VERBOSE as the second argument to re.compile().
re.compile() function->
    ignore whitespace and comments inside the regular expression string
'''

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
#we can make it simple by using verbose mode

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
\d{3} # first 3 digits
(\s|-|\.) # separator
\d{4} # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

#combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
'''
the re.compile() function takes only a single value as its second argument.
to fix the above limitation ->
use the pipe character (|) on them
'''

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)