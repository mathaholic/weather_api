# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:53:28 2016

@author: NicholeH
"""
#a script to pull the maximum and minimum temperature over the next three days
#in a user-provided city using the weather underground API.

import urllib
import json

#wrap the main code in a def so that it doens't automatically run
def main():
    #Prompt user for a city
    loc = input("Please enter a US city and state code in City, ST format:")
    cit = loc.split(', ')[0]
    #if the city has a space in it, replace with an underscore
    cit = cit.replace(" ", "_")  
    
    st = loc.split(', ')[1]
    if len(st)>2: print('Please run again with a valid state code.')
    else:
        site ='http://api.wunderground.com/api/614a3a459a2fc34a/forecast/q/'+st+'/'+cit+'.json'
        f = urllib.request.urlopen(site).read().decode("utf-8")
        parsed_json = json.loads(f)
        r = parsed_json['response']
        #check response for errors and ambiguous entries.
        if 'error' in r:
            print('Apologies, but that is not a valid US city.')
        else:
            high = list()
            low = list()
            for day in parsed_json['forecast']['simpleforecast']['forecastday']:
                 high.append(day['high']['fahrenheit'])
                 low.append(day['low']['fahrenheit'])
            hg = max(high)
            lw = min(low)
            print("The maximum temperature in",cit,"over the next three days is forcasted to be",hg,"degrees Fahrenheit.")
            print("The minimum temperature in",cit,"over the next three days is forcasted to be",lw,"degrees Fahrenheit.")
 
           
if __name__ == '__main__':
    main()