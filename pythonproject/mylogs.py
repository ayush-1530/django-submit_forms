import logging
name = 'GFG'
logging.error('%s raised an error', name)







# importing module
import logging

# Create and configure logger
logging.basicConfig(filename="pp.log", format='%(asctime)s %(message)s', filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
