from models import Payload
import json
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
import random
import names




engine = create_engine('sqlite:///payload.db', echo=False)

# create a configured "Session" class
Session = sessionmaker(bind=engine)
# create a Session
session = Session()
def make_payload():
    if not Payload.__table__.exists(engine):
        Payload.__table__.create(engine)
        print('{} created'.format(Payload.__tablename__))
    else:
        print('{} exists'.format(Payload.__tablename__))

def  load_payload():
    full = []
    for i  in range(100):
        out = {}
        out['gigya_id'] = random.randrange(100000,120000)
        out['docs'] = []
        for ii in range(random.randrange(2,7)):
            docs = {}
            docs['MRN'] =random.randrange(2000,7000)
            docs['name'] = names.get_full_name()
            out['docs'].append(docs)
        full.append(out)
        row = Payload(out['gigya_id'], json.dumps(out))
        session.add(row)
        session.commit()


if __name__ == "__main__":
    make_payload()
    load_payload()


[ p.payload for p in session.query(Payload).filter(Payload.gigya_id==117792)]


session.query(Payload.payload).filter(Payload.gigya_id==117792).first()[0]

