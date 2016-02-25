//#include <Tone.h>
//#include <SoftwareSerial.h>
int inputPin = 2;               // choose the input pin (for PIR sensor)
int pirState = LOW;             // we start, assuming no motion detected
int val = 0;                    // variable for reading the pin status
byte inbyte;                    // Byte recieved from the PI
void myTone(byte pin, uint16_t frequency, uint16_t duration)
{ // input parameters: Arduino pin number, frequency in Hz, duration in milliseconds
    unsigned long startTime=millis();
    unsigned long halfPeriod= 1000000L/frequency/2;
    pinMode(pin,OUTPUT);
    while (millis()-startTime< duration)
    {
        digitalWrite(pin,HIGH);
        delayMicroseconds(halfPeriod);
        digitalWrite(pin,LOW);
        delayMicroseconds(halfPeriod);

    }
    pinMode(pin,INPUT);
}

void setup() {
    pinMode(inputPin, INPUT);     // declare sensor as input
    Serial.begin(9600);

}

void loop(){

    val = digitalRead(2);               // read input value of IR sensor at pin two
    if (val == HIGH) {                  // check if the input is HIGH
        if (pirState == LOW) {            // Sensor was orginally in a state of no target
            Serial.println('i');            // Send Char command to serial port
            pirState = HIGH;                // Set the value of pir state
            delay(500);                     //Delay the adrudino half a sec to let the serial port give a response.
            if (Serial.available()>0)       // We recevied a response from the PI
            {
                while (Serial.available()>0)   // Runs as long as we recieve input from PI
                {
                    inbyte=(byte)Serial.read();  // Assinging the byte from the pi
                    if (inbyte=='C')             // Byte value for a match on cat
                    {
                        myTone(8,1000, 2000);         // tone on pin-8 with 1000 Hz for 2000 milliseconds

                    }

                }  
            }
            else                            // No Response from the Pi, default to cat identification
            {

                //myTone(8,1000, 2000);       // tone on pin-8 with 1000 Hz for 2000 milliseconds


            }
        }

    } else                              // Set the sensor state back to zero
    {
        if (pirState == HIGH)
        {pirState = LOW;}

    }

}


