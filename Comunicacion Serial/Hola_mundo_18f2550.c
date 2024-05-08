/* 
##############################################################################
##   M.C. Osbaldo Aragón Banderas, ITSRLL
##   "Programa básico puerto Serial para PIC 18F4550"
##
##   Microcontroladores 2018
##############################################################################
*/
#include <18F2550.h>
#fuses HS,NOWDT,NOPUT,NOLVP,BROWNOUT,NOCPD,NOWRT //Configuración Básica de FUSES
#use delay(clock=48MHz,crystal=4MHz,USB_FULL) //Usar cristal Externo de 4MHZ

#use rs232 (baud = 9600, xmit = pin_c6, rcv = pin_c7) //Puertos de transmisión y resepción estandar

void main()
{
   while(TRUE)
   {
      printf("Hola mundo \r");
      output_toggle(PIN_B0);
      delay_ms(1000);
   }

}
