# importing nse from nse tools
from nsetools import Nse

# creating a Nse object
nse = Nse()

# getting quote of the sbin
quote = nse.get_quote('sbin')

# printing company name
print(quote['companyName'])

# printing average price
print("Average Price : " + str(quote['averagePrice']))


# nse tools is not working becuase it is not updated from last long time.
