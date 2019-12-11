# Ansible Role apache2

This role installs and configures haproxy.

Haproxys configuration itself is mostly inside `/etc/haproxy/haproxy.cfg`, which is not very practical to abstract / template, so you will have to template it using a custom task in your playbook.

What the role can do for you however is concatinate your ssl certificate. Haproxy needs the certificate, key, intermediates and dhparam all in one file, so the role can do that for you. There are three ssl scenarios:
- A bought certificate (specify the certificate, key and intermediates in the vars)
- Letsencrypt (will have to run a post hook to concatinate the files and restart haproxy)
- Locally generating snakeoil certificates (concatinate the files and restart haproxy)

To be able to work with those usecases, you can let the role:
- concatinate files on the server
- do nothing

How you can use this is explained in the documented example playbook `molecule/default/playbook.yml`.


# Example play

An example play can be found in `molecule/default/playbook.yml`.

# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
