from django.shortcuts import render

def home(request):
    return render(request, "overview.html")
def overview(request):
    return render(request, "overview.html")
def calendar(request):
    days = list(range(18, 32))              # 18–31
    scheduled = [20, 21, 22]                # ডেমো: যেসব দিনে স্লট দেখাব

    upcoming = [
        {"date": "Mon, Jan 20", "time": "09:00", "status": "scheduled",
         "text": "Monday motivation post with team photo", "icons": ["Facebook","Instagram"]},
        {"date": "Mon, Jan 20", "time": "10:00", "status": "scheduled",
         "text": "Industry news update and our thoughts", "icons": ["TikTok"]},
        {"date": "Tue, Jan 21", "time": "11:20", "status": "scheduled",
         "text": "Thought leadership article about social media trends", "icons": ["Twitter","Facebook"]},
        {"date": "Wed, Jan 22", "time": "18:00", "status": "draft",
         "text": "Behind-the-scenes video content", "icons": ["TikTok","Facebook"]},
    ]
    stats = {"week": 12, "month": 45, "drafts": 3}

    return render(request, "calendar.html", {
        "days": days,
        "scheduled": scheduled,
        "upcoming": upcoming,
        "stats": stats,
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

