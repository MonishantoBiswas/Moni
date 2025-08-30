#define led 13
/** Manchester Coding:
*** Each byte starts with a black strips and ends with a black strip
*** After each byte, the LED must be turned on
*** Each bit sequence must be therefore 18 characters long.
*** Add dynamic transmission capability
*/

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  char character = 'm';
  while (true)
  {
    digitalWrite(led, LOW);
    delay(2);
    for (int j=7; j >= 0; j--)
    {
      bool byte = bitRead(character, j);
      Serial.print(byte?"01":"10");
      if (byte)
      {
        digitalWrite(led, LOW);
        delay(2);
        digitalWrite(led, HIGH);
        delay(2);
      }
      else
      {
        digitalWrite(led, HIGH);
        delay(2);
        digitalWrite(led, LOW);
        delay(2);
      }
    }
    digitalWrite(led, LOW);
    delay(2);
    digitalWrite(led, HIGH);
    delay(5000);
  }
}
