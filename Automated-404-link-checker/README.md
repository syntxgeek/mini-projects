# Automated 404 Link Checker (DevOps/QA)

## 🎯 Case Study: Hoboken Grace Church
I developed this tool to solve a specific problem for **Hoboken Grace Church**. Their site has 150+ pages, and manual link checking was inefficient. I built an automated solution to ensure their congregation always has access to working resources.

## 🛠️ Tech Stack
* **Lychee (Rust-based):** For high-speed link crawling.
* **GitHub Actions:** For CI/CD automation and scheduling (Cron).
* **Slack API:** For real-time team notifications.

## 🧠 Key Challenges & Solutions
* **Bot Blocking:** Identified that sites like Instagram and Amazon block automated crawlers. I implemented a `.lycheeignore` system with Regex to filter out these "false positives."
* **Handling Redirects:** Manually verified that legacy Amazon Appstore links were healthy for users even though they triggered 404s for bots, and documented these exclusions for the dev team.
* **Security:** Managed the integration using GitHub Secrets to protect the church's internal Slack Webhooks.