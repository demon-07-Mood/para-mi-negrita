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
        st.warning("⚠️ Sube tu archivo MP3 de Paulo Londra al repositorio y llámalo 'cancion.mp3'")

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
        # Cambia "cuysita" por la contraseña que elijas
        if palabra_clave.lower() == "cuysita": 
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Palabra clave incorrecta. Intenta de nuevo.")

# 2. SISTEMA PRINCIPAL
else:
    # Reproducir música continua de fondo
    cargar_musica("cancion.mp3")

    # A. MENÚ PRINCIPAL
    if st.session_state.pagina_actual == 'menu':
        st.title("🕰️ Bóveda de Recuerdos")
        st.write("Bienvenida. Elige a qué momento quieres viajar:")
        
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
            
            # Puedes usar st.image("foto_pasado.jpg") o st.video("video_pasado.mp4")
            st.info("Coloca aquí tu foto/video del pasado")
            
            st.write("""
            Escribe aquí el texto recordando cómo se conocieron y los bonitos 
            momentos de cuando empezaron a decirse mono y cuysita.
            """)

        # PRESENTE
        elif st.session_state.pagina_actual == 'presente':
            st.title("✨ Nuestro Presente")
            
            st.info("Coloca aquí tu foto/video del presente")
            
            st.write("""
            Escribe aquí tu mensaje sincero pidiendo disculpas por haberte 
            distanciado y reconociendo lo idiota que fuiste al dejar enfriar la amistad.
            """)

        # FUTURO
        elif st.session_state.pagina_actual == 'futuro':
            st.title("✨ Nuestro Futuro")
            
            st.info("Coloca aquí una foto/video sobre el futuro")
            
            st.write("""
            Escribe aquí lo que deseas para la amistad de aquí en adelante, 
            dejando en claro que no quieres dejarla morir.
            """)
