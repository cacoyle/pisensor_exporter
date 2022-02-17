# pisensor_exporter

Python daemon to export sensor (temperature, for now) for consumption by prometheus

### Setup
```bash
git clone https://github.com/cacoyle/pisensor_exporter.git
cd pisensor_exporter
python3 -m venv env  # Optional
. env/bin/activate   # Optional
pip install -r requirements.txt
cp sensor_config.py.dist sensor_config.py
# Add your sensors 
cp pisensor_exporter.service /etc/systemd/system
systemctl daemon-reload
systemctl start pisensor-exporter
```

### Testing
```
curl -s localhost:8888 | egrep -v '^#'
 .... 
temp_sensor{name="fridge_center",type="22"} 36.32
humidity_sensor{name="fridge_center",type="22"} 27.0
```
