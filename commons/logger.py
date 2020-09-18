# -*- coding: utf-8 -*-

"""日志"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
