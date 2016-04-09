# Written by Jonathan Saewitz, released April 8th, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)

import csv
from collections import Counter

#initialize variables
sanders_counter=Counter()
clinton_counter=Counter()
trump_counter=Counter()
cruz_counter=Counter()
kasich_counter=Counter()

state_abbrevations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"] #thank you, https://gist.github.com/JeffPaine/3083347

#fill each candidate's counter
#data from: http://www.fec.gov/disclosurep/pnational.do
with open('sanders.csv', 'r') as f:
	reader=csv.reader(f)
	reader.next()
	for row in reader:
		if row[5] in state_abbrevations:
			sanders_counter[row[5]]+=float(row[9])
			#row[5] is the state
			#row[9] is the amount given

with open('clinton.csv', 'r') as f:
	reader=csv.reader(f)
	reader.next()
	for row in reader:
		if row[5] in state_abbrevations:
			clinton_counter[row[5]]+=float(row[9])

with open('trump.csv', 'r') as f:
	reader=csv.reader(f)
	reader.next()
	for row in reader:
		if row[5] in state_abbrevations:
			trump_counter[row[5]]+=float(row[9])

with open('cruz.csv', 'r') as f:
	reader=csv.reader(f)
	reader.next() #skip the header row
	for row in reader:
		if row[5] in state_abbrevations:
			cruz_counter[row[5]]+=float(row[9])

with open('kasich.csv', 'r') as f:
	reader=csv.reader(f)
	reader.next()
	for row in reader:
		if row[5] in state_abbrevations:
			kasich_counter[row[5]]+=float(row[9])

for abbrev in state_abbrevations:
	#this ensures that no candidate is missing a state
	#if they are missing a state, assume they were given $0
	#from people in that state
	if not abbrev in sanders_counter.keys():
		sanders_counter[abbrev]=0
	if not abbrev in clinton_counter.keys():
		clinton_counter[abbrev]=0
	if not abbrev in trump_counter.keys():
		trump_counter[abbrev]=0
	if not abbrev in cruz_counter.keys():
		cruz_counter[abbrev]=0
	if not abbrev in kasich_counter.keys():
		kasich_counter[abbrev]=0

f=open('contributions_by_state.csv', 'w')
w=csv.writer(f)
w.writerow(["state", "sanders", "clinton", "trump", "cruz", "kasich"]) #write header row
for key in sorted(sanders_counter.iteritems()): #loop through every state and add the
												#candidates' donations, rounded to 2
												#decimal points, to the .csv
	state=key[0]
	sanders_amt=round(sanders_counter[state], 2)
	clinton_amt=round(clinton_counter[state], 2)
	trump_amt=round(trump_counter[state], 2)
	cruz_amt=round(cruz_counter[state], 2)
	kasich_amt=round(kasich_counter[state], 2)
	w.writerow([state, sanders_amt, clinton_amt, trump_amt, cruz_amt, kasich_amt])

f.close()
