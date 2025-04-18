# Flask Demo Project

这是一个使用 Flask 框架构建的示例项目，展示了基本的 Web 开发功能和最佳实践。

## 项目特点

- 使用 Flask 2.3.3 框架
- 响应式设计
- 现代化 UI 界面
- Docker 容器化部署
- CI/CD 自动化流程
- Nginx 反向代理

## 技术栈

- Python 3.9
- Flask 2.3.3
- HTML5 & CSS3
- Docker & Docker Compose
- Nginx
- Jenkins

## 项目结构

```
flask-cicd-demo/
├── app.py                 # Flask 应用主文件
├── requirements.txt       # Python 依赖
├── Dockerfile            # Docker 构建文件
├── docker-compose.yml    # Docker Compose 配置
├── Jenkinsfile          # Jenkins 流水线配置
├── .env                  # 环境变量配置
├── nginx/               # Nginx 配置
│   ├── nginx.conf
│   └── conf.d/
│       └── default.conf
├── static/              # 静态文件
│   └── css/
│       └── style.css
├── templates/           # HTML 模板
│   ├── index.html
│   └── about.html
└── tests/              # 测试文件
    ├── __init__.py
    └── test_app.py
```

## 快速开始

### 本地开发

1. 克隆项目：
```bash
git clone <repository-url>
cd flask-cicd-demo
```

2. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 运行应用：
```bash
python app.py
```

### Docker 部署

1. 配置环境变量：
```bash
cp .env.example .env
# 编辑 .env 文件，设置你的 Docker Hub 用户名
```

2. 构建并启动容器：
```bash
docker-compose up -d
```

3. 访问应用：
```
http://localhost
```

## CI/CD 流程

项目使用 Jenkins 实现自动化部署流程：

1. 代码检出
2. 安装依赖
3. 运行测试
4. 构建 Docker 镜像
5. 推送镜像到 Docker Hub
6. 部署应用

## 测试

运行测试：
```bash
python -m pytest tests/
```

## 环境变量

- `DOCKER_USERNAME`: Docker Hub 用户名
- `IMAGE_TAG`: Docker 镜像标签

## 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 联系方式

- 项目维护者: [Your Name](mailto:your.email@example.com)
- 项目链接: [Repository URL](https://github.com/yourusername/flask-cicd-demo) 