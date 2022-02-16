#include <18F2550.h>
#FUSES NOWDT 						//No Watch Dog Timer
#FUSES WDT128           //Watch Dog Timer uses 1:128 Postscale
#FUSES NOBROWNOUT  		  //No brownout reset
#FUSES NOLVP       			//No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O
#FUSES NOXINST  				//Extended set extension and Indexed Addressing mode disabled (Legacy mode)
#device ADC=16
#use delay(crystal=20000000)
#use rs232 (baud = 9600, xmit = pin_c6, rcv = pin_c7) 	//También se puede configurar el numero de bits y paridad
	
int main (void)
 { 
	int16 x = 0;
	int16 y = 0;
	setup_adc_ports(AN0_TO_AN1);
	setup_adc(ADC_CLOCK_DIV_2|ADC_TAD_MUL_0);

   while (1)
    {
		set_adc_channel(0);
		delay_us(10);
		x = read_adc();
		set_adc_channel(1);
		delay_us(10);
		y = read_adc();
		printf("Lectura del potenciometro 1 = %lu \r",x);
		printf("Lectura del potenciometro 2 = %lu \r",y);
		delay_ms(500);
	}

 }   
