# import gi
# gi.require_version("Gtk", "3.24")

from gi.repository import Gtk as g,cairo
try:
    from gi_composites import GtkTemplate
except:
    from sysmontask.gi_composites import GtkTemplate


if __name__=='sysmontask.sidepane':
    from sysmontask.sysmontask import files_dir
else:
    from sysmontask import files_dir

@GtkTemplate(ui=files_dir+'/diskSidepane.glade')
class diskSidepaneWidget(g.Box):

    # Required else you would need to specify the full module
    # name in mywidget.ui (__main__+MyWidget)
    __gtype_name__ = 'diskSidepaneWidget'
    
    disksidepanetextlabel= GtkTemplate.Child()
    disksidepanelabelvalue = GtkTemplate.Child()
    disksidepanedrawarea=GtkTemplate.Child()
    disk_switcher_button=GtkTemplate.Child()


    # Alternative way to specify multiple widgets
    #label1, entry = GtkTemplate.Child.widgets(2)

    def __init__(self):
        super(g.Box, self).__init__()
        
        # This must occur *after* you initialize your base
        self.init_template()
    
    def givedata(self,secondself,index):
        self.diskactiveArray=secondself.diskActiveArray[index]
    
    @GtkTemplate.Callback
    def on_diskSidepaneDrawArea_draw(self,dr,cr):
        cr.set_line_width(2)

        w=self.disksidepanedrawarea.get_allocated_width()
        h=self.disksidepanedrawarea.get_allocated_height()
        scalingfactor=h/100.0
        #creating outer rectangle
        cr.set_source_rgba(.109,.670,.0588,1)
        cr.set_line_width(3)
        cr.rectangle(0,0,w,h)
        cr.stroke()
        
        
        stepsize=w/99.0
        #print("in draw stepsize",stepsize)
        # for i in range(0,99):
        #     # not effcient way to fill the bars (drawing)
        #     cr.set_source_rgba(.431,1,.04,0.25)  #for changing the fill color
        #     cr.move_to(i*stepsize,scalingfactor*(100-self.diskactiveArray[i])+2)
        #     cr.line_to((i+1)*stepsize,scalingfactor*(100-self.diskactiveArray[i+1])+2)
        #     cr.line_to((i+1)*stepsize,h)
        #     cr.line_to(i*stepsize,h)
        #     cr.move_to(i*stepsize,scalingfactor*(100-self.diskactiveArray[i])+2)

        #     cr.fill()
        #     cr.stroke()
        #     # for outer line
        #     cr.set_line_width(1.5)
        #     cr.set_source_rgba(.109,.670,.0588,1) #for changing the outer line color
        #     cr.move_to(i*stepsize,scalingfactor*(100-self.diskactiveArray[i])+2)
        #     cr.line_to((i+1)*stepsize,scalingfactor*(100-self.diskactiveArray[i+1])+2)
        #     cr.stroke()

        cr.set_source_rgba(.109,.670,.0588,1) #for changing the outer line color
        cr.set_line_width(1.5)
        cr.move_to(0,scalingfactor*(100-self.diskactiveArray[0])+2)
        for i in range(0,99):
            cr.line_to((i+1)*stepsize,scalingfactor*(100-self.diskactiveArray[i+1])+2)
        cr.stroke_preserve()

        cr.set_source_rgba(.431,1,.04,0.25)  #for changing the fill color
        cr.line_to(w,h)
        cr.line_to(0,h)
        cr.move_to(0,scalingfactor*(100-self.diskactiveArray[0])+2)
        cr.fill()
        cr.stroke()


        return False

@GtkTemplate(ui=files_dir+'/netSidepane.glade')
class netSidepaneWidget(g.Box):

    # Required else you would need to specify the full module
    # name in mywidget.ui (__main__+MyWidget)
    __gtype_name__ = 'netSidepaneWidget'
    
    netsidepanetextlabel= GtkTemplate.Child()
    netsidepanelabelvalue = GtkTemplate.Child()
    netsidepanedrawarea=GtkTemplate.Child()
    net_switcher_button=GtkTemplate.Child()



    # Alternative way to specify multiple widgets
    #label1, entry = GtkTemplate.Child.widgets(2)

    def __init__(self):
        super(g.Box, self).__init__()
        
        # This must occur *after* you initialize your base
        self.init_template()
        self.netmxScalingFactor=1

    def givedata(self,secondself,index):
        self.netRecSpeedArray=secondself.netReceiveArray[index]
        self.netSendSpeedArray=secondself.netSendArray[index]

    @GtkTemplate.Callback
    def on_netSidepaneDrawArea_draw(self,dr,cr):
        cr.set_line_width(2)

        w=self.netsidepanedrawarea.get_allocated_width()
        h=self.netsidepanedrawarea.get_allocated_height()

        speedstep=250*1024          #250KB/s
        maximumcurrentspeed=max(max(self.netRecSpeedArray),max(self.netSendSpeedArray))
        currentscalespeed=self.netmxScalingFactor*speedstep
        while(currentscalespeed<maximumcurrentspeed):
            self.netmxScalingFactor+=1
            currentscalespeed=self.netmxScalingFactor*speedstep
        while(currentscalespeed>maximumcurrentspeed and self.netmxScalingFactor>1):
            self.netmxScalingFactor-=1
            currentscalespeed=self.netmxScalingFactor*speedstep
        

        scalingfactor=h/currentscalespeed
        #creating outer rectangle
        cr.set_source_rgba(.458,.141,.141,1)
        cr.set_line_width(3)
        cr.rectangle(0,0,w,h)
        cr.stroke()
        
        
        stepsize=w/99.0
        #print("in draw stepsize",stepsize)
        # for i in range(0,99):
        #     # not effcient way to fill the bars (drawing)
        #     cr.set_source_rgba(.709,.164,.164,.2)  #for changing the fill color
        #     cr.move_to(i*stepsize,scalingfactor*(currentscalespeed-self.netRecSpeedArray[i])+2)
        #     cr.line_to((i+1)*stepsize,scalingfactor*(currentscalespeed-self.netRecSpeedArray[i+1])+2)
        #     cr.line_to((i+1)*stepsize,h)
        #     cr.line_to(i*stepsize,h)
        #     cr.move_to(i*stepsize,scalingfactor*(currentscalespeed-self.netRecSpeedArray[i])+2)
        #     cr.fill()
        #     cr.stroke()

        #     # for outer line read speed
        #     cr.set_line_width(1.5)
        #     cr.set_source_rgba(.709,.164,.164,1) #for changing the outer line color
        #     cr.move_to(i*stepsize,scalingfactor*(currentscalespeed-self.netRecSpeedArray[i])+2)
        #     cr.line_to((i+1)*stepsize,scalingfactor*(currentscalespeed-self.netRecSpeedArray[i+1])+2)
        #     cr.stroke()

        #     #for write
        #     cr.set_source_rgba(1,.313,.313,.2)  #for changing the fill color
        #     cr.move_to(i*stepsize,scalingfactor*(currentscalespeed-self.netSendSpeedArray[i])+2)
        #     cr.line_to((i+1)*stepsize,scalingfactor*(currentscalespeed-self.netSendSpeedArray[i+1])+2)
        #     cr.line_to((i+1)*stepsize,h)
        #     cr.line_to(i*stepsize,h)
        #     cr.move_to(i*stepsize,scalingfactor*(currentscalespeed-self.netSendSpeedArray[i])+2)
        #     cr.fill()
        #     cr.stroke()

        #     # cr.set_dash([5.0])
        #     cr.set_source_rgba(1,.313,.313,1) #for changing the outer line color
        #     cr.move_to(i*stepsize,scalingfactor*(currentscalespeed-self.netSendSpeedArray[i])+2)
        #     cr.line_to((i+1)*stepsize,scalingfactor*(currentscalespeed-self.netSendSpeedArray[i+1])+2)
        #     cr.stroke()

        #efficient receive speed drawing
        cr.set_source_rgba(.709,.164,.164,1) #for changing the outer line color
        cr.set_line_width(1.5)
        cr.move_to(0,scalingfactor*(currentscalespeed-self.netRecSpeedArray[0])+2)
        for i in range(0,99):
            cr.line_to((i+1)*stepsize,scalingfactor*(currentscalespeed-self.netRecSpeedArray[i+1])+2)
        cr.stroke_preserve()

        cr.set_source_rgba(.709,.164,.164,.2)  #for changing the fill color
        cr.line_to(w,h)
        cr.line_to(0,h)
        cr.move_to(0,scalingfactor*(currentscalespeed-self.netRecSpeedArray[0])+2)
        cr.fill()
        cr.stroke()

        #efficient drawing for send
        cr.set_source_rgba(1,.313,.313,1) #for changing the outer line color
        cr.move_to(0,scalingfactor*(currentscalespeed-self.netSendSpeedArray[0])+2)
        cr.set_line_width(1.5)
        for i in range(0,99):
            cr.line_to((i+1)*stepsize,scalingfactor*(currentscalespeed-self.netSendSpeedArray[i+1])+2)
        cr.stroke_preserve()

        cr.set_source_rgba(1,.313,.313,.2)  #for changing the fill color
        cr.line_to(w,h)
        cr.line_to(0,h)
        cr.move_to(0,scalingfactor*(currentscalespeed-self.netSendSpeedArray[0])+2)
        cr.fill()
        cr.stroke()

        return False

@GtkTemplate(ui=files_dir+'/gpuSidepane.glade')
class gpuSidepaneWidget(g.Box):

    # Required else you would need to specify the full module
    # name in mywidget.ui (__main__+MyWidget)
    __gtype_name__ = 'gpuSidepaneWidget'
    
    gpusidepanetextlabel= GtkTemplate.Child()
    gpusidepanelabelvalue = GtkTemplate.Child()
    gpusidepanedrawarea=GtkTemplate.Child()
    gpu_switcher_button=GtkTemplate.Child()



    # Alternative way to specify multiple widgets
    #label1, entry = GtkTemplate.Child.widgets(2)

    def __init__(self):
        super(g.Box, self).__init__()
        
        # This must occur *after* you initialize your base
        self.init_template()
    
    def givedata(self,secondself):
        self.gpuutilArray=secondself.gpuUtilArray
    
    @GtkTemplate.Callback
    def gpuSidepaneDrawArea_draw(self,dr,cr):
        cr.set_line_width(2)

        w=self.gpusidepanedrawarea.get_allocated_width()
        h=self.gpusidepanedrawarea.get_allocated_height()
        scalingfactor=h/100.0
        #creating outer rectangle
        cr.set_source_rgba(0,.454,.878,1)
        cr.set_line_width(3)
        cr.rectangle(0,0,w,h)
        cr.stroke()
        
        
        stepsize=w/99.0
        #print("in draw stepsize",stepsize)
        # for i in range(0,99):
        #     # not effcient way to fill the bars (drawing)
        #     cr.set_source_rgba(.588,.823,.98,0.25)   #for changing the fill color
        #     cr.move_to(i*stepsize,scalingfactor*(100-self.gpuutilArray[i])+2)
        #     cr.line_to((i+1)*stepsize,scalingfactor*(100-self.gpuutilArray[i+1])+2)
        #     cr.line_to((i+1)*stepsize,h)
        #     cr.line_to(i*stepsize,h)
        #     cr.move_to(i*stepsize,scalingfactor*(100-self.gpuutilArray[i])+2)

        #     cr.fill()
        #     cr.stroke()
        #     # for outer line
        #     cr.set_line_width(1.5)
        #     cr.set_source_rgba(.384,.749,1.0,1) #for changing the outer line color
        #     cr.move_to(i*stepsize,scalingfactor*(100-self.gpuutilArray[i])+2)
        #     cr.line_to((i+1)*stepsize,scalingfactor*(100-self.gpuutilArray[i+1])+2)
        #     cr.stroke()

        cr.set_line_width(1.5)
        cr.set_source_rgba(.384,.749,1.0,1) #for changing the outer line color
        cr.move_to(0,scalingfactor*(100-self.gpuutilArray[0]))
        for i in range(0,99):
            cr.line_to((i+1)*stepsize,scalingfactor*(100-self.gpuutilArray[i+1]))
        cr.stroke_preserve()

        cr.set_source_rgba(.588,.823,.98,0.25)   #for changing the fill color
        cr.line_to(w,h)
        cr.line_to(0,h)
        cr.move_to(0,scalingfactor*(100-self.gpuutilArray[0]))
        cr.fill()
        cr.stroke()


        return False

def on_switcher_clicked(button,stack,curr_stack):
    if not button.get_name()==stack.get_visible_child_name():
        stack.set_visible_child_name(button.get_name())
        curr_stack=button.get_name()

def sidepaneinit(self):
    print("initialisating sidepane")
    button_counter=0 # button name counter
    
    self.cpuSidePaneLabelValue=self.builder.get_object('cpusidepanelabelvalue')
    self.cpuSidePaneDrawArea=self.builder.get_object('cpusidepanedrawarea')
    cpu_switcher_button=self.builder.get_object("cpu_switcher_button")
    cpu_switcher_button.connect('clicked',on_switcher_clicked,self.performanceStack,self.current_stack)
    cpu_switcher_button.set_name(f'page{button_counter}')
    button_counter+=1

    self.memSidePaneLabelValue=self.builder.get_object('memsidepanelabelvalue')
    self.memSidePaneDrawArea=self.builder.get_object('memsidepanedrawarea')
    mem_switcher_button=self.builder.get_object("mem_switcher_button")
    mem_switcher_button.connect('clicked',on_switcher_clicked,self.performanceStack,self.current_stack)
    mem_switcher_button.set_name(f'page{button_counter}')
    button_counter+=1

    self.diskSidepaneWidgetList={}
    for i in range(0,self.numOfDisks):
        self.diskSidepaneWidgetList[i]=diskSidepaneWidget()
        self.sidepaneBox.pack_start(self.diskSidepaneWidgetList[i],True,True,0)
        self.diskSidepaneWidgetList[i].disksidepanetextlabel.set_text(self.disklist[i])   
        self.diskSidepaneWidgetList[i].givedata(self,i)

        self.diskSidepaneWidgetList[i].disk_switcher_button.connect('clicked',on_switcher_clicked,self.performanceStack,self.current_stack)
        self.diskSidepaneWidgetList[i].disk_switcher_button.set_name(f'page{button_counter}')
        button_counter+=1

    if len(self.netNameList)!=0:
        self.netSidepaneWidgetList={}
        for i in range(0,self.numOfNets):
            self.netSidepaneWidgetList[i]=netSidepaneWidget()
            self.sidepaneBox.pack_start(self.netSidepaneWidgetList[i],True,True,0)
            self.netSidepaneWidgetList[i].netsidepanetextlabel.set_text(self.netNameList[i])
            self.netSidepaneWidgetList[i].givedata(self,i)

            self.netSidepaneWidgetList[i].net_switcher_button.connect('clicked',on_switcher_clicked,self.performanceStack,self.current_stack)
            self.netSidepaneWidgetList[i].net_switcher_button.set_name(f'page{button_counter}')
            button_counter+=1
    
    if(self.isNvidiagpu==1):
        self.gpuSidePaneWidget=gpuSidepaneWidget()
        self.sidepaneBox.pack_start(self.gpuSidePaneWidget,True,True,0)
        self.gpuSidePaneWidget.gpusidepanetextlabel.set_text(f'{self.gpuName.split()[-2]}{self.gpuName.split()[-1]}')
        self.gpuSidePaneWidget.givedata(self)

        ## unknown signal bug fixed
        self.gpuSidePaneWidget.gpu_switcher_button.connect('clicked',on_switcher_clicked,self.performanceStack,self.current_stack)
        self.gpuSidePaneWidget.gpu_switcher_button.set_name(f'page{button_counter}')
        button_counter+=1
    


def sidePaneUpdate(self):
    self.memSidePaneLabelValue.set_text(f'{self.usedd}/{self.memTotal} GiB\n{self.memPercent} %')
    
    ##disk sidepane
    for i in range(0,self.numOfDisks):
        try:
            self.diskSidepaneWidgetList[i].disksidepanelabelvalue.set_text(self.diskActiveString[i])

            self.diskSidepaneWidgetList[i].givedata(self,i)
        except Exception as e:
            print(f"some error in disksidepane update {e}")

    # net sidepane
    if(len(self.netNameList)!=0):
        for i in range(0,self.numOfNets):
            try:
                self.netSidepaneWidgetList[i].netsidepanelabelvalue.set_text(f'R:{self.byterecpersecString[i]}\nS:{self.bytesendpersecString[i]}')

                self.diskSidepaneWidgetList[i].givedata(self,i)
            except Exception as e:
                print(f"some error in netsidepane update {e}")
    
    if(self.isNvidiagpu==1):
        try:
            self.gpuSidePaneWidget.gpusidepanelabelvalue.set_text(self.gpuutil)
            self.gpuSidePaneWidget.givedata(self)
        except Exception as e:
            print(f"some error in gpusidepane update {e}")