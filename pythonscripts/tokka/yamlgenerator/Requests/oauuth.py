from pyjnius import autoclass
ah = autoclass('com.cerner.pophealth.programs.util.AuthHeader')
ret = ah.main(['-k','c0c11d7a-48c1-461d-8be9-56e9fb60b28f','-s','Jjftdr7d_z7kjM1_GTXKskfQZs9aCD1l'])
print(ret)