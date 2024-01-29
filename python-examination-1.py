"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.


def bake_time_remaining(elapsed_bake_time):
    """残りの焼き時間を計算する。

    :param elapsed_bake_time: int - 既に経過した焼き時間（分）。
    :return: int - 残りの焼き時間（分）。

    この関数は、既に経過した焼き時間を引数として受け取り、レシピの予定焼き時間から引いて、
    残りの焼き時間を計算します。
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(layers):
    """レシピの準備にかかる時間を計算する。

    :param layers: int - ラザニアの層の数。
    :return: int - 準備に要する時間（分）。

    この関数は、ラザニアの層の数を引数として受け取り、各層にかかる準備時間を掛け算して、
    合計の準備時間を計算します。
    """
    return layers * PREPARATION_TIME


# TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """調理にかかった合計時間を計算する。

    :param number_of_layers: int - ラザニアの層の数。
    :param elapsed_bake_time: int - 既に経過した焼き時間。
    :return: int - 準備と調理にかかった合計時間（分）。

    この関数は、ラザニアの層の数と既に経過した焼き時間を表す二つの整数を引数として受け取り、
    ラザニアを調理するのにかかった合計時間（分）を計算します。
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
