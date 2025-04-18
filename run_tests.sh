#!/bin/bash

# 安装测试依赖
pip install -r requirements.txt

# 运行测试
python -m pytest tests/ -v

# 生成测试覆盖率报告
python -m pytest --cov=app tests/ 