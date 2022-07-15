#define CLK D5
#define DT D6
#define SW D0
int LEDPIN = D1;


int counter = 0;
int currentStateCLK;
int lastStateCLK;
String currentDir ="";
unsigned long lastButtonPress = 0;

void setup () {

	Serial.begin(9600);

	pinMode(LEDPIN, OUTPUT);

	pinMode(CLK, INPUT);
	pinMode(DT, INPUT);
	pinMode(SW, INPUT);
	lastStateCLK = digitalRead(CLK);
}

void loop () {
	currentStateCLK = digitalRead(CLK);
	if (currentStateCLK != lastStateCLK  && currentStateCLK == 1){
		if (digitalRead(DT) != currentStateCLK) {
			counter --;
			currentDir ="CCW";
		} else {
			// Encoder is rotating CW so increment
			counter ++;
			currentDir ="CW";
		}
		/*Serial.print("Direction: ");*/
		Serial.println(currentDir);
		/*Serial.print(" | Counter: ");*/
		/*Serial.println(counter);*/
	}
	lastStateCLK = currentStateCLK;

	int btnState = digitalRead(SW);
	//If we detect LOW signal, button is pressed
	if (btnState == LOW) {
		//if 50ms have passed since last LOW pulse, it means that the
		//button has been pressed, released and pressed again
		if (millis() - lastButtonPress > 50) {
		    digitalWrite(LEDPIN, LOW);
			Serial.println("SW");
		}

		// Remember last button press event
		lastButtonPress = millis();
	} else {
		digitalWrite(LEDPIN, HIGH);
	}


	// Put in a slight delay to help debounce the reading
	delay(1);
}
