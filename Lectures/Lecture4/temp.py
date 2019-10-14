def make_query(sel):
    c = db.cursor().execute(sel)
    return c.fetchall()

make_query("SELECT * from candidates;")

def make_frame(list_of_tuples, legend=cont_cols):
    framelist=[]
    for i, cname in enumerate(legend):
        framelist.append((cname, [e[i] for e in list_of_tuples]))
    return pd.DataFrame.from_dict(dict(framelist))


[(28, 'Buckheit', 'Bruce', None, '8904 KAREN DR', None, 'FAIRFAX', 'VA', '220312731', 100, '2007-09-19', 20), 
 (78, 'Ranganath', 'Anoop', None, '2507 Willard Drive', None, 'Charlottesville', 'VA', '22903', -100, '2008-04-21', 32), 
 (89, 'Perreault', 'Louise', None, '503 Brockridge Hunt Drive', None, 'Hampton', 'VA', '23666', -34.08, '2008-04-21', 32), 
 (146, 'ABDELLA', 'THOMAS', 'M.', '4231 MONUMENT WALL WAY #340', None, 'FAIRFAX', 'VA', '220308440', 50, '2007-09-30', 35)
]