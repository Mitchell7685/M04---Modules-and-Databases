# 11.1 - 11.2
# >>> import zoo
# >>> zoo.hours()
# Open 9-5 daily
# >>> import zoo as menagerie                                                           )
# Open 9-5 dailyhours() 
def hours():
    print("Open 9-5 daily")

# 16.8
from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine("sqlite:///books.db")

metadata = MetaData()
metadata.reflect(bind=engine)

book = metadata.tables['book']

stmt = select(book.c.title).order_by(book.c.title)

with engine.connect() as conn:
    results = conn.execute(stmt)
    for row in results:
        print(row.title)