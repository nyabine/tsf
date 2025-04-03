i = 0
template = """
meta {{
  name: Test {}
  type: http
  seq: 2
}}

get {{
  url: http://158.160.56.133/api/pet/?page=1&page_size=20&species__name={}&breed__code={}&gender__code={}&age={}
  body: none
  auth: none
}}

params:query {{
  page: 1
  page_size: 20
  species__name: {}
  breed__code: {}
  gender__code: {}
  age: {}
}}
"""

while True:
    for l in input(f"{i}: ").split("\n"):
        ps = l.split("\t")
        if len(ps) == 1:
            break
        ps = [i, *ps, *ps]
        o = template.format(*ps)
        with open(f" Test {i}.bru", "w") as f:
            f.write(o)
        i += 1
