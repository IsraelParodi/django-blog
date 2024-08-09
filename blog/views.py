"""
Views for blog app
"""

from datetime import date
from django.http import Http404
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": """
            There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!
        """,
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """,
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": """
            Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...
        """,
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """,
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": """
            Nature is amazing! The amount of inspiration I get when walking in nature is incredible!
        """,
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """,
    },
]


# Create your views here.
def index(request):
    """
    Main page

    Args:
        request (_type_): _description_
    """
    sorted_posts = sorted(all_posts, key=lambda post: post["date"])
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    """
    Post Page

    Args:
        request (_type_): _description_
    """
    return render(request, "blog/all-posts.html", {"posts": all_posts})


def post_detail(request, slug):
    """
    Post detail page

    Args:
        request (_type_): _description_
    """
    try:
        post_found = next(post for post in all_posts if post["slug"] == slug)
        return render(request, "blog/post-detail.html", {"post": post_found})
    except Exception as error:
        raise Http404() from error
