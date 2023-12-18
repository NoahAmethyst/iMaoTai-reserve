from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendMsgReq(_message.Message):
    __slots__ = ("content", "chat", "group")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    content: str
    chat: int
    group: bool
    def __init__(self, content: _Optional[str] = ..., chat: _Optional[int] = ..., group: bool = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("nickname", "code", "remark", "owner", "cardName", "joinTime", "lastSpeakTime", "specialTitle")
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CARDNAME_FIELD_NUMBER: _ClassVar[int]
    JOINTIME_FIELD_NUMBER: _ClassVar[int]
    LASTSPEAKTIME_FIELD_NUMBER: _ClassVar[int]
    SPECIALTITLE_FIELD_NUMBER: _ClassVar[int]
    nickname: str
    code: int
    remark: str
    owner: int
    cardName: str
    joinTime: int
    lastSpeakTime: int
    specialTitle: str
    def __init__(self, nickname: _Optional[str] = ..., code: _Optional[int] = ..., remark: _Optional[str] = ..., owner: _Optional[int] = ..., cardName: _Optional[str] = ..., joinTime: _Optional[int] = ..., lastSpeakTime: _Optional[int] = ..., specialTitle: _Optional[str] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ("code", "name", "owner", "groupCreateTime", "GroupLevel", "MemberCount", "MaxMemberCount", "members")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    GROUPCREATETIME_FIELD_NUMBER: _ClassVar[int]
    GROUPLEVEL_FIELD_NUMBER: _ClassVar[int]
    MEMBERCOUNT_FIELD_NUMBER: _ClassVar[int]
    MAXMEMBERCOUNT_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    code: int
    name: str
    owner: int
    groupCreateTime: int
    GroupLevel: int
    MemberCount: int
    MaxMemberCount: int
    members: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, code: _Optional[int] = ..., name: _Optional[str] = ..., owner: _Optional[int] = ..., groupCreateTime: _Optional[int] = ..., GroupLevel: _Optional[int] = ..., MemberCount: _Optional[int] = ..., MaxMemberCount: _Optional[int] = ..., members: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class Resp(_message.Message):
    __slots__ = ("message", "self", "friends", "groups")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    message: str
    self: User
    friends: _containers.RepeatedCompositeFieldContainer[User]
    groups: _containers.RepeatedCompositeFieldContainer[Group]
    def __init__(self, message: _Optional[str] = ..., self: _Optional[_Union[User, _Mapping]] = ..., friends: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., groups: _Optional[_Iterable[_Union[Group, _Mapping]]] = ...) -> None: ...
