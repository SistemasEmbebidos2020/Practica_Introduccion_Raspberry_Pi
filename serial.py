# !/usr/bin/env python3
# Generated by Proteus Visual Designer for Raspberry Pi

# Modules
import var
import pio
import cpu
import Ports

def peripheral_setup () :
 pio.cpu=cpu.CPU ()
 pio.uart=Ports.UART ()

def peripheral_loop () :
 pass


def variables_setup () :
 var.Name = ''

def chart_SETUP () :
 pio.uart.setup(115200)
 pio.uart.print ("Whats your name? ")
 var.Name = pio.uart.input (True)
 pio.uart.println ("Hello "+var.Name)
 return

def chart_LOOP () :
 return

# Main function
def main () :
# Setup
 variables_setup ()
 peripheral_setup ()
 chart_SETUP ()
# Infinite loop
 while True :
  peripheral_loop ()
  chart_LOOP ()
# Command line execution
if __name__ == '__main__' :
   main()
