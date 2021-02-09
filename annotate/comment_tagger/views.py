from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Comment, Tag


def _get_new_comment(user):
    # TODO: add ownership property between user and comments
    in_review = Comment.objects.filter(in_review_by=user.id).first()
    return in_review if in_review else Comment.objects.filter(in_review_by=0, reviewed_by=0).first()


def _get_comment(comment_id):
    return get_object_or_404(Comment, id=comment_id)


def _load_tags(comment):
    tags = Tag.objects.all().order_by('text')
    used_tags = comment.tag_set.all().order_by('text')
    return tags, used_tags


def _build_common_context(comment):
    tags, used_tags = _load_tags(comment)
    return {
        'comment': comment,
        'comment_count': Comment.objects.count(),
        'unused_tags': [tag for tag in tags],
        'used_tags': list(used_tags),
    }


@login_required
def index(request):
    comment = _get_new_comment(request.user)
    comment.in_review_by = request.user.id
    comment.save()
    context = _build_common_context(comment)
    return render(request, 'comment_tagger/index.html', context)


@login_required
def complete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.reviewed_by = request.user.id
    comment.in_review_by = 0
    comment.save()
    return redirect(index)


@login_required()
def create_tag(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    tag = Tag(text=request.POST['tag_text'])
    tag.save()
    comment.tag_set.add(tag)
    comment.save()
    return redirect(request.META['HTTP_REFERER'], comment_id=comment_id)


@login_required()
def tag(request, comment_id, tag_id):
    comment = Comment.objects.get(id=comment_id)
    tag = Tag.objects.get(id=tag_id)
    comment.tag_set.add(tag)
    comment.save()
    return redirect(request.META['HTTP_REFERER'], comment_id=comment_id)


@login_required()
def remove(request, comment_id, tag_id):
    comment = Comment.objects.get(id=comment_id)
    tag = Tag.objects.get(id=tag_id)
    comment.tag_set.remove(tag)
    comment.save()
    return redirect(request.META['HTTP_REFERER'], comment_id=comment_id)


@login_required()
def select(request, comment_id):
    comment = _get_comment(comment_id)
    context = _build_common_context(comment)
    return render(request, 'comment_tagger/index.html', context)


@login_required()
def prev(request, comment_id):
    return redirect(reverse('comments.select', args=[comment_id - 1]))


@login_required()
def next(request, comment_id):
    return redirect(reverse('comments.select', args=[comment_id + 1]))
