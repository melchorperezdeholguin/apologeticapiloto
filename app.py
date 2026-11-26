import streamlit as st

# ======================
# Configuración de la página
# ======================
st.set_page_config(
    page_title="🕊️ Botiquín Espiritual",
    page_icon="🕊️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ======================
# Estilos personalizados (CSS)
# ======================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Poppins:wght@400;600&display=swap');

    :root {
        --primary: #4a7c59;
        --primary-dark: #355b43;
        --primary-light: #e8f0ea;
        --accent: #bfa64c;
        --bg-body: #f7f9f8;
        --card-bg: #ffffff;
        --text-main: #2d3748;
        --text-muted: #718096;
        --border: #e2e8f0;
        --shadow: 0 10px 40px -10px rgba(0, 0, 0, 0.08);
        --radius: 16px;
    }

    .main {
        padding: 2rem 1rem;
        background-color: var(--bg-body);
    }

    .block-container {
        padding-top: 2rem;
        max-width: 720px;
    }

    .app-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 0.25rem;
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .app-subtitle {
        text-align: center;
        color: var(--text-muted);
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
        font-family: 'Lora', serif;
    }

    .label-text {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 0.95rem;
        color: var(--text-main);
        margin-bottom: 0.5rem;
        display: block;
    }

    .stSelectbox > div > div {
        background-color: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        font-family: 'Poppins', sans-serif;
    }

    .stButton > button {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        border-radius: 10px;
        padding: 0.6rem 1rem;
        transition: all 0.2s ease;
        border: none;
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
        color: white;
    }

    .stButton > button[kind="primary"]:hover {
        filter: brightness(1.1);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(74, 124, 89, 0.3);
    }

    .stButton > button:not([kind="primary"]) {
        background-color: var(--card-bg);
        color: var(--text-main);
        border: 1px solid var(--border);
    }

    .stButton > button:not([kind="primary"]):hover {
        background-color: var(--primary-light);
        border-color: var(--primary);
    }

    .card {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-left: 5px solid var(--primary);
        border-radius: var(--radius);
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: var(--shadow);
        animation: fadeInUp 0.5s ease-out;
        position: relative;
        overflow: hidden;
    }

    .card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--primary), var(--accent));
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(15px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .emotion-label {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 1.05rem;
        color: var(--primary-dark);
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .ref {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 1.15rem;
        color: var(--primary);
        margin-bottom: 0.75rem;
        letter-spacing: 0.3px;
    }

    .verse-text {
        font-family: 'Lora', serif;
        font-style: italic;
        color: var(--text-main);
        font-size: 1.2rem;
        line-height: 1.7;
        margin: 1rem 0;
        border-left: 3px solid var(--accent);
        padding-left: 1rem;
    }

    .oracion {
        margin-top: 1.25rem;
        padding: 1.1rem 1.25rem;
        background: var(--primary-light);
        border-left: 4px solid var(--primary);
        border-radius: 10px;
        font-size: 0.98rem;
        color: var(--text-muted);
        line-height: 1.6;
    }

    .oracion strong {
        color: var(--primary-dark);
        font-family: 'Poppins', sans-serif;
    }

    .encouragement {
        margin-top: 1.25rem;
        padding: 1rem;
        background: #fbfdfb;
        border: 1px dashed var(--border);
        border-radius: 10px;
        text-align: center;
        font-family: 'Lora', serif;
        font-style: italic;
        color: var(--text-muted);
        font-size: 0.95rem;
    }

    .welcome-box {
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f4 100%);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 2.5rem 2rem;
        text-align: center;
        margin-top: 2rem;
        box-shadow: var(--shadow);
        animation: fadeInUp 0.6s ease-out;
    }

    .welcome-box h2 {
        font-family: 'Poppins', sans-serif;
        color: var(--primary-dark);
        margin-bottom: 0.75rem;
    }

    .welcome-box p {
        color: var(--text-muted);
        font-family: 'Lora', serif;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    .divine-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
    }

    .disclaimer {
        margin-top: 3rem;
        padding: 1.5rem;
        background: #fff;
        border: 1px solid var(--border);
        border-radius: var(--radius);
        font-size: 0.82rem;
        color: var(--text-muted);
        line-height: 1.6;
        text-align: center;
        box-shadow: var(--shadow);
    }

    .disclaimer strong {
        color: var(--primary-dark);
    }
    </style>
""", unsafe_allow_html=True)

# ======================
# Título y subtítulo
# ======================
st.markdown('<h1 class="app-title">🕊️ Botiquín Espiritual</h1>', unsafe_allow_html=True)
st.markdown('<p class="app-subtitle">¿Cómo te sientes hoy? La Palabra de Dios tiene una respuesta para tu corazón.</p>', unsafe_allow_html=True)

# ======================
# Diccionario de emociones → versículo, texto y oración
# ======================
versiculos = {
    "😠 Molesto / Enojado": {
        "ref": "Juan 14:27",
        "texto": "»Les dejo la paz, les doy mi paz; pero no se la doy a ustedes como la da el mundo. No se angustien ni tengan miedo.«",
        "oracion": "Señor, entrego mi enojo en Tus manos y te pido que Tu paz calme mi corazón."
    },
    "😔 Débil / Cansado": {
        "ref": "Isaías 40:31",
        "texto": "«Mas los que esperan en Jehová tendrán nuevas fuerzas; levantarán las alas como águilas; correrán, y no se cansarán; caminarán, y no se fatigarán.»",
        "oracion": "Dios, renueva mis fuerzas cuando me siento agotado y dame ánimo para seguir."
    },
    "😞 Solitario": {
        "ref": "Salmos 23",
        "texto": "«Jehová es mi pastor; nada me faltará. En lugares de delicados pastos me hará reposar; junto a aguas de descanso me pastoreará.»",
        "oracion": "Padre, gracias por caminar a mi lado aunque pase por valles oscuros; no estoy solo."
    },
    "😥 He pecado": {
        "ref": "Salmos 51",
        "texto": "«Misericordia de mí, oh Dios, según Tu misericordia; conforme a la multitud de Tus compasiones borra mis transgresiones.»",
        "oracion": "Señor, ayúdame a arrepentirme de corazón, límpiame y restaura el gozo de Tu salvación en mí."
    },
    "😰 Preocupado / Ansioso": {
        "ref": "Filipenses 4:6-7",
        "texto": "«No se angustien por nada; más bien, oren; pídanle a Dios en toda ocasión y denle gracias. Y la paz de Dios, esa paz que nadie puede comprender, cuidará sus corazones y pensamientos en Cristo.»",
        "oracion": "Dios, entrego mis preocupaciones en oración y recibo Tu paz que guarda mi corazón."
    },
    "😢 Infeliz": {
        "ref": "Colosenses 3:12-17",
        "texto": "«Revístanse, entonces, como escogidos de Dios, santos y amados, de entrañas de misericordia, bondad, humildad, mansedumbre, paciencia...»",
        "oracion": "Señor, restaura mi gozo y enséñame a vivir agradecido en todas las circunstancias."
    },
    "⚠️ En peligro": {
        "ref": "Salmos 91",
        "texto": "«El que habita al abrigo del Altísimo morará bajo la sombra del Omnipotente. Diré de Jehová: Él es mi refugio y mi fortaleza, mi Dios, en quien confío.»",
        "oracion": "Padre, Tú eres mi refugio y mi escudo; confío en Tu protección sobre mi vida."
    },
    "😭 Deprimido": {
        "ref": "Salmos 27",
        "texto": "«Jehová es mi luz y mi salvación; ¿a quién temeré? Jehová es la fortaleza de mi vida; ¿de quién he de espantarme?»",
        "oracion": "Dios, acerca Tu luz a mi oscuridad y sostén mi espíritu cuando me siento abatido."
    },
    "🤔 Falta de fe": {
        "ref": "Éxodo 14",
        "texto": "«Jehová peleará por ustedes, y ustedes estarán quietos.»",
        "oracion": "Señor, aumenta mi fe y enséñame a confiar en Ti, incluso cuando no veo el camino."
    },
    "💪 Necesito valor": {
        "ref": "Josué 1:9",
        "texto": "«¿No te he mandado? Esfuérzate y sé valiente. No temas ni desmayes, que yo soy el Señor tu Dios, y estaré contigo por dondequiera que vayas.»",
        "oracion": "Dios, dame valor para avanzar sabiendo que Tú estás conmigo en cada paso."
    },
    "🧭 Necesito dirección": {
        "ref": "Salmos 73:21-26",
        "texto": "«Mas yo estoy siempre contigo; Tú me sostienes de mi mano derecha. Con Tu consejo me guiarás, y después me recibirás en gloria.»",
        "oracion": "Señor, guía mis pasos y sé mi dirección cuando no sé qué decidir."
    },
    "🕊️ Buscando paz": {
        "ref": "Mateo 11:28-30",
        "texto": "«Vengan a mí todos ustedes, los agotados de tanto trabajar, que yo los haré descansar. Lleven mi yugo sobre ustedes, y aprendan de mí, que soy manso y humilde de corazón, y hallarán descanso para su alma.»",
        "oracion": "Jesús, descanso en Ti y entrego mi carga; hallo paz para mi alma en Ti."
    },
}

# ======================
# Selector de emoción
# ======================
st.markdown('<span class="label-text">Selecciona tu estado de ánimo:</span>', unsafe_allow_html=True)
sentimiento = st.selectbox(
    "Selecciona tu estado de ánimo:",
    options=list(versiculos.keys()),
    index=None,
    placeholder="Elige cómo te sientes...",
    label_visibility="collapsed"
)

# ======================
# Botones de acción
# ======================
col1, col2 = st.columns([1, 1])
with col1:
    obtener = st.button("Obtener Versículo", type="primary", use_container_width=True)
with col2:
    limpiar = st.button("Limpiar", use_container_width=True)

# Botón limpiar: borra el estado y recarga
if limpiar:
    for key in ["mostrar", "animacion"]:
        st.session_state.pop(key, None)
    st.rerun()

# Botón obtener: guarda selección en sesión
if obtener and sentimiento:
    st.session_state["mostrar"] = sentimiento
    st.session_state["animacion"] = True

# ======================
# Vista: bienvenida o resultado
# ======================
if "mostrar" not in st.session_state:
    st.markdown("""
        <div class="welcome-box">
            <span class="divine-icon">🕊️</span>
            <h2>Bienvenido a tu espacio de paz</h2>
            <p>Tómate un momento para respirar. Elige cómo te sientes y recibe una palabra de aliento y oración para tu día.</p>
        </div>
    """, unsafe_allow_html=True)
else:
    sentimiento_actual = st.session_state["mostrar"]
    data = versiculos[sentimiento_actual]

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<div class="emotion-label">{sentimiento_actual}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ref">{data["ref"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<p class="verse-text">{data["texto"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<div class="oracion"><strong>Oración corta:</strong> {data["oracion"]}</div>', unsafe_allow_html=True)
    st.markdown('<div class="encouragement">Recuerda que Dios siempre está contigo. ¡Ánimo! 🙏</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Animación solo una vez por clic
    if st.session_state.get("animacion"):
        st.balloons()
        st.session_state["animacion"] = False

# ======================
# Descargo de responsabilidad
# ======================
st.markdown("""
<div class="disclaimer">
⚠️ <strong>Aviso importante:</strong> Este botiquín espiritual es una herramienta de acompañamiento y oración. No reemplaza el consejo médico, psicológico ni psiquiátrico. Si sientes tristeza persistente, ansiedad abrumadora, pensamientos de autolesión o estás en crisis, busca ayuda profesional hoy mismo y habla con una persona de confianza. Pedir ayuda es un acto de cuidado y valentía.
</div>
""", unsafe_allow_html=True)
