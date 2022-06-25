from datetime import datetime
from appdir import db


class SensorData(db.Model):
    NodeID = db.Column(db.String(100), nullable=True)
    tpluviometer1 = db.Column(db.String(100), nullable=True)
    tpluviometer2 = db.Column(db.String(100), nullable=True)
    tpluviometer3 = db.Column(db.String(100), nullable=True)
    tanemometer = db.Column(db.String(100), nullable=True)
    twd = db.Column(db.String(100), nullable=True)
    tSoil_moist = db.Column(db.String(100), nullable=True)
    ttemp = db.Column(db.String(100), nullable=True)
    thumd = db.Column(db.String(100), nullable=True)
    tpres = db.Column(db.String(100), nullable=True)
    tLuminosity = db.Column(db.String(100), nullable=True)
    tbat = db.Column(db.Float(precision=6), nullable=True)
    ttime = db.Column(db.String(100), primary_key=True, nullable=False, unique=True)

    def __repr__(self):
        return f"{self.NodeID} {self.tpluviometer1} {self.tpluviometer2} {self.tpluviometer3} {self.tanemometer} {self.twd} {self.tSoil_moist} {self.ttemp} {self.thumd} {self.tpres} {self.tLuminosity} {self.tbat} {self.ttime}"