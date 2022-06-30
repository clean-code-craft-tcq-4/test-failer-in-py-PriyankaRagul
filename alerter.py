from alerter_stub import network_alert_stub 
alert_failure_count = 0
Threshold_Temp = 200

def network_alert(celcius):
	print(f'Production code is executing..')
    print(f'ALERT: Temperature is {celcius} celcius')
    if(celcius<=Threshold_Temp):    
      returnCode = 200     # Return 200 for ok
    elif(celcius>Threshold_Temp):
      returnCode = 500     # Return 500 for not-ok
    return returnCode

def farenheit2celcius(farenheit):
  celcius = (farenheit- 32) * 5 / 9
  return celcius

def alert_in_celcius(farenheit, fn_network_alert): #Used function pointer
    celcius = farenheit2celcius(farenheit)
    returnCode = fn_network_alert(celcius)
    if returnCode != 200:
        global alert_failure_count
        alert_failure_count += 1


#Test for temparature less than threshold
alert_in_celcius(380.5, network_alert) # prod code
assert(alert_failure_count==0)
alert_in_celcius(380.5, network_alert_stub) # stub code
assert(alert_failure_count==0)

#Test for temparature equals threshold
alert_in_celcius(392 , network_alert) # prod code
assert(alert_failure_count==0)
alert_in_celcius(392 , network_alert_stub)  # stub code
assert(alert_failure_count==0)

#Test for temparature greater than threshold 
alert_in_celcius(394.5 , network_alert)	# prod code
assert(alert_failure_count==1) 
alert_in_celcius(394.5 , network_alert_stub)  # stub code
assert(alert_failure_count==2) 
print(f'{alert_failure_count} alerts failed.')
print('All is well')
