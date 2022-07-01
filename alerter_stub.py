Threshold_Temp = 200

def network_alert_stub(celcius):
    print(f'Stub code is executing..')
    print(f'ALERT: Temperature is {celcius} celcius')
    if(celcius<=Threshold_Temp):    
      returnCode = 200     # Return 200 for ok
    elif(celcius>Threshold_Temp):
      returnCode = 500     # Return 500 for not-ok
    return returnCode
