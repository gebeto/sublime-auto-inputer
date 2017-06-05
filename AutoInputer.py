import sublime
import sublime_plugin
from time import sleep
from threading import Thread


class AutoInputCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		if args:
			self.on_done(args["text"])
			return
		self.view.settings().set("auto_indent", False)
		self.view.window().show_input_panel("Enter text", "", self.on_done, None, None)

	def on_done(self, text):
		win = self.view.window() 
		settings = self.view.settings()
		char_delay = self.get_setting("char_delay")
		print("Char Delay: ", char_delay)
		def th(char_delay):
			for char in text:
				sleep(char_delay)
				win.run_command("insert",{"characters": char}) 
			settings.set("auto_indent", True)
		Thread(target=th, args=[char_delay]).start()


	def get_setting(self, string):
        if self.view and self.view.settings().get(string):
            return self.view.settings().get(string)
        else:
            return sublime.load_settings('auto-inputer.sublime-settings').get(string)