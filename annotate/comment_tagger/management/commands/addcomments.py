import csv

from django.core.management.base import BaseCommand, CommandError
from comment_tagger.models import Comment


class Command(BaseCommand):
    help = 'update database with new comments'

    def add_arguments(self, parser):
        parser.add_argument('fname', type=str)

    def handle(self, *args, **options):
        fname = options['fname']
        with open(fname, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                code = row['code']
                text = row['comment']
                comment = Comment.objects.create(code=code, text=text)
                comment.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported %s' % fname))
