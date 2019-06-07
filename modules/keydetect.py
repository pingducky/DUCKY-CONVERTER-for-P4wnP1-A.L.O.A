def keydetect(): 	# function test P4wnP1
    from pynput.keyboard import Key, Listener

    #def on_press(key):
    #    print('{0} pressed'.format(
    #        key))
    print ("press \"CTRL z\" to exit\n\n")

    def on_release(key):
        print('|					{} pressed'.format(
            key))
        if key == Key.esc:
            # Stop listener
            return False

    # Collect events until released
    with Listener(
    #        on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
