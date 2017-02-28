# coding:utf-8




from __future__ import print_function
import test_environment
import kbqacn.resources as resources



test_environment.init_environment()


def test():
    print(resources.resources_path)
    print(resources.question_sparql_templates)


if __name__ == '__main__':
    test()


