* {
  box-sizing: border-box;
}

:root {
  --bg: #0b1020;
  --panel: #121a2c;
  --panel-strong: #182338;
  --panel-soft: #1b2640;
  --line: rgba(255, 255, 255, 0.09);
  --text: #edf3ff;
  --muted: #a2afd1;
  --primary: #7c9bff;
  --primary-strong: #5b7dff;
  --secondary: #5ae0c9;
  --highlight: #f5b65d;
  --danger: #ff7f96;
  --shadow: rgba(11, 16, 32, 0.6);
}

html, body {
  margin: 0;
  min-height: 100%;
  font-family: "Inter", sans-serif;
  background: radial-gradient(circle at top, #172547 0%, var(--bg) 42%);
  color: var(--text);
}

body {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
}

button, input, textarea {
  font: inherit;
}

.app-shell {
  width: min(1240px, 100%);
  min-height: 820px;
  display: grid;
  grid-template-columns: 280px minmax(0, 1fr);
  border: 1px solid var(--line);
  border-radius: 24px;
  overflow: hidden;
  background: rgba(10, 16, 29, 0.8);
  backdrop-filter: blur(12px);
  box-shadow: 0 30px 90px var(--shadow);
}

.sidebar {
  background: rgba(18, 26, 44, 0.95);
  border-right: 1px solid var(--line);
  padding: 24px 18px;
}

.brand-wrap {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 28px;
}

.brand-mark {
  width: 42px;
  height: 42px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, var(--secondary), var(--primary));
  color: #08111d;
  font-weight: 800;
  font-size: 1.35rem;
}

.eyebrow {
  margin: 0 0 6px;
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
}

h1, h2, p {
  margin: 0;
}

h1 {
  font-size: 1.8rem;
}

.nav {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 32px;
}

.nav-button {
  border: 1px solid var(--line);
  background: transparent;
  color: var(--text);
  padding: 14px 16px;
  border-radius: 12px;
  text-align: left;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s ease;
}

.nav-button:hover,
.nav-button.active {
  background: linear-gradient(135deg, rgba(124, 155, 255, 0.18), rgba(90, 224, 201, 0.12));
  border-color: rgba(124, 155, 255, 0.4);
}

.model-panel {
  border-top: 1px solid var(--line);
  padding-top: 20px;
}

.panel-label {
  font-size: 0.66rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 12px;
}

.model-card {
  padding: 12px 14px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--line);
  margin-bottom: 10px;
}

.model-card.active {
  background: rgba(124, 155, 255, 0.08);
  border-color: rgba(124, 155, 255, 0.35);
}

.model-card div {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  font-weight: 700;
}

.model-card span {
  opacity: 0.72;
  font-size: 0.75rem;
}

.model-card small {
  display: block;
  color: var(--muted);
  margin-top: 4px;
}

.main-panel {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.tab-panel {
  display: none;
  flex: 1;
  padding: 28px;
}

.tab-panel.active {
  display: flex;
  flex-direction: column;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding-bottom: 18px;
  border-bottom: 1px solid var(--line);
  margin-bottom: 22px;
}

.topbar h2 {
  font-size: clamp(1.4rem, 2vw, 2rem);
}

.status-pill {
  font-size: 0.76rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 7px 10px;
  border-radius: 999px;
  background: rgba(90, 224, 201, 0.12);
  color: var(--secondary);
  border: 1px solid rgba(90, 224, 201, 0.28);
}

.status-pill.beta {
  background: rgba(245, 182, 93, 0.12);
  color: var(--highlight);
  border-color: rgba(245, 182, 93, 0.3);
}

.chat-box {
  display: flex;
  flex-direction: column;
  gap: 18px;
  flex: 1;
  min-height: 440px;
  padding: 18px 8px 8px;
  overflow-y: auto;
}

.message {
  display: flex;
  gap: 12px;
  align-items: flex-end;
}

.message.user {
  justify-content: flex-end;
}

.message.user .bubble {
  background: linear-gradient(135deg, var(--primary), var(--primary-strong));
  color: white;
  border-bottom-right-radius: 8px;
}

.message.assistant .bubble {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--line);
  border-bottom-left-radius: 8px;
}

.avatar {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, var(--secondary), var(--primary));
  color: #071522;
  font-weight: 800;
  font-size: 0.9rem;
}

.message.user .avatar {
  display: none;
}

.bubble {
  max-width: min(70%, 620px);
  padding: 14px 16px;
  border-radius: 18px;
  line-height: 1.6;
  box-shadow: 0 10px 30px rgba(1, 5, 15, 0.15);
}

.bubble p {
  margin: 0;
}

.composer {
  display: flex;
  gap: 12px;
  padding-top: 18px;
  border-top: 1px solid var(--line);
  margin-top: 12px;
}

.composer input {
  flex: 1;
  border: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.02);
  color: var(--text);
  border-radius: 12px;
  padding: 16px 18px;
  outline: none;
}

.composer button,
.generate-button,
.preset-button {
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: transform 0.2s ease, opacity 0.2s ease;
}

.composer button,
.generate-button {
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  color: #061220;
  font-weight: 800;
  padding: 0 20px;
}

.composer button:hover,
.generate-button:hover,
.preset-button:hover {
  transform: translateY(-1px);
}

.experiment-layout {
  display: grid;
  grid-template-columns: minmax(280px, 420px) minmax(260px, 1fr);
  gap: 22px;
  flex: 1;
}

.experiment-form,
.art-panel {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 18px;
}

.experiment-form {
  display: flex;
  flex-direction: column;
}

.experiment-form label {
  font-weight: 600;
  margin-bottom: 10px;
}

.experiment-form textarea {
  width: 100%;
  resize: vertical;
  min-height: 130px;
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 14px 16px;
  background: rgba(9, 14, 24, 0.72);
  color: var(--text);
}

.preset-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 18px 0;
}

.preset-button {
  background: rgba(255, 255, 255, 0.04);
  color: var(--text);
  border: 1px solid var(--line);
  padding: 9px 12px;
}

.generate-button {
  padding: 14px 18px;
  width: 100%;
  margin-top: auto;
}

.art-panel {
  display: flex;
  flex-direction: column;
}

.art-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 14px;
  color: var(--muted);
}

.license-badge {
  font-size: 0.72rem;
  padding: 5px 8px;
  border: 1px solid rgba(90, 224, 201, 0.2);
  color: var(--secondary);
  border-radius: 999px;
  background: rgba(90, 224, 201, 0.08);
}

.pixel-art-wrap {
  flex: 1;
  background: linear-gradient(180deg, #0d1426 0%, #0b1221 100%);
  border: 1px solid var(--line);
  border-radius: 16px;
  display: grid;
  place-items: center;
  padding: 16px;
  min-height: 360px;
}

#pixel-art-canvas {
  width: min(100%, 320px);
  height: auto;
  image-rendering: pixelated;
  background: #111d30;
  border-radius: 12px;
  box-shadow: 0 18px 30px rgba(12, 18, 30, 0.5);
}

@media (max-width: 920px) {
  body {
    padding: 18px;
  }

  .app-shell {
    grid-template-columns: 1fr;
  }

  .sidebar {
    border-right: none;
    border-bottom: 1px solid var(--line);
  }

  .experiment-layout {
    grid-template-columns: 1fr;
  }
}
