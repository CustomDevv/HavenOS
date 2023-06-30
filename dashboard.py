import gi
import psutil

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class DashboardWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Dashboard")
        self.set_border_width(10)

        # Create a label to display CPU and RAM usage
        self.label = Gtk.Label()
        self.add(self.label)

        # Refresh the usage information every 1 second
        GLib.timeout_add_seconds(1, self.update_usage_info)

    def update_usage_info(self):
        # Get CPU and RAM usage information using psutil
        cpu_percent = psutil.cpu_percent()
        ram_percent = psutil.virtual_memory().percent

        # Update the label text with the usage information
        self.label.set_text(f"CPU Usage: {cpu_percent}%\nRAM Usage: {ram_percent}%")

        # Return True to continue updating the information periodically
        return True

win = DashboardWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
