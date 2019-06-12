
from __future__ import annotations

from typing import List
from typing import Type

from component.name import Name
from component.role import Role

from event.event import Event
from message.message import Message
from system.channel import Channel

from logcat.logcat import LogCat
import random
class CmdExit:
    @LogCat.log_func
    def __init__(self, servant: Type[Handler]):
        servant.on(Event.CMD_EXIT, self._on_cmd_exit)

    @LogCat.log_func
    def _on_cmd_exit(
        self, e: Event, entity: str = '', args: List[str] = []
    ) -> None:
        luckynumber = random.randint(0,100)
        if args:
            text = f'請不要輸入參數'

            Channel.to_role(entity, Message.TEXT, text)
        else:
            text = f'{Name.instance(entity).text} 的幸運數字{" ".join(str(luckynumber))}請記住這個號碼'

            role = Role.instance(entity)
            Channel.to_room(role.room, Message.TEXT, text)

# cmd_say.py
