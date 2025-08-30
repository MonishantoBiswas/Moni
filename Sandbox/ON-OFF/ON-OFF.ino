const int ledPin = 13;  // Pin number for the LED (change this to your setup)

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  while (1){
    digitalWrite(ledPin, HIGH);  // Turn on the LED
    delay(5);              // Wait for the specified ON time
    digitalWrite(ledPin, LOW);   // Turn off the LED
    delay(5);             // Wait for the specified OFF time
  }
}
