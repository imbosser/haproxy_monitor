from haproxyadmin import haproxy
hap = haproxy.HAProxy(socket_dir='/var/run/haproxy')
frontends = hap.frontends()
for frontend in frontends:
 print(frontend.name, frontend.requests, frontend.process_nb)
 FRONTEND_METRICS = ['scur', 'stot']
 for m in FRONTEND_METRICS:
    print("name {} value {}".format(m, frontend.metric(m)))

backends = hap.backends()
for backend in backends:
   print(backend.name, backend.requests, backend.process_nb)
   BACKEND_METRICS = ['scur', 'stot']
   for m in BACKEND_METRICS:
    print("name {} value {}".format(m, backend.metric(m)))
   servers = backend.servers()
   for server in servers:
      print(" ", server.name, server.requests)

