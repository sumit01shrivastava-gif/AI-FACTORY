from logging_engine.logger import Logger


def test_logger():

    logger = Logger()

    logger.write("hello")

    assert len(
        logger.read()
    ) == 1
