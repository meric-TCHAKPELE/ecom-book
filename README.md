# 🚀 E-Book Landing Page — Guide de déploiement

Formation : **E-Commerce & Dropshipping Masterclass**
Auteur     : **TCHEKPELE Koboyo Méric**

---

## Structure du projet

```
ecom_backend/
├── app.py               ← Serveur Flask (back-end)
├── templates/
│   └── index.html       ← Page d'atterrissage (front-end)
├── requirements.txt     ← Dépendances Python
├── Procfile             ← Commande de démarrage (Railway / Render)
└── README.md            ← Ce fichier
```

---

## Comment ça marche

```
Visiteur
   │
   ▼
GET /              → affiche la page de vente (index.html)
   │
   │  clique sur "Obtenir l'E-Book"
   ▼
GET /acheter       → enregistre le clic dans les logs
   │                 puis redirige (HTTP 302)
   ▼
https://xenniebt.mychariow.shop/prd_ovnmq5   ← page Chariow
```

Le paramètre `?source=` permet de tracer l'origine :
- `/acheter?source=instagram`
- `/acheter?source=tiktok`
- `/acheter?source=whatsapp`

---

## Déploiement sur Railway (recommandé — gratuit)

### 1. Installer Railway CLI
```bash
npm install -g @railway/cli   # ou télécharger depuis railway.app
```

### 2. Créer un compte sur https://railway.app

### 3. Déployer
```bash
cd ecom_backend
railway login
railway init          # créer un nouveau projet
railway up            # déployer
```

Railway détecte automatiquement Python + le Procfile.
Votre site sera disponible sur une URL du type :
`https://votre-projet.up.railway.app`

---

## Déploiement sur Render (alternatif — gratuit)

1. Créer un compte sur https://render.com
2. New → Web Service → connecter votre repo GitHub
3. Paramètres :
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command**  : `gunicorn app:app --bind 0.0.0.0:$PORT`
4. Cliquer sur **Deploy**

---

## Tester en local

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur
python app.py

# Ouvrir dans le navigateur
# http://localhost:5000
```

---

## Personnaliser les sources de trafic

Utilisez des liens différents selon vos canaux marketing :

| Canal       | Lien à partager                         |
|-------------|------------------------------------------|
| Instagram   | `https://votre-site.com/acheter?source=instagram` |
| TikTok      | `https://votre-site.com/acheter?source=tiktok`    |
| WhatsApp    | `https://votre-site.com/acheter?source=whatsapp`  |
| Facebook    | `https://votre-site.com/acheter?source=facebook`  |
| Direct      | `https://votre-site.com/acheter`                  |

Les statistiques apparaissent dans les **logs du serveur**.

---

## Endpoints disponibles

| Route          | Description                          |
|----------------|--------------------------------------|
| `GET /`        | Page de vente (affiche)              |
| `GET /acheter` | Redirige vers Chariow                |
| `GET /api/stats` | Info JSON (sanity check)           |
| `GET /health`  | Vérification santé du serveur        |
