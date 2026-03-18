import requests
from datetime import datetime
import pytz

def format_event_schedule():
    url = "https://www.scaler.com/academy/mentee/events"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.scaler.com/academy/mentee-dashboard/todos?utm_medium=direct&utm_source=none&utm_content=/",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRF-Token": "e+U7MbVYUuHx6q1rpGX2tlYhgi6A3F0wuDiz7XCYoRvbHPAI/ISSVkoaaziOm//j2QUAVNyxgQTipug0HKy3DQ==",
        "App-Name": "desktop",
        "Cookie": "_clck=19nm5sr%5E2%5Eg2u%5E0%5E2177; _scaler_session=YTAyMEhhbnBuWUozdmhJS0t6cXU0Z0FUV1gyc2JYMFdrRFNjdnFVZkVtMGlId1VvL251bHJrTTQyVHZqNU42Sy9wcDdaZTZlRUwzY0ZLMDc0ZUlrNVV3MDlaUmhQZmEyVldBUk5UNENJYVZRa0VuZTl6SXFWemp2NEI2WTRybkRWWTVjc3BsdDBkL1VXakdoNC9YTm5DUjZuNS94YTNML0hKNFhHdkoxSVR1VUliUndtSTQyS0FIZDRlYWw5ajNTaEJYektMb2hhWFR4eDhSVitMWU40VmVUQW1qM0I5Mk9yZDhRVXFHVzFNWGtVU0VNclJBTUZFSXgrQWN1VGFWMTBXc0lZVzBNQnhhV3hWR3NDT3g0U1N0djFHTUdsTVoraW1idXNQVHlROTlmOUZBK0lXQ25hLzdCQSt4NXo2d3VpS1czZkFNT3JKSCs3bnBKUTB2SThkeXlXMU5PR0QrbmlFb3ZhSkEwZUdKdWhVaEVJTWZvRFBNMTJzKzZOMFpSMWNxUUp4NFJIZWVYU3M1YXFEWmVndHdsZFRqeFBwQWZVKzdGVHBnaStlN1V6N1FQSlA0eXJMODEyT3ozM2R2N0pUSmVjNzJrOWMyV2tmTUJ6eC9jMllEdWlsUVZod1pnSEVZVlZHT3hvMW10VERpdUtnZk1BaENTeWZ3SHJlamo1YU5Cd2dZRm9HSWdxR2lnb0RpMkxWSXdzU3dOcCt1YzFCUER2dWk4VDFiNnNvZlZRb3l1MnlSRXZPcE5mN3h6LS1kdXZ1SjNrWGxzTlozOHRydnBWcTZBPT0%3D--9bff344abc8086d37c1a52bc11cace93d0c2d149; XSRF-TOKEN=bBGjbWlAHDdeuRlu2VX1WShEM3oDmnqq76bNT%2B9ZqMrM6GhUIJzcgOVJ3z3zq%2FwMp2CxAF%2F3pp61OJaWg22%2B3A%3D%3D; remember_user_token=W1s3NTA1MTYzXSwiNXduc2c3Q3hOc2lTTXJkUHd0NjUiLCIxNzY4Nzk4NTIxLjkzNTgyMDMiXQ%3D%3D--48c8e1aa8c158192f55af68c8dbaef481fe8de23; auth_session_id=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzLmFjY291bnRzLnNjYWxlci5jb20iLCJhdWQiOiJzY2FsZXIiLCJzdWIiOiJzY2FsZXIjdXNlciM3NTA1MTYzIiwic2Vzc2lvbl9pZCI6InNlc3Npb24jYWN0aXZlIzM4U2dqYlBlcTBWNkR0Qjh6c3E1bHBLTFltdiIsImlhdCI6MTc2ODc5ODUyMSwic2Vzc2lvbl9zb3VyY2UiOiJzZWNvbmRhcnkiLCJleHAiOjE3NzEzOTA1MjF9.0eDTlcEH-6r79jAvCnEEHNmZ_mw9grZg7jpzdYNskEI"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except Exception:
        return

    events = data.get("futureEvents", [])
    if not events:
        return

    grouped_events = {}
    ist = pytz.timezone('Asia/Kolkata')

    for event in events:
        utc_dt = datetime.strptime(event['date'], "%Y-%m-%dT%H:%M:%S.000Z")
        utc_dt = pytz.utc.localize(utc_dt)
        ist_dt = utc_dt.astimezone(ist)
        
        date_str = ist_dt.strftime("%a %d/%m")
        time_str = ist_dt.strftime("%I:%M %p").lower()
        
        if date_str not in grouped_events:
            grouped_events[date_str] = []
        
        grouped_events[date_str].append(f"[{time_str}] : {event['title']}")

    # Sort dates by actual datetime value
    dates = sorted(grouped_events.keys(), key=lambda d: datetime.strptime(d, "%a %d/%m"))
    for date in dates:
        print(f"[{date}]\n-------")
        for session in grouped_events[date]:
            print(f"{session}")
        print("--------------------------------------------------------")

if __name__ == "__main__":
    format_event_schedule()

