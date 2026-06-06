import random
import textwrap

from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth import get_user_model

from applications.models.company import Company
from applications.models.vacancy import Vacancy
from applications.models.comment import Comment


def _short_text(prefix, i):
    return f"{prefix} {i} - " + ("Sample description. " * 3).strip()


class Command(BaseCommand):
    help = "Populate database with sample Users, Companies, Vacancies and Comments."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=100, help="Number of vacancies to create")

    @transaction.atomic
    def handle(self, *args, **options):
        count = options.get("count") or 100
        User = get_user_model()

        # Create some employer users and companies first
        num_employers = max(5, count // 5)
        employers = []
        companies = []
        for i in range(num_employers):
            username = f"employer_{i}"
            user, created = User.objects.get_or_create(
                username=username,
                defaults={"email": f"{username}@example.com", "role": "employer"},
            )
            if created:
                user.set_password("password")
                user.save()

            employers.append(user)

            company, _ = Company.objects.get_or_create(
                company_name=f"Company {i}",
                defaults={"user": user, "description": _short_text("Company description", i)},
            )
            companies.append(company)

        # Ensure at least one student user exists for comments
        student, _ = User.objects.get_or_create(
            username="student_1", defaults={"email": "student1@example.com", "role": "student"}
        )

        # Create vacancies
        created_vacancies = []
        for i in range(count):
            comp = random.choice(companies)
            title = f"Vacancy Title {i}"
            description = _short_text("Vacancy description", i)
            vacancy = Vacancy.objects.create(
                company=comp,
                title=title,
                description=description,
                is_active=True,
                job_type=random.choice(["full_time", "part_time", "contract", "freelance", "internship"]),
                salary_min=random.randint(200, 1000) * 10,
                salary_max=random.randint(1001, 5000) * 10,
                experience_years=random.choice([0, 1, 2, 3, 5, 10]),
            )
            created_vacancies.append(vacancy)

        # Create comments: 0-3 comments per vacancy
        all_users = list(User.objects.all())
        total_comments = 0
        for v in created_vacancies:
            for j in range(random.randint(0, 3)):
                author = random.choice(all_users) if all_users else student
                Comment.objects.create(user=author, vacancy=v, body=f"Comment {j} on {v.title}")
                total_comments += 1

        self.stdout.write(self.style.SUCCESS(f"Created {len(employers)} employers, {len(companies)} companies, {len(created_vacancies)} vacancies and {total_comments} comments."))
