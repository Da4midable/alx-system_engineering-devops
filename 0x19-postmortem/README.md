# Postmortem: Nginx Not Listening on Port 80

## Issue Summary

**Duration of Outage**: June 14, 2024, 10:00 AM to 11:30 AM (UTC)

**Impact**: The outage affected 100% of users attempting to access the web server. Users experienced a "connection refused" error when trying to connect to the server on port 80. This resulted in a complete service disruption for all users relying on the web application hosted on the server.

**Root Cause**: Nginx was not properly configured to listen on port 80.

## Timeline

- **10:00 AM**: Issue detected via a monitoring alert indicating that the web server was not responding to HTTP requests.
- **10:05 AM**: Initial investigation by the engineer confirmed that Nginx was running but not listening on port 80.
- **10:15 AM**: Checked Nginx configuration files and found no obvious misconfigurations.
- **10:25 AM**: Restarted Nginx service, but the issue persisted.
- **10:30 AM**: Noticed an error log indicating a binding issue on port 80.
- **10:35 AM**: Suspected port 80 might be used by another service, investigated using `netstat`.
- **10:45 AM**: Confirmed no other service was using port 80.
- **10:50 AM**: Reviewed Nginx default configuration file and found the `listen` directive missing.
- **11:00 AM**: Added the `listen` directive to Nginx configuration and restarted the service.
- **11:10 AM**: Verified that Nginx was now listening on port 80 and serving requests.
- **11:30 AM**: Issue resolved and monitoring confirmed service restoration.

## Root Cause and Resolution

**Root Cause**: The root cause of the issue was a missing `listen` directive in the Nginx configuration file, which prevented Nginx from binding to port 80.

**Resolution**: The issue was resolved by adding the correct `listen` directive to the Nginx configuration file. Specifically, the following line was added to the server block in the `/etc/nginx/sites-available/default` configuration file:

```nginx
server {
    listen 80;
    server_name localhost;

    location / {
        root /var/www/html;
        index index.html index.htm;
    }
}
