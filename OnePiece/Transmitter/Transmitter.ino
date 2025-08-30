#define led 13
#define de 2000
/** Manchester Coding:
*** First two bits indicate if the byte is new or not
*** Next 16 bits contain the data
*** Next 1 bit is the ending bit
*** After each byte, the LED must be turned on
*** Each bit sequence must be therefore 19 characters long.
*** Add dynamic transmission capability
*/

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("What's Your message?:");
  while (Serial.available() == 0) {}
  String message = Serial.readString();
  Serial.print("Your Message: ");
  Serial.print(message);
  Serial.println("Bit Sequence:");
  bool current = true;
  for (int i = 0; i < message.length() - 1; i++)
  {
    current = !current;
    char character = message[i];
    for (int k = 0; k < 3; k++)
    {
      digitalWrite(led, LOW);
      delayMicroseconds(de);
      if (current)
      {
        digitalWrite(led, HIGH);
      }
      delayMicroseconds(de);
      for (int j = 7; j >= 0; j--)
      {
        bool byte = bitRead(character, j);
        Serial.print(byte?"01":"10");
        if (byte)
        {
          digitalWrite(led, LOW);
          delayMicroseconds(de);
          digitalWrite(led, HIGH);
          delayMicroseconds(de);
        }
        else
        {
          digitalWrite(led, HIGH);
          delayMicroseconds(de);
          digitalWrite(led, LOW);
          delayMicroseconds(de);
        }
      }
      digitalWrite(led, LOW);
      delayMicroseconds(de);
      digitalWrite(led, HIGH);
      delay(10); // Decrease to increase speed
    }
    Serial.println();
  }
}
