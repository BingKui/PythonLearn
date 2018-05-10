# 熟悉创建一个网站的步骤 和需要的包

# 环境搭建
# 安装 lpthw.web 

# pip install lpthw.web   
# 有可能会用到 sudo 命令

# 简单的 hollow world 项目

# bin/app.py

import web

urls = ('/', 'index')

app = web.application(urls, globals())

class index:
    def GET(self):
        greeting = "Hellow World"
        return greeting

if __name__ == "__main__":
    app.run()

# 运行
# python bin/app.py

# python 项目运行都是在根目录执行运行命令，不用一步一步进入子目录去运行


# 创建基本的模板文件
# templates/index.html

# 模板工作原理
# 1.在 bin/app.py 里面添加一个叫做 render 的新变量， 它本身是一个 web.template.render 对象
# 2.将 template/ 作为参数传递给这个对象，告诉 render 从哪里加载模板
# 3.浏览器触发 index.GET 后，调用render.index，将 greeting 作为一个变量传递给它
# 4.渲染模板
# 5.模板文件缩进敏感，执行模板中的函数
# 6.模板检查需要的变量，存在打印内容，不存在打印其他内容

