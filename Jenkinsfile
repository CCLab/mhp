node {
  // Checkout latest revision of code
  def projectName = "mhp"
  def gitVars = checkout([
    $class: 'GitSCM',
    branches: scm.branches,
    doGenerateSubmoduleConfigurations: false,
    extensions: [[
      $class: 'SubmoduleOption',
      disableSubmodules: false,
      parentCredentials: true,
      recursiveSubmodules: true,
      reference: '',
      trackingSubmodules: false
    ]],
    submoduleCfg: [],
    userRemoteConfigs: scm.userRemoteConfigs
  ])

  def gitShortCommit = gitVars.GIT_COMMIT.take(6)
  def rebuildFile = "$JENKINS_HOME/envfile_$JOB_BASE_NAME"
  // Environment rebuild check file
  if (env.JOB_BASE_NAME.startsWith("PR-")) {
        rebuildFile = "$JENKINS_HOME/envfile_PR_$JOB_BASE_NAME"
  }
  // How much time environment is considered to be "fresh"
  def envUpdate = System.currentTimeMillis() - 7 * 24 * 60 * 60 * 1000 // days * hours * minutes * seconds * miliseconds
  // From now we want to use private registry
  docker.withRegistry('https://registry.laboratorium.ee/', 'docker-registry-login') { // docker-registry-login is declared in Jenkins secrets
    // Check if we need to rebuild environment container when requirements or Dockerfile.base is changed
    print("Previous commit: $gitVars.GIT_PREVIOUS_COMMIT")
    print("Current commit: $gitVars.GIT_COMMIT")

    def shouldRebuild = sh(
        script: "git diff --name-only $gitVars.GIT_PREVIOUS_COMMIT $gitVars.GIT_COMMIT | egrep 'Dockerfile.base|requirements' -c || true",
        returnStdout: true
    ).trim().toInteger()

    // Check if environment is not fresh or we are on the first commit
    rebuild = new File(rebuildFile)
    if (!rebuild.isFile() || (rebuild.lastModified() < envUpdate) || !gitVars.GIT_PREVIOUS_COMMIT) {
        print("Environment base container is not fresh, will be rebuilt")
        shouldRebuild+=1
        rebuild.createNewFile()
        rebuild.write("Last environment build: $gitVars.GIT_BRANCH-$gitShortCommit")
    }
    // Check if this is a pull request to run lightweight process
    if (shouldRebuild > 0) {
        stage('Rebuild Environment') {
            // Rebuild Environment docker
            sh 'cp Dockerfile.base Dockerfile'
            def base_image = docker.build("registry.laboratorium.ee/$projectName/$projectName-base:latest", '.')
            base_image.push('latest')
        }
    } else {
        stage('Rebuild Environment') {
            print("Environment up-to-date. Skipping")
        }
    }
    stage('Rebuild Application') {
        // Rebuild application container on top of environment container
        sh 'cp Dockerfile.app Dockerfile'
        def app = docker.build("registry.laboratorium.ee/$projectName/$projectName:latest", '.')
    }
    stage('Execute tests') {
        docker.image("registry.laboratorium.ee/postgres/postgres:latest").withRun("") { c ->
            docker.image("registry.laboratorium.ee/postgres/postgres:latest").inside("--link ${c.id}:db") {
                /* Wait until postgresql service is up */
                sh 'export PGPASSWORD=postgres; while ! psql -h db --user postgres -c "select 1"; do sleep 1; done'
            }

            def app = docker.image("registry.laboratorium.ee/$projectName/$projectName:latest")
            app.inside("--env-file $WORKSPACE/deployment/ci_environment.properties --link ${c.id}:db") {
                //
                // THIS IS THE PLACE WHERE YOU SHOULD HAVE EXECUTE WORKFLOW RELATED TO TESTS!
                //
                sh "cd /code/ && flake8 . && ./run_js_scss_linters.py && python3 manage.py test"
            }
            // Skip docker tagging and push if this is a PR
            if (!(env.JOB_BASE_NAME.startsWith("PR-"))) {
                // Save latest tag
                app.tag('latest')
                app.push('latest')
            }

            //Save branch-commit tag
            def branch = gitVars.GIT_BRANCH.split('/')[-1]
            print("Push for branch: $branch")
            app.tag("$branch-$gitShortCommit")
            app.push("$branch-$gitShortCommit")
        }
    }
    stage('Docker Cleanup') {
        // Clean everything related to project that was built before project base environment latest docker
        // Due to escape hell, better is to split this to more lines
        def docker = 'docker image rm --force $(docker images --filter "before=registry.laboratorium.ee/'
        def docker2 = '-base" | grep "'
        def awk = '" | awk "{print $3}" | xargs) > /dev/null 2>&1 || docker image prune --force --filter "dangling=true"'
        sh "$docker$projectName/$projectName$docker2$projectName$awk"
    }
  }
}
