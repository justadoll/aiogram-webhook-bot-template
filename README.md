# Aiogram-Webhook Bot Template

#### 1. Install Requirements 
   * `pip install -r requirements.txt`

#### 2. Change Config:
   * Rename `.env.dist` to `.env`
   * Insert your values 

#### 3. Webhook setup:
* Make get request
    `https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://your.domain.com/hook/<TOKEN>/`

#### 4. Nginx /etc/nginx/sites-avaiable/ example config with certbot (Let's Encrypt):
```
    server {
        listen 443 ssl;
        server_name your.domain.com;

        ssl_certificate /etc/letsencrypt/live/your.domain.com/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/your.domain.com/privkey.pem; # managed by Certbot
        location /hook {
                proxy_pass http://127.0.0.1:8443;
                proxy_buffering off;
                proxy_set_header X-Real-IP $remote_addr;
        }
    }
```

#### 5. Run bot:
   * `python3 app.py`
