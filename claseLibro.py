class libro:

    def __init__(self, titulo, autor, editor, ISBN, año):
        self.titulo= titulo
        self.autor= autor
        self.editor= editor
        self.ISBN=ISBN
        self.año= año

    def setTitulo(self,titulo):
        self.titulo=titulo

    def setAutor(self,autor):
        self.autor=autor

    def setEditor(self,editor):
        self.editor=editor

    def setISBN(self,ISBN):
        self.ISBN= ISBN

    def setAño(self,año):
        self.año=año

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getEditor(self):
        return self.editor
    def getISBN(self):
        return self.ISBN

    def getAño(self):
        return self.año