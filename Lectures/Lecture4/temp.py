def make_query(sel):
    c = db.cursor().execute(sel)
    return c.fetchall()

make_query("SELECT * from candidates;")