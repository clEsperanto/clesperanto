def main():
    import sys
    from ._clesperanto import clesperanto

    viewer = clesperanto()

    for pos, arg in enumerate(sys.argv):
        print('Argument %d: %s' % (pos, arg))

    import napari
    napari.run()


if __name__ == '__main__':
    main()