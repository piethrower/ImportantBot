#!/usr/bin/python3

import discord
import time
class Voice_User():
    """Represents a Discord user.
    Attributes
    -----------
    user: :class:`User`
        The discord user.
    channel: :class:`VoiceChannel`
        The discord voice channel the user is connected to.
    time_alone_start: :class:`float`
        The system time at which the member started being alone
    is_alone: :class:`bool`
        Whether the user is alone in the channel
     """
    user: discord.User
    channel: discord.VoiceChannel
    time_alone_start: float
    is_alone: bool
    def __init__(self):
        self.time_alone_start = 0
        self.is_alone = False
