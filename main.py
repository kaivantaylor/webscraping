from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# We can directly try to fetch html code, however this does not address any cases
# where error might occur
# html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")

# Instead we can do a try-catch statement
try:
    html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
except HTTPError as e:
    # return null, break, or do some other "Plan B"
    print(e)
else:
    # program continues. Note: If you return or break in the
    # exception catch, you do not need to use the "else statement"

    bsObj = BeautifulSoup(html.read(), features="html.parser")
    print(bsObj.h1)

# Another way to do things
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
# If an HTTP error code is returned, the program prints the error
# and does not execute the rest of the program under the else statement
if html is None:
    print("URL is not found")

# We also need to know that when we try to call a tag, it may not be there
# meaning we will get an AttributeError thrown when we access a tag on a 
# None object.

# html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
# bsjObj = BeautifulSoup(html)
# print(bsjObj.nonExistentTag)
# # Prints out a None
# print(bsjObj.nonExistentTag.h1)
# # Throws an attribute error

# We can guard against this situation by using a try-catch statement to
# catch any inputs that would cause an attribute error to be thrown

# try:
#     bsObj.nonExistingTag.anotherTag
# except AttributeError as e:
#     print("Tag not found 1")
# else:
#     if(bsObj.nonExistingTag) == None:
#         print("Tag not found")
#     else:
#         print(bsObj.nonExistingTag)

