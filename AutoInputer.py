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
		char_delay = sublime.load_settings('auto-inputer.sublime-settings').get("char_delay")
		print(char_delay)
		print(type(char_delay))
		def th():
			for char in text:
				sleep(0.02)
				win.run_command("insert",{"characters": char}) 
			settings.set("auto_indent", True)
		Thread(target=th).start()

