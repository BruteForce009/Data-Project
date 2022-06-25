from flask import render_template, url_for, flash, redirect, get_flashed_messages, request
from appdir import app, db
import appdir.models
# from appdir.models import User
import time


@app.route('/', methods=['GET','POST'])
@app.route("/data", methods=['GET','POST'])
def data():
    NodeID = request.args.get('NodeID')
    pm1 = request.args.get('tpluviometer1')
    pm2 = request.args.get('tpluviometer2')
    pm3 = request.args.get('tpluviometer3')
    am = request.args.get('tanemometer')
    vane_str = request.args.get('twd')
    sm = request.args.get('tSoil_moist')
    temp = request.args.get('ttemp')
    humd = request.args.get('thumd')
    pres = request.args.get('tpres')
    lum = request.args.get('tLuminosity')
    bat = request.args.get('tbat')
    timex = request.args.get('ttime')
    sensordata = appdir.models.SensorData(NodeID=NodeID, tpluviometer1=pm1, tpluviometer2=pm2, tpluviometer3=pm3, tanemometer=am, twd=vane_str, tSoil_moist=sm, ttemp=temp, thumd=humd, tpres=pres, tLuminosity=lum, tbat=bat, ttime=timex)
    db.session.add(sensordata)
    db.session.commit()
    sensors = appdir.models.SensorData.query.all()
    return render_template('data_.html', sensors=sensors)


@app.route("/data_")
def data_():
    sensors = appdir.models.SensorData.query.all()
    return render_template('data_.html', sensors=sensors)

