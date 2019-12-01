from flask import Flask, render_template, request, redirect
import serial

#start app with the name of the script
app = Flask(__name__)
#create a serial port and open it
#ser = serial.Serial('COM10', 115200)
#use below if Linux
ser = serial.Serial('/dev/ttyACM0', 115200)

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
    if ser.isOpen():
        ser.write(command.encode())
        response = ser.readline()

    if response == "Success":
        if slave_number == 1:
            status.slave1 = "On" if led_action==1 else "Off" 
        elif slave_number == 2:
            status.slave2 = "On" if led_action==1 else "Off"
        elif slave_number == 3:
            status.slave3 = "On" if led_action==1 else "Off"
    else:
        if slave_number == 1:
            status.slave1 = "Error Occured - Uncontrollable"
        elif slave_number == 2:
            status.slave2 = "Error Occured - Uncontrollable"
        elif slave_number == 3:
            status.slave3 = "Error Occured - Uncontrollable"

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)