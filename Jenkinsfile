pipeline {
    agent any
    
    environment {
        DOCKER_USERNAME = credentials('docker-hub-username')
        DOCKER_PASSWORD = credentials('docker-hub-password')
        IMAGE_NAME = 'flask-demo'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
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
                    # 创建 .env 文件
                    echo "DOCKER_USERNAME=${DOCKER_USERNAME}" > .env
                    echo "IMAGE_TAG=${IMAGE_TAG}" >> .env
                    
                    # 部署应用
                    docker-compose down
                    docker-compose pull
                    docker-compose up -d
                    
                    # 验证部署
                    sleep 10
                    curl -f http://localhost || exit 1
                '''
            }
        }
    }
    
    post {
        always {
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