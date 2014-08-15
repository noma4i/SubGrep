import sublime, sublime_plugin

class SubGrepCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      if not region.empty():
        selection = self.view.substr(region)
        title = "Grep: [%s]" % selection
        syntax = self.view.settings().get('syntax')
        self.view.run_command( 'show_grep', {'title': title, 'selection': selection, 'syntax': syntax} )
class ShowGrepCommand(sublime_plugin.TextCommand):
  def run(self,edit,title,selection,syntax):
    self.grep_view(edit,title,selection, syntax)

  def grep_view(self, edit, title, selection, syntax):
    panel = self.view.window().new_file()
    panel.set_name(title)
    panel.set_scratch(True)
    panel.set_syntax_file(syntax)

    text = self.view.substr(sublime.Region(0, self.view.size()))
    result = ""
    for line in text.split('\n'):
      if selection in line:
        result += "%s\n" % line.lstrip(' ')

    panel.insert(edit, 0, result)
    panel.set_read_only(False)

    return panel
