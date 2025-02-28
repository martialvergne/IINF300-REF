# Mise en place d'un déploiement continu d'une application docker sur Harbor
## Présentation du repo

Ce repo possède un dossier `docker` , dans celui-ci on retrouve un fichier `Dockerfile` qui créé une application basée sur les sources dans le dossier `docker/app`.

Nous retrouvons également le dossier `.github/workflows`. Dans celui-ci nous retrouvons le fichier build-demo qui sert pour la mise en place d'une pipeline qui permet de déployer une image sur harbor. Plus d'info "https://docs.github.com/en/actions/writing-workflows/quickstart"

## Consignes d'amélioration 

### Exercice 1

Par groupe clonez ce repo et vérifiez que le workflow fonctionne bien. 

Attention, placez le mot de passe habituel qui va bien dans https://github.com/___urldevotrerepo___/settings/secrets/actions et changez `harbor.kakor.ovh/ipi/correction` par `harbor.kakor.ovh/ipi/groupe-x`.

## Exercice 2

En partant de l'exemple https://github.com/marketplace/actions/python-linter, mettez en place un linter pour le code Python dans un job séparé dans le fichier `build-demo.yml`

## Exercice 3

Mettez en place Hadolint via l'exemple du repo ci-dessous de la même manière que pour PEP8 : https://github.com/marketplace/actions/python-linter

## Exercice 4 

En partant de l'exemple fonctionnel du lien suivant https://aschmelyun.com/blog/using-docker-run-inside-of-github-actions/, testez l'image en vous assurant que vous pouvez créer un nouveau livre en utilisant la commande suivante : ```curl --header "Content-Type: application/json" http://localhost:5000/librairie/livres -d '{"titre": "DevSecOps DEAVSETS", "auteur": "Jordan Assouline"}' ```

## Exercice 5

En vous connectant sur https://sonarqube.apps.openshift.kakor.ovh en utilisant le user ipi et le mot passe habituel dédoublé, générez un token qui vous servira pour ajouter le job suivant :

```
  sonarqube:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0
    - name: SonarQube Scan
      uses: SonarSource/sonarqube-scan-action@<ce/actions/official-sonarqube-scan
      env:
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        SONAR_HOST_URL: https://sonarqube.apps.openshift.kakor.ovh
```

> Attention à mettre votre token dans les secret github et à modifier le fichier `sonar-project.properties` pour que le nom de projet soit dépendant du groupe

## Exercice 6

Mise en place du Helm. 

Afin de pouvoir déployer notre application, il va falloir créer une nouvelle chart helm basée sur l'ébauche du dossier ```librairie-helm``` .

Pour créer la chart helm, voici les consignes à suivre :

- Ajoutez un deployment `python` dans templates. Variabilisez le nom de l'image et exposez le port 5000.
- Ajoutez un service du même nom qui va pointer sur le port 5000 du déploiement afin de relier celui-ci au service.  

## Exercice 7

A partir de l'image harbor.kakor.ovh/public/oc-helm:1.0 créez une pipeline Github qui va lancer les actions suivantes : 

S'authentifier au cluster à partir d'un token généré à partir de l'interface graphique d'openshift ( https://console-openshift-console.apps.openshift.kakor.ovh ) :
```oc login ....```

Puis déployez l'application avec helm en utilisant le sha du commit pour coller à la version de l'image :
``` helm upgrade --install groupe-x librairie-helm/ --set image=<urlimage>:${{ github.sha }} ```

## Exercice 8

A partir de l'exemple ci-dessous, créez une règle sur un port TCP de votre choix qui va utiliser la Security Group :

```
---
apiVersion: networking.openstack.crossplane.io/v1alpha1
kind: SecgroupV2
metadata:
  name: example-security-group
  namespace: crossplane-system
spec:
  forProvider:
    name: "exemple-nsg"
    description: "Example security group"
    region: "RegionOne"
    tenantId: "2e4f56f043fc49db886d5d54625cad33"
  providerConfigRef:
    name: provider-openstack-config
```

Basez-vous sur la description de l'api https://marketplace.upbound.io/providers/crossplane-contrib/provider-openstack/v0.4.0/resources/networking.openstack.crossplane.io/SecgroupRuleV2/v1alpha1 comme fait pendant le cours. 

Créez le fichier dans la chart helm et redéployez. 
