const int pin1 = 8;
const int pin2 = 13;

void setup() {
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
}

void loop() {
  digitalWrite(pin1, HIGH);
  digitalWrite(pin2, LOW);
  delay(1000); // 1 second delay
  digitalWrite(pin1, LOW);
  digitalWrite(pin2, HIGH);
  delay(1000); // 1 second delay
}
