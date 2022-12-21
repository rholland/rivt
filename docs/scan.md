# Module scan

None

None

??? example "View Source"
        #!

        

        import os

        import datetime

        

        __version__ = "0.9.0"

        __author__ = 'rholland'

        

        

        class Checkrivt:

            """check rivt syntax and log

            

            Arguments:

                logname {[type]} -- [description]

            

            Returns:

                [type] -- [description]

            """

        

            def __init__(self, logname):

                

                self.logname = logname

        

            def logstart(self):

                """delete log file and initialize new file

        

                """

                try: os.remove(self.logname)

                except: pass

                with open(self.logname, 'w') as lg:

                    lg.write("< start log: " + str(datetime.datetime.now()) + "  >\n")

                return self.logname

        

            def logwrite(self, logstrg, flg=0):

                """write processes to log file, option echo to terminal

        

                """

                #print('log', logstrg)

                with open(self.logname, 'a') as lg:

                    logstrg += '\n'

                    lg.write(logstrg)

                if flg:

                    print(logstrg)

        

            def logclose(self):

                """close log file

        

                """

                try:

                    with open(self.logname, 'a') as lg:

                        lg.write("\n< close log: "  + str(datetime.datetime.now()) + " >")

                except IOError:

                    print('error: problem closing log file')

        

        

            def filesummary():

                """file name summary table

        

                """

                filesum1 = ("Path Summary\n"

                            "============================"

                            "\nproject path :\n    {}\n"    

                            "\ndesign file :\n    {}\n"

                            "\nlog file :\n    {}"

                            "\ncalc path :\n    {}").format(cfg.ppath.strip(), 

                                                    cfg.dfile, cfg.tlog, cfg.cpath) 

        

        

        class CheckDesign:

            """[summary]

            """

            

            

            def varsummary():

                """variable summary table

                

                """

                

                print("Variable Summary")

                print("================")

                print(cfg.varevaled)

        

        

            pass

## Classes

### CheckDesign

```python3
class CheckDesign(
    /,
    *args,
    **kwargs
)
```

#### Methods

    
#### varsummary

```python3
def varsummary(
    
)
```

    
variable summary table

??? example "View Source"
            def varsummary():

                """variable summary table

                

                """

                

                print("Variable Summary")

                print("================")

                print(cfg.varevaled)

### Checkrivt

```python3
class Checkrivt(
    logname
)
```

check rivt syntax and log

Arguments:
    logname {[type]} -- [description]

Returns:
    [type] -- [description]

#### Methods

    
#### filesummary

```python3
def filesummary(
    
)
```

    
file name summary table

??? example "View Source"
            def filesummary():

                """file name summary table

        

                """

                filesum1 = ("Path Summary\n"

                            "============================"

                            "\nproject path :\n    {}\n"    

                            "\ndesign file :\n    {}\n"

                            "\nlog file :\n    {}"

                            "\ncalc path :\n    {}").format(cfg.ppath.strip(), 

                                                    cfg.dfile, cfg.tlog, cfg.cpath) 

    
#### logclose

```python3
def logclose(
    self
)
```

    
close log file

??? example "View Source"
            def logclose(self):

                """close log file

        

                """

                try:

                    with open(self.logname, 'a') as lg:

                        lg.write("\n< close log: "  + str(datetime.datetime.now()) + " >")

                except IOError:

                    print('error: problem closing log file')

    
#### logstart

```python3
def logstart(
    self
)
```

    
delete log file and initialize new file

??? example "View Source"
            def logstart(self):

                """delete log file and initialize new file

        

                """

                try: os.remove(self.logname)

                except: pass

                with open(self.logname, 'w') as lg:

                    lg.write("< start log: " + str(datetime.datetime.now()) + "  >\n")

                return self.logname

    
#### logwrite

```python3
def logwrite(
    self,
    logstrg,
    flg=0
)
```

    
write processes to log file, option echo to terminal

??? example "View Source"
            def logwrite(self, logstrg, flg=0):

                """write processes to log file, option echo to terminal

        

                """

                #print('log', logstrg)

                with open(self.logname, 'a') as lg:

                    logstrg += '\n'

                    lg.write(logstrg)

                if flg:

                    print(logstrg)