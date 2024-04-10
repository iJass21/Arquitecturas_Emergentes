from mininet.topo import Topo

class Act_1(Topo):
    "Topologia Simple"

    def build(self):
        # Añadiendo Hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Añadiendo Switchs
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Añadiendo Links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(s1, s2)
        self.addLink(s2, s3, bw=10, delay="15ms")
        self.addLink(s3, s4, bw=10, delay="30ms", loss=10)
        self.addLink(h3, s3)
        self.addLink(h4, s4)

topos = { "topo": ( lambda : Act_1() ) }