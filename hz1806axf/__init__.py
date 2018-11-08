from __future__ import absolute_import
from .celery import app as cerlery_app
import pymysql
pymysql.install_as_MySQLdb()