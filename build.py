# -*- coding: utf-8 -*-
"""Baut aus src/ die einzelne Datei index.html.  Aufruf: python build.py"""
import os, subprocess, sys, json
ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")

def rd(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return f.read()

subprocess.check_call([sys.executable, os.path.join(SRC, "geo.py")], cwd=SRC, stdout=subprocess.DEVNULL)
geo = json.dumps(json.load(open(os.path.join(SRC, "geo.json"), encoding="utf-8")), ensure_ascii=False, separators=(",", ":"))
geo = geo.replace("</", "<" + chr(92) + "/")

kaps = [rd("kap%d.js" % i) for i in range(1, 10)]
script = "\n".join([rd("prelude.js"), "const GEO = " + geo + ";", *kaps, rd("engine.js")])

html = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#12355B">
<title>Rom – vom Dorf zum Weltreich</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
%s
</style>
</head>
<body>
<a class="skip" href="#main">Zum Inhalt springen</a>
<div id="app"></div>
<noscript><p style="padding:1em">Diese Seite braucht JavaScript.</p></noscript>
<script>
%s
</script>
</body>
</html>
""" % (rd("style.css"), script)

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
with open(os.path.join(ROOT, "tests", "bundle.js"), "w", encoding="utf-8") as f:
    f.write(script)
print("index.html: %d KB" % (len(html) // 1024))
