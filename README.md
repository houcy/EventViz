# EventViz

A web application to display log (or whatever parsable source) events in a timeline. It has a Flask based interface
and uses MongoDB for storage.

This application is not meant to be used as a log management tool, but more as an easy way to visualize and
make searches on a pre-filtered set of events.

## Screenshots

### Main View

![Main View](http://img845.imageshack.us/img845/7219/o0au.png "Main View")

### Timeline View

![Timeline View](http://img22.imageshack.us/img22/5413/akxz.png "Timeline View")

### Timeline Event Details

![Timeline Event Details](http://img560.imageshack.us/img560/2237/g7gp.png "Timeline Event Details")

### Search View

![Search View](http://img713.imageshack.us/img713/6708/qtl4.png "Search View")

## Features

* Group events per project
* Timeline visualization
  * Browsable, zoomable
  * Display any field(s)
  * Group by any field
  * Double-click an event to see all its fields
* Events search
  * String matching
  * Substring matching
  * Regular expression matching

## Requirements

* Software
  * Python 2.x
  * MongoDB
* Python libraries
  * PyMongo
  * Flask
  * Flask-Script
  * Flask-Assets
  * YUIcompressor

Required Python libraries can be installed using the provided `requirements.txt`.

    pip install -r requirements.txt

## Usage

All the administration commands are implemented in the `manage.py` script. Commands switches meaning can
be viewed using `./manage.py <command> -h`, and available commands can be listed by calling the script
without any argument.

### Configuration

Default configuration variables are stored in the `settings.py` file. To prevent making changes to a versioned file,
you should create a `prod_settings.py` file where you'd override the options you want, it will be automatically loaded.

Here are the options **you really should change**:

* `DEBUG`: Displays `Werkzeug` integrated debugger when an exception is raised. Gives access to a Python shell
in the application's context. You really don't want that in a production environment!
* `SECRET_KEY`: The key used to sign cookies. Set this to a very long random value.

For the remaining configuration variables, just look at the `settings.py` file, it should be self-explanatory.

### Workflow

* Load some data using the `./manage.py load_data` command
* Run the integrated server using the `./manage.py runserver` command
* Connect to http://127.0.0.1:5000 with your web browser

Once you've selected a project, two sections will become available, 'timeline' where you can navigate through events (you can
see an event's details by double-clicking it), and 'search' where your search results are displayed in a sortable grid.

### Deployment

To serve the application using something else than the integrated server (Apache, nginx, ...), please refer to
the related [Flask documentation](http://flask.pocoo.org/docs/deploying/).

## Documentation


See the [Wiki](https://github.com/mattoufoutu/EventViz/wiki)
