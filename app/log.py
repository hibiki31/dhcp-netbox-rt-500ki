import logging

def setup_logger(name):
    """
    ロガーをセットアップする関数。

    この関数は指定された名前でロガーを作成し、DEBUGレベルのログメッセージを
    標準出力に表示するためのストリームハンドラを設定します。
    ログメッセージは日時、ログレベル、メッセージの形式でフォーマットされます。
    通常、__name__を指定してロガーを作成します。

    パラメータ:
    name (str): ロガーの名前。

    戻り値:
    logging.Logger: 設定済みのロガーオブジェクト。
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
    ch.setFormatter(ch_formatter)
    ch.setLevel(logging.DEBUG)

    logger.addHandler(ch)

    return logger