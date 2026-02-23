# Bright Finch Coaching — Website

## 📸 IMAGE CHECKLIST (pull from old site before going live!)

Go to https://www.brightfinchcoaching.com and save the following:

| File to save as | Source on old site |
|---|---|
| `images/hero.jpg` | Hero zebra finch / nature background |
| `images/offering-1.jpg` | Clarity & Momentum offering image |
| `images/offering-2.jpg` | Rise & Realign offering image |
| `images/offering-3.jpg` | Reset & Reconnect offering image |
| `images/retreat.jpg` | Bordeaux / Clarity Uncorked image |
| `images/jen.jpg` | Jen's headshot (IMG_8474) |
| `images/contact.jpg` | Contact section photo |
| `images/logo.png` | Bright Finch logo |

> To save images: right-click → "Save image as..." or use browser dev tools → Network → Images

## 📝 Form Setup (Formspree)
1. Go to https://formspree.io → create a free account
2. Create a new form → copy the form ID
3. In `contact.html`, replace `REPLACE_ME` in the form action URL

## 🚀 Deploying to GitHub Pages

1. Create a new GitHub repo (e.g. `brightfinchcoaching`)
2. Push all files from this folder
3. Go to repo Settings → Pages → Source: main branch / root
4. Site will be live at `https://yourusername.github.io/brightfinchcoaching`

## 🌐 Moving Domain to Cloudflare + GitHub Pages

1. **Sign up at Cloudflare** (free tier is fine)
2. Add your domain `brightfinchcoaching.com`
3. Cloudflare will scan existing DNS records
4. Update your domain registrar nameservers to Cloudflare's (shown in onboarding)
5. In Cloudflare DNS, add:
   - `A` record: `@` → `185.199.108.153`
   - `A` record: `@` → `185.199.109.153`
   - `A` record: `@` → `185.199.110.153`
   - `A` record: `@` → `185.199.111.153`
   - `CNAME` record: `www` → `yourusername.github.io`
6. In GitHub repo Settings → Pages → Custom domain: enter `brightfinchcoaching.com`
7. Check "Enforce HTTPS" (after cert provisions, ~10 min)

## File Structure
```
/
├── index.html        ← Home
├── offerings.html    ← Offerings
├── about.html        ← About Jen
├── contact.html      ← Contact / Book
├── css/
│   └── style.css
├── js/
│   └── main.js
└── images/           ← Add images here!
    └── (empty — see checklist above)
```
