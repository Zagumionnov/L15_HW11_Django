from django.core.management.base import BaseCommand
from polls.models import Question as Poll
from faker import Faker


class Command(BaseCommand):
    help = 'Create question for polls'

    def add_arguments(self, parser):
        parser.add_argument('-q', '--question', type=int, default=10)

    def handle(self, *args, **options):
        faker = Faker()
        self.stdout.write('Start create question')
        for _ in range(options['question']):
            poll = Poll()
            poll.question_text = faker.sentence(nb_words=5).replace(".", "?")
            poll.pub_date = faker.date_time()
            poll.opened = bool()
            poll.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully inserted {options['question']} polls"))

