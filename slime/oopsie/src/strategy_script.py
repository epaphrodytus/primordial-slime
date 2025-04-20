from oopsie.strategy import Metadata, DatabaseSaver, FileBasedSaver

if __name__ == '__main__':
    metadata = Metadata(DatabaseSaver)
    metadata.save()
    metadata.set_saver(FileBasedSaver)
    metadata.save()
    print(f"The Metadata object knows how to operate a saver")
    print(f"The Metadata objects expects to call the same method")
    print(f"And hand in the same things")
    print(f"The Context class could hand itself or it could hand data")
    print(f"The idea is that the algorithm is not within the object")
    print(f"That is calling it in the first place")
