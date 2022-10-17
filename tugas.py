#!/usr/bin/env python

'Setting position of the nodes'

import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(args):

    net = Mininet_wifi()

    info("*** Creating nodes\n")
    h1 = net.addHost('h1', mac='00:00:00:00:00:01', ip='10.0.0.2/8')
    
    sta1 = net.addStation( 'sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', position='25,50,0', range='20' )
    sta2 = net.addStation( 'sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', position='25,50,0', range='20' )
    sta3 = net.addStation( 'sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8', position='25,50,0', range='20' )
    sta4 = net.addStation( 'sta4', mac='00:00:00:00:00:05', ip='10.0.0.5/8', position='25,50,0', range='20' )
    
    ap1 = net.addAccessPoint('ap1', ssid='new-ssid1', mode='g', channel='1', position='50,50,0', range='40' )
    ap2 = net.addAccessPoint('ap2', ssid='new-ssid2', mode='g', channel='1', position='100,50,0', range='40' )
    ap3 = net.addAccessPoint('ap3', ssid='new-ssid3', mode='g', channel='1', position='150,50,0', range='40' )
    
    s4 = net.addSwitch('s4')
    
    c1 = net.addController('c1')

    net.setPropagationModel(model="logDistance", exp=4.3)

    info("*** Configuring WiFi Nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")
    net.addLink(h1, s4)
    net.addLink(ap1, s4)
    net.addLink(ap2, s4)
    net.addLink(ap3, s4)
    
    net.addLink(ap1, sta1)
    net.addLink(ap1, sta2)
    net.addLink(ap1, sta3)
    net.addLink(ap1, sta4)
    
    net.plotGraph(max_x=200, max_y=200)
    
    net.startMobility(time=0)
    net.mobility(sta1, 'start', time=1, position='25,50,0')
    net.mobility(sta1, 'stop', time=30, position='150,50,0')
    
    net.mobility(sta2, 'start', time=1, position='25,50,0')
    net.mobility(sta2, 'stop', time=40, position='150,50,0')
    
    net.mobility(sta3, 'start', time=1, position='25,50,0')
    net.mobility(sta3, 'stop', time=50, position='150,50,0')
    
    net.mobility(sta4, 'start', time=1, position='25,50,0')
    net.mobility(sta4, 'stop', time=60, position='150,50,0')
    net.stopMobility(time=60)
    
    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])
    ap2.start([c1])
    ap3.start([c1])
    s4.start([c1])

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
