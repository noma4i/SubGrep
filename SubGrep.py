import sublime, sublime_plugin

class SubGrepCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    title = "Grep: [TEST]"
    for region in self.view.sel():
      if not region.empty():
        selection = self.view.substr(region)
        self.view.run_command( 'show_grep', {'title': title, 'selection': selection} )

class ShowGrepCommand(sublime_plugin.TextCommand):
  def run(self,edit,title,selection):
    self.grep_view(edit,title,selection)

  def grep_view(self, edit, title, content, **kwargs):
    syntax = 'Packages/Markdown/Markdown.tmLanguage'
    panel = self.view.window().new_file()
    panel.set_name(title)
    panel.set_scratch(True)
    panel.set_syntax_file(syntax)

    panel.insert(edit, 0, content)
    panel.set_read_only(True)

    return panel
