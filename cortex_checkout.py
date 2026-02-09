import streamlit as st
import time
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="WebTemplates Pro - Templates de Sites Prontos",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS ULTRA VIBRANTE COM ANIMAÇÕES INCRÍVEIS
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800;900&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(-45deg, #FF006E, #FB5607, #FFBE0B, #8338EC, #3A86FF, #FF006E);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        font-family: 'Poppins', sans-serif;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    [data-testid="stDecoration"] { display: none; }
    
    .main {
        padding: 0 !important;
        background: transparent;
    }
    
    /* HERO SECTION - EXPLOSÃO DE CORES */
    .hero-section {
        background: linear-gradient(135deg, #FF006E 0%, #FB5607 25%, #FFBE0B 50%, #8338EC 75%, #3A86FF 100%);
        background-size: 400% 400%;
        animation: gradient 8s ease infinite;
        color: white;
        padding: 150px 40px;
        text-align: center;
        position: relative;
        overflow: hidden;
        clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        width: 800px;
        height: 800px;
        background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%);
        border-radius: 50%;
        top: -200px;
        right: -200px;
        animation: float 20s ease-in-out infinite;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
        border-radius: 50%;
        bottom: -150px;
        left: -150px;
        animation: float 25s ease-in-out infinite reverse;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-30px) scale(1.1); }
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 900px;
        margin: 0 auto;
    }
    
    .hero-subtitle {
        font-size: 18px;
        font-weight: 700;
        letter-spacing: 3px;
        margin-bottom: 20px;
        opacity: 0.95;
        text-transform: uppercase;
        animation: slideInDown 0.8s ease;
    }
    
    .hero-title {
        font-size: 84px;
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 30px;
        text-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        animation: slideInUp 0.8s ease 0.2s both;
        background: linear-gradient(45deg, #FFFFFF, #FFE5E5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero-description {
        font-size: 20px;
        line-height: 1.8;
        margin-bottom: 50px;
        opacity: 0.95;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        animation: slideInUp 0.8s ease 0.4s both;
    }
    
    @keyframes slideInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(255, 0, 110, 0.5); }
        50% { box-shadow: 0 0 40px rgba(255, 0, 110, 0.8); }
    }
    
    /* BOTÃO CTA - SUPER VIBRANTE */
    .cta-button {
        display: inline-block;
        background: linear-gradient(135deg, #FFE5E5 0%, #FFFFFF 100%);
        color: #FF006E;
        padding: 18px 60px;
        border-radius: 50px;
        font-weight: 900;
        font-size: 18px;
        text-decoration: none;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        border: 3px solid white;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
        animation: pulse 2s ease-in-out infinite;
    }
    
    .cta-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s;
    }
    
    .cta-button:hover {
        transform: translateY(-5px) scale(1.1);
        box-shadow: 0 25px 60px rgba(255, 0, 110, 0.4);
        animation: glow 1s ease-in-out infinite;
    }
    
    .cta-button:hover::before {
        left: 100%;
    }
    
    /* SEÇÕES COM FUNDO TRANSPARENTE */
    .section {
        padding: 120px 40px;
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }
    
    .section-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 20px;
        line-height: 1.2;
        color: white;
        text-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
        animation: slideInUp 0.8s ease;
    }
    
    .section-title .highlight {
        background: linear-gradient(135deg, #FFBE0B, #FB5607);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 900;
    }
    
    .section-description {
        font-size: 20px;
        color: rgba(255, 255, 255, 0.95);
        line-height: 1.8;
        margin-bottom: 60px;
        max-width: 700px;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    /* CARROSSEL HORIZONTAL */
    .carousel-section {
        padding: 100px 40px;
        max-width: 1400px;
        margin: 0 auto;
        position: relative;
        z-index: 1;
    }
    
    .carousel-title {
        font-size: 56px;
        font-weight: 900;
        margin-bottom: 20px;
        line-height: 1.2;
        color: white;
        text-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
    }
    
    .carousel-description {
        font-size: 20px;
        color: rgba(255, 255, 255, 0.95);
        line-height: 1.8;
        margin-bottom: 50px;
        max-width: 700px;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    .carousel-wrapper {
        display: flex;
        gap: 20px;
        overflow-x: auto;
        scroll-behavior: smooth;
        padding: 20px;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 25px;
        scrollbar-width: thin;
        scrollbar-color: rgba(255, 190, 11, 0.5) rgba(255, 255, 255, 0.1);
    }
    
    .carousel-wrapper::-webkit-scrollbar {
        height: 8px;
    }
    
    .carousel-wrapper::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    
    .carousel-wrapper::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #FF006E, #FFBE0B);
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    
    .carousel-wrapper::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #FFBE0B, #FF006E);
    }
    
    .carousel-item {
        flex: 0 0 350px;
        min-width: 350px;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        overflow: hidden;
        border: 2px solid rgba(255, 255, 255, 0.2);
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        cursor: pointer;
        position: relative;
    }
    
    .carousel-item:hover {
        transform: translateY(-15px) scale(1.05);
        box-shadow: 0 25px 60px rgba(255, 0, 110, 0.4);
        border-color: rgba(255, 255, 255, 0.4);
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0.1) 100%);
    }
    
    .carousel-image {
        width: 100%;
        height: 250px;
        object-fit: cover;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 80px;
        background: linear-gradient(135deg, #FF006E, #8338EC);
    }
    
    .carousel-content {
        padding: 20px;
    }
    
    .carousel-item-title {
        font-size: 20px;
        font-weight: 800;
        color: white;
        margin-bottom: 10px;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .carousel-item-desc {
        font-size: 14px;
        color: rgba(255, 255, 255, 0.85);
        line-height: 1.6;
    }
    
    .carousel-badge {
        position: absolute;
        top: 15px;
        right: 15px;
        background: linear-gradient(135deg, #FF006E, #FB5607);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 5px 15px rgba(255, 0, 110, 0.3);
    }
    
    /* CARDS ULTRA VIBRANTES */
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 30px;
        margin-top: 60px;
    }
    
    .card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 50px 40px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        border: 2px solid rgba(255, 255, 255, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .card::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(255, 255, 255, 0.3), transparent);
        border-radius: 50%;
        opacity: 0;
        transition: all 0.6s ease;
    }
    
    .card:hover {
        transform: translateY(-20px) scale(1.05) rotate(2deg);
        box-shadow: 0 20px 60px rgba(255, 0, 110, 0.4);
        border-color: rgba(255, 255, 255, 0.4);
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0.1) 100%);
    }
    
    .card:hover::before {
        opacity: 1;
        top: -25%;
        right: -25%;
    }
    
    .card-icon {
        font-size: 64px;
        margin-bottom: 20px;
        display: inline-block;
        animation: bounce 2s ease-in-out infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }
    
    .card-title {
        font-size: 28px;
        font-weight: 800;
        margin-bottom: 15px;
        color: white;
        text-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
    }
    
    .card-description {
        font-size: 16px;
        color: rgba(255, 255, 255, 0.9);
        line-height: 1.7;
    }
    
    /* PRICING CARDS - SUPER DESTAQUE */
    .pricing-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(10px);
        border-radius: 25px;
        padding: 50px 40px;
        border: 2px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        overflow: hidden;
    }
    
    .pricing-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #FF006E, #FB5607, #FFBE0B, #8338EC, #3A86FF);
        background-size: 200% 100%;
        animation: shimmer 3s ease infinite;
    }
    
    @keyframes shimmer {
        0% { background-position: 0% 0%; }
        100% { background-position: 200% 0%; }
    }
    
    .pricing-card.featured {
        border-color: rgba(255, 255, 255, 0.4);
        box-shadow: 0 20px 60px rgba(255, 0, 110, 0.3);
        transform: scale(1.08);
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0.1) 100%);
    }
    
    .pricing-card:hover {
        transform: translateY(-15px);
        box-shadow: 0 25px 70px rgba(255, 0, 110, 0.4);
        border-color: rgba(255, 255, 255, 0.3);
    }
    
    .pricing-card.featured:hover {
        transform: scale(1.12) translateY(-15px);
    }
    
    .price {
        font-size: 56px;
        font-weight: 900;
        color: white;
        margin-bottom: 20px;
        text-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    }
    
    .price-label {
        font-size: 16px;
        color: rgba(255, 255, 255, 0.8);
        margin-bottom: 15px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .price-description {
        font-size: 18px;
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 30px;
        line-height: 1.6;
        font-weight: 600;
    }
    
    .price-features {
        text-align: left;
        margin-bottom: 40px;
    }
    
    .price-feature {
        font-size: 15px;
        color: rgba(255, 255, 255, 0.85);
        padding: 12px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .price-feature:hover {
        color: white;
        padding-left: 10px;
    }
    
    .price-feature::before {
        content: '✨ ';
        color: #FFBE0B;
        font-weight: 800;
        margin-right: 10px;
    }
    
    /* TESTIMONIAL CARDS */
    .testimonial-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 50px 40px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border-left: 6px solid #FFBE0B;
        margin-bottom: 30px;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .testimonial-card::before {
        content: '"';
        position: absolute;
        top: -20px;
        left: 20px;
        font-size: 120px;
        color: rgba(255, 190, 11, 0.2);
        font-weight: 900;
    }
    
    .testimonial-card:hover {
        transform: translateX(10px);
        box-shadow: 0 15px 50px rgba(255, 0, 110, 0.3);
        border-left-color: #FF006E;
    }
    
    .testimonial-text {
        font-size: 18px;
        color: rgba(255, 255, 255, 0.95);
        line-height: 1.8;
        margin-bottom: 25px;
        font-style: italic;
        position: relative;
        z-index: 1;
    }
    
    .testimonial-author {
        font-weight: 800;
        color: #FFBE0B;
        font-size: 18px;
    }
    
    .testimonial-role {
        font-size: 15px;
        color: rgba(255, 255, 255, 0.7);
        margin-top: 5px;
    }
    
    /* FORM SECTION */
    .form-section {
        padding: 100px 40px;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(10px);
        border-radius: 30px;
        margin: 60px 40px;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    .form-container {
        max-width: 700px;
        margin: 0 auto;
    }
    
    .form-title {
        font-size: 48px;
        font-weight: 900;
        margin-bottom: 15px;
        color: white;
        text-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    }
    
    .form-subtitle {
        font-size: 18px;
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 40px;
    }
    
    /* FOOTER */
    .footer {
        background: linear-gradient(135deg, rgba(0, 0, 0, 0.8), rgba(51, 51, 51, 0.8));
        backdrop-filter: blur(10px);
        color: white;
        padding: 60px 40px;
        text-align: center;
        border-top: 3px solid rgba(255, 190, 11, 0.3);
    }
    
    .footer-links {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-bottom: 30px;
        flex-wrap: wrap;
    }
    
    .footer-link {
        color: rgba(255, 255, 255, 0.8);
        text-decoration: none;
        transition: all 0.3s ease;
        font-weight: 600;
    }
    
    .footer-link:hover {
        color: #FFBE0B;
        transform: translateY(-3px);
    }
    
    .footer-copyright {
        font-size: 15px;
        color: rgba(255, 255, 255, 0.6);
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding-top: 30px;
    }
    
    /* STREAMLIT OVERRIDES */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #FF006E, #FB5607);
        color: white;
        border: none;
        padding: 16px 24px;
        border-radius: 15px;
        font-weight: 700;
        font-size: 18px;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 10px 30px rgba(255, 0, 110, 0.3);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #FB5607, #FFBE0B);
        transform: translateY(-5px);
        box-shadow: 0 20px 50px rgba(255, 0, 110, 0.5);
    }
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 15px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        padding: 15px;
        font-size: 16px;
        background: rgba(255, 255, 255, 0.1);
        color: white;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {
        color: rgba(255, 255, 255, 0.6);
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #FFBE0B;
        box-shadow: 0 0 0 3px rgba(255, 190, 11, 0.2);
        background: rgba(255, 255, 255, 0.15);
    }
    
    /* RESPONSIVIDADE */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 48px;
        }
        
        .section-title {
            font-size: 36px;
        }
        
        .carousel-title {
            font-size: 36px;
        }
        
        .hero-section {
            padding: 80px 20px;
            clip-path: none;
        }
        
        .section {
            padding: 60px 20px;
        }
        
        .carousel-section {
            padding: 60px 20px;
        }
        
        .carousel-item {
            flex: 0 0 280px;
            min-width: 280px;
        }
        
        .pricing-card.featured {
            transform: scale(1);
        }
        
        .pricing-card.featured:hover {
            transform: scale(1.05) translateY(-15px);
        }
        
        .form-section {
            margin: 40px 20px;
        }
        
        .footer-links {
            gap: 15px;
        }
    }
</style>
"""

# Injetar CSS
st.markdown(custom_css, unsafe_allow_html=True)

# ==================== HERO SECTION ====================
hero_html = """
<div class="hero-section">
    <div class="hero-content">
        <div class="hero-subtitle">⚡ Crie seu site em 5 minutos ⚡</div>
        <div class="hero-title">Lance seu novo site profissional em minutos, sem a dependência de um programador</div>
        <div class="hero-description">
            Escolha entre dezenas de templates prontos, personalize do jeito que quiser e economize até 80%. Seu site no ar hoje, sem complicações.
        </div>
    </div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# ==================== SEÇÃO DE CARROSSEL HORIZONTAL ====================
st.markdown("""
<div class="carousel-section">
    <div class="carousel-title">Veja nossos <span style="background: linear-gradient(135deg, #FFBE0B, #FB5607); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">templates em ação</span></div>
    <div class="carousel-description">
        Deslize para o lado e explore todos os templates disponíveis. Cada um é uma obra de arte pronta para usar!
    </div>
</div>
""", unsafe_allow_html=True)

# Dados dos templates
templates_data = [
    {
        "title": "Consultório Dentário",
        "desc": "Landing page profissional com agendamento online integrado",
        "category": "Saúde"
    },
    {
        "title": "E-commerce Fashion",
        "desc": "Loja online completa com carrinho e pagamento integrado",
        "category": "Vendas"
    },
    {
        "title": "Criador de Conteúdo",
        "desc": "Portfolio e venda de cursos com área de membros",
        "category": "Digital"
    },
    {
        "title": "Salão de Beleza",
        "desc": "Agendamento, galeria de trabalhos e promoções",
        "category": "Serviços"
    },
    {
        "title": "Academia de Fitness",
        "desc": "Planos, horários de aulas e área de alunos",
        "category": "Fitness"
    },
    {
        "title": "Restaurante",
        "desc": "Cardápio interativo, reservas e delivery integrado",
        "category": "Alimentos"
    },
    {
        "title": "Imobiliária",
        "desc": "Catálogo de imóveis com filtros avançados",
        "category": "Imóveis"
    },
    {
        "title": "Agência Digital",
        "desc": "Portfolio de projetos e formulário de contato",
        "category": "Agência"
    },
]

# Renderizar carrossel com HTML puro - CORRIGIDO
carousel_html = '<div class="carousel-wrapper">'
for template in templates_data:
    carousel_html += f'''<div class="carousel-item">
        <div class="carousel-badge">{template['category']}</div>
        <div class="carousel-image">📱</div>
        <div class="carousel-content">
            <div class="carousel-item-title">{template['title']}</div>
            <div class="carousel-item-desc">{template['desc']}</div>
        </div>
    </div>'''
carousel_html += '</div>'

st.markdown(carousel_html, unsafe_allow_html=True)

# ==================== SEÇÃO DE BENEFÍCIOS ====================
st.markdown("""
<div class="section">
    <div class="section-title">Por que escolher nossos templates?</div>
    <div class="section-description">
        Oferecemos soluções completas, profissionais e fáceis de usar para qualquer tipo de negócio.
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-icon">⚡</div>
        <div class="card-title">SUPER RÁPIDO</div>
        <div class="card-description">
            Seu site estará pronto em apenas 5 minutos. Sem complicações, sem esperas. Sério mesmo!
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-icon">🎨</div>
        <div class="card-title">TOTALMENTE CUSTOMIZÁVEL</div>
        <div class="card-description">
            Personalize cores, textos e imagens facilmente. O código está pronto para você ajustar.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-icon">📱</div>
        <div class="card-title">RESPONSIVO</div>
        <div class="card-description">
            Funciona perfeitamente em celulares, tablets e desktops. Sem problemas em nenhum lugar!
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==================== SEÇÃO DE EXEMPLOS ====================
st.markdown("""
<div class="section">
    <div class="section-title">Exemplos de sites criados</div>
    <div class="section-description">
        Veja alguns dos templates que você pode usar hoje mesmo. Cada um é uma obra de arte!
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

examples = [
    {"title": "Consultório Dentário", "desc": "Landing page para dentistas com agendamento", "emoji": "🦷"},
    {"title": "E-commerce", "desc": "Loja online pronta para vender seus produtos", "emoji": "🛍️"},
    {"title": "Criador de Conteúdo", "desc": "Portfolio e venda de cursos online", "emoji": "🎬"},
]

for col, example in zip([col1, col2, col3], examples):
    with col:
        st.markdown(f"""
        <div class="card">
            <div class="card-icon">{example['emoji']}</div>
            <div class="card-title">{example['title']}</div>
            <div class="card-description">{example['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

# ==================== SEÇÃO DE ESPECIALIDADES ====================
st.markdown("""
<div class="section">
    <div class="section-title">Templates para todos os tipos de negócio</div>
    <div class="section-description">
        Temos soluções prontas para qualquer segmento. Escolha a que mais se encaixa no seu negócio.
    </div>
</div>
""", unsafe_allow_html=True)

specialties = [
    {"emoji": "🦷", "name": "Dentistas", "desc": "Consultórios e clínicas"},
    {"emoji": "💇", "name": "Salões", "desc": "Beleza e estética"},
    {"emoji": "🏋️", "name": "Academias", "desc": "Fitness e musculação"},
    {"emoji": "🍔", "name": "Restaurantes", "desc": "Cardápio e delivery"},
    {"emoji": "📚", "name": "Educação", "desc": "Cursos e treinamentos"},
    {"emoji": "🏠", "name": "Imobiliárias", "desc": "Venda de imóveis"},
    {"emoji": "👔", "name": "Consultoria", "desc": "Serviços profissionais"},
    {"emoji": "🎨", "name": "Agências", "desc": "Design e criação"},
    {"emoji": "💼", "name": "Escritórios", "desc": "Advocacia e contabilidade"},
]

cols = st.columns(3)
for idx, specialty in enumerate(specialties):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="card">
            <div class="card-icon">{specialty['emoji']}</div>
            <div class="card-title">{specialty['name']}</div>
            <div class="card-description">{specialty['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

# ==================== SEÇÃO DE PREÇOS ====================
st.markdown("""
<div class="section">
    <div class="section-title">Planos e preços</div>
    <div class="section-description">
        Escolha o plano que melhor se adequa às suas necessidades. Todos com suporte completo!
    </div>
</div>
""", unsafe_allow_html=True)

pricing_col1, pricing_col2, pricing_col3 = st.columns(3)

with pricing_col1:
    st.markdown("""
    <div class="pricing-card">
        <div class="price-label">Básico</div>
        <div class="price">R$ 97</div>
        <div class="price-description">Perfeito para começar</div>
        <div class="price-features">
            <div class="price-feature">1 template de site</div>
            <div class="price-feature">Customização básica</div>
            <div class="price-feature">Suporte por email</div>
            <div class="price-feature">Documentação completa</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with pricing_col2:
    st.markdown("""
    <div class="pricing-card featured">
        <div class="price-label">⭐ Profissional</div>
        <div class="price">R$ 197</div>
        <div class="price-description">Mais popular</div>
        <div class="price-features">
            <div class="price-feature">5 templates de site</div>
            <div class="price-feature">Customização avançada</div>
            <div class="price-feature">Suporte prioritário</div>
            <div class="price-feature">Atualizações gratuitas</div>
            <div class="price-feature">Certificado de conclusão</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with pricing_col3:
    st.markdown("""
    <div class="pricing-card">
        <div class="price-label">Premium</div>
        <div class="price">R$ 397</div>
        <div class="price-description">Acesso total</div>
        <div class="price-features">
            <div class="price-feature">Todos os 30+ templates</div>
            <div class="price-feature">Customização ilimitada</div>
            <div class="price-feature">Suporte 24/7</div>
            <div class="price-feature">Acesso a comunidade</div>
            <div class="price-feature">Bônus exclusivos</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==================== SEÇÃO DE TESTIMONIAIS ====================
st.markdown("""
<div class="section">
    <div class="section-title">O que nossos clientes dizem</div>
    <div class="section-description">
        Histórias reais de pessoas que transformaram seus negócios com nossos templates.
    </div>
</div>
""", unsafe_allow_html=True)

testimonials = [
    {
        "text": "Criei meu site em 5 minutos e já estou recebendo clientes! Não acreditava que era tão fácil. Recomendo muito!",
        "author": "Marina Silva",
        "role": "Dentista - São Paulo"
    },
    {
        "text": "Melhor investimento que fiz. O template é profissional e fácil de customizar. Meu faturamento triplicou!",
        "author": "Carlos Mendes",
        "role": "Criador de Conteúdo - Rio de Janeiro"
    },
    {
        "text": "Saí do zero para ter uma loja online profissional em poucas horas. Muito bom mesmo!",
        "author": "Ana Costa",
        "role": "Lojista - Belo Horizonte"
    },
]

for testimonial in testimonials:
    st.markdown(f"""
    <div class="testimonial-card">
        <div class="testimonial-text">"{testimonial['text']}"</div>
        <div class="testimonial-author">{testimonial['author']}</div>
        <div class="testimonial-role">{testimonial['role']}</div>
    </div>
    """, unsafe_allow_html=True)

# ==================== SEÇÃO DE FORMULÁRIO ====================
st.markdown("""
<div class="form-section">
    <div class="form-container">
        <div class="form-title">🚀 Comece AGORA!</div>
        <div class="form-subtitle">Preencha seus dados e acesse os templates incríveis</div>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    name = st.text_input("Seu Nome", placeholder="João Silva")

with col2:
    email = st.text_input("Seu Email", placeholder="joao@example.com")

col1, col2 = st.columns([1, 1])

with col1:
    phone = st.text_input("Seu Telefone", placeholder="(11) 99999-9999")

with col2:
    business = st.text_input("Tipo de Negócio", placeholder="Ex: Dentista, Loja, etc")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("🚀 ACESSAR TEMPLATES AGORA", use_container_width=True):
        if name and email and phone and business:
            st.success(f"🎉 Ótimo, {name}! Você será redirecionado para o checkout em breve.")
            st.info("Clique no botão abaixo para finalizar sua compra:")
            st.markdown("""
            <a href="https://eduzz.com" target="_blank" style="
                display: inline-block;
                background: linear-gradient(135deg, #FF006E, #FB5607);
                color: white;
                padding: 20px 60px;
                border-radius: 15px;
                text-decoration: none;
                font-weight: 900;
                font-size: 18px;
                box-shadow: 0 15px 40px rgba(255, 0, 110, 0.4);
                text-transform: uppercase;
                letter-spacing: 2px;
                transition: all 0.3s ease;
            ">💳 Ir para Checkout Eduzz</a>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Por favor, preencha todos os campos!")

# ==================== FOOTER ====================
st.markdown("""
<div class="footer">
    <div class="footer-links">
        <a href="#" class="footer-link">Sobre</a>
        <a href="#" class="footer-link">Templates</a>
        <a href="#" class="footer-link">Preços</a>
        <a href="#" class="footer-link">Contato</a>
        <a href="#" class="footer-link">Termos de Uso</a>
    </div>
    <div class="footer-copyright">
        © 2025 WebTemplates Pro. Todos os direitos reservados. 🚀
    </div>
</div>
""", unsafe_allow_html=True)
