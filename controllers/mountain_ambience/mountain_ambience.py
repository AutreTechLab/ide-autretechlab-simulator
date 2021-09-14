"""mountain_ambience controller."""

from controller import Supervisor
from controller import Speaker

# create the Supervisor instance.
supervisor = Supervisor()
timestep = int(supervisor.getBasicTimeStep())

speaker = supervisor.getSpeaker("mountain_speaker")
Speaker.playSound(speaker, speaker, "mountain_ambience.wav", 0.9, 1, 0, True)

while supervisor.step(timestep) != -1:
    pass
