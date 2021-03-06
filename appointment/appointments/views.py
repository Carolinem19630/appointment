from django.shortcuts import render, redirect
from .models import Appointment, Attendee

# Create your views here.

def index(request):
    return render(request, "appointments/index.html", {
        "appointments": Appointment.objects.all()
    })

def appointments(request, appointments_id):
    appointment = Appointment.objects.get(id=appointments_id)
    attendees = appointment.attendees.all()
    non_attendees = Attendee.objects.exclude(appointments=appointment).all()
    return render(request, "appointments/appointment.html", {
        "appointment": appointment,
        "attendees": attendees,
        "non_attendees": non_attendees
    })

def attend(request, appointments_id):

    # For a post request, add a new appointment
    if request.method == "POST":

        # Accessing the appointment
        appointment = Appointment.objects.get(pk=appointments_id)

        # Finding the attendee id from the submitted form data
        attendee_id = int(request.POST["attendee"])

        # Finding the attendee based on the id
        attendee = Attendee.objects.get(pk=attendee_id)

        # Add attendee to the appointment
        attendee.appointments.add(appointment)

        # Redirect user to appointment page
        return HttpResponseRedirect(reverse("appointments", args=(appointments.id,)))