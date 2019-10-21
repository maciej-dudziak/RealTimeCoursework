# RealTimeCoursework
## 1. Instructions
You will need to work somewhat with one other pair,as you will need access to four development boards. 

The intent is to create a simple meshnetwork for your internet of things (IoT):

    1.One of the four boards should interface to a host computer via serial RS232 emulated over USB. A simple web server program running on the host should issue commands over the serialinterface to turn the lights ofall three boards on or off. A standard web browser should be able to connect to this server; the server will present a page with “on” and “off” buttons for the lights.The web page should also report lights that are uncontrollable because of communication failure.
    
    2.The other threeboards should be programmed similarly; they receive, if they can, radio messages from the host interface board or the other slave, act on them locally, and relay to the other slavesif necessary.
    
    3.There should bea convincing demonstration of forwarding and of failover; as some of the slave boards go out of range of the master, “mesh” communications should be maintained until failure is eventually reported through the web interface.
