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
