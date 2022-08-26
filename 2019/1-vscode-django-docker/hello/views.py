from datetime import datetime

from django.shortcuts import redirect, render
from django.views.generic import ListView

from hello.forms import LogMessageForm
from hello.models import LogMessage


class HomeListView(ListView):
    """Renders the home page, with a list of all polls."""

    model = LogMessage

    def get_context_data(self, **kwargs):
        return super(HomeListView, self).get_context_data(**kwargs)


def about(request):
    """Renders the about page."""
    return render(request, "hello/about.html")


def contact(request):
    """Renders the contact page."""
    return render(request, "hello/contact.html")


def hello_there(request, name):
    """Renders the hello_there page.
    Args:
        name: Name to say hello to
    """
    return render(
        request, "hello/hello_there.html", {"name": name, "date": datetime.now()}
    )


def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method != "POST" or not form.is_valid():
        return render(request, "hello/log_message.html", {"form": form})
    message = form.save(commit=False)
    message.log_date = datetime.now()
    message.save()
    return redirect("home")
