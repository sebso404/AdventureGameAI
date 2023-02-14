import flask


# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html', name='Sebi')



if __name__ == '__main__':
    APP.debug=True
    APP.run()

    #changes 21:49

    #Changes 6:39

