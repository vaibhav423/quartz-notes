---
tags:
  - Keep/Color/Blue
  - Keep/Archived
---

sudo setfacl -R -m u:www-data:rwx /path # to grant perm


<VirtualHost *:80>
    DocumentRoot /

    <Directory />
        DAV On
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all denied

        AuthType Basic
        AuthName "WebDAV"
        AuthUserFile /etc/apache2/.htpasswd
        Require valid-user
    </Directory>
    RewriteRule ^/k$ /home/ubuntu/
    RewriteRule ^/$ /home/ubuntu/html/upload.html
</VirtualHost>


