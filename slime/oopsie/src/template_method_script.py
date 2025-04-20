from oopsie.template_method import ReleaseDocumentYmlParser, ReleaseDocumentExcelParser, ReleaseDocumentParser


if __name__ == '__main__':
    parser = ReleaseDocumentParser()
    parser.read(r"\some\random\path")
    print('---')
    print('---')
    parser = ReleaseDocumentExcelParser()
    parser.read(r"\some\random\path")
    print('---')
    print('---')
    parser = ReleaseDocumentYmlParser()
    parser.read(r"\some\random\path")
    print('---')
    print('---')
    print("The benefit is that the person sub-classing the object")
    print("only needs to override the template method and the rest of the")
    print("algorithm should work with the base class' other primitive operations")