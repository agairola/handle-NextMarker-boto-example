import boto3

wafClient = boto3.client('wafv2')

def get_all_welacl(start_marker=None, webacl_list=None):
    wafClient = boto3.client('wafv2')
    params = None
    if start_marker:
        params = start_marker
        wafListGlobal = wafClient.list_web_acls(Scope='REGIONAL', Limit=10,NextMarker=params)
    else:
        wafListGlobal = wafClient.list_web_acls(Scope='REGIONAL', Limit=10)
    if webacl_list:
        wafListGlobal['WebACLs'].extend(webacl_list)
    while 'NextMarker' in wafListGlobal:
        next_marker = wafListGlobal['NextMarker']
        webacl_list = wafListGlobal['WebACLs']
        wafListGlobal = get_all_welacl(next_marker,webacl_list)
    return wafListGlobal