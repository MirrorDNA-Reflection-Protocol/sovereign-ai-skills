# /cert — SSL Certificate Monitor

Check SSL certificate expiry for all live domains.

## Steps

1. **Check all domains**
```bash
for domain in activemirror.ai beacon.activemirror.ai id.activemirror.ai docs.activemirror.ai; do
  echo -n "$domain: "
  echo | openssl s_client -servername $domain -connect $domain:443 2>/dev/null | openssl x509 -noout -dates 2>/dev/null | grep notAfter | sed 's/notAfter=//'
done
```

2. **Flag any expiring within 14 days**
3. **Report table**: domain, expiry date, days remaining, status
