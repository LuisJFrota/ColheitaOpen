from apscheduler.schedulers.background import BackgroundScheduler
from services.email_services import send_email
from services.rent_services import get_all_rents
from datetime import datetime, timedelta

def check_deadlines():
    rents = get_all_rents()

    now = datetime.now()

    for rent in rents:
        deadline = rent.date 
        customer_email = rent.client.email

        if deadline - timedelta(hours=1) <= now < deadline:
            send_email(
                to=customer_email,
                subject="Lembrete de devolução",
                message=f"Olá! Seu prazo de devolução expira em 1 hora."
            )

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_deadlines, 'interval', minutes=5)  
    scheduler.start()
