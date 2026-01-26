import streamlit as st
from datetime import datetime, timedelta

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Cortex - Checkout",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- ESTILO PREMIUM (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    html, body, .stApp {
        background: linear-gradient(135deg, #F0FFFE 0%, #E8F8FF 100%) !important;
    }
    
    /* Container Principal */
    .checkout-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 40px 20px;
    }
    
    /* Header */
    .header {
        text-align: center;
        margin-bottom: 50px;
    }
    
    .header h1 {
        color: #952791;
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.02em;
    }
    
    .header p {
        color: #666;
        font-size: 1.1rem;
        margin-top: 10px;
    }
    
    /* Urgência */
    .urgency-banner {
        background: linear-gradient(90deg, #FF6B6B 0%, #FF8E72 100%);
        color: white;
        padding: 15px 20px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 30px;
        font-weight: 700;
        font-size: 1rem;
    }
    
    /* Grid de Produtos */
    .products-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 30px;
        margin-bottom: 50px;
    }
    
    @media (max-width: 768px) {
        .products-grid {
            grid-template-columns: 1fr;
        }
    }
    
    /* Card de Produto */
    .product-card {
        background: white;
        border-radius: 16px;
        padding: 40px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
    }
    
    .product-card.featured {
        border: 2px solid #37D087;
        background: linear-gradient(135deg, #FFFFFF 0%, #F0FFFE 100%);
    }
    
    .product-card.featured::before {
        content: "MAIS POPULAR";
        display: block;
        background: linear-gradient(90deg, #37D087 0%, #39D7FE 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 800;
        width: fit-content;
        margin: -50px 0 20px 0;
        letter-spacing: 0.05em;
    }
    
    .product-title {
        color: #952791;
        font-size: 1.5rem;
        font-weight: 800;
        margin: 0 0 15px 0;
    }
    
    .product-description {
        color: #666;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 25px;
    }
    
    .price {
        font-size: 2.5rem;
        color: #952791;
        font-weight: 800;
        margin: 20px 0;
    }
    
    .price-small {
        font-size: 0.9rem;
        color: #999;
        margin-bottom: 25px;
    }
    
    .features-list {
        list-style: none;
        padding: 0;
        margin: 25px 0;
    }
    
    .features-list li {
        color: #666;
        padding: 10px 0;
        border-bottom: 1px solid #f0f0f0;
        display: flex;
        align-items: center;
    }
    
    .features-list li:last-child {
        border-bottom: none;
    }
    
    .features-list li::before {
        content: "✓";
        color: #37D087;
        font-weight: 800;
        margin-right: 12px;
        font-size: 1.2rem;
    }
    
    .btn-checkout {
        background: linear-gradient(90deg, #37D087 0%, #39D7FE 100%);
        color: white;
        border: none;
        padding: 16px 32px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 1rem;
        cursor: pointer;
        width: 100%;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 20px;
    }
    
    .btn-checkout:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(55, 208, 135, 0.3);
    }
    
    /* Order Bump */
    .order-bump {
        background: linear-gradient(135deg, #FFF9E6 0%, #FFFBF0 100%);
        border: 2px solid #FFD700;
        border-radius: 16px;
        padding: 30px;
        margin: 40px 0;
        position: relative;
    }
    
    .order-bump::before {
        content: "⚡ OFERTA RELÂMPAGO";
        position: absolute;
        top: -15px;
        left: 20px;
        background: linear-gradient(90deg, #FFD700 0%, #FFA500 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 0.05em;
    }
    
    .order-bump h3 {
        color: #952791;
        font-size: 1.3rem;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    
    .order-bump p {
        color: #666;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    .bump-price {
        font-size: 1.8rem;
        color: #952791;
        font-weight: 800;
        margin: 15px 0;
    }
    
    .bump-original {
        text-decoration: line-through;
        color: #999;
        font-size: 0.9rem;
        margin-right: 10px;
    }
    
    .bump-savings {
        background: #FFD700;
        color: #333;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 700;
    }
    
    /* Depoimentos */
    .testimonials {
        margin: 60px 0;
    }
    
    .testimonials h2 {
        color: #952791;
        font-size: 2rem;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 800;
    }
    
    .testimonials-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px;
    }
    
    .testimonial-card {
        background: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
    }
    
    .stars {
        color: #FFD700;
        font-size: 1.2rem;
        margin-bottom: 15px;
    }
    
    .testimonial-text {
        color: #666;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 15px;
        font-style: italic;
    }
    
    .testimonial-author {
        color: #952791;
        font-weight: 700;
        font-size: 0.9rem;
    }
    
    .testimonial-role {
        color: #999;
        font-size: 0.85rem;
    }
    
    /* Bônus */
    .bonus-section {
        background: linear-gradient(135deg, #E8F5E9 0%, #F1F8E9 100%);
        border-radius: 16px;
        padding: 40px;
        margin: 50px 0;
        border-left: 5px solid #37D087;
    }
    
    .bonus-section h3 {
        color: #952791;
        font-size: 1.5rem;
        margin-bottom: 25px;
        font-weight: 800;
    }
    
    .bonus-item {
        display: flex;
        align-items: flex-start;
        margin-bottom: 20px;
    }
    
    .bonus-icon {
        font-size: 1.5rem;
        margin-right: 15px;
        min-width: 30px;
    }
    
    .bonus-content h4 {
        color: #952791;
        margin: 0 0 5px 0;
        font-size: 1rem;
    }
    
    .bonus-content p {
        color: #666;
        margin: 0;
        font-size: 0.9rem;
    }
    
    /* FAQ */
    .faq-section {
        margin: 60px 0;
    }
    
    .faq-section h2 {
        color: #952791;
        font-size: 2rem;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 800;
    }
    
    .faq-item {
        background: white;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 15px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
    }
    
    .faq-question {
        color: #952791;
        font-weight: 700;
        font-size: 1rem;
        margin-bottom: 10px;
    }
    
    .faq-answer {
        color: #666;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #999;
        font-size: 0.9rem;
        padding: 40px 20px;
        border-top: 1px solid #e0e0e0;
        margin-top: 60px;
    }
    
    .footer a {
        color: #952791;
        text-decoration: none;
    }
    
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTEÚDO ---
st.markdown('<div class="checkout-container">', unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header">
        <h1>🧠 Inteligência Cortex</h1>
        <p>Convivemos, trabalhamos e nos relacionamos com outras pessoas o tempo todo, entender o comportamento humano se torna uma habilidade essencial de sobrevivência e inteligência emocional. </p>
    </div>
    """, unsafe_allow_html=True)

# Urgência
dias_restantes = 3
st.markdown(f"""
    <div class="urgency-banner">
        ⏰ OFERTA ESPECIAL DE CAMPANHA!
    </div>
    """, unsafe_allow_html=True)

# Produtos
st.markdown('<div class="products-grid">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""<div class="product-card">
<h3 class="product-title">Plataforma de aprendizado Cortex</h3>

<p class="product-description">
Aprenda os princípios fundamentais do comportamento humano através de 21 dias de atividades práticas e transformadoras.
</p>

<div class="price">R$ 39,90</div>
<p class="price-small">Acesso vitalício</p>

<ul class="features-list">
<li>21 dias de atividades práticas</li>
<li>Conteúdo baseado em comportamento humano</li>
<li>Acesso vitalício à plataforma</li>
<li>Atualizações futuras incluídas</li>
<li>Suporte por email</li>
</ul>

<button class="btn-checkout" onclick="window.open('https://seulink.eduzz.com/cortex-ia', '_blank')">
Quero acessar agora
</button>
</div>""", unsafe_allow_html=True)


with col2:
    st.markdown("""<div class="product-card featured">
<h3 class="product-title">Plataforma de aprendizado Cortex + Chat IA</h3>

<p class="product-description">
Aprenda + Receba análises comportamentais personalizadas com nossa IA especializada. A melhor combinação para transformação.
</p>

<div class="price">R$ 79,90</div>
<p class="price-small">Acesso vitalício a ambos</p>

<ul class="features-list">
<li>Acesso a todo aprendizado da plataforma</li>
<li>Chat IA com análise comportamental</li>
<li>Plano de ação customizado</li>
<li>Análise de padrões comportamentais</li>
<li>Diagnóstico personalizado</li>
<li>Suporte 7 dias por semana</li>
</ul>

<button class="btn-checkout" onclick="window.open('https://seulink.eduzz.com/cortex-ia-completo', '_blank')">
Garantir a experiência completa
</button>
</div>""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# Order Bump
st.markdown("""<div class="order-bump">
<h3>🤖 Adicione somente a IA por apenas R$ 59,90</h3>

<p>
Caso queira, adicione somente nossa IA com análise comportamental e receba diagnósticos personalizados, planos de ação e acompanhamento contínuo.
</p>

<div class="bump-price">
R$ 59,90
<span class="bump-original">R$ 79,90</span>
<span class="bump-savings">-25% OFF</span>
</div>

<p style="color: #666; margin: 15px 0;">
✓ Análise de padrões comportamentais<br>
✓ Diagnóstico personalizado<br>
✓ Soluções para problemas específicos<br>
✓ Plano de ação customizado<br>
✓ Acesso vitalício
</p>

<button class="btn-checkout" onclick="window.open('https://seulink.eduzz.com/cortex-ia-chat', '_blank')">
Adicionar Chat IA Agora
</button>
</div>""", unsafe_allow_html=True)


# Bônus
st.markdown("""<div class="bonus-section">
<h3>🎁 Bônus exclusivos</h3>

<div class="bonus-item">
    <div class="bonus-icon">📚</div>
    <div class="bonus-content">
        <h4>Acesso vitalício</h4>
        <p>Todo o conteúdo, incluindo suas atualizações, estará disponível para ver e revisar quando quiser.</p>
    </div>
</div>

<div class="bonus-item">
    <div class="bonus-icon">🤖</div>
    <div class="bonus-content">
        <h4>Acesso ao Chat IA</h4>
        <p>Também vitalício, pagamento único, seu assistente pessoal de inteligência emocional e comportamento humano 24h por dia.</p>
    </div>
</div>

<div class="bonus-item">
    <div class="bonus-icon">📖</div>
    <div class="bonus-content">
        <h4>Suporte rápido e humano</h4>
        <p>Suporte para responder todas as suas dúvidas, com atendimento de um time de especialistas.</p>
    </div>
</div>
</div>""", unsafe_allow_html=True)


# Depoimentos
st.markdown("""<div class="testimonials">
<h2>O que dizem nossos clientes</h2>

<div class="testimonials-grid">

<div class="testimonial-card">
    <div class="stars">⭐⭐⭐⭐⭐</div>
    <p class="testimonial-text">
    "Sempre gostei de estudar sobre nosso comportamento. Em 21 dias aprendi MUITO sobre linguagem corporal. Consigo agora compreender diversas situações."
    </p>
    <div class="testimonial-author">Ricardo Murata</div>
    <div class="testimonial-role">Empreendedor</div>
</div>

<div class="testimonial-card">
    <div class="stars">⭐⭐⭐⭐⭐</div>
    <p class="testimonial-text">
    "As atividades práticas são ótimas, nada de teoria chata e tudo aquilo que já sabemos."
    </p>
    <div class="testimonial-author">Luiza Sabino</div>
    <div class="testimonial-role">Profissional de RH</div>
</div>

<div class="testimonial-card">
    <div class="stars">⭐⭐⭐⭐⭐</div>
    <p class="testimonial-text">
    "O Chat IA é sensacional! Tirei diversas dúvidas que carregava e recebi um norte que funcionou para mim"
    </p>
    <div class="testimonial-author">Ana Costa</div>
    <div class="testimonial-role">Estudante</div>
</div>

</div>
</div>""", unsafe_allow_html=True)


# FAQ
st.markdown("""<div class="faq-section">
<h2>Perguntas Frequentes</h2>

<div class="faq-item">
    <div class="faq-question">❓ Qual e-mail de suporte para tirar minhas dúvidas</div>
    <div class="faq-answer">
    Nosso time está 100% disponível para você no e-mail suporte@cortexinteligencia.com
    </div>
</div>

<div class="faq-item">
    <div class="faq-question">❓ Posso acessar o conteúdo para sempre?</div>
    <div class="faq-answer">
    Sim! Você tem acesso vitalício à plataforma de estudos. Pode revisar o conteúdo quantas vezes quiser e receberá todas as atualizações futuras.
    </div>
</div>

<div class="faq-item">
    <div class="faq-question">❓ O Chat IA pode ser acessado por onde?</div>
    <div class="faq-answer">
    Você pode acessar a IA de qualquer lugar: celular, computador, tablet ou qualquer dispositivo com internet. Ela funciona integrada à maior plataforma de IA do mundo (OpenAI), garantindo acesso simples e imediato pelo navegador ou app, sem instalações complicadas.
    </div>
</div>

<div class="faq-item">
    <div class="faq-question">❓ Qual é a forma de pagamento?</div>
    <div class="faq-answer">
    Aceitamos todos os métodos de pagamento através da Eduzz: cartão de crédito, débito, Pix, boleto e outras opções.
    </div>
</div>

<div class="faq-item">
    <div class="faq-question">❓ Posso comprar apenas o Chat IA sem o curso?</div>
    <div class="faq-answer">
    Sim! O Chat IA é um produto independente. Você pode comprar apenas o curso, apenas o Chat ou ambos com desconto no combo.
    </div>
</div>

</div>""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>© 2026 Cortex IA. Todos os direitos reservados.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
