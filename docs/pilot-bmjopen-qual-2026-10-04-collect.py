"""Collect the BMJ Open pilot sample: list 2024 qualitative studies (seed 20261004), download review histories from Europe PMC, keep first-round reports. Run in a scratch folder; report text never enters the repository."""
import json, urllib.request, urllib.parse, random
q='JOURNAL:"BMJ Open" AND TITLE:"qualitative study" AND PUB_YEAR:2024'
rows=[]; cur="*"
while True:
    u="https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode(dict(query=q,format="json",pageSize=1000,resultType="lite",cursorMark=cur))
    d=json.load(urllib.request.urlopen(u))
    rows+=d["resultList"]["result"]
    if d.get("nextCursorMark") in (None,cur) or not d["resultList"]["result"]: break
    cur=d["nextCursorMark"]
rows=[r for r in rows if r.get("pmcid") and "mixed" not in r["title"].lower()]
rows.sort(key=lambda r:r["pmcid"])
random.Random(20261004).shuffle(rows)
json.dump([{k:r[k] for k in ("pmcid","doi","title")} for r in rows],open("sample_order.json","w"),indent=1)
print(len(rows))
import json, urllib.request, zipfile, io, os, subprocess
rows=json.load(open("sample_order.json"))
os.makedirs("rc",exist_ok=True); got=[]
for r in rows[:30]:
    try:
        z=zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{r['pmcid']}/supplementaryFiles",timeout=60).read()))
    except Exception as e:
        print(r["pmcid"],"ERR",e); continue
    names=[n for n in z.namelist() if "review" in n.lower()]
    if not names: print(r["pmcid"],"no review file"); continue
    p=f"rc/{r['pmcid']}.pdf"; open(p,"wb").write(z.read(names[0]))
    subprocess.run(["pdftotext","-layout",p,p[:-4]+".txt"])
    got.append(r["pmcid"]); print(r["pmcid"],"ok",r["title"][:90])
import re, glob, os
os.makedirs("r1",exist_ok=True); tot=0; words=0; out=[]
start=re.compile(r"^\s*(REVIEWER(\s+NAME)?\s{2,}\S|Reviewer\s+\d+\s*$)")
for f in sorted(glob.glob("rc/*.txt")):
    t=open(f).read(); pm=os.path.basename(f)[:-4]
    m=re.search(r"VERSION 1\s*[-–]\s*REVIEW(.*?)(VERSION 1\s*[-–]\s*AUTHOR RESPONSE|VERSION 2\s*[-–]\s*REVIEW|$)",t,re.S)
    if not m: print(pm,"no v1"); continue
    reps=[]; cur=None
    for line in m.group(1).split("\n"):
        if start.match(line): cur=[]; reps.append(cur); continue
        if cur is None: continue
        if re.match(r"^\s*(REVIEWER (AFFILIATION|CONFLICT)|REVIEW RETURNED|Name\s|Affiliation\s|Date\s|COI\s|OF INTEREST|competing interests)",line): continue
        line=re.sub(r"^\s*(GENERAL COMMENTS|Comments)\s{2,}","",line)
        cur.append(line.strip())
    for i,body in enumerate(reps,1):
        txt="\n".join(body).strip()
        open(f"r1/{pm}_R{i}.txt","w").write(txt); words+=len(txt.split())
    out.append((pm,len(reps))); tot+=len(reps)
print(out); print("papers",len(out),"reports",tot,"words",words)
