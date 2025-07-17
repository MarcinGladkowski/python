from media_tools.audio.utils import enhance as enhance_audio
from media_tools.graphics.utils import enhance as enhance_graphics

print("enhance audio")
enhance_audio()
print("enhance graphics")
enhance_graphics()

# or
from media_tools import (
    audio_enhance,
    graphics_enhance
)
