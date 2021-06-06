pipeline{
        agent any
        environment {
            app_version = 'v1'
            TEST_DATABASE_URI = credentials('TEST_DATABASE_URI')
            DATABASE_URI = credentials('DATABASE_URI')
            DOCKER_USERNAME = credentials('DOCKER_USERNAME')
            DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
            }
        stages{
            stage('Run pytest'){
                steps{
                    script{
                            sh 'bash jenkins/test.sh'
                            }
                        }
                    }
            stage('Push'){
                steps{
                    script{
                            sh 'bash jenkins/push.sh'
                            }
                        }
                    }
          stage('Ansible Configuration'){
                steps{
                    script{
                            sh 'bash jenkins/ansible.sh'
                            }
                        }
                    }
            stage('Install docker and set up swarm'){
                steps{
                    script{
                            sh 'ansible-playbook -i inventory.yaml playbook.yaml'
                            }
                        }
                    }
        }
}
