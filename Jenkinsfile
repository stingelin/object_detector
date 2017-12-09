#!/usr/bin/env groovy

pipeline {
    agent {
        docker {
            image 'continuumio/miniconda3'
            args '-u 0 --rm --name ai-conda -v /etc/passwd:/etc/passwd -v /etc/group:/etc/group -v /home/jenkins/.conda3/pkgs:/home/jenkins/.conda/pkgs:rw,z'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            environment {
                CONDA_ENV = "${env.WORKSPACE}/test/${env.STAGE_NAME}"
            }
            steps {
                sh 'conda info'
                sh 'ls -la /opt/conda/pkgs'
                sh 'conda env create -q -f environment.yml -p $CONDA_ENV'
                sh '''#!/bin/bash -ex
                    source $CONDA_ENV/bin/activate $CONDA_ENV
                    pytest -vs utils/
                    python -m unittest discover -s object_detection -p "*_test.py"
                '''

            }
        }

        stage('Deploy - Staging'){
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo 'Placeholder: Deploying to staging/dev'
            }
        }

        stage('Sanity check') {
            steps {
                input "Does the staging env look good? Good enough to deploy into production?"
            }
        }

        stage('Deploy - Production') {
            steps {
                echo 'Placeholder: Deploying to prod'
            }
        }
    }

    post {
        always {
            echo 'The job has finished.'
            slackSend channel: '#ai-nsf-jenkins-jobs',
                color: 'good',
                message: "The pipeline ${currentBuild.fillDisplayName} completed."
        }
        success {
            slackSend channel: '#ai-nsf-jenkins-jobs',
                color: 'good',
                message: "The pipeline ${currentBuild.fillDisplayName} completed successfully."
        }
        unstable {
            slackSend channel: '#ai-nsf-jenkins-jobs',
                color: 'warning',
                message: "The pipeline ${currentBuild.fillDisplayName} is unstable. Check it out here: ${env.BUILD_URL}"
        }
        failure {
            slackSend channel: '#ai-nsf-jenkins-jobs',
                color: 'danger',
                message: "@all The pipeline ${currentBuild.fillDisplayName} has failed! Check it out here: ${env.BUILD_URL}"
        }
        /*
        changed {

        }
        */
    }
}