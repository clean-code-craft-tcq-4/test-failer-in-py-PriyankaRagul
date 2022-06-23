alert_failure_count =0
Threshold_temp = 100
def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    if (celcius <=100 and celcius>=0):
        return 200
    # Return 500 for not-ok
    else:
        return 500

def alert_in_celcius(farenheit):
    global alert_failure_count
    alert_failure_count=0
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        alert_failure_count+=1
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
       
alert_in_celcius(400.5)
assert(alert_failure_count==0)
alert_in_celcius(303.6)
assert(alert_failure_count==0)
alert_in_celcius(100.6)
assert(alert_failure_count==0)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
