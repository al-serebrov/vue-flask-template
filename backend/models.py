#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Searches(db.Model):
    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        unique=True,
        nullable=False)

    category_id = db.Column(db.Integer, nullable=True)
    category = db.Column(db.String, nullable=True)

    mark_id = db.Column(db.Integer, nullable=True)
    mark = db.Column(db.String, nullable=True)

    model_id = db.Column(db.Integer, nullable=True)
    model = db.Column(db.String, nullable=True)

    bodystyle_id = db.Column(db.Integer, nullable=True)
    bodystyle = db.Column(db.String, nullable=True)

    start_year = db.Column(db.Integer, nullable=True)
    end_year = db.Column(db.Integer, nullable=True)

    state_id = db.Column(db.Integer, nullable=True)
    state = db.Column(db.String, nullable=True)

    city_id = db.Column(db.Integer, nullable=True)
    city = db.Column(db.String, nullable=True)

    fuels_id = db.Column(db.String, nullable=True)
    fuels = db.Column(db.String, nullable=True)

    color_id = db.Column(db.Integer, nullable=True)
    color = db.Column(db.Integer, nullable=True)

    gears_id = db.Column(db.String, nullable=True)
    gears = db.Column(db.String, nullable=True)

    driver_type_id = db.Column(db.Integer, nullable=True)
    driver_type = db.Column(db.String, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
