import pychromecast
import time

"""from pychromecast.controllers.youtube import YouTubeController

chromecasts = pychromecast.get_chromecasts()
tv = chromecasts[0][0]
tv.wait()

youtube = YouTubeController()

# Conecta YouTubeController al dispositivo Chromecast
tv.register_handler(youtube)

# Reproduce un video de YouTube
youtube.play_video('_0wdproot34')

"""
NAME = "COMEDOR"

chromecasts = pychromecast.get_chromecasts()[0]

cast = list(filter(lambda i: i.cast_info.friendly_name.startswith(NAME), chromecasts))[0]
cast.wait()

print(f"Conectado a {cast.cast_info.friendly_name}")

video_path = 'https://www.videozas.com/media_gratis/imagenes_landings/encanto/es/video-invitacion-encanto-digital-whatsapp.jpg'

mc = cast.media_controller
mc.play_media(video_path, 'image/jpg')
mc.block_until_active()

"""
crear un servidor django y postear un video en tiempo real, luego de eso pasarle el url a el chrome para que lo vea
"""