from django.shortcuts import redirect, render, get_object_or_404

from .models import Destination, Comments
from django.contrib.auth.decorators import login_required
from .models import Destination, VisitorTracking


# Create your views here.

def index(request):
    
   
    dects = Destination.objects.all()
    
    return render(request, 'index.html', {'dects' : dects})




def description(request, id):
        dect = get_object_or_404(Destination, id=id)    
        comments = Comments.objects.filter(destination_name=dect, parent=None)  # Get only top-level comments (not replies)
        total_comments = Comments.objects.filter(destination_name=dect, parent=None).count()
        
            

        if request.user.is_authenticated:
            if request.method == 'POST':
                comment_text = request.POST.get('comment')
                parent_id = request.POST.get('parent_id')  # Get the parent comment ID (if it's a reply)
                

                if comment_text:
                    parent_comment = None
                    if parent_id:
                        parent_comment = Comments.objects.get(id=parent_id)  # Get the parent comment

                    comment = Comments.objects.create(
                        comment=comment_text,
                        user=request.user,
                        destination_name=dect,
                        parent=parent_comment  # Assign parent comment (or None if it's a top-level comment)
                    )
                    return redirect('description', id=dect.id)
        else:
            return redirect('login')

        return render(request, 'description.html', {'dect': dect, 'comments': comments, 'total_comments':total_comments})


def like_dislike_comment(request, comment_id, action):
    comment = get_object_or_404(Comments, id=comment_id)

    if request.user.is_authenticated:
        if action == 'like':
            if request.user in comment.likes.all():
                comment.likes.remove(request.user)  # Unlike if already liked
            else:
                comment.likes.add(request.user)  # Like
                comment.dislikes.remove(request.user)  # Remove dislike if present
        
        elif action == 'dislike':
            if request.user in comment.dislikes.all():
                comment.dislikes.remove(request.user)  # Remove dislike
            else:
                comment.dislikes.add(request.user)  # Dislike
                comment.likes.remove(request.user)  # Remove like if present
    else:
        return redirect('login')

    return redirect(request.META.get('HTTP_REFERER', 'description'))  # Redirect back to the same page