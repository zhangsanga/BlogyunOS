from flask_cors import CORS

from app.router import service

application = service.get_app()

# 添加跨域插件
CORS(application, supports_credentials=True)

if __name__ == '__main__':

    # 启动服务器
    application.run(debug=True)
