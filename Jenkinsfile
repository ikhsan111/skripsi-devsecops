pipeline {
    agent any

    tools {
        // Memanggil alat Scanner yang sudah kita install tadi
        sonarQubeScanner 'SonarScanner'
    }

    stages {
        stage('1. Ambil Kode (Checkout)') {
            steps {
                // Mengambil kode terbaru dari GitHub
                checkout scm
            }
        }

        stage('2. Analisis Keamanan (SAST)') {
            steps {
                script {
                    // Mengirim kode ke SonarQube
                    // 'SonarQube' adalah nama server yang kita setting di System
                    withSonarQubeEnv('SonarQube') {
                        sh 'sonar-scanner'
                    }
                }
            }
        }

        stage('3. Quality Gate (HARD BLOCKING)') {
            steps {
                // MENUNGGU HASIL RAPOR DARI SONARQUBE
                timeout(time: 2, unit: 'MINUTES') { 
                    script {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            // JIKA NILAI MERAH, MATIKAN PIPELINE!
                            error "SKRIPSI ALERT: Pipeline diblokir karena ada celah keamanan! Status: ${qg.status}"
                        }
                    }
                }
            }
        }

        stage('4. Deploy Aplikasi') {
            steps {
                echo 'Tahap ini HANYA jalan jika kode aman...'
            }
        }
    }
}
