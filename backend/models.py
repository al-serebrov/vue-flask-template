#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Messages(db.Model):
    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    last_modified_at = db.Column(db.DateTime, nullable=True)
    msg = db.Column(db.String, nullable=False)

    def __init__(self, id=None, msg=None):
        if not id:
            id = uuid4()
        self.id = id
        self.created_at = datetime.datetime.utcnow()
        self.last_modified_at = self.created_at
        self.msg = msg

    def __repr__(self):
        return f"<Message {self.msg}>"
