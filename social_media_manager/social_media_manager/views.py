from django.shortcuts import render

def home(request):
    return render(request, "overview.html")
def overview(request):
    return render(request, "overview.html")
def calendar(request):
    upcoming = [
        {"date": "Mon, Jan 20", "time": "09:00", "status": "scheduled",
         "text": "Monday motivation post with team photo", "icons": ["facebook", "instagram"]},
        {"date": "Mon, Jan 20", "time": "10:00", "status": "scheduled",
         "text": "Industry news update and our thoughts", "icons": ["tiktok"]},
        {"date": "Tue, Jan 21", "time": "11:20", "status": "scheduled",
         "text": "Thought leadership article about social media trends", "icons": ["twitter","facebook"]},
        {"date": "Wed, Jan 22", "time": "18:00", "status": "draft",
         "text": "Behind-the-scenes video content", "icons": ["tiktok","facebook"]},
    ]
    stats = {"week": 12, "month": 45, "drafts": 3}
    days = list(range(18, 32))

    return render(request, "calendar.html", {
        "upcoming": upcoming,
        "stats": stats,
        "days": days,
    })
def compose(request):
    return render(request, "compose.html")
def analytics(request):
    return render(request, "analytics.html")
def accounts(request):
    return render(request, "accounts.html")
def inbox(request):
    return render(request, "inbox.html")
def team(request):
    return render(request, "team.html")
def settings(request):
    return render(request, "settings.html")

