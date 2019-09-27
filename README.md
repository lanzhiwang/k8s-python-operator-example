k8s-python-operator-example
---------------------------
Kubernetes operator written in Python.

* «[Writing a Kubernetes Operator in Python without frameworks and SDK](https://medium.com/flant-com/kubernetes-operator-in-python-451f2d2e33f3)».
* [无需框架和SDK！使用Python来写一个Kubernetes Operator](http://dockerone.com/article/9248)


#### Launching the operator
```bash
usage: copyrator [-h] [--namespace NAMESPACE] [--rule-name RULE_NAME]

Copyrator - copy operator.

optional arguments:
  -h, --help            show this help message and exit
  --namespace NAMESPACE
                        Operator Namespace (or ${NAMESPACE}), default: default
  --rule-name RULE_NAME
                        CRD Name (or ${RULE_NAME}), default: main-rule
``` 
