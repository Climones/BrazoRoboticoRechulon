//Conexión to guapa al  ESP-8266

//Importamos librerías
#include "ESP8266WiFi.h"

//Variables
  const char* ssid = "ESIBot";
  const char* password = "AlbaritoWelb?";
  //Objeto WiFiServer Como parámetro se pasa el puerto al que estÃ¡ conectado
  WiFiServer Server(80);
  String msg;

  

void setup() {
    Serial.begin(115200);
    delay(1000);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    if(WiFi.status() == WL_NO_SSID_AVAIL){
    Serial.println("Error con el nombre del punto de acceso");
 }else if(WiFi.status() == WL_CONNECT_FAILED){
          Serial.println("Error en la contraseÃ±a");
 }else{
    Serial.println("Conectando..");
  }
 }
 Serial.print("Conectado a WiFi. IP:");
 Serial.println(WiFi.localIP());
 Server.begin();
}
void loop() {
WiFiClient client = Server.available();
 if (client) {
 while (client.connected()) {
 while (client.available()>0) {
 char c = client.read();
 Serial.write(c);
 msg =msg+c;
 }
 if(msg!=""){
 client.print("este es su mensaje:"+msg);
 msg="";
 }
 delay(10);
 }
 client.stop();
 Serial.println("Client disconnected");
 }
}
