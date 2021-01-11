from tkinter import *
import requests

show = Tk()
show.title("Weather App")
show.geometry("750x600")
show.configure(background="Aqua")

def grtweather():
    url ='http://api.openweathermap.org/data/2.5/weather'
    weatherkey= 'f28ba72d6153b34d2539254645987590'
    loc = txtcity.get()
    par = {'appid': weatherkey, 'q': loc, 'units': "Metric"}
    result = requests.get(url, params=par)
    res = result.json()

    lbl_out_temp.config(text=(res['main']['temp']))
    lbl_out_windspeed.config(text=res['wind']['speed'])
    lbl_out_humidity.config(text=res['main']['humidity'])
    lbl_out_pressure.config(text=res['main']['pressure'])



lblcity= Label(show, text= "Enter City:", bg="skyblue")
lblcity.pack()
txtcity= Entry(show , width= 30)
txtcity.pack()

lbl_temp = Label(show, text="Temperature:")
lbl_temp.place(x=30,y=160)

lbl_out_temp = Label(show)
lbl_out_temp.place(x=190,y=160)

lbl_pressure= Label (show, text="Pressure:")
lbl_pressure.place(x=30,y=260)

lbl_out_pressure = Label(show,)
lbl_out_pressure .place(x=190,y=260)

lbl_windspeed = Label (show, text="windspeed:")
lbl_windspeed.place(x=30,y=360)

lbl_out_windspeed  = Label(show,)
lbl_out_windspeed .place(x=190,y=360)

lbl_humidity = Label (show, text="humidity:")
lbl_humidity.place(x=30,y=460)

lbl_out_humidity = Label(show,)
lbl_out_humidity.place(x=190,y=460)

#Buttons
search_btn = Button(show,text='Search Weather', width= 15,bg="green", command=grtweather )
search_btn.place(x=310,y=70)

show.mainloop()
