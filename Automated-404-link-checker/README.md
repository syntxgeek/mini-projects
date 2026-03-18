# 🔗 Automated 404 Link Checker (DevOps/QA)

This project provides an automated solution for maintaining website health by identifying broken links before they impact SEO or user experience. 

---

## 🎯 Case Study: Hoboken Grace Church
I developed and deployed this specific system for **Hoboken Grace Church** to monitor their 150+ page website. 

### **The Problem**
The organization relied on manual link checking, which was time-consuming and prone to human error. Legacy links (like old Amazon Appstore redirects) and bot-blocking from social media platforms created "noise" in standard reporting tools.

### **The Solution**
I engineered a custom **GitHub Actions** workflow that:
* **Automates QA:** Runs every Monday at 3:00 AM to ensure zero downtime for church resources.
* **Filters False Positives:** Implemented a regex-based `.lycheeignore` system to skip known bot-blocking sites (Instagram, LinkedIn, Gusto).
* **Legacy Support:** Manually verified and documented legacy Amazon redirects that were triggering "false" 404s, ensuring the team only receives alerts for actual breakages.
* **Real-time Alerts:** Integrated a secure **Slack Webhook** to notify the dev team instantly upon a failed scan.

### 🛡️ Smart Filtering & Bot Handling
One of the core challenges was handling "False 404s" from platforms like Instagram, LinkedIn, and YouTube that block automated crawlers. 

* **Status Code Filtering:** Instead of ignoring these domains entirely (which would hide actual broken links), I configured the workflow to `accept 403, 429` status codes. 
* **Result:** The system ignores security-based blocks but will still trigger an alert if a link returns a true `404 Not Found`.
* **Manual Verification:** I implemented a process for identifying "Bot-only 404s" (where a link works for humans but fails for bots due to YouTube Studio 'Embedding' restrictions), providing actionable data for the media team.

  
---


## 🛠️ Technical Stack
* **Tool:** [Lychee](https://github.com/lycheeverse/lychee) (High-speed Rust-based link checker).
* **CI/CD:** GitHub Actions (Cron scheduling & Workflow Dispatch).
* **Notifications:** Slack API via Incoming Webhooks.
* **Security:** GitHub Encrypted Secrets for API protection.

## 🚀 How to Use This Template
1.  **Clone the Repo:** Add the `.github/workflows/link-checker.yml` and `.lycheeignore` to your project.
2.  **Configure Target:** Update the target URL in the `.yml` file's `args` section.
3.  **Set Secrets:** Add a GitHub Repository Secret named `SLACK_WEBHOOK_URL` with your Slack Webhook URL.
4.  **Customize Ignores:** Add any site-specific patterns to `.lycheeignore`.

## 📈 Manual Trigger
To run a scan outside of the Monday 3:00 AM schedule:
1.  Navigate to the **Actions** tab in GitHub.
2.  Select **Automated 404 Link Checker**.
3.  Click **Run workflow**.

---
*Developed as a contribution to the Hoboken Grace Tech Team to improve site reliability and community engagement.*
