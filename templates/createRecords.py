import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
      return psycopg2.connect("dbname=db")
    except:
      print("Connection failed")


def dbChange(sql, params):
    """Helper function to write to the database

    This function establishes a connection with the database, creates a
    transaction, commits the transaction and closes the connection.

    Args:
      sql       : the sql that we want to run
      params    : a tuple containing the values that we want to combine with
                  the sql to create the transaction while using python's /
                  psycopg2's syntax to protect against sql injections.

    Returns     : any return value required by the sql parameter
                  False if the query did not return any value
    """

    # connect to the database and run the query
    db = connect()
    cursor = db.cursor()
    cursor.execute(sql, params)

    # commits the transaction and return the result of the query if any
    try:
        result = cursor.fetchone()
    except:
        result = False
    finally:
        db.commit()
        db.close()
    return result


def createPainting(name):
    dbChange('INSERT INTO painting (title, description, galleryId, paintingDate, memberId, image,' \
              'medium, sold, price) VALUES (%s)', \
              (name,))


    image = Column(String(), nullable=True)
    medium = Column(String(), nullable=True)
    sold = Column(Boolean(), nullable=False)
    price = Column(Numeric(), nullable=True)
