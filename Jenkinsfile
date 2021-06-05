pipeline{
        agent any
        environment {
            app_version = 'v1'
            TEST_DATABASE_URI = credentials('TEST_DATABASE_URI')
            TEST_SECRET = credentials('TEST_SECRET')
            DATABASE_URI = credentials('DATABASE_URI')
            SECRET = credentials('SECRET')
            DOCKER_USERNAME = credentials('DOCKER_USERNAME')
            DOCKER_PASSWORD = credentials('DOCKER_PASSWORD')
            }
        stages{
            stage('Run pytest'){
                steps{
                    script{
                            sh 'bash scripts/test.sh'
                            }
                        }
                    }
            stage('Push'){
                steps{
                    script{
                            sh 'bash scripts/push.sh'
                            }
                        }
                    }
        //    stage('Ansible Configuration'){
        //         steps{
        //             script{
        //                     sh 'bash scripts/ansible.sh'
        //                     }
        //                 }
        //             }
        //     stage('Install docker and set up swarm'){
        //         steps{
        //             script{
        //                     sh 'ansible-playbook -i inventory.yaml playbook.yaml'
        //                     }
        //                 }
        //             }
        }
}
