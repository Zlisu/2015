ins="""
INSERT INTO candidates (id, first_name, last_name, middle_name, party) \
    VALUES (?,?,?,?,?);
"""

slines = []
with open("candidates.txt") as fd:
    for l in fd.readlines():
        slines.append(l.strip().split('|'))
    
    for line in slines[1:]:
        theid, first_name, last_name, middle_name, party = line
        valstoinsert = (int(theid), first_name, last_name, middle_name, party)
        print(ins, valstoinsert)
