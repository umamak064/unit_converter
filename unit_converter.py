import streamlit as st

st.title("UNIT CONVERTER")
st.write("### Converts Lenght Height & Time Instantly")

category=st.selectbox("📌choose a category",["Length","Weight","Time"])

def convert_unit(category,value,unit):
    if category=="Length":
        if unit=="Kilometers to miles":
          return value * 0.621371
        elif unit=="miles to kilometers":
          return value / 0.621371
        elif unit == "Meters to feet":
            return value * 3.28084
        elif unit == "Feet to meters":
            return value / 3.28084
        elif unit == "Centimeters to inches":
            return value * 0.393701
        elif unit == "Inches to centimeters":
            return value / 0.393701
        elif unit == "Yards to meters":
            return value * 0.9144
        elif unit == "Meters to yards":
            return value / 0.9144
        elif unit == "Miles to feet":
            return value * 5280
        elif unit == "Feet to miles":
            return value / 5280
        
    elif category=="Weight":
        if unit=="Kilograms to pounds":
          return value * 2.20462
        elif unit=="Pounds to kilograms":
          return value / 2.20462  
        elif unit == "Grams to ounces":
            return value * 0.035274
        elif unit == "Ounces to grams":
            return value / 0.035274
        elif unit == "Tons to kilograms":
            return value * 907.184
        elif unit == "Kilograms to tons":
            return value / 907.184
        
    elif  category=="Time":
        if unit=="Minutes to seconds":
          return value * 60
        elif unit=="Seconds to minutes":
          return value / 60 
        elif unit=="Minutes to hours":
          return value / 60
        elif unit=="Hours to minutes":
          return value * 60     
        elif unit=="Days to hours":
          return value * 24
        elif unit=="Hours to days":
          return value / 24         
        
    return 0

if category=="Length":
    unit=st.selectbox("📏choose conversion",["Kilometers to miles","miles to kilometers", "Meters to feet", "Feet to meters", "Centimeters to inches", "Inches to centimeters", "Yards to meters", "Meters to yards", "Miles to feet", "Feet to miles",])    

elif  category=="Weight":
    unit=st.selectbox("⚖️choose conversion",["Kilograms to pounds", "Pounds to kilograms", "Grams to ounces", "Ounces to grams","Tons to kilograms", "Kilograms to tons"]) 

elif  category=="Time":
    unit=st.selectbox("⏳choose conversion",["Minutes to seconds", "Seconds to minutes", "Minutes to hours", "Hours to minutes", "Days to hours", "Hours to days"] )      
    
value =st.number_input("Enter the value to convert")
if st.button("convert"):
   result= convert_unit(category,value,unit)
   st.success(f"The result is {result:.2f}")
    