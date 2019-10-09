import kubernetes

from copyrator.const import CRD_GROUP, CRD_VERSION, CRD_PLURAL

__all__ = [
    'load_crd',
]


def load_crd(namespace, name):
    """
    Method for CRD loading.
    It is used to get the object's watching settings.
    """
    client = kubernetes.client.ApiClient()
    custom_api = kubernetes.client.CustomObjectsApi(client)

    crd = custom_api.get_namespaced_custom_object(
        CRD_GROUP,  # flant.com
        CRD_VERSION,  # v1
        namespace,  # default
        CRD_PLURAL,  # copyrators
        name,  # main-rule
    )

    # {'ruleType': 'configmap', 'selector': {'copyrator': 'true'}, 'namespace': ['default']}
    return {x: crd[x] for x in ('ruleType', 'selector', 'namespace')}

