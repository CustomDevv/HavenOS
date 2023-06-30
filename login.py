import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class LoginWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Login")
        self.set_border_width(10)

        # Create a vertical box container
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Add username entry
        username_entry = Gtk.Entry()
        username_entry.set_placeholder_text("Username")
        vbox.pack_start(username_entry, True, True, 0)

        # Add password entry
        password_entry = Gtk.Entry()
        password_entry.set_placeholder_text("Password")
        password_entry.set_visibility(False)
        vbox.pack_start(password_entry, True, True, 0)

        # Add login button
        login_button = Gtk.Button(label="Login")
        login_button.connect("clicked", self.on_login_clicked)
        vbox.pack_start(login_button, True, True, 0)

    def on_login_clicked(self, button):
        # Here, you can implement the login logic
        # Retrieve the entered username and password
        username = username_entry.get_text()
        password = password_entry.get_text()

        # Validate the credentials and perform necessary actions
        # such as opening the dashboard window or showing an error message

win = LoginWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
