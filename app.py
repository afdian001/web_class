import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import datetime
import pytz

class view:
    def __init__(self):
        st.title('Clasico')
        st.header('web for calss')


        self.option_menu()

        # side bar
    def option_menu(self,):
        with st.sidebar:
            selected = option_menu("Menu", ["Home", 'Jadwal','Tugas','Catatan'], 
            icons=['house', 'calendar','pencil','newspaper'], menu_icon="cast", default_index=0)
        if (selected == "Home"):
            self.home()

        elif (selected == "Jadwal"):
            self.jadwal()

        elif (selected == "Tugas"):
            self.tugas()

        elif (selected == "Catatan"):
            self.catatan()

    # home
    def home(self):
        st.header('Home',divider='rainbow')
        cont = st.container()
        colom_1,colom_3 = cont.columns([0.7, 0.3])
        text_home = open(r'asset\text\home.txt',mode='r').read()

        with colom_1:
            st.markdown(text_home)

        with colom_3:
            st.image('asset\image\home_image.jpeg')




    # jadwal
    def jadwal(self,):
        st.header('Jadwal',divider='rainbow')
        cont = st.container()
        colom_1,colom_3 = cont.columns([0.3, 0.7])

        data = pd.read_excel('asset\jadwal\jadwal_12_MIPA_1.xlsx',sheet_name='Sheet1').loc[:,'START TIME':'SABTU']
        self.jadwal = pd.DataFrame(data).fillna('')
        self.jadwal.index = self.jadwal.index +1

        with colom_1:
            self.today()
            pass

        with colom_3:
            tabcon = st.container()
            tabcon.table(self.jadwal)

        # tugas
    def tugas(self,):
        st.title('Tugas')

        # Catatan
    def catatan(self,):
        st.title('Catatan')

   

    def today(self):
        self.hari = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
        jam = self.hari.hour
        nom_hari = self.hari.weekday()
        st.subheader('Jadwal Sekarang')
        jad = self.jadwal

        senin = jad['SENIN']
        selasa = jad['SELASA']
        rabu = jad['RABU']
        kamis = jad['KAMIS']
        jumat = jad['JUMAT']
        sabtu = jad['SABTU']
        

        match nom_hari:
            case 0:
                if (jam <= 14):
                    st.table(senin)
                if (jam >= 14):
                    st.table(selasa)

            case 1:
                if (jam <= 14):
                    st.table(selasa)
                if (jam >= 14):
                    st.table(rabu)

            case 2:
                if (jam <= 14):
                    st.table(rabu)
                if (jam >= 14):
                    st.table(kamis)

            case 3:
                if (jam <= 14):
                    st.table(kamis)
                if (jam >= 14):
                    st.table(jumat)

            case 4:
                if (jam <= 14):
                    st.table(jumat)
                if (jam >= 14):
                    st.table(sabtu)

            case 5:
                if (jam <= 14):
                    st.table(sabtu)
                if (jam >= 14):
                    st.table(senin)




if __name__ == '__main__':
    view()
    