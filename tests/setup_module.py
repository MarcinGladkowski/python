from unittest import TestCase, main

def setUpModule():
    print('* Prepare module')


def tearDownModule():
    print('* Closing, cleaning module')


class IntegrationTest(TestCase):
    def setUp(self) -> None:
        print('* Prepare test')

    def tearDown(self) -> None:
        print('* Cleaning test class')

    def test_end_to_end(self):
        print('* Test end to end')


if __name__ == '__main__':
    main()
