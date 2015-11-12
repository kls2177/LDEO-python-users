
#class Citation:
class Citation(object):

    def __init__(self, title=None, authors=[], journal=None, year=0):
        self.title = title
        self.authors = authors
        self.journal = journal
        assert isinstance(year, int), 'Year needs to be an integer'
        self.year = year

    def format_reference(self):
        #return self.title + ' (' + str(self.year) + ')'
        return '%s (%04d)' % (self.title, self.year)
