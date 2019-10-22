from flask import Flask, render_template, request, redirect
import serial

#start app with the name of the script
app = Flask(__name__)
#create a serial port and open it
#ser = serial.Serial('COM3', 9600)

class LED_status():
    slave1 = "Off"
    slave2 = "Off"
    slave3 = "Off"
status = LED_status()

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html", status = status)

#control LED on the slaves
@app.route("/slave/<int:slave_number>/<int:led_action>")
def slave1_led(slave_number,led_action):
    #command structure: { <id> - id of the slave (1, 2 or 3), <operation> - operation on LED (0 - turn off, 1 - turn on) }
    command = "{}.{}".format(slave_number, led_action)
    #send command to master device
    #if ser.is_open():
    #    ser.write(command)
    #    response = ser.read(30)
    #    if response == "1":
    #       
    #else:
    status.slave1 = "On"
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)