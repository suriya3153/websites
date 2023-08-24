import streamlit as st
import re
from streamlit_option_menu import option_menu
import pandas as pd
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
def updates(name,number,age,distance,status,god,all_res,last_res,not_res_count,pos_res):
    booleans=True
    if len(name)==0:
        st.error("name is empty")
        booleans=False
        
    else:
        pattern = r'^\d{10}$'
        # Use the re.match() function to check if the number matches the pattern
        if re.match(pattern, number):
            if age!="-":
                try:
                    # Convert the input to an integer
                    age = int(age)
                    
                    # Check if the age is within a reasonable range (e.g., between 0 and 150)
                    if 0 <= age <= 150:
                        booleans= True
                    else:
                        st.error("not in range 0 to 150")
                        booleans=  False
                except ValueError:
                    st.error("enter valid age")
                    # If conversion to integer fails, the input is not a valid age
                    booleans=  False
                
        else:
            st.error("enter valid number")
            booleans= False
    
    if booleans == True:
        csv_filename = "existing_data.csv"
        
        # New data to append
        new_data = [name, number, age, distance, status, god, all_res, last_res, not_res_count, pos_res]
        columns = ["Name", "Number", "Age", "Distance", "Status", "God", "All_Res", "Last_Res", "Not_Res_Count", "Pos_Res"]
        
        # Read existing CSV into a DataFrame
        try:
            existing_df = pd.read_csv(csv_filename)
        except FileNotFoundError:
            existing_df = pd.DataFrame(columns=columns)
        
        # Check if username already exists
        if selected=="Add Contact":
            if name in existing_df["Name"].values:
                st.error("Error: Username already exists.")
            else:
                # Create a DataFrame for the new row
                new_row_df = pd.DataFrame([new_data], columns=columns)
                
                # Concatenate existing DataFrame with the new row DataFrame
                updated_df = pd.concat([existing_df, new_row_df], ignore_index=True)
                
                # Save the updated DataFrame back to the CSV file
                try:
                    updated_df.to_csv(csv_filename, index=False)
                    st.success("Data appended to CSV successfully!")
                except Exception as e:
                    print("Error:", e)
        else:
            new_row_df = pd.DataFrame([new_data], columns=columns)
            
            # Concatenate existing DataFrame with the new row DataFrame
            updated_df = pd.concat([existing_df, new_row_df], ignore_index=True)
            
            # Save the updated DataFrame back to the CSV file
            try:
                updated_df.to_csv(csv_filename, index=False)
                st.success("Data appended to CSV successfully!")
            except Exception as e:
                print("Error:", e)

with st.sidebar:
    selected=option_menu(menu_title="Main Menu", options=["Add Contact","On Going","Not Interested","Interested","Stats"])
    

if selected=="Add Contact":
    name=st.text_input("name*")
    number=st.text_input("mobile number*")
    age=st.text_input("age (optional)")
    if len(age)==0:
        age="-"
    distance=st.text_input("distance")
    if len(distance)==0:
        distance="-"
    status = st.selectbox("religions: ",
                     ['Hinduism', 'Christianity', 'Islam',"Other"])
    if status=="Other":
        status=st.text_input("Enter The religions:")
    God_belive = st.selectbox("God_belive: ",
                     ['Yes', 'No', 'maybe','Want to find',"Other"])
    if God_belive=="Other":
        God_belive=st.text_input("Enter The God_belive:")
    
    all_res={}
    res_count=st.number_input("call_count",step=1,value=0)
    for i in range(res_count-len(all_res)):
        date=st.date_input("date",key=f"date{i}")
        time=st.time_input("time",key=f"time{i}")
        responss=st.selectbox("respons: ",
                         ['not response',"now invited",'interested', 'wrong number', 'not interested',"Other"],key=f"response{i}")
        if responss=="Other":
            responss=st.text_input("Enter The response:",key=f"responses{i}")
    
            
        all_res[f"{name}_{i}"]={"date":date,"time":f"{time}","response":responss}
    last_response="-"
    if len(all_res)!=0:
        last_response=all_res[list(all_res.keys())[-1]]["response"]
    not_res_count=0
    postive_res=0
    for key, value in all_res.items():
        if value["response"]!='not response':
            postive_res=postive_res+1
        else:
            not_res_count=not_res_count+1
    

                 
    if(st.button('save')):
        updates(name,number,age,distance,status,God_belive,all_res,last_response,not_res_count,postive_res)
        
        pass
if selected=="On Going":
    csv_filename = "existing_data.csv"
    
    # New data to append
   
    try:
        existing_df = pd.read_csv(csv_filename)
        st.write(existing_df)
    except FileNotFoundError:
        pass
    
