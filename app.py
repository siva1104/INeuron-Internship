import pandas as pd
import numpy as np
import pickle
import streamlit as st

sales_model = pickle.load(open('C:/Users/R SIVAKUMAR/Downloads/store sales prediction/model.pkl','rb'))

def main():
    st.title('Store Sales Prediction')
    
    item_Fat = ['Low Fat','Regular']
    items = ['Food','Non-Consumable','Drinks']
    outlet_loc_type = ['Tier 1','Tier 3','Tier 2']
    outlet_size = ['High','Medium','Low']
    outlet_types = ['Supermarket Type1','Supermarket Type2','SuperMarket Type3','Grocery Store']
    years = ['37','35','25','24','23','20','18','15','13']
    
    Item_Weight = st.number_input("Item_Weight",min_value=(4.555),max_value=(21.35))
    
    Item_Fat_Content = st.selectbox("Item_Fat_Content",item_Fat)
    if (Item_Fat_Content== 'Low Fat'):
        Item_Fat_Content = 0
    else:
        Item_Fat_Content = 1
        
    Item_Type_Combined = st.selectbox("Item_Type_Combined",items)
    if (Item_Type_Combined == 'Food'):
        Item_Type_Combined = 1
    elif (Item_Type_Combined == 'Non-Consumable'):
        Item_Type_Combined = 2
    else:
        Item_Type_Combined = 0
    

    Outlet_Size = st.selectbox("Outlet_Size",outlet_size)
    if (Outlet_Size == 'Medium'):
        Outlet_Size = 1
    elif (Outlet_Size == 'High'):
        Outlet_Size = 0
    else:
        Outlet_Size = 2
        
    Outlet_Location_Type = st.selectbox("Outlet_Location_Type",outlet_loc_type)
    if (Outlet_Location_Type == 'Tier 1'):
        Outlet_Location_Type = 0
    elif (Outlet_Location_Type == 'Tier 3'):
        Outlet_Location_Type = 2
    else:
        Outlet_Location_Type = 1

    Item_MRP = st.number_input("Item_MRP",min_value=(31.29),max_value=(266.8884))
    
    Outlet_Type = st.selectbox("Outlet_Type",outlet_types)
    if (Outlet_Type == 'Supermarket Type1'):
        Outlet_Type = 1
    elif (Outlet_Type == 'Supermarket Type2'):
        Outlet_Type = 2
    elif (Outlet_Type == 'Grocery Store'):
        Outlet_Type = 0
    else:
        Outlet_Type = 3
        
    Outlet_Years = st.selectbox("Outlet_Years",years)
    
    #Item_Weight, Item_Fat_Content, Item_Type, Item_MRP = st.beta_columns(4)
    #Outlet_Size, Outlet_Location_Type, Outlet_Type,Years_Established = st.beta_columns(4) 
    
    train = [Item_Weight, Item_Fat_Content, Item_Type_Combined,
       Item_MRP, Outlet_Size, Outlet_Location_Type, Outlet_Type,
       Outlet_Years]
    
    features_value = [np.array(train)]
    
    features_names = ['Item_Weight', 'Item_Fat_Content', 'Item_Type_Combined',
       'Item_MRP', 'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type',
       'Outlet_Years']
    
    df = pd.DataFrame(features_value, columns=features_names)
    
    if st.button("Predict"):
        makeprediction = sales_model.predict(df)
        output = round(makeprediction[0],2)
        st.success('The Sales are $ {}'.format(output))

    
    
if __name__=='__main__':
    main()