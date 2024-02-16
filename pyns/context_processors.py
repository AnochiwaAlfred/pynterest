




from pyns.models import *


def frontendContent(request):
    context = {}
    context['pyns_online'] = [
        "https://i.pinimg.com/736x/b7/bb/c9/b7bbc9a4340900f7215f795af3cc6913.jpg",
        "https://i.pinimg.com/236x/70/03/bd/7003bd82665123649e1dbffeb347cfc5.jpg",
        "https://i.pinimg.com/236x/46/df/89/46df897a502f6af49155e6266d32f5de.jpg",
        "https://i.pinimg.com/236x/a4/3f/6f/a43f6fc04385b1d1a28ea8ecae635902.jpg",
        "https://i.pinimg.com/236x/91/33/ca/9133cad615af0dd04b515c6e3b90d00a.jpg",
        "https://i.pinimg.com/236x/11/0a/0b/110a0b4c85e5c6411a08ca250d5b0e2e.jpg",
        "https://i.pinimg.com/236x/a0/ab/e1/a0abe142ebfc046db34dc35fa1c7c522.jpg",
        "https://i.pinimg.com/236x/eb/b8/79/ebb879de3d701a9fdca42e786df650dd.jpg",
        "https://i.pinimg.com/236x/fa/93/71/fa93718a0487425e07250c21fd88f0dd.jpg",
        "https://i.pinimg.com/236x/f6/0f/7e/f60f7e6c43346bcfbbf682d8bd7882bb.jpg",
        "https://i.pinimg.com/236x/70/11/e1/7011e173cf9ed72f3a2958ab91e915c2.jpg",
        "https://i.pinimg.com/236x/f6/0f/7e/f60f7e6c43346bcfbbf682d8bd7882bb.jpg",
        "https://i.pinimg.com/564x/91/91/a5/9191a5d529bae0099d6ba59d19908740.jpg",
        "https://i.pinimg.com/236x/c9/13/e6/c913e634053d4b3ffbb52e141c216d6c.jpg",
        "https://i.pinimg.com/474x/a8/55/08/a8550836913397c989ac7ee7482e1b8d.jpg",
        "https://i.pinimg.com/236x/b6/5a/ac/b65aacf621f34ae3398d6527a3f731a7.jpg",
    ]
    context['pyns'] = Pyn.objects.all()
    likes = [like.pyn for like in Likes.objects.filter(user_id=request.user.id)]
    context["likes"]=likes
    
    return context