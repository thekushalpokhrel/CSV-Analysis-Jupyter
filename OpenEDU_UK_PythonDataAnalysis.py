#You are asked to write Python code to assign these populations to  variables and print out the sum of the #populations in thousands. Don't try to round your answers.

#You could use variable names e.g. sAfricaPop, mozambiquePop etc but the names aren't important as you won't #using them later.

#Hint 1: Python needs a print statement to print out answers, unlike in your notebooks where you just put in the #name of the variable.

#e.g.

#pop = 5000

#print(pop)        #prints out 500

#Hint 2: The data isn't in thousands, unlike that downloaded from the WHO site. Remember the order of precedence #rules of BIDMAS when you are deciding if brackets will be necessary in your Python code. BIDMAS rules say that #any expression within Brackets should be calculated first, then any Indices (often called powers), followed by #Divisions and Multiplications and finally Additions and Subtractions.


#Population by country
#Country	Population
#South Africa	52 776 000
#Mozambique	25 834 000
#Angola	       21 472
#Equatorial Guinea	     757 000
#Guinea-Bissau	  1 704 000

#Answer

sa = 52776000.00
mo = 25834000.00
an = 21472.00
eg = 757000.00
gb = 1704000.00

print((sa+mo+an+eg+gb)/1000)



#ou have been given a partially completed Python function called rangeOfDeaths to calculate the range of the deaths which should return the range of deaths in 5 African countries.

#These deaths in each country have already been assigned for you to variables: deathsInSA, deathsInM, deathsInA, deathsInEG and deathsInGB.

#Add the additional lines of code necessary for result to hold the difference between the largest and smallest number of deaths. This should be a positive number.

#You should make use of the Python functions you have learned about this week in your code.

#Hint 1: You will need to make use of local variables in this function.

#Hint 2: Make sure your code is all indented correctly or it will not run.

def rangeOfDeaths():
    deathsInSA = 25000
    deathsInM = 18000
    deathsInA = 6900
    deathsInEG = 67
    deathsInGB = 1200

    return result

def rangeOfDeaths():
    deathsInSA = 25000
    deathsInM = 18000
    deathsInA = 6900
    deathsInEG = 67
    deathsInGB = 1200
    largest = max(deathsInSA, deathsInM, deathsInA, deathsInEG, deathsInGB)
    smallest = min(deathsInSA, deathsInM, deathsInA, deathsInEG, deathsInGB)
    result = (largest - smallest)
    return result
