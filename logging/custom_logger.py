import logging

"""
Usage of __name__ allows to set module name as logger name. Good practice. 
"""
logger = logging.getLogger(__name__)
logger.warning("Custom logger exception")

