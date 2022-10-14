Background
TechTrends is an online website used as a news sharing platform, that enables consumers to access the latest news within the cloud-native ecosystem. In addition to accessing the available articles, readers are able to create new media articles and share them.

Imagine the following scenario: you joined a small team as a Platform Engineer. The team is composed of 2 developers, 1 platform engineer (you), 1 project manager, and 1 manager. The team was assigned with the TechTrends project, aiming to build a fully functional online news sharing platform. The developers in the team are currently working on the first prototype of the TechTrends website. As a platform engineer, you should package and deploy TechTrends to Kubernetes using a CI/CD pipeline.

The web application is written using the Python Flask framework. It uses SQLite, a lightweight disk-based database to store the submitted articles.

Below you can examine the main components of the firsts prototype of the application:

Users > TechTrends UI > Articles > SQLite db

Additionally, the initial sitemap of the website can be found below:

TechTrends
    -About
    -Index
    -New Post
    -404 Page

Where:

About page - presents a quick overview of the TechTrends site
Index page - contains the content of the main page, with a list of all available posts within TechTrends
New Post page - provides a form to submit a new post
404 page - is rendered when an article ID does not exist is accessed
And lastly, the first prototype of the application is storing and accessing posts from the "POSTS" SQL table. A post entry contains the post ID (primary key), creation timestamp, title, and content. The "POSTS" table schema can be examined below:

POSTS
ID*,Integer
Created,Timestamp
Title,Text
Content,Text

Project Steps Overview
1. Apply the best development practices and develop the status and health check endpoints for the TechTrends application.
2. Package the TechTrends application by creating a Dockerfile and Docker image.
3. Implement the Continuous Integration practices, by using GitHub Actions to automate the build and push of the Docker image to DockerHub.
4. Construct the Kubernetes declarative manifests to deploy TechTrends to a sandbox namespace within a Kubernetes cluster. The cluster should be            provisioned using k3s in a vagrant box.
5. Template the Kubernetes manifests using a Helm chart and provide the input configuration files for staging and production environments.
6. Implement the Continuous Delivery practices, by deploying the TechTrends application to staging and production environments using ArgoCD and the Helm chart.