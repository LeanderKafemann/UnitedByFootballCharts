import requests as r
import webbrowser as wb

print("ViewManager loading...")
print("ViewManager for UnitedByFootballCharts 1.1.0")
print("Connecting to network...")
print("Ready.")
print("Views on LK-Media...")
v3_ = str(r.get("https://lkunited.pythonanywhere.com/lkm?id=UnitedByFootball").content)
v3 = v3_[v3_.find("Views: ")+7: v3_.find("--<")]
print("LK-Media: ", v3)
print("Views on Soundcloud...")
#v2_ = str(r.get("https://soundcloud.com/burkhardffabian/united-by-football-we-are-the?si=1f31e07726254fddba00786dc206e795&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing").content)
#v2__ = v2_.find('property="soundcloud:play_count" content="')
v2 = input("Views on Soundcloud:")#v2_[v2__+42: v2__+46]
print("Soundcloud: ", v2)
print("Views on YT#1...")
v1_ = str(r.get("https://www.youtube.com/watch?v=IUxCbll1gyQ").content)
v1__ = v1_.find('"viewCount":{"simpleText":"')
v1 = v1_[v1__+27: v1__+32].replace(".", "")
print("YT#1: ", v1)
print("Views on YT#2...")
v4_ = str(r.get("https://www.youtube.com/watch?v=mSFrmj0YuqM&list=OLAK5uy_mJE6Si6ESHj2T4_V4PDW_WJqypOhK-llw").content)
v4__ = v4_.find('"viewCount":{"simpleText":"')
v4 = v4_[v4__+27: v4__+30].replace(".", "")
print("YT#2: ", v4)
print("Views on YT#3...")
v5_ = str(r.get("https://www.youtube.com/watch?v=E-ETkrYU1tM").content)
v5__ = v5_.find('"viewCount":{"simpleText":"')
v5 = v5_[v5__+27: v5__+32].replace(".", "")
print("YT#3: ", v5)
print("Views on Spotify...")
if input("Open in Webbrowser to check views?") == "":
    wb.open("https://open.spotify.com/intl-de/track/3wpOFbEemiEaw3zXDZspeq")
v6 = input("Views on Spotify: ")
vges = str(int(v1)+int(v2)+int(v3)+int(v4)+int(v5)+int(v6))
print("Gesamt: ", vges)
input("Continue...")
date = input("Enter date DD.MM.YYYY: ")
translate = input("Enter translation var: ")
SCHABLONE = """
<g class="bar" transform="translate(0, {})">
    <title>{}</title>
    <rect width="{}" height="45"/>
    <text x="{}" y="35">{}: {}</text>
    <g class="bar purple" tabindex="0">
        <rect width="{}" height="45" />
        <text x="20" y="35">YouTube #1: {}</text>
    </g>
    <g class="bar green" tabindex="0">
        <rect width="{}" height="45" x="{}" />
        <text x="{}" y="35">Soundcloud: {}</text>
    </g>
    <g class="bar yellow" tabindex="0">
        <rect width="{}" height="45" x="{}" />
        <text x="{}" y="35">LK-Media: {}</text>
    </g>
    <g class="bar orange" tabindex="0">
        <rect width="{}" height="45" x="{}" />
        <text x="{}" y="35">YouTube #2: {}</text>
    </g>
    <g class="bar red" tabindex="0">
        <rect width="{}" height="45" x="{}" />
        <text x="{}" y="35">YouTube #3: {}</text>
    </g>
    <g class="bar blue" tabindex="0">
        <rect width="{}" height="45" x="{}" />
        <text x="{}" y="35">Spotify: {}</text>
    </g>
</g>"""
#translate, date, width_ges, x_ges, date, views_ges, width_yt1, views_yt1,
#width_sc, start_sc, views_sc, width_lk, start_lk, x_lk, views_lk,
#width_yt2, start_yt2, x_yt2, views_yt2, width_yt3, x_yt3, views_yt3,
#width_sf, x_sf, views_sf
w1 = str(round(int(v1)/5))
w2 = str(round(int(v2)/5))
w3 = str(round(int(v3)/5))
w4 = str(round(int(v4)/5))
w5 = str(round(int(v5)/5))
w6 = str(round(int(v6)/5))
wges = str(int(w1)+int(w2)+int(w3)+int(w4)+int(w5)+int(w6))
s2 = w1
s3 = str(int(s2)+int(w2))
s4 = str(int(s3)+int(w3))
s5 = str(int(s4)+int(w4))
s6 = str(int(s5)+int(w5))
sEnd = int(s6)+int(w6)
print(SCHABLONE.format(translate, date, wges, str(sEnd+750), date, vges, w1, v1, w2, s2, str(int(s2)+20), v2, w3, s3, str(sEnd+50), v3, w4, s4, str(sEnd+250), v4, w5, s5, str(sEnd+500), v5, w6, s6, str(int(s6)+20), v6))
input("Finish...")