# PFSenseLeasesToDnsmasq
Get static leases from pfsense config.xml and convert them to dnsmasq format

pfsense's `config.xml` looks something like this:

```
	<staticmap>
		<mac>10:7b:44:8f:a1:37</mac>
		<cid>bigserver</cid>
		<ipaddr>192.168.1.10</ipaddr>
		<hostname>bigserver</hostname>
		<descr></descr>
		<filename></filename>
		<rootpath></rootpath>
		<defaultleasetime></defaultleasetime>
		<maxleasetime></maxleasetime>
		<gateway></gateway>
		<domain></domain>
		<domainsearchlist></domainsearchlist>
		<ddnsdomain></ddnsdomain>
		<ddnsdomainprimary></ddnsdomainprimary>
		<ddnsdomainkeyname></ddnsdomainkeyname>
		<ddnsdomainkey></ddnsdomainkey>
		<tftp></tftp>
		<ldap></ldap>
	</staticmap>
```

and this is what you get:
```
$ ./convert.py -c config.xml
dhcp-host=lan,10:7b:44:8f:a1:37,192.168.1.10 # bigserver
dhcp-host=lan,14:dd:a9:dc:44:fc,192.168.1.14 # homeserver
dhcp-host=lan,f0:4f:7c:f2:2c:b4,192.168.1.44 # kindle
dhcp-host=lan,62:63:65:31:34:65,192.168.1.142 # media
dhcp-host=lan,36:61:36:66:32:34,192.168.1.143 # Gogs
dhcp-host=lan,36:61:36:66:32:36,192.168.1.144 # web
dhcp-host=lan,36:61:36:66:32:35,192.168.1.145 # db
dhcp-host=lan,36:33:35:34:62:36,192.168.1.146 # mumble
dhcp-host=lan,e2:30:1c:f3:86:32,192.168.1.147 # dns
dhcp-host=lan,32:62:32:65:36:63,192.168.1.150 # books
dhcp-host=lan,66:33:33:62:35:62,192.168.1.152 # aptcacher
dhcp-host=lan,5e:d1:c9:2a:ef:df,192.168.1.154 # jenkins
dhcp-host=lan,2e:a1:12:5a:9d:64,192.168.1.155 # taskserver
dhcp-host=lan,16:c6:e6:1b:64:6a,192.168.1.156 # grafana
dhcp-host=lan,46:a5:13:b0:fc:ef,192.168.1.160 # lbalancer1
dhcp-host=lan,e2:b9:1d:26:54:ab,192.168.1.161 # lbalancer2
dhcp-host=lan,1a:64:b6:bf:36:17,192.168.1.170 # odroid-u2
dhcp-host=lan,00:1e:06:32:04:a7,192.168.1.171 # odroid-xu4
dhcp-host=lan,00:1e:06:33:28:05,192.168.1.172 # odroid-c2
```
