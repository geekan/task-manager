from flask import Flask
from flask import request
#pip install MySQL-python
import mysql.connector
import pymysql
from time import gmtime, strftime, localtime
from werkzeug import secure_filename

app = Flask(__name__)

cnx = pymysql.connect(user='root', password='',
                              host='127.0.0.1',
                              database='bige',
                              cursorclass=pymysql.cursors.DictCursor)
cnx.autocommit = True

@app.route('/')
def hello_world():
    with cnx.cursor() as cur:
        cur.execute("DESC basic_tasks")
        desc = cur.fetchall()

        cur.execute("SELECT * FROM basic_tasks where finish_time=''")
        rows = cur.fetchall()

        # We don't have the direct url to display image(maybe), consider to store image url directly.
        # for r in rows:
        #    r['image_path'] = "<a href='http://long-long-long-name-for-pc.anwcl.com:5001/produce/input/" + r['image_path'].split('/')[-1] + "'>" + r['image_path'] + "</a>"

        return 'Scheme:</br>' + str(desc) + '</br></br>' + 'All Tasks:</br>' + '</br>'.join([str(row) for row in rows])

@app.route('/file-store', methods=['POST'])
def style_image():
    print('request.headers:' + str(request.headers))
    f = request.files['file']
    file_path = './file-store/' + secure_filename(f.filename.split('/')[-1])
    f.save(file_path)

@app.route('/task/create', methods=['POST'])
def task_create():
    print('request.headers:' + str(request.headers))
    print(str(request.form))

    # We don't save image while create task.
    # Use file-store api to store files.
    #f = request.files['image']
    #image_path = '/Users/wuchenglin/git/neural-style/produce/input/' + secure_filename(f.filename.split('/')[-1])
    #f.save(image_path)

    image_id = request.form['image_id']

    current_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sql_insert_template = "INSERT INTO basic_tasks values ('{create_time}', '{finish_time}', '{image_path}', '{image_id}', '{style_image}', {in_process}, '{user_id}', '')" # start_time last

    style_image = 'examples/inputs/starry_night.jpg'
    if request.form.get('style_image_path'):
        style_image = request.form['style_image_path']

    user_id = ''
    if request.form.get('user_id'):
        user_id = request.form['user_id']

    sql_insert = sql_insert_template.format(create_time=current_time, finish_time='', image_path=image_path, image_id=image_id, style_image=style_image, in_process=0, user_id=user_id)
    #sql_insert = sql_insert_template.format(create_time=current_time, finish_time='', image_path=image_path, image_id=image_id, style_image='examples/inputs/shennaichuan.jpg', in_process=0)
    print(sql_insert)
    with cnx.cursor() as cur:
        cur.execute(sql_insert)

    return ''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
