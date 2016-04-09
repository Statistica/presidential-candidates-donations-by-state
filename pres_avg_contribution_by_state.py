# Written by Jonathan Saewitz, released April 8th, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)

import csv, us
from collections import Counter

sanders_counter=Counter()
clinton_counter=Counter()
trump_counter=Counter()
cruz_counter=Counter()
kasich_counter=Counter()

with open('contributions_by_state.csv', 'r') as f:
	reader=csv.reader(f)
	reader.next() #skip the header row
	#row[0] is the state
	#row[1] is sanders' total contributions from that state
	#row[2] is clinton's...
	#row[3] is trump's...
	#row[4] is cruz's...
	#row[5] is kasich's...
	for row in reader:
		state=row[0]
		sanders_counter[state]+=float(row[1])
		clinton_counter[state]+=float(row[2])
		trump_counter[state]+=float(row[3])
		cruz_counter[state]+=float(row[4])
		kasich_counter[state]+=float(row[5])

populations={}
with open('state_populations.csv', 'r') as f: #data from: https://www.census.gov/popest/data/state/totals/2015/tables/NST-EST2015-01.csv
	reader=csv.reader(f)
	for i in range(9):#skip the header rows
		reader.next()
	for i in range(51): #loop through the 51 states + DC
		row=reader.next()
		state=row[0].replace(".", "") #row[0] is the state, and make ".Alabama"->"Alabama"
		state_abbrev=us.states.lookup(unicode(state)).abbr
		population=int(row[8].replace(",", "")) #row[8] is the state's population
		populations[state_abbrev]=population

f=open('avg_contribution_by_state.csv', 'w')
w=csv.writer(f)
w.writerow(["state", "sanders_avg", "clinton_avg", "trump_avg", "cruz_avg", "kasich_avg"]) #write header row
for key in sorted(sanders_counter.iteritems()): #loop through every state and add the
												#candidates' donations, rounded to 2
												#decimal points, to the .csv
	state=key[0]
	state_pop=populations[state]
	sanders_amt=sanders_counter[state]/state_pop
	clinton_amt=clinton_counter[state]/state_pop
	trump_amt=trump_counter[state]/state_pop
	cruz_amt=cruz_counter[state]/state_pop
	kasich_amt=kasich_counter[state]/state_pop
	w.writerow([state, sanders_amt, clinton_amt, trump_amt, cruz_amt, kasich_amt])

f.close()
