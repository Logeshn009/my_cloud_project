import pymysql
from app import app
from tables import Results
from db_config import mysql
from flask import flash, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from logging import FileHandler, WARNING


@app.route('/new_user')
def add_user_view():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add_user():
    conn = None
    cursor = None
    try:
        _date = request.form['date']
        _deaths = request.form['deaths']
        _discharge = request.form['discharge']
        _negative = request.form['deaths']
        _positive = request.form['positive']
        _samples = request.form['samples']
        _state = request.form['state']
        # _password = request.form['inputPassword']
        # validate the received values
        if _date and _deaths and _discharge and _negative and _positive and _samples and _state and request.method == 'POST':
            # do not save password as a plain text
            # _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "INSERT INTO Covid_new(Date_of_Record, No_of_Deaths, No_of_Discharge, No_of_Negative, No_of_Positive, No_of_Samples, State_Name) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            data = (_date, _deaths, _discharge, _negative, _positive, _samples, _state)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Covid19 data added successfully!')
            return redirect('/')
        else:
            return 'Error while adding user'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/')
def users():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM Covid_new")
        rows = cursor.fetchall()
        table = Results(rows)
        table.border = True
        return render_template('users.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/edit/<int:id>')
def edit_view(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s", id)
        row = cursor.fetchone()
        if row:
            return render_template('edit.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['POST'])
def update_user():
    conn = None
    cursor = None
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        _id = request.form['id']
        # validate the received values
        if _name and _email and _password and _id and request.method == 'POST':
            # do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            print(_hashed_password)
            # save edits
            sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
            data = (_name, _email, _hashed_password, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('User updated successfully!')
            return redirect('/')
        else:
            return 'Error while updating user'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete/<int:id>')
def delete_user(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
        conn.commit()
        flash('User deleted successfully!')
        return redirect('/')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run()
