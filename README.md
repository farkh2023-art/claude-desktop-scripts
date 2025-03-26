# claude-desktop-scripts
Elle contient tous les scripts d’exemples organisés par outils (Notion, Puppeteer, YouTube, MCP, DeepSeek)
# 📦 Claude Desktop - Scripts d'exemples

Ce dépôt contient des **scripts d'exemple** pour interagir avec les différents outils disponibles dans la version Claude Desktop, notamment :

- 🎥 Extraction de transcription YouTube
- 📘 Automatisation de Notion
- 🌐 Navigation web avec Puppeteer
- ⚙️ Lancement de serveurs MCP (local & distant)
- 💬 Génération de texte via DeepSeek

---

## 📚 Structure du dépôt

claude-desktop-scripts/ │ ├── notion/ │ └── notion_create_database.py │ ├── puppeteer/ │ └── puppeteer_click.js │ ├── youtube/ │ └── get_transcript_example.py │ ├── mcp/ │ ├── install_local_mcp_server.sh │ └── install_repo_mcp_server.sh │ └── deepseek/ └── chat_completion_example.py


---

## 🧰 Détails des outils

### 🎥 YouTube Transcript
- **Script :** [`get_transcript_example.py`](youtube/get_transcript_example.py)
- Utilise `youtube-transcript-api` pour extraire automatiquement la transcription d'une vidéo YouTube.

### 📘 Notion
- **Script :** [`notion_create_database.py`](notion/notion_create_database.py)
- Crée une base de données dans Notion avec l'API officielle.

### 🌐 Puppeteer
- **Script :** [`puppeteer_click.js`](puppeteer/puppeteer_click.js)
- Automatise les clics sur une page web (accepter cookies, cliquer bouton, etc.).

### ⚙️ MCP Server
- **Script local :** [`install_local_mcp_server.sh`](mcp/install_local_mcp_server.sh)
- **Script en ligne :** [`install_repo_mcp_server.sh`](mcp/install_repo_mcp_server.sh)

### 💬 DeepSeek
- **Script :** [`chat_completion_example.py`](deepseek/chat_completion_example.py)
- Génère une réponse simple à un prompt conversationnel.

---

## 🛠️ Pré-requis

- Python 3.x
- Node.js (pour Puppeteer)
- Token API Notion (pour les scripts Notion)
- Clé API ou wrapper personnalisé pour Claude/DeepSeek

---

## 📜 Licence

Ce dépôt est sous licence MIT. Vous pouvez l’utiliser, le modifier, le distribuer librement.

---

## 🤝 Contribuer

Tu souhaites ajouter d'autres scripts utiles ?
- Fork le dépôt
- Crée une branche
- Propose une Pull Request ✅

---

## 🔗 Liens utiles

- [API Notion](https://developers.notion.com/)
- [Puppeteer Docs](https://pptr.dev/)
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)
- [DeepSeek](https://deepseek.com/)
