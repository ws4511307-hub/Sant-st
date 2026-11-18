import sqlite3
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "chave_secreta_athletepulse_super_segura"
DB_NAME = "usuarios.db"


# 1. Cria o banco de dados e a tabela de usuários automaticamente
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha_hash TEXT NOT NULL
        )
    """)

    # Cria um usuário padrão de teste caso o banco esteja vazio
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", ("treinador@equipe.com",))
    if not cursor.fetchone():
        senha_criptografada = generate_password_hash("123456")
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)",
            ("Treinador Principal", "treinador@equipe.com", senha_criptografada),
        )

    conn.commit()
    conn.close()


# 2. Rota da tela de Login
@app.route("/")
@app.route("/login")
def login_page():
    return render_template("login.html")


# 3. Rota que recebe o e-mail e senha do formulário e valida no banco
@app.route("/api/login", methods=["POST"])
def api_login():
    dados = request.get_json()
    email = dados.get("email", "").strip().lower()
    senha = dados.get("password", "")

    if not email or not senha:
        return jsonify({"sucesso": False, "mensagem": "Preencha e-mail e senha."}), 400

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, senha_hash FROM usuarios WHERE email = ?", (email,))
    usuario = cursor.fetchone()
    conn.close()

    if usuario and check_password_hash(usuario[2], senha):
        session["usuario_id"] = usuario[0]
        session["usuario_nome"] = usuario[1]
        return jsonify({
            "sucesso": True,
            "mensagem": f"Bem-vindo, {usuario[1]}! Entrando no painel...",
            "redirect": "/dashboard"
        })

    return jsonify({"sucesso": False, "mensagem": "E-mail ou senha incorretos."}), 401


# 4. Rota para cadastrar novos usuários no banco
@app.route("/api/registrar", methods=["POST"])
def api_registrar():
    dados = request.get_json()
    nome = dados.get("nome", "Novo Treinador").strip()
    email = dados.get("email", "").strip().lower()
    senha = dados.get("password", "")

    if not email or not senha:
        return jsonify({"sucesso": False, "mensagem": "Informe e-mail e senha para cadastrar."}), 400

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        senha_hash = generate_password_hash(senha)
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)",
            (nome, email, senha_hash),
        )
        conn.commit()
        conn.close()
        return jsonify({"sucesso": True, "mensagem": "Conta criada com sucesso! Já pode entrar."})
    except sqlite3.IntegrityError:
        return jsonify({"sucesso": False, "mensagem": "Este e-mail já está cadastrado."}), 409


# 5. Rota protegida do Dashboard
@app.route("/dashboard")
def dashboard_page():
    if "usuario_id" not in session:
        return redirect(url_for("login_page"))
    return f"""
    <body style="background:#050505; color:#fff; font-family:sans-serif; padding:40px;">
      <h1 style="color:#a3e635;">Bem-vindo ao Dashboard, {session['usuario_nome']}!</h1>
      <p>Login autenticado com sucesso pelo banco de dados SQLite.</p>
      <a href="/logout" style="color:#bef264;">Sair</a>
    </body>
    """


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_page"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
