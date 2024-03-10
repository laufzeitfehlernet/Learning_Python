import requests
import time
import pytz
from mastodon import Mastodon
from datetime import datetime

def conv_to_excel(number):
    return str(number).replace('.',',')
    
def separator(string, number = 50):
    string += '_'* number
    string += '\n'
    return string
    
def convert_time(utc_time_str):
	form = '%Y-%m-%d %H:%M'
	utc_time = datetime.strptime(utc_time_str, form)
	utc = pytz.timezone('UTC')
	utc_time_only = utc.localize(utc_time)
	mez = pytz.timezone('Europe/Berlin')
	local_time = utc_time_only.astimezone(mez)
	local_time_str = str(local_time.hour) + ':' + str(local_time.minute)
	return local_time_str


def start_post(zaehler):
    actual_weather_data = inhalte["currently"]
    timestamp = actual_weather_data["time"]
    date = datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y') 
    zeit = time.localtime()
    zeit = time.strftime("%H:%M")
    actual_temperature = actual_weather_data["temperature"]
    feels_like = actual_weather_data["apparentTemperature"]
    wind_speed = actual_weather_data["windSpeed"]
    precip_prop = actual_weather_data["precipProbability"]
    prpcip_type = actual_weather_data["precipType"]
    pressure    = actual_weather_data["pressure"]
    humidity    = actual_weather_data["humidity"]
    icon        = actual_weather_data["icon"]
    predict     = inhalte["daily"]
    predict_data = predict['data']
    predict_data_day= predict_data[2]
    sunrise_raw = predict_data_day["sunriseTime"]
    sunset_raw  = predict_data_day["sunsetTime"]
    sunrise = convert_time(str(datetime.utcfromtimestamp(sunrise_raw).strftime('%Y-%m-%d %H:%M')))
    sunset  = convert_time(str(datetime.utcfromtimestamp(sunset_raw).strftime('%Y-%m-%d %H:%M')))
    temp_high = predict_data_day["temperatureHigh"]
    temp_low  = predict_data_day["temperatureLow"]
    moon_phase = predict_data_day["moonPhase"]

    str_time = 'Wir schreiben den ' + date + ', es ist ' + zeit + ' Uhr.'
    str_temp = 'Draußen sind es gerade ' + str(round(actual_temperature,1)) + '°C und fühlt sich an wie ' + str(round(feels_like,1)) + '°C.'
    str_pres = 'Der Luftdruck beträgt ' + str(pressure) + ' mbar und wir haben eine Luftfeuchtigkeit von '+ str(round(humidity*100,0)) + '%.'
    str_pred = 'Morgen geht die Sonne um ' + str(sunrise) + ' Uhr auf und um ' + str(sunset) + ' Uhr wieder unter.'
    str_pret = 'Die Tiefstemperatur wird morgen ' + str(round(temp_low,1)) + '°C und die Höchsttemperatur ' + str(round(temp_high,1)) + '°C sein.'

# Konsolenausgabe
    print('_'* 30)
    print(str_time)
    print(str_temp)
    print(str_pres)
    print(str_pred)
    print(str_pret)
    print('_'* 30)
    
    troet = str_time + '\n' + str_temp + '\n' + str_pres + '\n' + str_pred + '\n' + str_pret + '\n'

# Daten speichern in CSV
    log_data = str(date) + ' ' + str(zeit) + ';' + conv_to_excel(actual_temperature) + ';' + conv_to_excel(pressure) 
    log_data +=  ';' + conv_to_excel(humidity) + ';' + conv_to_excel(wind_speed) + ';\n' 
    try:
        file = open('log_data.csv','a')
        file.writelines(log_data)
        file.close()
    except:
        write_CSV = False
    else:
        write_CSV = True

# Mastodon-Post
    try:
        mastodon = Mastodon( access_token = 'pytooter_usercred_user.secret', api_base_url = 'https://mastodon.insance')
        mastodon.toot(troet)
    except:
        mastodon_post = False
        print('Fehler beim Posten!')
    else:
        mastodon_post = True
    
# Protokoll ausgeben
    logfile_data = separator('')
    logfile_data += date + ' - ' + zeit + ': ' + str(zaehler) + '. Durchlauf seit Nullstart\n'
    logfile_data += 'Konsolenausgabe:\n' 
    logfile_data = separator(logfile_data)
    logfile_data += troet
    logfile_data = separator(logfile_data)
    
    if write_CSV:
        logfile_data += 'Daten erfolgreich gespeichert\n'
    else:
        logfile_data += 'Fehler bei der Datensicherung\n'
    if mastodon_post:
        logfile_data += 'Daten erfolgreich getrötet\n'
    else:
        logfile_data += 'Fehler beim Tröt\n'

    try:
        file = open('logfile.txt','a')
        file.writelines(logfile_data)
        file.close()
    except:
        print('LOGFILE KONNTE GESCHRIEBEN WERDEN!')
    else:
        pass
# Start_Post() ENDE




def error_message(content):
    print('Es ist ein Fehler aufgetreten: ' + content)
    t = time.localtime()
    zeit = time.strftime("%d.%m.%Y - %H:%M:%S")
    stunde = time.strftime("%H", t)
    minute = time.strftime("%M", t)
    sekunde = time.strftime("%S", t)
    logfile_data = separator('')
    logfile_data = zeit + ': Folgender Fehler - ' + content + '\n'
    logfile_data = separator(logfile_data)
    try:
        file = open('logfile.txt','a')
        file.writelines(logfile_data)
        file.close()
    except:
        print('LOGFILE KONNTE GESCHRIEBEN WERDEN!')
    else:
        pass


# Neue Api für die Wetterdienst


#minute = time.strftime("%M", t)
#sekunde = time.strftime("%S", t)
zaehler = 1
letzte_stunde = 99

try:
    while True:
        
        t = time.localtime()
        stunde = time.strftime("%H", t)
        
        if stunde != letzte_stunde: 

            try:
                # Neue API/Neuer Weeterdienst
                response = requests.get('https://api.pirateweather.net/forecast/APIKEY/50.937193%2C6.961422?exclude=minutely&units=si')
                
            except:
                error_request = True
            else:
                error_request = False
            
            if error_request:
                error_message('Fehler beim Abholen der Daten aus der API')
                time.sleep(300)
                continue
                
            response.encoding = 'utf-8'
            inhalte = response.json()
            
            file = open('lastdata.txt','w')
            file.writelines(inhalte)
            file.close()
            
            try:
                error_message(inhalte["message"])
                time.sleep(300)
            except:
                start_post(zaehler)
                letzte_stunde = stunde 
                zaehler += 1
            
except KeyboardInterrupt:
    pass

