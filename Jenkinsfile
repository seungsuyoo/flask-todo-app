pipeline {
  agent any

  environment {
    APP_NAME = 'flask-todo-app'
    APP_PORT = '5000'
  }

  stages {
    stage('준비') {
      steps {
        echo '애플리케이션 빌드 시작'
        checkout scm
      }
    }

    stage('의존성 설치') {
      steps {
        sh '''
        python3 -m venv venv
        . venv/bin/activate
        pip install -r requirements.txt
        '''
      }
    }

    stage('Unit 테스트') {
      steps {
        sh '''
        . venv/bin/activate
        pytest test_app.py -v --junit-xml=unit-results.xml
        '''
      }
    }
  }

  post {
    always {
      junit '*-results.xml'
    }
    success {
      echo '모든 단계 성공'
    }
    failure {
      echo '빌드 실패'
    }
  }
}