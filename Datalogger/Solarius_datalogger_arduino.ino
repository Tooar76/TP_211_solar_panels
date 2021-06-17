#include <SPI.h>
#include <SD.h>

const char* filename = "Datalogger_solarius.csv";

File file;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(10, OUTPUT);

  if (!SD.begin(10)){
    Serial.println("Error : Push the resert button");
    for(;;);
  }

  file = SD.open(filename, FILE_WRITE);
}

void loop() {
  // put your main code here, to run repeatedly:

  measure();
  delay(1000);
}

void measure(){
  int val = analogRead(A0);
  float tension = val/1023. 0 * 5.0;
  float R= 100.0;
  float intensity = tension/R;
  float power = intensity * tension;
  file.println(power);
  file.flush();
}
