"""
Test custom Django management commands
"""
from unittest.mock import patch
from psycopg import OperationalError as PsycopgError
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
  """Test commands"""

  def test_wait_for_db_ready(self, patched_check):
    """Test waiting for database if database ready"""
    patched_check.return_value = True

    call_command('wait_for_db')

    patched_check.assert_called_once_with(databases=['default'])

  @patch('time.sleep')
  def test_wait_db_delay(self, patched_sleep, patched_check):
    """Test waiting for database when getting OperationalError."""
    # This serves to mock the exceptions, this tells that the first two times
    # call the PsycopgError Exception, then the next 3 times OperationalError
    # and finally return True when the database is ready to receive connections
    patched_check.side_effect = [PsycopgError] * 2 + \
      [OperationalError] * 3 + [True]

    call_command('wait_for_db')

    self.assertEqual(patched_check.call_count, 6)
    patched_check.assert_called_with(databases=['default'])