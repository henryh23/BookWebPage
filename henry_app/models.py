from app import db
from sqlalchemy import ForeignKey
import datetime


class Book(db.Model):
    __tablename__ = 'Book'
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    subtitle = db.Column(db.String(100))
    pub_year = db.Column(db.Integer)
    changed_by = db.Column(db.String(100))
    contributors = db.relationship("Contributor", backref="Book")


class Contributor(db.Model):
    __tablename__ = 'Contributor'
    contributor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, ForeignKey('Book.book_id'))
    last_name = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    role = db.Column(db.String(100))
    changed_by = db.Column(db.String(100))


class Locked_Field(db.Model):
    __tablename__ = 'Locked_Field'
    locked_field_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    table_name = db.Column(db.String(100))
    id = db.Column(db.Integer)
    field = db.Column(db.String(100))
    locked = db.Column(db.Integer)
    locked_by = db.Column(db.String(100))
    comment = db.Column(db.String(500))


class Book_Upload_File(db.Model):
    __tablename__ = 'Book_Upload_File'
    book_upload_file_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    upload_type = db.Column(db.String(100))
    file_type = db.Column(db.String(100))
    onix_version = db.Column(db.String(100))
    onix_form = db.Column(db.String(100))
    file_name = db.Column(db.String(100))
    delivered_by = db.Column(db.String(100))
    muse_user_id = db.Column(db.String(100))
    received = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Book_Upload_Assignment(db.Model):
    __tablename__ = 'Book_Upload_Assignment'
    book_upload_assignment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_upload_file_id = db.Column(db.Integer)
    line_number = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Book_Upload_Data(db.Model):
    __tablename__ = 'Book_Upload_Data'
    book_upload_core_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_upload_assignment_id = db.Column(db.Integer)
    publisher = db.Column(db.String(100))
    title = db.Column(db.String(100))
    subtitle = db.Column(db.String(100))
    series_title = db.Column(db.String(100))
    series_volume = db.Column(db.String(100))
    published_date = db.Column(db.Date)
    distribution_date = db.Column(db.Date)
    manufacture_date = db.Column(db.Date)
    copyright_date = db.Column(db.Date)
    cc_license_date = db.Column(db.Date)
    cc_license = db.Column(db.String(100))
    place_publication = db.Column(db.String(100))
    description = db.Column(db.String(10000))
    funder = db.Column(db.String(100))
    page_count = db.Column(db.Integer)
    illustration = db.Column(db.Integer)
    print_url = db.Column(db.String(100))
    language = db.Column(db.String(100))
    doi = db.Column(db.String(100))
    print_url = db.Column(db.String(100))
    open_access = db.Column(db.String(100))
    audience = db.Column(db.String(100))
    imprints = db.Column(db.String(100))
    oclc = db.Column(db.String(100))
    loc_call_numer = db.Column(db.String(100))
    dewey_call_number = db.Column(db.String(100))
    price = db.Column(db.Float)
    isbn_json = db.Column(db.Text)
    contributor_json = db.Column(db.Text)
    subject_json = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
