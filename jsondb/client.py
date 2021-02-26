import os
import json


class Client:
  def __init__(self, path=''):
    self._path = path
    self._conn = None

  def get_conn(self, file):
    if not file:
      if not self._conn:
        raise FileNotFoundError("File not found")
      else:
        conn = self._path + self._conn
    else:
      conn = self._path + file + '.json'
    return conn

  def create(self, file=None):
    conn = self.get_conn(file)
    
    if os.path.exists(conn):
      raise FileExistsError("File already exists")
    f = open(conn, 'w+')
    f.write('{}')
    f.close()
    return True
  
  def remove(self, file=None):
    conn = self.get_conn(file)
    
    if not os.path.exists(conn):
      raise FileNotFoundError("File not found")
    os.remove(conn)
    return True
  
  def dump(self, key, value, file=None):
    conn = self.get_conn(file)
    
    with open(conn, 'r') as f:
      load = json.load(f)

    load[key] = value
    with open(conn, 'w') as f:
      json.dump(load, f)
    return True
  
  def connect(self, file):
    if not os.path.exists(f'{self._path}{file}.json'):
      raise FileNotFoundError("File not found")
    self._conn = file + '.json'
    return True
  
  def connect_clear(self):
    self._conn = None

  def load(self, key, file=None):
    conn = self.get_conn(file)
    
    
    with open(conn, 'r') as f:
      load = json.load(f)
    
    return load[key]
  

  def delete(self, key, file = None):
    conn = self.get_conn(file)
    

    with open(conn, 'r') as f:
      load = json.load(f)
  
    del load[key]
  
    with open(conn, 'w') as f:
      json.dump(load, f)
  
    return True