import csv
from datetime import datetime as dt

from .models import Level, LevelPrize, Player, PlayerLevel, Prize


def awarding_prize(player, level, prize, is_completed, score=0) -> LevelPrize:
    PlayerLevel.objects.get_or_create(
        player=player,
        level=level,
        completed=dt.today(),
        is_completed=is_completed,
        score=score,
    )
    new_lewel_prize = LevelPrize.objects.get_or_create(
        level=level,
        prize=prize,
        received=dt.today(),
    )
    return new_lewel_prize


def read_players_data() -> csv:
    output_file = 'output.csv'
    with open(output_file, 'w', newline='') as output_file:
        writer, dict_pryze = csv.writer(output_file), {}
        players_level = PlayerLevel.objects.select_related('player').all()
        level_pryzes = LevelPrize.objects.select_related('level').all()
        for prize in level_pryzes:
            dict_pryze.update({str(prize.level.pk): prize.prize.title})
        for pl in players_level:
            writer.writerow(
                [
                    pl.player.player_id,
                    pl.level.title,
                    pl.is_completed,
                    dict_pryze[str(pl.level.pk)],
                ],
            )
    return output_file


player = Player.objects.select_related().first()
level = Level.objects.select_related().first()
prize = Prize.objects.select_related().first()
awarding_prize(player, level, prize, True, 7)
read_players_data()
