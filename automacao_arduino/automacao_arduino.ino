//Programa : Teste Modulo Rele Arduino 2 canais - Lampadas
//Autor : FILIPEFLOP
 
//Porta ligada ao pino IN1 do modulo
int porta_rele1 = 13;

  
void setup()
{
  //Define pinos para o rele como saida
  pinMode(porta_rele1, OUTPUT); 
  Serial.begin(9600);
}
   
void loop()
{
  char command;

  command = Serial.read();

  if (command == '1'){
    digitalWrite(porta_rele1, LOW);  //Liga rele 1
    Serial.println("LED está aceso.");    
  }
  else if(command == '2'){
    digitalWrite(porta_rele1, HIGH); //Desliga rele 1
    Serial.println("LED está apagado.");
  }

}
