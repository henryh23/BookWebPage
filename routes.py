from flask import Blueprint, render_template, request, redirect, url_for
from app import mysql

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route('/')
def show_home():
    return ("<html><h1>Welcome: I like Tables!</h1></html>")


@main_blueprint.route('/books')
def show_sample_template():

    # Establish a database connection
    cur = mysql.connection.cursor()

    cur.execute("SELECT b.book_id, b.title, b.subtitle, b.author_first, b.author_last, b.pub_year, b.copyright_year, b.country, p.pub_name FROM Book AS b LEFT OUTER  JOIN Publisher AS p ON b.pub_id = p.pub_id ORDER BY book_id")
    books = cur.fetchall()
    book_string = str(books)
    title = "Books"

    header_list = [
        'Book ID',
        'Title',
        'Subtitle',
        'Author First',
        'Author Last',
        'Publishing Year',
        'Copyright Year',
        'Country',
        'Publisher'
        ]
    
    rows = []
    for book in books:
        row_data = []
        for column in book:
            row_data.append(column)
        if row_data[-1] == None:
            row_data[-1] = "No Publisher"
        rows.append(row_data)
    
    return render_template(
        '/example.html',
        title=title,
        headers = header_list,
        table_rows = rows,
    )

@main_blueprint.route('/publishers')
def show_publisher_template():

    # Establish a database connection
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM Publisher")
    publishers = cur.fetchall()
    publisher_string = str(publishers)
    title = "Publishers"

    header_list = [
        'Publisher Id',
        'Name',
        'Address',
        'Phone Number'
        ]
    
    rows = []
    for publisher in publishers:
        row_data = []
        for column in publisher:
            row_data.append(column)
        rows.append(row_data)

    return render_template(
        '/example.html',
        title=title,
        headers = header_list,
        table_rows = rows,
    )

#Test for git
@main_blueprint.route('/upload_book' , methods = ['GET','POST'])
def show_insert():


    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT pub_name, pub_id from Publisher")
        publishers = cur.fetchall()

        rows = []
        for publisher in publishers:
            pub_name = publisher[0]
            pub_id = publisher[1]
            rows.append({'pub_id': pub_id, 'pub_name': pub_name})

        return render_template('/insert.html', publishers = rows)
 
    if request.method == 'POST':
        cur = mysql.connection.cursor()

        title = request.form['title']
        subtitle = request.form["subtitle"] or None
        author_first = request.form["author_first"] or None
        author_last = request.form["author_last"] or None
        pub_year = request.form["pub_year"] or None
        copyright_year = request.form["copyright_year"] or None
        country = request.form["country"] or None
        publisher = request.form['publisher'] or None

        cur.execute("INSERT INTO Book (title, subtitle, author_first, author_last, pub_year, copyright_year, country, pub_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (title, subtitle, author_first, author_last, pub_year, copyright_year, country,publisher))
        
        mysql.connection.commit()
        return redirect('/upload_book')
    

@main_blueprint.route('/update_book' , methods = ['GET','POST'])
def show_update():
    cur = mysql.connection.cursor()
    cur.execute("SELECT book_id, title from Book")
    books = cur.fetchall()

    rows = []

    for book in books:
        book_id = book[0]
        title = book[1]
        
        rows.append({
            'book_id': book_id, 
            'title': title,
            })
        


    if request.method == 'GET':


        return render_template('/preUpdate.html', books = rows)
 
    if request.method == 'POST':

        selected_book = request.form['book']
        return redirect(f'/update_book/change/{selected_book}')
    


@main_blueprint.route('/update_book/change/<int:selected_book>', methods=['GET', 'POST'])
def show_update2(selected_book):

    cur = mysql.connection.cursor()
    cur.execute("SELECT * from Book WHERE book_id = %s", (selected_book,))
    books = cur.fetchall()

    rows = []
#testeewew

    for book in books:
        book_id = book[0]
        title = book[1]
        subtitle = book[2]
        author_first = book[3]
        author_last = book[4]
        pub_year = book[5]
        copyright_year = book[6]
        country = book[7]
        pub_id = book[8]
        rows.append({
            'book_id': book_id, 
            'title': title,
            'subtitle': subtitle,
            'author_first': author_first,
            'author_last': author_last,
            'pub_year': pub_year,
            'copyright_year': copyright_year,
            'country': country,
            'pub_ib': pub_id
            })
        


    if request.method == 'GET':
        cur.execute("SELECT pub_name, pub_id from Publisher")
        publishers = cur.fetchall()

        publisher_rows = []
        for publisher in publishers:
            pub_name = publisher[0]
            pub_id = publisher[1]
            publisher_rows.append({'pub_id': pub_id, 'pub_name': pub_name})

        return render_template('/update.html', books = rows, publishers = publisher_rows)
 
    if request.method == 'POST':
        title = request.form.get('title') or None
        subtitle = request.form.get('subtitle') or None
        author_first = request.form.get('author_first') or None
        author_last = request.form.get('author_last') or None
        pub_year = request.form.get('pub_year') or None
        copyright_year = request.form.get('copyright_year') or None
        country = request.form.get('country') or None
        publisher = request.form.get('publisher') or None

        cur.execute("UPDATE Book SET title=%s, subtitle=%s, author_first=%s, author_last=%s, pub_year=%s, copyright_year=%s, country=%s, pub_id=%s WHERE book_id=%s", (title, subtitle, author_first, author_last, pub_year, copyright_year, country, publisher, book_id))

        mysql.connection.commit()
        return redirect('/update_book')
    #sql alchemy
  #source tree, git