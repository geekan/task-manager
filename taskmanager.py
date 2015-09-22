from flask import Flask
from flask import request
#pip install MySQL-python
import mysql.connector
import pymysql
from time import gmtime, strftime, localtime
from werkzeug import secure_filename

from sqlalchemy import create_engine
engine = create_engine('mysql://root@localhost/bige', echo=True)

app = Flask(__name__)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, func, desc
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class ReprMixin(object):

  def __init__(self):
    # these properties are to make this example self documenting.  remove them from your implementation.
    # when you only find this comment when you're debugging an unexpected value you'll know someone on
    # your team blindly copy pasted :D
    self._privateVar = "This method relies on all private vars being prefixed with an underscore"
    self.publicVar = "See me in repr"

  def __repr__(self):

    def filter_properties(obj):
      # this function decides which properties should be exposed through repr
      # todo: don't show methods
      properties = obj.__dict__.keys()
      for prop in properties:
        if prop[0] != "_":
          yield (getattr(obj, prop), prop)
      return

    prop_tuples = filter_properties(self)
    prop_string_tuples = (": ".join(prop) for prop in prop_tuples)
    prop_output_string = " | ".join(prop_string_tuples)
    cls_name = self.__class__.__name__
    return "<%s('%s')>" % (cls_name, prop_output_string)

class ImageNeuralTask(Base, ReprMixin):
    __tablename__ = 'image_neural_task'

    id = Column(String(255), primary_key=True)
    status = Column(String(255), default='')
    create_time = Column(String(255), default='')
    start_time = Column(String(255), default='')
    finish_time = Column(String(255), default='')
    image_path = Column(String(255), default='')
    image_url = Column(String(255), default='')
    style_image = Column(String(255), default='')


def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

init_db()

@app.route('/')
def hello_world():
    tmp_task = ImageNeuralTask(id='1', create_time='111')
    session.merge(tmp_task)

    tasks = session.query(ImageNeuralTask).filter_by(finish_time='')

    # return 'Scheme:</br>' + str(desc) + '</br></br>' + 'All Tasks:</br>' + '</br>'.join([str(row) for row in rows])
    return '<br/>'.join(tasks)

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
    app.run(debug=True, host='0.0.0.0', port=5002)
