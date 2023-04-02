countries = ["Ukraine","Japan","Poland"]
capitals = {
          countries[0]:"Kyiv",
          countries[1]:"Tokio",
          countries[2]:"Warsaw"
          }
print(countries[0]+": "+capitals[countries[0]],
      countries[1]+": "+capitals[countries[1]],
      countries[2]+": "+capitals[countries[2]],
      sep='\n')
#or
"""
print(str(capitals).replace('{','')
                   .replace('\'','')
                   .replace('}','')
                   .replace(', ','\n'))
"""