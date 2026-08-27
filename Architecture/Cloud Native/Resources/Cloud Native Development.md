# Cloud Native Development

Tags: cloud-native, development, kubernetes
Link: https://www.youtube.com/watch?v=wZjxK8K1-Xo
Type: Talk

[Cloud Native Development - Pablo Chico de Guzmán](https://www.youtube.com/watch?v=wZjxK8K1-Xo)

- Cloud Native means: Dynamic resources + Centralized logging + Centralized metrics + Replicable (docker)
- Local development comes with many integration challenges. Local environments are not cloud native (do not meet characteristics above)
- Take Development as seriously as Production:
    - Same hardware, network, ingress controllers, certificates, kubernetes manifests and kubernetes version/configuration
    - Keep differences at a minimum
- New scenarios enabled by this approach:
    - High performance computing during development
    - Pair programming across services
    - Remotely fix other dev's environments. Example: something broke in the DB in your local machine, someone from other team needs to join you and fix it in your machine. With this approach she can fix it for you asynchronously in the remote env.
    - No mocks, no proxies, entire stack available
    - Access to testing third-party APIs usually are only accessible from integration environments, having these dev clusters in there allow to use the APIs.
- Drawbacks of remote cloud native development:
    - Development feedback is slower. Locally code - build - test is very quick (hot reloading, etc)
- How to, tooling:
    - Skaffold / Draft. Automatic but still slow
    - Telepresence: [https://www.telepresence.io](https://www.telepresence.io/) Makes local machine seem as within the remote k8s cluster, meaning my local service under dev can access remote k8s deployed services and viceversa.
        - Does not integrate using same manifests, resources for service under dev are not dynamic, does not allow collaboration.
    - Eclipse Che: requires IDE
    - CND (su libro): local dev container is deployed within the cluster using the manifests. However, instead of re-deploying on every change, a container is injected in the remote pod and synchronises code/artifacts upon changes.