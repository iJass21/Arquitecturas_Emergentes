from mininet.topo import Topo

class Act_4(Topo) :
    " Topologia Simple"

    def build(self) :
        # hosts
        h_Chile = self.addHost('h1')
        h_Australia = self.addHost('h2')

        # Añadiendo Switchs
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Add links
        self.addLink( h_Chile , s1 )
        self.addLink( s1 , s2 , bw =5, delay="50ms", loss =2)
        self.addLink( s2 , s3 , bw =10, delay="70ms", loss =2)
        self.addLink( s3 , s4 , bw =5, delay="30ms", loss =2)
        self.addLink( h_Australia , s4 )

topos = {"topo": ( lambda : Act_4 () ) }

# class Act_4(Topo):
#     "Topologia Simple"

#     def build(self):
#         # hosts
#         h_Chile = self.addHost('h1')
#         h_Australia = self.addHost('h2')

#         # Añadiendo Switchs
#         s1 = self.addSwitch('s1')
#         s2 = self.addSwitch('s2')
#         s3 = self.addSwitch('s3')
#         s4 = self.addSwitch('s4')

#         # Add links
#         self.addLink(h_Chile, s1)
#         self.addLink(s1, s2, bw=5, delay="50ms", loss=2)
#         self.addLink(s2, s3, bw=10, delay="70ms", loss=2)
#         self.addLink(s3, s4, bw=5, delay="30ms", loss=2)
#         self.addLink(h_Australia, s4)

# topos = {"topo": (lambda: Act_4())}

# # Obtener la topología
# topo = Act_4()

# # Obtener el objeto host h2
# h2 = topo.get('h2')

# # Iniciar servidor FTP en h2
# h2.cmd('sudo apt-get install -y vsftpd')
# h2.cmd('sudo service vsftpd start')
