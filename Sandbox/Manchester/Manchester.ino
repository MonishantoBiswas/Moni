//Binary Transmitter
#define led 13
String message; //initiate variable
String prompt = "What is your message?"; //initiate prompt
String confirm = "Your message is "; //repeats message
int bytes[256];
int data[256];
float voltageValue;

void setup() {
  Serial.begin(9600); //initiate serial monitor
  pinMode(led, OUTPUT);
  
}

void loop() {
  Serial.println(prompt); //ask for input

  while (Serial.available() == 0); { //wait for input
  }
  message = Serial.readString(); //write input to variable
  Serial.println(confirm); //repeat message
  Serial.println(message); //
  digitalWrite(led,HIGH);
  delayMicroseconds(80);
  digitalWrite(led,LOW);
  for (int i=0; i < message.length(); i++)
  {
    char character = message.charAt(i);
    for (int j=7; j >= 0; j--)
    {
      bool byte = bitRead(character, j);
      Serial.print(byte?"01":"10");
      if (byte)
      {
        digitalWrite(led, LOW);
        delayMicroseconds(40);
        digitalWrite(led, HIGH);
        delayMicroseconds(40);
      }
      else
      {
        digitalWrite(led, HIGH);
        delayMicroseconds(40);
        digitalWrite(led, LOW);
        delayMicroseconds(40);
      }
    }
  }
  Serial.println("");
}
