import pyvisa
import numpy as np
import matplotlib.pyplot as plt
import time

# GPIB 설정
rm = pyvisa.ResourceManager()
keithley = rm.open_resource('GPIB::24::INSTR')  # 적절한 GPIB 주소를 사용하세요

# KEITHLEY 초기화 및 설정
keithley.write('*RST')  # 장비 초기화
keithley.write(':SOUR:FUNC VOLT')  # 전압 소스 설정
keithley.write(':SOUR:VOLT:MODE SWE')  # 스윕 모드 설정
keithley.write(':SOUR:VOLT:START 0')  # 시작 전압 설정
keithley.write(':SOUR:VOLT:STOP 5')  # 종료 전압 설정
keithley.write(':SOUR:VOLT:STEP 0.1')  # 스텝 전압 설정
keithley.write(':SENS:FUNC "CURR"')
keithley.write(':SENS:CURR:PROT 0.1')

keithley.write(':SOUR:SWE:RANG AUTO')  # 자동 범위 설정
keithley.write(':SOUR:SWE:SPAC LIN')  # 선형 스윕 설정
keithley.write(':SOUR:DEL 1')  # 각 측정 사이의 지연 시간 설정 (1초)
keithley.write(':TRIG:COUN 51')  # 스윕 포인트 수 설정 (0부터 5까지 0.1 스텝이므로 51 포인트)
keithley.write(':OUTP ON') 


keithley.write('READ?')
keithley.write(':OUTP OFF') 
keithley.close()
