from utility.config import Config

class App:
    def __init__(self):
        pass

    def main(self):
        config = Config.initialize()
        print('Started App')

if __name__ == '__main__':
    app = App()
    app.main()
