import pytest
import game as coin_game


def test_game_object_can_be_created_without_args():
    obj = coin_game.GameObject()
    assert obj.position is None
    assert obj.body_color is None


def test_player_is_game_object():
    assert issubclass(coin_game.Player, coin_game.GameObject)


def test_coin_is_game_object():
    assert issubclass(coin_game.Coin, coin_game.GameObject)


def test_player_starts_in_center():
    player = coin_game.Player()
    center_x = coin_game.SCREEN_WIDTH // 2 // coin_game.GRID_SIZE * coin_game.GRID_SIZE
    center_y = coin_game.SCREEN_HEIGHT // 2 // coin_game.GRID_SIZE * coin_game.GRID_SIZE
    assert player.position == (center_x, center_y)


def test_player_wraps_around():
    player = coin_game.Player()
    # сдвиг далеко вправо
    for _ in range(coin_game.GRID_WIDTH + 5):
        player.move(1, 0)
    x, y = player.position
    assert 0 <= x < coin_game.SCREEN_WIDTH


def test_coin_not_on_player():
    player = coin_game.Player()
    coin = coin_game.Coin()
    for _ in range(20):
        coin.randomize_position(player.position)
        assert coin.position != player.position