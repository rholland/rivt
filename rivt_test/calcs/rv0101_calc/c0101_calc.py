import rivtapi as rv

rv.R("""new section | calc title | inter | 1
    
    new R text
    
    """)

rv.I("""new I section | default
    
    new I text
    
    """)

rv.V("""new V section | default | nosub
    
    new Value text
    
    || image |  filename |  scale


    """)

rv.T("""new T section | default 
    
    new Table text
    
    || attach | test.pdf | nonumber     
    """)