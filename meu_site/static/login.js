
document.addEventListener("DOMContentLoaded", () => {
  const passwordInput = document.getElementById("password");
  const togglePasswordBtn = document.getElementById("togglePassword");
  const eyeOpen = document.getElementById("eyeOpen");
  const eyeClosed = document.getElementById("eyeClosed");
  const loginForm = document.getElementById("loginForm");
  const statusToast = document.getElementById("statusToast");

  // --- CARROSSEL LENDO AS IMAGENS DO HTML ---
  const slides = document.querySelectorAll(".sip-slide-img");
  const sportBadge = document.querySelector(".sip-sport-badge");
  const sportNameEl = document.getElementById("sportName");
  const dotsContainer = document.getElementById("sliderDots");

  let currentSlide = 0;

  if (slides.length > 0) {
    const firstSlide = slides.item(0);
    sportNameEl.textContent = firstSlide.getAttribute("data-sport");

    slides.forEach((_, idx) => {
      const dot = document.createElement("span");
      dot.className = idx === 0 ? "sip-dot active" : "sip-dot";
      dotsContainer.appendChild(dot);
    });

    const dots = dotsContainer.querySelectorAll(".sip-dot");

    setInterval(() => {
      slides.item(currentSlide).classList.remove("active");
      dots.item(currentSlide).classList.remove("active");

      currentSlide = (currentSlide + 1) % slides.length;

      const nextSlide = slides.item(currentSlide);
      nextSlide.classList.add("active");
      dots.item(currentSlide).classList.add("active");

      const nextSport = nextSlide.getAttribute("data-sport");
      sportBadge.classList.add("switching");
      setTimeout(() => {
        sportNameEl.textContent = nextSport;
        sportBadge.classList.remove("switching");
      }, 200);
    }, 4500);
  }

  // --- FUNÇÕES DO FORMULÁRIO ---
  function showFeedback(message) {
    statusToast.textContent = message;
    statusToast.classList.add("visible");
  }

  togglePasswordBtn.addEventListener("click", () => {
    const isPassword = passwordInput.type === "password";
    passwordInput.type = isPassword ? "text" : "password";

    eyeOpen.classList.toggle("sip-hidden", isPassword);
    eyeClosed.classList.toggle("sip-hidden", !isPassword);

    togglePasswordBtn.setAttribute(
      "aria-label",
      isPassword ? "Esconder a senha" : "Mostrar a senha"
    );
    togglePasswordBtn.setAttribute("aria-pressed", String(isPassword));
  });

    loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = passwordInput.value;

    if (!email || !password) {
      showFeedback("Por favor, preencha seu e-mail e senha para entrar.");
      return;
    }

    try {
      const resposta = await fetch("/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
      });

      const resultado = await resposta.json();
      showFeedback(resultado.mensagem);

      if (resultado.sucesso) {
        setTimeout(() => {
          window.location.href = resultado.redirect;
        }, 1000);
      }
    } catch (erro) {
      showFeedback("Erro ao conectar com o servidor Python.");
    }
  });


  document.getElementById("googleBtn").addEventListener("click", () => {
    showFeedback("Autenticação com Google iniciada.");
  });

  document.getElementById("resetPasswordLink").addEventListener("click", (e) => {
    e.preventDefault();
    showFeedback("Link de recuperação de senha enviado para o seu e-mail.");
  });

  document.getElementById("createAccountLink").addEventListener("click", (e) => {
    e.preventDefault();
    showFeedback("Redirecionando para a tela de cadastro...");
  });
});