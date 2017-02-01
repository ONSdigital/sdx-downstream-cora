import unittest
from unittest.mock import MagicMock
import json
import logging
from structlog import wrap_logger
from app.processors.cora_processor import CoraProcessor
from tests.test_data import cora_survey
from app.helpers.sdxftp import SDXFTP
from app import settings

logger = wrap_logger(logging.getLogger(__name__))


class TestCoraProcessor(unittest.TestCase):

    def setUp(self):
        survey = json.loads(cora_survey)
        self._ftp = SDXFTP(logger, settings.FTP_HOST, settings.FTP_USER, settings.FTP_PASS)
        self.processor = CoraProcessor(logger, survey, self._ftp)

    def test_tx_id_should_be_set(self):
        self.assertIsNotNone(self.processor.tx_id)

    def test_transform_failure(self):
        self.processor.transform = MagicMock(return_value=None)
        result = self.processor.process()
        self.assertFalse(result)

    def test_process_failure(self):
        self.processor.transform = MagicMock(return_value="success")
        self.processor.deliver_zip = MagicMock(return_value=False)
        result = self.processor.process()
        self.assertFalse(result)

    def test_process_success(self):
        self.processor.transform = MagicMock(return_value="success")
        self.processor.deliver_zip = MagicMock(return_value=True)
        result = self.processor.process()
        self.assertTrue(result)
