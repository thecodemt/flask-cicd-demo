pipeline {
    agent any
    
    environment {
        DOCKER_USERNAME = credentials('docker-hub-username')
        DOCKER_PASSWORD = credentials('docker-hub-password')
        IMAGE_NAME = 'flask-demo'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        DEPLOY_TIMEOUT = '60'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Run Tests in Docker') {
            steps {
                sh '''
                    # 构建测试镜像
                    docker build -t ${DOCKER_USERNAME}/${IMAGE_NAME}-test:${IMAGE_TAG} -f Dockerfile.test .
                    
                    # 在容器中运行测试
                    docker run --rm \
                        -v ${WORKSPACE}/test-reports:/app/test-reports \
                        ${DOCKER_USERNAME}/${IMAGE_NAME}-test:${IMAGE_TAG}
                '''
            }
            post {
                always {
                    junit '**/test-reports/*.xml'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} .
                    docker build -t ${DOCKER_USERNAME}/${IMAGE_NAME}:latest .
                '''
            }
        }
        
        stage('Push Docker Image') {
            steps {
                sh '''
                    echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin
                    docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
                    docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:latest
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                    # 验证环境变量
                    if [ -z "${DOCKER_USERNAME}" ] || [ -z "${IMAGE_TAG}" ]; then
                        echo "Error: Required environment variables are not set"
                        exit 1
                    fi
                    
                    # 备份当前部署
                    if docker-compose ps | grep -q "Up"; then
                        docker-compose ps > deployment_backup.txt
                        echo "Current deployment backed up"
                    fi
                    
                    # 创建 .env 文件
                    echo "DOCKER_USERNAME=${DOCKER_USERNAME}" > .env
                    echo "IMAGE_TAG=${IMAGE_TAG}" >> .env
                    
                    # 部署应用
                    docker-compose down
                    docker-compose pull
                    docker-compose up -d
                    
                    # 等待服务启动
                    echo "Waiting for services to start..."
                    timeout ${DEPLOY_TIMEOUT} bash -c '
                        while ! curl -f http://localhost:5000/health > /dev/null 2>&1; do
                            echo "Waiting for service to be healthy..."
                            sleep 5
                        done
                    '
                    
                    # 验证部署
                    if [ $? -eq 0 ]; then
                        echo "Deployment successful!"
                        # 清理旧镜像
                        docker image prune -f
                    else
                        echo "Deployment failed, initiating rollback..."
                        # 回滚到上一个版本
                        if [ -f deployment_backup.txt ]; then
                            docker-compose down
                            docker-compose up -d
                        fi
                        exit 1
                    fi
                '''
            }
        }
    }
    
    post {
        always {
            sh '''
                # 清理工作空间
                rm -f .env deployment_backup.txt
                docker-compose down || true
            '''
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
} 