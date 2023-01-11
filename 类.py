'''
定义类
'''


class Student(object):
    
    def _init_(self, name, age):
        self.name = name
        self.age = age
    
    def study(self, course_name):
        print('%s 正在学习%s.' % (self.name, course_name))
    
    def watch_movie(self):
        if self.age < 18:
            print('%s 只能看xx.' % self.name)
        else:
            print('%s 正在xxx.' % self.name)


def main():
    stu1 = Student();
    stu1.name = "Jack"
    stu1.age = 18
    
    stu1.study('Python设计')
    
    stu1.watch_movie()

if __name__ == '__main__':
    main()
