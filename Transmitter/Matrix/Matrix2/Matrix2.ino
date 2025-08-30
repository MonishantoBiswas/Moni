void setup() {
  for(int i=0; i<8; i++)
  {
    pinMode(i, OUTPUT);
  }
}

void loop() {
  for(int i=0; i<4; i++)
  {
    digitalWrite(i, HIGH);
  }
    for(int j=4; j<8; j++)
    {
      digitalWrite(j, LOW);
    }
}
