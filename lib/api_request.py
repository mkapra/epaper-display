def get_servers():
    return {
            "sun":     True,
            "jupyter": True,
            "sun":     True,
            "theoden": True,
            "gimli":   False
    }

def get_mail_status():
    return {
      "acme-mailcow": {
        "container": "acme-mailcow",
        "image": "mailcow/acme:1.63",
        "started_at": "2019-12-22T21:00:08.270660275Z",
        "state": "error",
        "type": "info"
      },
      "clamd-mailcow": {
        "container": "clamd-mailcow",
        "image": "mailcow/clamd:1.35",
        "started_at": "2019-12-22T21:00:01.622856172Z",
        "state": "running",
        "type": "info"
      },
      "dockerapi-mailcow": {
        "container": "dockerapi-mailcow",
        "image": "mailcow/dockerapi:1.36",
        "started_at": "2019-12-22T20:59:59.984797808Z",
        "state": "running",
        "type": "info"
      },
      "dovecot-mailcow": {
        "container": "dovecot-mailcow",
        "image": "mailcow/dovecot:1.104",
        "started_at": "2019-12-22T21:00:08.988680259Z",
        "state": "running",
        "type": "info"
      },
      "ipv6nat-mailcow": {
        "container": "ipv6nat-mailcow",
        "image": "robbertkl/ipv6nat",
        "started_at": "2019-12-22T21:06:37.273225445Z",
        "state": "running",
        "type": "info"
      },
      "memcached-mailcow": {
        "container": "memcached-mailcow",
        "image": "memcached:alpine",
        "started_at": "2019-12-22T20:59:58.0907785Z",
        "state": "running",
        "type": "info"
      },
      "mysql-mailcow": {
        "container": "mysql-mailcow",
        "image": "mariadb:10.3",
        "started_at": "2019-12-22T21:00:02.201937528Z",
        "state": "running",
        "type": "info"
      },
      "netfilter-mailcow": {
        "container": "netfilter-mailcow",
        "image": "mailcow/netfilter:1.31",
        "started_at": "2019-12-22T21:00:09.851559297Z",
        "state": "running",
        "type": "info"
      },
      "nginx-mailcow": {
        "container": "nginx-mailcow",
        "image": "nginx:mainline-alpine",
        "started_at": "2019-12-22T21:00:12.9843038Z",
        "state": "running",
        "type": "info"
      },
      "olefy-mailcow": {
        "container": "olefy-mailcow",
        "image": "mailcow/olefy:1.2",
        "started_at": "2019-12-22T20:59:59.676259274Z",
        "state": "running",
        "type": "info"
      },
      "php-fpm-mailcow": {
        "container": "php-fpm-mailcow",
        "image": "mailcow/phpfpm:1.55",
        "started_at": "2019-12-22T21:00:00.955808957Z",
        "state": "running",
        "type": "info"
      },
      "postfix-mailcow": {
        "container": "postfix-mailcow",
        "image": "mailcow/postfix:1.44",
        "started_at": "2019-12-22T21:00:07.186717617Z",
        "state": "running",
        "type": "info"
      },
      "redis-mailcow": {
        "container": "redis-mailcow",
        "image": "redis:5-alpine",
        "started_at": "2019-12-22T20:59:56.827166834Z",
        "state": "running",
        "type": "info"
      },
      "rspamd-mailcow": {
        "container": "rspamd-mailcow",
        "image": "mailcow/rspamd:1.56",
        "started_at": "2019-12-22T21:00:12.456075355Z",
        "state": "running",
        "type": "info"
      },
      "sogo-mailcow": {
        "container": "sogo-mailcow",
        "image": "mailcow/sogo:1.65",
        "started_at": "2019-12-22T20:59:58.382274592Z",
        "state": "running",
        "type": "info"
      },
      "solr-mailcow": {
        "container": "solr-mailcow",
        "image": "mailcow/solr:1.7",
        "started_at": "2019-12-22T20:59:59.635413798Z",
        "state": "running",
        "type": "info"
      },
      "unbound-mailcow": {
        "container": "unbound-mailcow",
        "image": "mailcow/unbound:1.10",
        "started_at": "2019-12-22T20:59:58.760595825Z",
        "state": "running",
        "type": "info"
      },
      "watchdog-mailcow": {
        "container": "watchdog-mailcow",
        "image": "mailcow/watchdog:1.65",
        "started_at": "2019-12-22T20:59:56.028660382Z",
        "state": "running",
        "type": "info"
      }
    }

def get_mail_status_stats():
    count = 0
    not_ok = []
    for container, infos in get_mail_status().items():
        count += 1
        if infos["state"] != "running":
            not_ok.append(container)

    return count, not_ok
