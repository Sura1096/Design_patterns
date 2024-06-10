class Document:
    def show(self):
        raise NotImplementedError()


class ODFDocument(Document):
    def show(self):
        print('Open document format')


class MSOfficeDocument(Document):
    def show(self):
        print('MS Office document format')


class Application:
    def create_document(self, doc_type):
        raise NotImplementedError()


class MyApplication(Application):
    def create_document(self, doc_type):
        if doc_type == 'odf':
            return ODFDocument()
        elif doc_type == 'doc':
            return MSOfficeDocument()


if __name__ == '__main__':
    app = MyApplication()
    app.create_document('odf').show()
    app.create_document('doc').show()
