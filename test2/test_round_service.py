import pytest

from app.services.round_services import(
    RoundTabulation,
    LEAVE_COMMENT,
    CALL_IPHONE,
    DISLIKE,
    GO_LIVE,
    POST_SELFIE,
    DONT_POST,
    NO_MOVE,
    DISLIKE_DM,
    POST_SELFIE_PTS,
    POST_SELFIE_DM, 
    GO_LIVE_DM,
    NO_MOVE_DM,

)

from app.services import round_service, message_service
from app.models import Move, Message, GamePlayer

@pytest.mark.django_db
def test_iphone_go_live_do_selfie(rnd, p_1, p_2, p_3, move):
    move(round=rnd, action_type=GO_LIVE, player=p_1, victim=None)
    move(round=rnd, action_type=CALL_IPHONE, player=p_2, victim=p_3)
    move(round=rnd, action_type=POST_SELFIE, player=p_3, victim=None)
    tab = RoundTabulation(rnd).tabulate()
    assert tab[p_1.id] == 0
    assert tab[p_2.id] == GO_LIVE_DM
    assert tab[p_3.id] == GO_LIVE_DM

@pytest.mark.django_db
def test_go_live_with_call(rnd, p_1, p_2, p_3, p_4, p_5, move):
    move(round=rnd, action_type=GO_LIVE, player=p_1, victim=None)
    move = move(round=rnd, action_type=CALL_IPHONE, player=p_2, victim=p_1)
    move(round=rnd, action_type=DISLIKE, player=p_3, victim=p_1)
    move(round=rnd, action_type=DISLIKE, player=p_4, victim=p_1)
    move(round=rnd, action_type=LEAVE_COMMENT, player=p_5, victim=p_1)
    tab = RoundTabulation(rnd).tabulate()
    
    assert message(rnd.game, p_2.user.username) in message_service.iphone_msg(move, p_1.user.username)
    assert p_1.go_live == 1
    assert tab[p_1.id] == -50