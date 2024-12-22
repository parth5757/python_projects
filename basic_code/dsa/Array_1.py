# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expense = [2200, 2350, 2600, 2130, 2190]

Jan = 1
Feb = 2
Mar = 3
Apr = 4
May = 5
quarter = [Jan, Feb, Mar]

# 1. In Feb, how many dollars you spent extra compare to January?

print("Feb extra spent compare to jan:", expense[Feb-1] - expense[Jan-1])

# 2. Find out your total expense in first quarter (first three months) of the year.

print("total expense of fist 3 quarter of year:", sum(expense[i] for i in quarter))

# 3. Find out if you spent exactly 2000 dollars in any month
print("exact expense is 2000:", 2000 not in expense) #not in, in, is

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
Jun = 6
expense.append(1980)
print("Add new month june:", expense[Jun-1])

# 5. Rs.200 get refund in April
refund = 200
print("Rs.200 refund in April:", expense[Apr-1] + refund)