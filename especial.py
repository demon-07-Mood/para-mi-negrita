import streamlit as st
import base64

# Configuración inicial de la página
st.set_page_config(page_title="Bóveda de Recuerdos", page_icon="⏳", layout="centered")

# --- FUNCIONES AUXILIARES ---

def cargar_musica(ruta_archivo):
    # Oculta el reproductor y hace que la música suene en bucle
    try:
        with open(ruta_archivo, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # HTML de audio con autoplay y loop oculto
            audio_html = f'''
                <audio autoplay loop style="display:none;">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            '''
            st.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ No se encontró el archivo de audio 'cancion.mp3'")

# Inicializar variables de sesión
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'pagina_actual' not in st.session_state:
    st.session_state.pagina_actual = 'menu'

# --- INTERFAZ ---

# 1. SISTEMA DE LOGIN
if not st.session_state.logged_in:
    st.title("🔐 Acceso Secreto")
    st.write("Ingresa la palabra clave para entrar a la bóveda:")
    
    palabra_clave = st.text_input("Palabra clave", type="password")
    
    if st.button("Entrar"):
        # Puedes cambiar "cuysita" por la palabra clave que desees
        if palabra_clave.lower() == "cuysita": 
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Palabra clave incorrecta. Intenta de nuevo.")

# 2. SISTEMA PRINCIPAL
else:
    # Reproducir música de fondo (cancion.mp3)
    cargar_musica("cancion.mp3")

    # A. MENÚ PRINCIPAL
    if st.session_state.pagina_actual == 'menu':
        st.title("🕰️ Bóveda de Recuerdos")
        st.write("Bienvenida Cuysita🫶. Elige a qué momento quieras recordar🥹:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("⏪ Pasado"):
                st.session_state.pagina_actual = "pasado"
                st.rerun()
        with col2:
            if st.button("▶️ Presente"):
                st.session_state.pagina_actual = "presente"
                st.rerun()
        with col3:
            if st.button("⏩ Futuro"):
                st.session_state.pagina_actual = "futuro"
                st.rerun()

    # B. PÁGINAS DE CONTENIDO (Pasado, Presente, Futuro)
    else:
        if st.button("🔙 Regresar a la Bóveda"):
            st.session_state.pagina_actual = 'menu'
            st.rerun()
            
        st.divider()

        # PASADO
        if st.session_state.pagina_actual == 'pasado':
            st.title("✨ Nuestro Pasado")
            
            # Carga de tu video subido
            try:
                st.video("video_pasado.mp4")
            except Exception:
                st.warning("No se pudo cargar 'video_pasado.mp4'")
            
            st.write("""
            El mejor recuerdo q tengo, unos de los principales diria yo, 
            gracias por darme ese lindo momento donde te comiste tdo😿,
            pero aun asi me qedo con lo lindo q la pasamos juntos mi Cuysita 
            TE LO AGRADEZO TE TODO CORAZON🫶
            """)

        # PRESENTE
        elif st.session_state.pagina_actual == 'presente':
            st.title("✨ Nuestro Presente")
            
            # Carga de tu foto de presente subida
            try:
                st.image("foto_presente.jpg", use_container_width=True)
            except Exception:
                st.warning("No se pudo cargar 'foto_presente.jpg'")
            
            st.write("""
            Pasar de bellos momentos a un presente solitario,
            donde nos bucamos pero no nos encontramos, donde
            pediste mi ayude y no estuve ahi para dartelo, no 
            sabes lo mucho q me arrepiento no haberte valorado
            ESPERO ME PERDONES Y PODRAMOS VOLVER A RETOMAR ESA
            LINDA AMISTAD Q TENIAMOS MI CUYSITA NEGRITA🥺🫶
            """)

        # FUTURO
        elif st.session_state.pagina_actual == 'futuro':
            st.title("✨ Nuestro Futuro")
            
            # Carga de tu foto de futuro subida (.png)
            try:
                st.image("foto_futuro.png", use_container_width=True)
            except Exception:
                st.warning("No se pudo cargar 'foto_futuro.png'")
            
            st.write("""
            Y BUENO SOLO ESPERO UN FUTURO COMO EL DE ESTA IMAGEN
            AUNK LA VEAS GRACIOSAA, TU MI CUYSITA, Y YO TU MONO
            JSJSJS DANDONOS UN ABRAZO DSP DE AVER RECUPERADO 
            NUESTRA LINDA AMISTAD MI MEJOR AMIGA🥺🫶
            """)
