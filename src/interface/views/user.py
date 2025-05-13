import streamlit as st

def user_page():
    #header
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <div class="header-ipea">
        <h3 class="titulo-ipea">Relatórios inteligentes IPEA</h3>
        <a href="login.py" class="login-icon" >
            <i class="fas fa-user-circle"></i>
        </a>
    </div>
                """, unsafe_allow_html=True)
    
    

    # Layout centralizado
    st.markdown('<h1 class="title">Gov Insights</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="form-container">
    <label for="email">Endereço de e-mail</label>
    <input type="text" id="email" name="email" class="custom-input">

    <label for="senha">Senha</label><br>
    <input type="password" id="senha" name="senha" class="custom-input"><br>
    <a href="#" class="forgot-link center-text">Esqueceu sua senha? Clique aqui</a>
    """, unsafe_allow_html=True)


    st.markdown("""
        <button class="login-button" type="button" onclick="login()">Entrar</button>
        <script>
            function login() {
                window.alert("Login enviado!");
            }
        </script>
    """, unsafe_allow_html=True)
    #mudança 


    st.markdown("<hr><p style='text-align:center'>ou</p><hr>", unsafe_allow_html=True)

    st.markdown("""
    <div class="social-buttons">
        <div class="social-btn facebook">
            <img width="20" height="20" src="https://img.icons8.com/material-rounded/20/ffffff/facebook-new.png" alt="facebook-new" style="margin-right: 8px;" />
            Facebook
        </div>
        <div class="social-btn google">
            <img width="20" height="20" src="https://img.icons8.com/ios-glyphs/20/ffffff/google-logo--v1.png" alt="google-logo--v1" style="margin-right: 8px;" />
            Google
        </div>
    </div>
    """, unsafe_allow_html=True)