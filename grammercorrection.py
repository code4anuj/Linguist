from gingerit.gingerit import GingerIt

text = 'The smelt of fliwers bring back memories.'

parser = GingerIt()
ct = parser.parse(text)
print(ct)
