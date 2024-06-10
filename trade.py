import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as sp
import plotly.express as px
from plotly.subplots import make_subplots

def main():
    with open('styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    with st.sidebar:
        # st.image('https://www.vabysmo-hcp.com/content/dam/gene/vabysmo-hcp/logos/vabysmo-logo-og.genecoreimg.1200.png')
        drugs_selected = st.multiselect(
        "Drugs Selected",
        ["Drug 1", "Drug 2", "Drug 3", "Drug 4","Drug 5"],
        ["Drug 1", "Drug 2", "Drug 3", "Drug 4","Drug 5"])
        disease_indication=st.sidebar.selectbox('Disease Indication',['WET AMD','DME'])
        time_horizon=st.sidebar.selectbox('Time Horizon (in Years)',['1','2','3','4','5'])
        with open('time_horizon.txt','w') as f:
            f.write(time_horizon)
        patient_support=st.sidebar.selectbox('Patient Support',['Yes','No'])
        if patient_support == "Yes":
            drug1_cost_per_vial=30000  #---Drug 1 = Faricimab
            drug2_cost_per_vial=24000 #---Drug 2 = Aflibercept
            drug3_cost_per_vial=35000 #---Drug 3 = Brolucizumab
            drug4_cost_per_vial=25000  #---Drug 4 = Ranibizumab
            drug5_cost_per_vial=20000  #---Drug 5 = Rani Biosimilar
            
        else:
            drug1_cost_per_vial=75000  #---Drug 1 = Faricimab
            drug2_cost_per_vial=60000 #---Drug 2 = Aflibercept
            drug3_cost_per_vial=35000 #---Drug 3 = Brolucizumab
            drug4_cost_per_vial=25000  #---Drug 4 = Ranibizumab
            drug5_cost_per_vial=20000  #---Drug 5 = Rani Biosimilar
        
        naive_switch=st.sidebar.selectbox('Naive/Switch',['Naive','Switch'])
        clinical_status=st.sidebar.selectbox('Clinical Status',['Per Label','RWE'])
    
        if(disease_indication=="WET AMD" and time_horizon=="1" and naive_switch=="Naive" and clinical_status=="Per Label"):
            user_info = {"Drug 1": "6", "Drug 2": "8", "Drug 3": "8", "Drug 4": "12", "Drug 5": "12"}
            
            table = """
                    <style>
                    .centered-table {
                        width: 100%;
                    }
                    .centered-table th, .centered-table td {
                        text-align: center;
                        width: 70px;
                    }
                    </style>
                    <table class='centered-table'>
                    <tr><th>Drug</th><th>Dosage</th></tr>
                    """
            for key in user_info.keys():
                table += f"<tr><td>{key}</td><td>{user_info[key]}</td></tr>"
            table += "</table>"
            st.sidebar.markdown(table, unsafe_allow_html=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
            drug1_dosage=6
            drug2_dosage=8
            drug3_dosage=8
            drug4_dosage=12
            drug5_dosage=12

        elif(disease_indication=="WET AMD" and time_horizon=="2" and naive_switch=="Naive" and clinical_status=="Per Label"):
            user_info = {"Drug 1": "9", "Drug 2": "14", "Drug 3": "12", "Drug 4": "24", "Drug 5": "24"}
            
            table = """
                    <style>
                    .centered-table {
                        width: 100%;
                    }
                    .centered-table th, .centered-table td {
                        text-align: center;
                        width: 70px;
                    }
                    </style>
                    <table class='centered-table'>
                    <tr><th>Drug</th><th>Dosage</th></tr>
                    """
            for key in user_info.keys():
                table += f"<tr><td>{key}</td><td>{user_info[key]}</td></tr>"
            table += "</table>"
            st.sidebar.markdown(table, unsafe_allow_html=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
            drug1_dosage=9
            drug2_dosage=14
            drug3_dosage=12
            drug4_dosage=24
            drug5_dosage=24

        elif(disease_indication=="WET AMD" and time_horizon=="3" and naive_switch=="Naive" and clinical_status=="Per Label"):
            user_info = {"Drug 1": "12", "Drug 2": "20", "Drug 3": "16", "Drug 4": "36", "Drug 5": "36"}
            
            table = """
                    <style>
                    .centered-table {
                        width: 100%;
                    }
                    .centered-table th, .centered-table td {
                        text-align: center;
                        width: 70px;
                    }
                    </style>
                    <table class='centered-table'>
                    <tr><th>Drug</th><th>Dosage</th></tr>
                    """
            for key in user_info.keys():
                table += f"<tr><td>{key}</td><td>{user_info[key]}</td></tr>"
            table += "</table>"
            st.sidebar.markdown(table, unsafe_allow_html=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
            drug1_dosage=12
            drug2_dosage=20
            drug3_dosage=16
            drug4_dosage=36
            drug5_dosage=36

        elif(disease_indication=="WET AMD" and time_horizon=="4" and naive_switch=="Naive" and clinical_status=="Per Label"):
            user_info = {"Drug 1": "15", "Drug 2": "26", "Drug 3": "20", "Drug 4": "48", "Drug 5": "48"}
            
            table = """
                    <style>
                    .centered-table {
                        width: 100%;
                    }
                    .centered-table th, .centered-table td {
                        text-align: center;
                        width: 70px;
                    }
                    </style>
                    <table class='centered-table'>
                    <tr><th>Drug</th><th>Dosage</th></tr>
                    """
            for key in user_info.keys():
                table += f"<tr><td>{key}</td><td>{user_info[key]}</td></tr>"
            table += "</table>"
            st.sidebar.markdown(table, unsafe_allow_html=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
            drug1_dosage=15
            drug2_dosage=26
            drug3_dosage=20
            drug4_dosage=48
            drug5_dosage=48
        
        elif(disease_indication=="WET AMD" and time_horizon=="5" and naive_switch=="Naive" and clinical_status=="Per Label"):
            user_info = {"Drug 1": "18", "Drug 2": "32", "Drug 3": "24", "Drug 4": "60", "Drug 5": "60"}
            
            table = """
                    <style>
                    .centered-table {
                        width: 100%;
                    }
                    .centered-table th, .centered-table td {
                        text-align: center;
                        width: 70px;
                    }
                    </style>
                    <table class='centered-table'>
                    <tr><th>Drug</th><th>Dosage</th></tr>
                    """
            for key in user_info.keys():
                table += f"<tr><td>{key}</td><td>{user_info[key]}</td></tr>"
            table += "</table>"
            st.sidebar.markdown(table, unsafe_allow_html=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
            drug1_dosage=18
            drug2_dosage=32
            drug3_dosage=24
            drug4_dosage=60
            drug5_dosage=60
        
        elif(disease_indication=="DME" and time_horizon=="1" and naive_switch=="Naive" and clinical_status=="Per Label"):
            user_info = {"Drug 1": "6", "Drug 2": "9", "Drug 3": "9", "Drug 4": "12", "Drug 5": "12"}
            
            table = """
                    <style>
                    .centered-table {
                        width: 100%;
                    }
                    .centered-table th, .centered-table td {
                        text-align: center;
                        width: 70px;
                    }
                    </style>
                    <table class='centered-table'>
                    <tr><th>Drug</th><th>Dosage</th></tr>
                    """
            for key in user_info.keys():
                table += f"<tr><td>{key}</td><td>{user_info[key]}</td></tr>"
            table += "</table>"
            st.sidebar.markdown(table, unsafe_allow_html=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
            drug1_dosage=6
            drug2_dosage=9
            drug3_dosage=9
            drug4_dosage=12
            drug5_dosage=12
        
        
        elif(disease_indication=="DME" and time_horizon=="2" and naive_switch=="Naive" and clinical_status=="Per Label"):
            user_info = {"Drug 1": "9", "Drug 2": "15", "Drug 3": "13", "Drug 4": "24", "Drug 5": "24"}
            
            table = """
                    <style>
                    .centered-table {
                        width: 100%;
                    }
                    .centered-table th, .centered-table td {
                        text-align: center;
                        width: 70px;
                    }
                    </style>
                    <table class='centered-table'>
                    <tr><th>Drug</th><th>Dosage</th></tr>
                    """
            for key in user_info.keys():
                table += f"<tr><td>{key}</td><td>{user_info[key]}</td></tr>"
            table += "</table>"
            st.sidebar.markdown(table, unsafe_allow_html=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
            drug1_dosage=9
            drug2_dosage=15
            drug3_dosage=13
            drug4_dosage=24
            drug5_dosage=24
        
        
        elif(disease_indication=="DME" and time_horizon=="3" and naive_switch=="Naive" and clinical_status=="Per Label"):
            user_info = {"Drug 1": "12", "Drug 2": "21", "Drug 3": "17", "Drug 4": "36", "Drug 5": "36"}
            
            table = """
                    <style>
                    .centered-table {
                        width: 100%;
                    }
                    .centered-table th, .centered-table td {
                        text-align: center;
                        width: 70px;
                    }
                    </style>
                    <table class='centered-table'>
                    <tr><th>Drug</th><th>Dosage</th></tr>
                    """
            for key in user_info.keys():
                table += f"<tr><td>{key}</td><td>{user_info[key]}</td></tr>"
            table += "</table>"
            st.sidebar.markdown(table, unsafe_allow_html=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
            drug1_dosage=12
            drug2_dosage=21
            drug3_dosage=17
            drug4_dosage=36
            drug5_dosage=36
        
        
        elif(disease_indication=="DME" and time_horizon=="4" and naive_switch=="Naive" and clinical_status=="Per Label"):
            user_info = {"Drug 1": "15", "Drug 2": "27", "Drug 3": "21", "Drug 4": "48", "Drug 5": "48"}
            
            table = """
                    <style>
                    .centered-table {
                        width: 100%;
                    }
                    .centered-table th, .centered-table td {
                        text-align: center;
                        width: 70px;
                    }
                    </style>
                    <table class='centered-table'>
                    <tr><th>Drug</th><th>Dosage</th></tr>
                    """
            for key in user_info.keys():
                table += f"<tr><td>{key}</td><td>{user_info[key]}</td></tr>"
            table += "</table>"
            st.sidebar.markdown(table, unsafe_allow_html=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
            drug1_dosage=15
            drug2_dosage=27
            drug3_dosage=21
            drug4_dosage=48
            drug5_dosage=48
        
        
        elif(disease_indication=="DME" and time_horizon=="5" and naive_switch=="Naive" and clinical_status=="Per Label"):
            user_info = {"Drug 1": "18", "Drug 2": "33", "Drug 3": "25", "Drug 4": "60", "Drug 5": "60"}
            
            table = """
                    <style>
                    .centered-table {
                        width: 100%;
                    }
                    .centered-table th, .centered-table td {
                        text-align: center;
                        width: 70px;
                    }
                    </style>
                    <table class='centered-table'>
                    <tr><th>Drug</th><th>Dosage</th></tr>
                    """
            for key in user_info.keys():
                table += f"<tr><td>{key}</td><td>{user_info[key]}</td></tr>"
            table += "</table>"
            st.sidebar.markdown(table, unsafe_allow_html=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
            drug1_dosage=18
            drug2_dosage=33
            drug3_dosage=25
            drug4_dosage=60
            drug5_dosage=60

        elif(disease_indication=="WET AMD" and naive_switch=="Switch" and clinical_status=="Per Label"):
            user_info = {"Drug 1": "3", "Drug 2": "6", "Drug 3": "4", "Drug 4": "12", "Drug 5": "12"}        
            table = """
                    <style>
                    .centered-table {
                        width: 100%;
                    }
                    .centered-table th, .centered-table td {
                        text-align: center;
                        width: 70px;
                    }
                    </style>
                    <table class='centered-table'>
                    <tr><th>Drug</th><th>Dosage</th></tr>
                    """
            for key in user_info.keys():
                table += f"<tr><td>{key}</td><td>{user_info[key]}</td></tr>"
            table += "</table>"
            st.sidebar.markdown(table, unsafe_allow_html=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
            drug1_dosage=3
            drug2_dosage=6
            drug3_dosage=4
            drug4_dosage=12
            drug5_dosage=12
        
        elif(disease_indication=="DME" and naive_switch=="Switch" and clinical_status=="Per Label"):
            user_info = {"Drug 1": "3", "Drug 2": "6", "Drug 3": "4", "Drug 4": "12", "Drug 5": "12"}        
            table = """
                    <style>
                    .centered-table {
                        width: 100%;
                    }
                    .centered-table th, .centered-table td {
                        text-align: center;
                        width: 70px;
                    }
                    </style>
                    <table class='centered-table'>
                    <tr><th>Drug</th><th>Dosage</th></tr>
                    """
            for key in user_info.keys():
                table += f"<tr><td>{key}</td><td>{user_info[key]}</td></tr>"
            table += "</table>"
            st.sidebar.markdown(table, unsafe_allow_html=True)
            st.sidebar.markdown("<br>", unsafe_allow_html=True)
            drug1_dosage=3
            drug2_dosage=6
            drug3_dosage=4
            drug4_dosage=12
            drug5_dosage=12

        elif(clinical_status=="RWE"):
            if 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)

            elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug5_dosage=0

            elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug4_dosage=0

            elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug3_dosage=0

            elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug2_dosage=0
            
            elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug1_dosage=0

            elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug5_dosage=0
                drug4_dosage=0

            elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug4_dosage=0
                drug3_dosage=0

            elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug2_dosage=0
                drug3_dosage=0

            elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug1_dosage=0
                drug2_dosage=0
            
            elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug4_dosage=0
                drug2_dosage=0
            
            elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug1_dosage=0
                drug3_dosage=0

            elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug2_dosage=0
                drug5_dosage=0

            elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug5_dosage=0
                drug3_dosage=0

            elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug5_dosage=0
                drug1_dosage=0
            
            elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug1_dosage=0
                drug4_dosage=0

            elif 'Drug 1' in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=0
                drug4_dosage=0
                drug5_dosage=0

            elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug2_dosage=0
                drug4_dosage=0
                drug5_dosage=0
            
            elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug2_dosage=0
                drug3_dosage=0
                drug5_dosage=0

            elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug2_dosage=0
                drug3_dosage=0
                drug4_dosage=0

            elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug1_dosage=0
                drug4_dosage=0
                drug5_dosage=0
            
            elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug1_dosage=0
                drug3_dosage=0
                drug5_dosage=0
            
            elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug1_dosage=0
                drug3_dosage=0
                drug4_dosage=0

            elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug1_dosage=0
                drug2_dosage=0
                drug5_dosage=0
            
            elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug1_dosage=0
                drug2_dosage=0
                drug4_dosage=0

            elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' in drugs_selected:
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug1_dosage=0
                drug2_dosage=0
                drug3_dosage=0
            
            elif 'Drug 1' in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
                drug1_dosage=st.sidebar.selectbox('Drug 1 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug2_dosage=0
                drug3_dosage=0
                drug4_dosage=0
                drug5_dosage=0
                
            
            elif 'Drug 1' not in drugs_selected and 'Drug 2' in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
                drug2_dosage=st.sidebar.selectbox('Drug 2 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=2)
                drug1_dosage=0
                drug3_dosage=0
                drug4_dosage=0
                drug5_dosage=0
            
            elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' not in drugs_selected:
                drug3_dosage=st.sidebar.selectbox('Drug 3 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=4)
                drug2_dosage=0
                drug1_dosage=0
                drug4_dosage=0
                drug5_dosage=0
            
            elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' in drugs_selected and 'Drug 5' not in drugs_selected:
                drug4_dosage=st.sidebar.selectbox('Drug 4 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug2_dosage=0
                drug3_dosage=0
                drug1_dosage=0
                drug5_dosage=0
            
            elif 'Drug 1' not in drugs_selected and 'Drug 2' not in drugs_selected and 'Drug 3' not in drugs_selected and 'Drug 4' not in drugs_selected and 'Drug 5' in drugs_selected:
                drug5_dosage=st.sidebar.selectbox('Drug 5 RWE Dosage',['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],index=7)
                drug2_dosage=0
                drug3_dosage=0
                drug4_dosage=0
                drug1_dosage=0
        
        procedure_cost =st.sidebar.selectbox('Procedure Cost',['₹1000','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000','₹6000','₹7000','₹8000','₹9000','₹10,000','₹11,000','₹12,000','₹13,000','₹14,000','₹15,000','₹16,000','₹17,000','₹18,000','₹19,000','₹20,000','₹21,000','₹22,000','₹23,000','₹24,000','₹25,000','₹26,000','₹27,000','₹28,000','₹29,000','₹30,000'])
        oct_cost = st.sidebar.selectbox('OCT Cost',['₹0','₹200','₹300','₹500','₹700','₹1000','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000'],index=1)
        consulting_charges = st.sidebar.selectbox('Consultating Charges',['₹0','₹200','₹300','₹500','₹700','₹1000','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000'],index=1)
        miscellaneous_cost = st.sidebar.selectbox('Miscellaneous Cost',['₹0','₹100','₹200','₹300','₹400','₹500','₹600','₹700','₹800','₹900','₹1000','₹1200','₹1400','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000'],index=1)
        travel_cost = st.sidebar.selectbox('Travel Cost',['₹0','₹100','₹200','₹300','₹400','₹500','₹600','₹700','₹800','₹900','₹1000','₹1200','₹1400','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000'],index=1)
        food_cost = st.sidebar.selectbox('Food Cost',['₹0','₹100','₹200','₹300','₹400','₹500','₹600','₹700','₹800','₹900','₹1000','₹1200','₹1400','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000'],index=1)
        patient_lost_opportunity_cost = st.sidebar.selectbox('Lost Opportunity Cost/Day (Patient)',['₹1000','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000','₹6000','₹7000','₹8000','₹9000','₹10,000','₹11,000','₹12,000','₹13,000','₹14,000','₹15,000','₹16,000','₹17,000','₹18,000','₹19,000','₹20,000'])
        caregiver_lost_opportunity_cost = st.sidebar.selectbox('Lost Opportunity Cost/Day (Caregiver)',['₹1000','₹1500','₹2000','₹2500','₹3000','₹3500','₹4000','₹4500','₹5000','₹6000','₹7000','₹8000','₹9000','₹10,000','₹11,000','₹12,000','₹13,000','₹14,000','₹15,000','₹16,000','₹17,000','₹18,000','₹19,000','₹20,000'])
        #..............................Final Costs...........................................................
        procedure_cost=procedure_cost[1:]
        if ',' in procedure_cost:
            procedure_cost=procedure_cost.replace(',','')
            procedure_cost=int(procedure_cost)
        else:
            procedure_cost=int(procedure_cost)

        consulting_charges=int(consulting_charges[1:])
        oct_cost=int(oct_cost[1:])
        miscellaneous_cost=int(miscellaneous_cost[1:])
        travel_cost=int(travel_cost[1:])
        food_cost=int(food_cost[1:])

        patient_lost_opportunity_cost=patient_lost_opportunity_cost[1:]
        if ',' in patient_lost_opportunity_cost:
            patient_lost_opportunity_cost=patient_lost_opportunity_cost.replace(',','')
            patient_lost_opportunity_cost=int(patient_lost_opportunity_cost)
        else:
            patient_lost_opportunity_cost=int(patient_lost_opportunity_cost)

        caregiver_lost_opportunity_cost=caregiver_lost_opportunity_cost[1:]
        if ',' in caregiver_lost_opportunity_cost:
            caregiver_lost_opportunity_cost=caregiver_lost_opportunity_cost.replace(',','')
            caregiver_lost_opportunity_cost=int(caregiver_lost_opportunity_cost)
        else:
            caregiver_lost_opportunity_cost=int(caregiver_lost_opportunity_cost)

 #--------Drug 1----------------------------------------------------------------------------
        drug1_dosage=int(drug1_dosage)
        drug1_dosage_half=drug1_dosage/2

        drug1_total_package_cost=int((drug1_cost_per_vial+procedure_cost)*drug1_dosage)
        drug1_total_consulting_charges=int(consulting_charges*(drug1_dosage+drug1_dosage_half))
        drug1_total_oct_charges=int(oct_cost*(drug1_dosage+drug1_dosage_half))
        drug1_total_travel_food_cost=int((travel_cost+food_cost+miscellaneous_cost)*(drug1_dosage+drug1_dosage_half))
        drug1_total_opportunity_cost_lost=int((patient_lost_opportunity_cost*(drug1_dosage+drug1_dosage_half))+(caregiver_lost_opportunity_cost*(drug1_dosage+drug1_dosage_half)))

        drug1_total_cost_per_patient=drug1_total_package_cost+drug1_total_consulting_charges+drug1_total_oct_charges+drug1_total_travel_food_cost+drug1_total_opportunity_cost_lost
        
        #--------Drug 2-----------------------------------------------------------------------------
        drug2_dosage=int(drug2_dosage)
        drug2_dosage_half=drug2_dosage/2

        drug2_total_package_cost=int((drug2_cost_per_vial+procedure_cost)*drug2_dosage)
        drug2_total_consulting_charges=int(consulting_charges*(drug2_dosage+drug2_dosage_half))
        drug2_total_oct_charges=int(oct_cost*(drug2_dosage+drug2_dosage_half))
        drug2_total_travel_food_cost=int((travel_cost+food_cost+miscellaneous_cost)*(drug2_dosage+drug2_dosage_half))
        drug2_total_opportunity_cost_lost=int((patient_lost_opportunity_cost*(drug2_dosage+drug2_dosage_half))+(caregiver_lost_opportunity_cost*(drug2_dosage+drug2_dosage_half)))

        drug2_total_cost_per_patient=drug2_total_package_cost+drug2_total_consulting_charges+drug2_total_oct_charges+drug2_total_travel_food_cost+drug2_total_opportunity_cost_lost
        
        #--------Drug 3--------------------------------------------------------------------------
        drug3_dosage=int(drug3_dosage)
        drug3_dosage_half=drug3_dosage/2

        drug3_total_package_cost=int((drug3_cost_per_vial+procedure_cost)*drug3_dosage)
        drug3_total_consulting_charges=int(consulting_charges*(drug3_dosage+drug3_dosage_half))
        drug3_total_oct_charges=int(oct_cost*(drug3_dosage+drug3_dosage_half))
        drug3_total_travel_food_cost=int((travel_cost+food_cost+miscellaneous_cost)*(drug3_dosage+drug3_dosage_half))
        drug3_total_opportunity_cost_lost=int((patient_lost_opportunity_cost*(drug3_dosage+drug3_dosage_half))+(caregiver_lost_opportunity_cost*(drug3_dosage+drug3_dosage_half)))

        drug3_total_cost_per_patient=drug3_total_package_cost+drug3_total_consulting_charges+drug3_total_oct_charges+drug3_total_travel_food_cost+drug3_total_opportunity_cost_lost

        
    #--------Drug 4----------------------------------------------------------------------------------------
        drug4_dosage=int(drug4_dosage)
        drug4_dosage_half=drug4_dosage/2

        drug4_total_package_cost=int((drug4_cost_per_vial+procedure_cost)*drug4_dosage)
        drug4_total_consulting_charges=int(consulting_charges*(drug4_dosage+drug4_dosage_half))
        drug4_total_oct_charges=int(oct_cost*(drug4_dosage+drug4_dosage_half))
        drug4_total_travel_food_cost=int((travel_cost+food_cost+miscellaneous_cost)*(drug4_dosage+drug4_dosage_half))
        drug4_total_opportunity_cost_lost=int((patient_lost_opportunity_cost*(drug4_dosage+drug4_dosage_half))+(caregiver_lost_opportunity_cost*(drug4_dosage+drug4_dosage_half)))

        drug4_total_cost_per_patient=drug4_total_package_cost+drug4_total_consulting_charges+drug4_total_oct_charges+drug4_total_travel_food_cost+drug4_total_opportunity_cost_lost
    #--------Drug 5----------------------------------------------------------------------------------------
        drug5_dosage=int(drug5_dosage)
        drug5_dosage_half=drug5_dosage/2

        drug5_total_package_cost=int((drug5_cost_per_vial+procedure_cost)*drug5_dosage)
        drug5_total_consulting_charges=int(consulting_charges*(drug5_dosage+drug5_dosage_half))
        drug5_total_oct_charges=int(oct_cost*(drug5_dosage+drug5_dosage_half))
        drug5_total_travel_food_cost=int((travel_cost+food_cost+miscellaneous_cost)*(drug5_dosage+drug5_dosage_half))
        drug5_total_opportunity_cost_lost=int((patient_lost_opportunity_cost*(drug5_dosage+drug5_dosage_half))+(caregiver_lost_opportunity_cost*(drug5_dosage+drug5_dosage_half)))

        drug5_total_cost_per_patient=drug5_total_package_cost+drug5_total_consulting_charges+drug5_total_oct_charges+drug5_total_travel_food_cost+drug5_total_opportunity_cost_lost

        if 'Drug 1' not in drugs_selected:
            drug1_total_package_cost=0
            drug1_total_consulting_charges=0
            drug1_total_oct_charges=0
            drug1_total_travel_food_cost=0
            drug1_total_opportunity_cost_lost=0
            drug1_total_cost_per_patient=0


        if 'Drug 2' not in drugs_selected:
            drug2_total_package_cost=0
            drug2_total_consulting_charges=0
            drug2_total_oct_charges=0
            drug2_total_travel_food_cost=0
            drug2_total_opportunity_cost_lost=0
            drug2_total_cost_per_patient=0


        if 'Drug 3' not in drugs_selected:
            drug3_total_package_cost=0
            drug3_total_consulting_charges=0
            drug3_total_oct_charges=0
            drug3_total_travel_food_cost=0
            drug3_total_opportunity_cost_lost=0
            drug3_total_cost_per_patient=0

        if 'Drug 4' not in drugs_selected:
            drug4_total_package_cost=0
            drug4_total_consulting_charges=0
            drug4_total_oct_charges=0
            drug4_total_travel_food_cost=0
            drug4_total_opportunity_cost_lost=0
            drug4_total_cost_per_patient=0
        
        if 'Drug 5' not in drugs_selected:
            drug5_total_package_cost=0
            drug5_total_consulting_charges=0
            drug5_total_oct_charges=0
            drug5_total_travel_food_cost=0
            drug5_total_opportunity_cost_lost=0
            drug5_total_cost_per_patient=0

    # Main page
    st.title('I-Open')
    data=pd.read_csv('Display_data.csv')
    def wes_to_indian_conversion(n):
        n=str(n)
        if len(n)>3:
            fisrt_nos=n[:-3]
            last_3=n[-3:]
            org_no=""
            if len(fisrt_nos)%2==0:
                for i in range(len(fisrt_nos)):
                    if i!=0 and i%2==0:
                        org_no=org_no+","+fisrt_nos[i]
                    else:
                        org_no=org_no+fisrt_nos[i]
                org_no="₹"+org_no+","+last_3
                return org_no
            else:
                for i in range(len(fisrt_nos)):
                    if i==0:
                        org_no=fisrt_nos[i]+","+org_no
                    elif i%2==0:
                        org_no=org_no+fisrt_nos[i]+","
                    else:
                        org_no=org_no+fisrt_nos[i]
                org_no="₹"+org_no+last_3
                return org_no
        else:
            org_no="₹"+n
            return org_no

    def str_to_int(n):
        n=n.replace(",","")
        n=n[1:]
        return int(n)
    
    data.loc[0,'Total Package Cost']=wes_to_indian_conversion(drug1_total_package_cost)
    data.loc[0,'Consulting Charges']=wes_to_indian_conversion(drug1_total_consulting_charges)
    data.loc[0,'OCT Charges']=wes_to_indian_conversion(drug1_total_oct_charges)
    data.loc[0,'Travel and Food Costs']=wes_to_indian_conversion(drug1_total_travel_food_cost)
    data.loc[0,'Total Opportunity Cost Lost']=wes_to_indian_conversion(drug1_total_opportunity_cost_lost)
    data.loc[0,'Total Cost/Patient']=wes_to_indian_conversion(drug1_total_cost_per_patient)

    data.loc[1,'Total Package Cost']=wes_to_indian_conversion(drug2_total_package_cost)
    data.loc[1,'Consulting Charges']=wes_to_indian_conversion(drug2_total_consulting_charges)
    data.loc[1,'OCT Charges']=wes_to_indian_conversion(drug2_total_oct_charges)
    data.loc[1,'Travel and Food Costs']=wes_to_indian_conversion(drug2_total_travel_food_cost)
    data.loc[1,'Total Opportunity Cost Lost']=wes_to_indian_conversion(drug2_total_opportunity_cost_lost)
    data.loc[1,'Total Cost/Patient']=wes_to_indian_conversion(drug2_total_cost_per_patient)

    data.loc[2,'Total Package Cost']=wes_to_indian_conversion(drug3_total_package_cost)
    data.loc[2,'Consulting Charges']=wes_to_indian_conversion(drug3_total_consulting_charges)
    data.loc[2,'OCT Charges']=wes_to_indian_conversion(drug3_total_oct_charges)
    data.loc[2,'Travel and Food Costs']=wes_to_indian_conversion(drug3_total_travel_food_cost)
    data.loc[2,'Total Opportunity Cost Lost']=wes_to_indian_conversion(drug3_total_opportunity_cost_lost)
    data.loc[2,'Total Cost/Patient']=wes_to_indian_conversion(drug3_total_cost_per_patient)

    data.loc[3,'Total Package Cost']=wes_to_indian_conversion(drug4_total_package_cost)
    data.loc[3,'Consulting Charges']=wes_to_indian_conversion(drug4_total_consulting_charges)
    data.loc[3,'OCT Charges']=wes_to_indian_conversion(drug4_total_oct_charges)
    data.loc[3,'Travel and Food Costs']=wes_to_indian_conversion(drug4_total_travel_food_cost)
    data.loc[3,'Total Opportunity Cost Lost']=wes_to_indian_conversion(drug4_total_opportunity_cost_lost)
    data.loc[3,'Total Cost/Patient']=wes_to_indian_conversion(drug4_total_cost_per_patient)

    data.loc[4,'Total Package Cost']=wes_to_indian_conversion(drug5_total_package_cost)
    data.loc[4,'Consulting Charges']=wes_to_indian_conversion(drug5_total_consulting_charges)
    data.loc[4,'OCT Charges']=wes_to_indian_conversion(drug5_total_oct_charges)
    data.loc[4,'Travel and Food Costs']=wes_to_indian_conversion(drug5_total_travel_food_cost)
    data.loc[4,'Total Opportunity Cost Lost']=wes_to_indian_conversion(drug5_total_opportunity_cost_lost)
    data.loc[4,'Total Cost/Patient']=wes_to_indian_conversion(drug5_total_cost_per_patient)
    # df_html = data.to_html(index=False)
    # st.write(df_html, unsafe_allow_html=True)
    # st.markdown('&nbsp;')

    
    import plotly.express as px

    graph_data = data.copy()
    graph_data['Total Package Cost'] = graph_data['Total Package Cost'].apply(str_to_int)
    graph_data['Consulting Charges'] = graph_data['Consulting Charges'].apply(str_to_int)
    graph_data['OCT Charges'] = graph_data['OCT Charges'].apply(str_to_int)
    graph_data['Travel and Food Costs'] = graph_data['Travel and Food Costs'].apply(str_to_int)
    graph_data['Total Opportunity Cost Lost'] = graph_data['Total Opportunity Cost Lost'].apply(str_to_int)
    graph_data['Total Cost/Patient'] = graph_data['Total Cost/Patient'].apply(str_to_int)

    melted_data = graph_data.melt(id_vars='Drugs', value_vars=['Total Package Cost', 'Consulting Charges', 'OCT Charges', 'Travel and Food Costs', 'Total Opportunity Cost Lost', 'Total Cost/Patient'])

    # Divide 'value' by 1000 to convert to 'k'
    melted_data['value'] = melted_data['value'] / 1000

    fig = px.bar(melted_data, x='Drugs', y='value', color='variable', barmode='group', labels={'value': 'Cost in Thousands'}, hover_data=melted_data.columns, hover_name='variable')

    # Update hovertemplate to reflect the change in 'value'
    fig.update_traces(hovertemplate='Drug: %{x}<br>Cost Type: %{hovertext}<br>Total Cost: ₹%{y:,.0f}k')
    fig.update_yaxes(tickprefix="₹",ticksuffix="k")
    fig.update_xaxes( title_text='')
    fig.update_layout(legend_title_text='',height=300)
    st.write(fig)

    html_data = data.to_html(index=False)
    html_data = html_data.replace('<table', '<table class="iopendata" style="table-layout: fixed;" ')
    html_data = html_data.replace('<thead>', '<thead><style>.iopendata th:first-child { width: 70px; } .iopendata td, .iopendata th { text-align: center; }</style>')
    st.markdown(html_data, unsafe_allow_html=True)  
    #st.dataframe(data,hide_index=True)
    store_data=data.copy()
    store_data.to_csv('Display_data.csv',index=False)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#..............................Total Package Cost...............................................
    custom_style = """
                    <style>
                        .custom-title {
                            font-size: 30px;
                            padding: 10px; /* Adjust padding as needed */
                            margin-left: 200px; /* Adjust margin as needed */
                            margin-top:25px;
                            font-weight: bold;
                        }
                    </style>
                    """

    st.markdown(f"{custom_style}<div class='custom-title'>Total Package Cost</div>", unsafe_allow_html=True)
    package_cost_dataset=data.copy()
    #.......................Drug-1 Values............................................................
    drug_1_package_cost=str_to_int(package_cost_dataset.loc[0,"Total Package Cost"])
    drug_1_direct_costs=str_to_int(package_cost_dataset.loc[0,'Consulting Charges'])+str_to_int(package_cost_dataset.loc[0,'OCT Charges'])
    drug_1_indirect_costs=str_to_int(package_cost_dataset.loc[0,'Travel and Food Costs'])+str_to_int(package_cost_dataset.loc[0,'Total Opportunity Cost Lost'])
    drug_1_total_cost=drug_1_package_cost+drug_1_direct_costs+drug_1_indirect_costs
    try:
        drug_1_package_cost_percent=round((drug_1_package_cost/drug_1_total_cost)*100)
        drug_1_direct_costs_percent=round((drug_1_direct_costs/drug_1_total_cost)*100)
        drug_1_indirect_costs_percent=round((drug_1_indirect_costs/drug_1_total_cost)*100)
    except ZeroDivisionError:
        drug_1_package_cost_percent=0
        drug_1_direct_costs_percent=0
        drug_1_indirect_costs_percent=0    

    
    #.......................Drug-2 Values............................................................
    drug_2_package_cost=str_to_int(package_cost_dataset.loc[1,"Total Package Cost"])
    drug_2_direct_costs=str_to_int(package_cost_dataset.loc[1,'Consulting Charges'])+str_to_int(package_cost_dataset.loc[1,'OCT Charges'])
    drug_2_indirect_costs=str_to_int(package_cost_dataset.loc[1,'Travel and Food Costs'])+str_to_int(package_cost_dataset.loc[1,'Total Opportunity Cost Lost'])
    drug_2_total_cost=drug_2_package_cost+drug_2_direct_costs+drug_2_indirect_costs
    try:
        drug_2_package_cost_percent=round((drug_2_package_cost/drug_2_total_cost)*100)
        drug_2_direct_costs_percent=round((drug_2_direct_costs/drug_2_total_cost)*100)
        drug_2_indirect_costs_percent=round((drug_2_indirect_costs/drug_2_total_cost)*100)
    except ZeroDivisionError:
        drug_2_package_cost_percent=0
        drug_2_direct_costs_percent=0
        drug_2_indirect_costs_percent=0

    
    #.......................Drug-3 Values............................................................
    drug_3_package_cost=str_to_int(package_cost_dataset.loc[2,"Total Package Cost"])
    drug_3_direct_costs=str_to_int(package_cost_dataset.loc[2,'Consulting Charges'])+str_to_int(package_cost_dataset.loc[2,'OCT Charges'])
    drug_3_indirect_costs=str_to_int(package_cost_dataset.loc[2,'Travel and Food Costs'])+str_to_int(package_cost_dataset.loc[2,'Total Opportunity Cost Lost'])

    drug_3_total_cost=drug_3_package_cost+drug_3_direct_costs+drug_3_indirect_costs

    try:
        drug_3_package_cost_percent=round((drug_3_package_cost/drug_3_total_cost)*100)
        drug_3_direct_costs_percent=round((drug_3_direct_costs/drug_3_total_cost)*100)
        drug_3_indirect_costs_percent=round((drug_3_indirect_costs/drug_3_total_cost)*100)
    except ZeroDivisionError:
        drug_3_package_cost_percent=0
        drug_3_direct_costs_percent=0
        drug_3_indirect_costs_percent=0
    
    #.......................Drug-4 Values............................................................
    drug_4_package_cost=str_to_int(package_cost_dataset.loc[3,"Total Package Cost"])
    drug_4_direct_costs=str_to_int(package_cost_dataset.loc[3,'Consulting Charges'])+str_to_int(package_cost_dataset.loc[3,'OCT Charges'])
    drug_4_indirect_costs=str_to_int(package_cost_dataset.loc[3,'Travel and Food Costs'])+str_to_int(package_cost_dataset.loc[3,'Total Opportunity Cost Lost'])

    drug_4_total_cost=drug_4_package_cost+drug_4_direct_costs+drug_4_indirect_costs

    try:
        drug_4_package_cost_percent=round((drug_4_package_cost/drug_4_total_cost)*100)
        drug_4_direct_costs_percent=round((drug_4_direct_costs/drug_4_total_cost)*100)
        drug_4_indirect_costs_percent=round((drug_4_indirect_costs/drug_4_total_cost)*100)
    except ZeroDivisionError:
        drug_4_package_cost_percent=0
        drug_4_direct_costs_percent=0
        drug_4_indirect_costs_percent=0
    
    
    #.......................Drug-5 Values............................................................
    drug_5_package_cost=str_to_int(package_cost_dataset.loc[4,"Total Package Cost"])
    drug_5_direct_costs=str_to_int(package_cost_dataset.loc[4,'Consulting Charges'])+str_to_int(package_cost_dataset.loc[4,'OCT Charges'])
    drug_5_indirect_costs=str_to_int(package_cost_dataset.loc[4,'Travel and Food Costs'])+str_to_int(package_cost_dataset.loc[4,'Total Opportunity Cost Lost'])

    drug_5_total_cost=drug_5_package_cost+drug_5_direct_costs+drug_5_indirect_costs

    try:
        drug_5_package_cost_percent=round((drug_5_package_cost/drug_5_total_cost)*100)
        drug_5_direct_costs_percent=round((drug_5_direct_costs/drug_5_total_cost)*100)
        drug_5_indirect_costs_percent=round((drug_5_indirect_costs/drug_5_total_cost)*100)
    except ZeroDivisionError:
        drug_5_package_cost_percent=0
        drug_5_direct_costs_percent=0
        drug_5_indirect_costs_percent=0
  
  
    df1 = pd.DataFrame({"Cost Type": ["Package Costs", "Direct Costs", "Indirect Costs"], "Values": [drug_1_package_cost_percent, drug_1_direct_costs_percent, drug_1_indirect_costs_percent]})
    df2 = pd.DataFrame({"Cost Type": ["Package Costs", "Direct Costs", "Indirect Costs"], "Values": [drug_2_package_cost_percent, drug_2_direct_costs_percent, drug_2_indirect_costs_percent]})
    df3 = pd.DataFrame({"Cost Type": ["Package Costs", "Direct Costs", "Indirect Costs"], "Values": [drug_3_package_cost_percent, drug_3_direct_costs_percent, drug_3_indirect_costs_percent]})
    df4 = pd.DataFrame({"Cost Type": ["Package Costs", "Direct Costs", "Indirect Costs"], "Values": [drug_4_package_cost_percent, drug_4_direct_costs_percent, drug_4_indirect_costs_percent]})
    df5 = pd.DataFrame({"Cost Type": ["Package Costs", "Direct Costs", "Indirect Costs"], "Values": [drug_5_package_cost_percent, drug_5_direct_costs_percent, drug_5_indirect_costs_percent]})

    # Create a pie chart for each drug
    fig1 = px.pie(df1, values='Values', names='Cost Type')
    fig2 = px.pie(df2, values='Values', names='Cost Type')
    fig3 = px.pie(df3, values='Values', names='Cost Type')
    fig4 = px.pie(df4, values='Values', names='Cost Type')
    fig5 = px.pie(df5, values='Values', names='Cost Type')

    # Create subplots
    fig = sp.make_subplots(rows=1, cols=5, subplot_titles=('Drug 1', 'Drug 2', 'Drug 3', 'Drug 4', 'Drug 5'), specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}]])

    # Add pie charts to subplots
    fig.add_trace(fig1['data'][0], row=1, col=1)
    fig.add_trace(fig2['data'][0], row=1, col=2)
    fig.add_trace(fig3['data'][0], row=1, col=3)
    fig.add_trace(fig4['data'][0], row=1, col=4)
    fig.add_trace(fig5['data'][0], row=1, col=5)

    # Update hovertemplate to round off percentages
    # fig.update_traces()

    fig.update_layout(height=330,width=720)

    # Display the figure with streamlit
    st.plotly_chart(fig)


    st.markdown("""
                <style>
                div.user-select-none.svg-container{
                    height: 230px !important;
                }
                </style>
                """, unsafe_allow_html=True)
    

    package_cost_data=pd.DataFrame({f"Total Package Costs @ Year {time_horizon}":package_cost_dataset['Drugs'].tolist(),'Total Package Cost':package_cost_dataset['Total Package Cost'].tolist(),'Direct Costs':[wes_to_indian_conversion(drug_1_direct_costs),wes_to_indian_conversion(drug_2_direct_costs),wes_to_indian_conversion(drug_3_direct_costs),wes_to_indian_conversion(drug_4_direct_costs),wes_to_indian_conversion(drug_5_direct_costs)],'Indirect Costs':[wes_to_indian_conversion(drug_1_indirect_costs),wes_to_indian_conversion(drug_2_indirect_costs),wes_to_indian_conversion(drug_3_indirect_costs),wes_to_indian_conversion(drug_4_indirect_costs),wes_to_indian_conversion(drug_5_indirect_costs)],'Total Costs':package_cost_dataset['Total Cost/Patient'].tolist()})

    st.dataframe(package_cost_data,hide_index=True,width=800)

    cost_type_display_data=pd.DataFrame({'Type of Cost':['Direct Cost','Indirect Cost','Total Package Costs'],'Cost Components':['Consulting Cost + OCT Charges','Travel and Food Costs + Lost Opportunity Cost of Patient and Caregiver','Injection + Procedure Costs']})
    cost_type_display_data = cost_type_display_data.to_html(index=False)
    cost_type_display_data = cost_type_display_data.replace('<table', '<table class="cost_type_display_data" style="table-layout: fixed;" ')
    cost_type_display_data = cost_type_display_data.replace('<thead>', '<thead><style>.cost_type_display_data th:first-child { width: 200px; } .cost_type_display_data th:nth-child(2) { width: 530px; } .cost_type_display_data td, .cost_type_display_data th { text-align: center; font-size: 13px;}</style>')
    st.markdown(cost_type_display_data, unsafe_allow_html=True)
  
   
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#....................................Cumulative Comparison of Costs....................................
    custom_style = """
                        <style>
                            .cumulative_comparison_of_costs_title{
                                font-size: 30px;
                                padding: 10px; /* Adjust padding as needed */
                                margin-left: 0px; /* Adjust margin as needed */
                                margin-top:25px;
                                font-weight: bold;
                            }
                        </style>
                        """

    st.markdown(f"{custom_style}<div class='cumulative_comparison_of_costs_title'>Cumulative Comparison of Costs over the years </div>", unsafe_allow_html=True)
    st.write("Select the Drugs to be compared:")
    drop_col1,drop_col2=st.columns(2)
    with drop_col1:
        selected_drug_1=st.selectbox("First Drug",['Drug 1','Drug 2','Drug 3','Drug 4','Drug 5'])
    with drop_col2:
        selected_drug_2=st.selectbox("Second Drug",['Drug 2','Drug 1','Drug 3','Drug 4','Drug 5'])

    
    col1,col2=st.columns(2)
    with col1:
        if selected_drug_1=="Drug 1":
            if time_horizon=="1":
                
                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[450000,40500,43200,0,0,0,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹43,200","₹40,500","₹4,50,000"],"2":["₹0","₹0","₹0"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})
                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            
            elif time_horizon=="2":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹43,200","₹40,500","₹4,50,000"],"2":["₹64,800","₹60,750","₹6,75,000"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})
                
                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[450000,40500,43200,675000,60750,64800,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
            
            elif time_horizon=="3":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹43,200","₹40,500","₹4,50,000"],"2":["₹64,800","₹60,750","₹6,75,000"],"3":["₹86,400","₹81,000","₹9,00,000"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[450000,40500,43200,675000,60750,64800,900000,81000,86400,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
            
            elif time_horizon=="4":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹43,200","₹40,500","₹4,50,000"],"2":["₹64,800","₹60,750","₹6,75,000"],"3":["₹86,400","₹81,000","₹9,00,000"],"4":["₹1,08,000","₹1,01,250","₹11,25,000"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[450000,40500,43200,675000,60750,64800,900000,81000,86400,1125000,101250,108000,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
                    
            elif time_horizon=="5":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹43,200","₹40,500","₹4,50,000"],"2":["₹64,800","₹60,750","₹6,75,000"],"3":["₹86,400","₹81,000","₹9,00,000"],"4":["₹1,08,000","₹1,01,250","₹11,25,000"],"5":["₹1,29,000","₹1,21,500","₹13,50,000"]})
                
                chart_df=pd.DataFrame({'year':[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[450000,40500,43200,675000,60750,64800,900000,81000,86400,1125000,101250,108000,1350000,121500,129000]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

        elif selected_drug_1=="Drug 2":
            if time_horizon=="1":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹4,80,000"],"2":["₹0","₹0","₹0"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[480000,54000,57600,0,0,0,0,0,0,0,0,0,0,0,0]})
 
                chart_df['cost'] = chart_df['cost'] / 1000 
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="2":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹4,80,000"],"2":["₹1,00,800","₹94,500","₹8,40,000"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})
                
                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[480000,54000,57600,840000,94500,100800,0,0,0,0,0,0,0,0,0]})  
                
                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="3":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹4,80,000"],"2":["₹1,00,800","₹94,500","₹8,40,000"],"3":["₹1,44,000","₹1,35,000","₹12,00,000"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})  

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[480000,54000,57600,840000,94500,100800,1200000,135000,144000,0,0,0,0,0,0]})   
 
                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})   

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="4":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹4,80,000"],"2":["₹1,00,800","₹94,500","₹8,40,000"],"3":["₹1,44,000","₹1,35,000","₹12,00,000"],"4":["₹1,87,200","₹1,75,500","₹15,60,000"],"5":["₹0","₹0","₹0"]})  

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[480000,54000,57600,840000,94500,100800,1200000,135000,144000,1560000,175500,187200,0,0,0]})   

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)    
            
            
            elif time_horizon=="5":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹4,80,000"],"2":["₹1,00,800","₹94,500","₹8,40,000"],"3":["₹1,44,000","₹1,35,000","₹12,00,000"],"4":["₹1,87,200","₹1,75,500","₹15,60,000"],"5":["₹2,30,400","₹2,16,000","₹19,20,000"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[480000,54000,57600,840000,94500,100800,1200000,135000,144000,1560000,175500,187200,1920000,216000,230400]}) 

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False}) 

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

        elif selected_drug_1=="Drug 3":
            if time_horizon=="1":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹3,20,000"],"2":["₹0","₹0","₹0"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[320000,54000,57600,0,0,0,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="2":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹3,20,000"],"2":["₹86,400","₹81,000","₹4,80,000"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]}) 

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[320000,54000,57600,480000,81000,86400,0,0,0,0,0,0,0,0,0]}) 

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="3":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹3,20,000"],"2":["₹86,400","₹81,000","₹4,80,000"],"3":["₹1,15,200","₹1,08,000","₹6,40,000"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})   

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[320000,54000,57600,480000,81000,86400,640000,108000,115200,0,0,0,0,0,0]}) 

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="4":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹3,20,000"],"2":["₹86,400","₹81,000","₹4,80,000"],"3":["₹1,15,200","₹1,08,000","₹6,40,000"],"4":["₹1,44,000","₹1,35,000","₹8,00,000"],"5":["₹0","₹0","₹0"]})
                
                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[320000,54000,57600,480000,81000,86400,640000,108000,115200,800000,135000,144000,0,0,0]}) 

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
            
            elif time_horizon=="5":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹3,20,000"],"2":["₹86,400","₹81,000","₹4,80,000"],"3":["₹1,15,200","₹1,08,000","₹6,40,000"],"4":["₹1,44,000","₹1,35,000","₹8,00,000"],"5":["₹1,72,000","₹1,62,000","₹9,60,000"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[320000,54000,57600,480000,81000,86400,640000,108000,115200,800000,135000,144000,960000,162000,172000]}) 

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
            
                
        elif selected_drug_1=="Drug 4":
            if time_horizon=="1":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,96,000"],"2":["₹0","₹0","₹0"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[396000,81000,86400,0,0,0,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="2":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,96,000"],"2":["₹1,72,800","₹1,62,000","₹7,92,000"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[396000,81000,86400,792000,162000,172800,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="3":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,96,000"],"2":["₹1,72,800","₹1,62,000","₹7,92,000"],"3":["₹2,59,200","₹2,43,000","₹11,88,000"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})   

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[396000,81000,86400,792000,162000,172800,1188000,243000,259200,0,0,0,0,0,0]}) 

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="4":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,96,000"],"2":["₹1,72,800","₹1,62,000","₹7,92,000"],"3":["₹2,59,200","₹2,43,000","₹11,88,000"],"4":["₹3,45,600","₹3,24,000","₹15,84,000"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[396000,81000,86400,792000,162000,172800,1188000,243000,259200,1584000,324000,345600,0,0,0]}) 

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
            
            elif time_horizon=="5":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,96,000"],"2":["₹1,72,800","₹1,62,000","₹7,92,000"],"3":["₹2,59,200","₹2,43,000","₹11,88,000"],"4":["₹3,45,600","₹3,24,000","₹15,84,000"],"5":["₹4,32,000","₹4,05,000","₹19,80,000"]})


                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[396000,81000,86400,792000,162000,172800,1188000,243000,259200,1584000,324000,345600,1980000,405000,432000]}) 

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
            
        elif selected_drug_1=="Drug 5":
            if time_horizon=="1":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,00,000"],"2":["₹0","₹0","₹0"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[300000,81000,86400,0,0,0,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="2":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,00,000"],"2":["₹1,72,800","₹1,62,000","₹6,00,000"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[300000,81000,86400,600000,162000,172800,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="3":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,00,000"],"2":["₹1,72,800","₹1,62,000","₹6,00,000"],"3":["₹2,59,200","₹2,43,000","₹9,00,000"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[300000,81000,86400,600000,162000,172800,900000,243000,259200,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
                

            elif time_horizon=="4":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,00,000"],"2":["₹1,72,800","₹1,62,000","₹6,00,000"],"3":["₹2,59,200","₹2,43,000","₹9,00,000"],"4":["₹3,45,600","₹3,24,000","₹12,00,000"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[300000,81000,86400,600000,162000,172800,900000,243000,259200,1200000,324000,345600,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
            
            elif time_horizon=="5":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,00,000"],"2":["₹1,72,800","₹1,62,000","₹6,00,000"],"3":["₹2,59,200","₹2,43,000","₹9,00,000"],"4":["₹3,45,600","₹3,24,000","₹12,00,000"],"5":["₹4,32,000","₹4,05,000","₹15,00,000"]})   
      
                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect','Total_Package_Cost','Direct','Indirect'],'cost':[300000,81000,86400,600000,162000,172800,900000,243000,259200,1200000,324000,345600,1500000,405000,432000]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,showlegend=False)
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(tickformat=',',ticksuffix="k",tickprefix="₹")
                st.plotly_chart(fig,config={'displayModeBar': False})

                
                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
                
    
    with col2:
        if selected_drug_2=="Drug 1":
            if time_horizon=="1":

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[450000,40500,43200,0,0,0,0,0,0,0,0,0,0,0,0]})
            
                chart_df['cost'] = chart_df['cost'] / 1000
                
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})
                
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹43,200","₹40,500","₹4,50,000"],"2":["₹0","₹0","₹0"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})
                
                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
            
            elif time_horizon=="2":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹43,200","₹40,500","₹4,50,000"],"2":["₹64,800","₹60,750","₹6,75,000"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})
                
                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[450000,40500,43200,675000,60750,64800,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000
                
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
            
            elif time_horizon=="3":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹43,200","₹40,500","₹4,50,000"],"2":["₹64,800","₹60,750","₹6,75,000"],"3":["₹86,400","₹81,000","₹9,00,000"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[450000,40500,43200,675000,60750,64800,900000,81000,86400,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
            
            elif time_horizon=="4":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹43,200","₹40,500","₹4,50,000"],"2":["₹64,800","₹60,750","₹6,75,000"],"3":["₹86,400","₹81,000","₹9,00,000"],"4":["₹1,08,000","₹1,01,250","₹11,25,000"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[450000,40500,43200,675000,60750,64800,900000,81000,86400,1125000,101250,108000,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)
                    
            elif time_horizon=="5":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹43,200","₹40,500","₹4,50,000"],"2":["₹64,800","₹60,750","₹6,75,000"],"3":["₹86,400","₹81,000","₹9,00,000"],"4":["₹1,08,000","₹1,01,250","₹11,25,000"],"5":["₹1,29,000","₹1,21,500","₹13,50,000"]})

                
                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[450000,40500,43200,675000,60750,64800,900000,81000,86400,1125000,101250,108000,1350000,121500,129000]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

        elif selected_drug_2=="Drug 2":
            if time_horizon=="1":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹4,80,000"],"2":["₹0","₹0","₹0"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[480000,54000,57600,0,0,0,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="2":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹4,80,000"],"2":["₹1,00,800","₹94,500","₹8,40,000"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})
                
                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[480000,54000,57600,840000,94500,100800,0,0,0,0,0,0,0,0,0]})  

                chart_df['cost'] = chart_df['cost'] / 1000
                
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="3":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹4,80,000"],"2":["₹1,00,800","₹94,500","₹8,40,000"],"3":["₹1,44,000","₹1,35,000","₹12,00,000"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})  

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[480000,54000,57600,840000,94500,100800,1200000,135000,144000,0,0,0,0,0,0]})  

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})    

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)

            elif time_horizon=="4":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹4,80,000"],"2":["₹1,00,800","₹94,500","₹8,40,000"],"3":["₹1,44,000","₹1,35,000","₹12,00,000"],"4":["₹1,87,200","₹1,75,500","₹15,60,000"],"5":["₹0","₹0","₹0"]})  

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[480000,54000,57600,840000,94500,100800,1200000,135000,144000,1560000,175500,187200,0,0,0]})   

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)    
            
            
            elif time_horizon=="5":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹4,80,000"],"2":["₹1,00,800","₹94,500","₹8,40,000"],"3":["₹1,44,000","₹1,35,000","₹12,00,000"],"4":["₹1,87,200","₹1,75,500","₹15,60,000"],"5":["₹2,30,400","₹2,16,000","₹19,20,000"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[480000,54000,57600,840000,94500,100800,1200000,135000,144000,1560000,175500,187200,1920000,216000,230400]})  

                
                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True) 

        elif selected_drug_2=="Drug 3":
            if time_horizon=="1":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹3,20,000"],"2":["₹0","₹0","₹0"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[320000,54000,57600,0,0,0,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  

            elif time_horizon=="2":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹3,20,000"],"2":["₹86,400","₹81,000","₹4,80,000"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]}) 

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[320000,54000,57600,480000,81000,86400,0,0,0,0,0,0,0,0,0]}) 

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  

            elif time_horizon=="3":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹3,20,000"],"2":["₹86,400","₹81,000","₹4,80,000"],"3":["₹1,15,200","₹1,08,000","₹6,40,000"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})   

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[320000,54000,57600,480000,81000,86400,640000,108000,115200,0,0,0,0,0,0]}) 

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  

            elif time_horizon=="4":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹3,20,000"],"2":["₹86,400","₹81,000","₹4,80,000"],"3":["₹1,15,200","₹1,08,000","₹6,40,000"],"4":["₹1,44,000","₹1,35,000","₹8,00,000"],"5":["₹0","₹0","₹0"]})
                
                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[320000,54000,57600,480000,81000,86400,640000,108000,115200,800000,135000,144000,0,0,0]}) 

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  
            
            elif time_horizon=="5":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹57,600","₹54,000","₹3,20,000"],"2":["₹86,400","₹81,000","₹4,80,000"],"3":["₹1,15,200","₹1,08,000","₹6,40,000"],"4":["₹1,44,000","₹1,35,000","₹8,00,000"],"5":["₹1,72,000","₹1,62,000","₹9,60,000"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[320000,54000,57600,480000,81000,86400,640000,108000,115200,800000,135000,144000,960000,162000,172000]}) 

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  
            
                
        elif selected_drug_2=="Drug 4":
            if time_horizon=="1":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,96,000"],"2":["₹0","₹0","₹0"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[396000,81000,86400,0,0,0,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  

            elif time_horizon=="2":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,96,000"],"2":["₹1,72,800","₹1,62,000","₹7,92,000"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[396000,81000,86400,792000,162000,172800,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  

            elif time_horizon=="3":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,96,000"],"2":["₹1,72,800","₹1,62,000","₹7,92,000"],"3":["₹2,59,200","₹2,43,000","₹11,88,000"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})   

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[396000,81000,86400,792000,162000,172800,1188000,243000,259200,0,0,0,0,0,0]}) 

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  

            elif time_horizon=="4":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,96,000"],"2":["₹1,72,800","₹1,62,000","₹7,92,000"],"3":["₹2,59,200","₹2,43,000","₹11,88,000"],"4":["₹3,45,600","₹3,24,000","₹15,84,000"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[396000,81000,86400,792000,162000,172800,1188000,243000,259200,1584000,324000,345600,0,0,0]}) 

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True) 
            
            elif time_horizon=="5":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,96,000"],"2":["₹1,72,800","₹1,62,000","₹7,92,000"],"3":["₹2,59,200","₹2,43,000","₹11,88,000"],"4":["₹3,45,600","₹3,24,000","₹15,84,000"],"5":["₹4,32,000","₹4,05,000","₹19,80,000"]})


                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[396000,81000,86400,792000,162000,172800,1188000,243000,259200,1584000,324000,345600,1980000,405000,432000]}) 

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  
            
        elif selected_drug_2=="Drug 5":
            if time_horizon=="1":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,00,000"],"2":["₹0","₹0","₹0"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[300000,81000,86400,0,0,0,0,0,0,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  

            elif time_horizon=="2":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,00,000"],"2":["₹1,72,800","₹1,62,000","₹6,00,000"],"3":["₹0","₹0","₹0"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[300000,81000,86400,600000,162000,172800,0,0,0,0,0,0,0,0,0]})

                
                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  

            elif time_horizon=="3":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,00,000"],"2":["₹1,72,800","₹1,62,000","₹6,00,000"],"3":["₹2,59,200","₹2,43,000","₹9,00,000"],"4":["₹0","₹0","₹0"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[300000,81000,86400,600000,162000,172800,900000,243000,259200,0,0,0,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True) 
                

            elif time_horizon=="4":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,00,000"],"2":["₹1,72,800","₹1,62,000","₹6,00,000"],"3":["₹2,59,200","₹2,43,000","₹9,00,000"],"4":["₹3,45,600","₹3,24,000","₹12,00,000"],"5":["₹0","₹0","₹0"]})

                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[300000,81000,86400,600000,162000,172800,900000,243000,259200,1200000,324000,345600,0,0,0]})

                chart_df['cost'] = chart_df['cost'] / 1000

                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h"
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  
            
            elif time_horizon=="5":
                display_df=pd.DataFrame({"Cost Type":['Indirect Costs','Direct Costs','Total Package Cost'],'1':["₹86,400","₹81,000","₹3,00,000"],"2":["₹1,72,800","₹1,62,000","₹6,00,000"],"3":["₹2,59,200","₹2,43,000","₹9,00,000"],"4":["₹3,45,600","₹3,24,000","₹12,00,000"],"5":["₹4,32,000","₹4,05,000","₹15,00,000"]})   
      
                chart_df=pd.DataFrame({'year':["1","1","1","2","2","2","3","3","3","4","4","4","5","5","5"],'cost_type':['Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs','Total Package Cost','Direct Costs','Indirect Costs'],'cost':[300000,81000,86400,600000,162000,172800,900000,243000,259200,1200000,324000,345600,1500000,405000,432000]})

                chart_df['cost'] = chart_df['cost'] / 1000
                
                fig = px.bar(chart_df, x="year", y="cost", color="cost_type")
                fig.update_layout(height=325,width=340,  legend=dict(
                                                                        yanchor="bottom",
                                                                        y=1.02,
                                                                        xanchor="right",
                                                                        x=1,
                                                                        orientation="h",
                                                                    ))
                fig.update_xaxes(showticklabels=False, title_text='')
                fig.update_yaxes(title_text='',tickformat=',',ticksuffix="k",tickprefix="₹")
                
                st.plotly_chart(fig,config={'displayModeBar': False})

                display_df = display_df.to_html(index=False)
                display_df = display_df.replace('<table', '<table class="table4" style="table-layout: fixed; width: 100%;" ')
                display_df = display_df.replace('<thead>', '<thead><style>.table4 th:first-child { width: 70px; } .table4 td, .table4 th { text-align: center;vertical-align: middle; font-size: 0.73em; width: auto; }</style>')
                st.markdown(display_df, unsafe_allow_html=True)  


if __name__ == "__main__":
    main()
