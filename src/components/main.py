import logging
import time
from analytics_worker import settings
from analytics_worker.tasks import data_processing

logger = logging.getLogger(__name__)

def main():
    while True:
        try:
            logger.info('Starting data processing task')
            data_processing.process_data()
            logger.info('Data processing task completed successfully')
        except Exception as e:
            logger.error('Error processing data: %s', e)
        finally:
            # Wait for 5 minutes before checking again
            time.sleep(300)

if __name__ == '__main__':
    main()