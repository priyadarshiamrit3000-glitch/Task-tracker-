#!/usr/bin/env python3
"""Recompute the Content-Security-Policy in index.html.

Run after ANY edit to the inline <script> or <style> in index.html:
    python3 tools/update-csp.py
The page only runs code/styles whose hash is listed in the policy, so a stale
hash makes the browser block the app (fail closed).
"""
import base64, hashlib, re, sys
path = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
s = open(path, encoding='utf-8').read()
def h(tag):
    m = re.findall(r'<%s>(.*?)</%s>' % (tag, tag), s, re.S)
    assert len(m) == 1, 'expected exactly one inline <%s>' % tag
    return "'sha256-%s'" % base64.b64encode(hashlib.sha256(m[0].encode('utf-8')).digest()).decode()
csp = ("default-src 'none'; script-src %s; style-src %s; "
       "connect-src https://script.google.com https://script.googleusercontent.com; "
       "img-src data:; base-uri 'none'; form-action 'none'; object-src 'none'") % (h('script'), h('style'))
s, n = re.subn(r'(<meta http-equiv="Content-Security-Policy" content=")[^"]*(">)', lambda m: m.group(1) + csp + m.group(2), s)
assert n == 1
open(path, 'w', encoding='utf-8').write(s)
print('CSP updated')
