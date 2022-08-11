def whos_first(p1, p2):
    shot = p1.find('B') - p2.find('B')
    if shot < 0:
        return ('p1')
    elif shot > 0:
        return ('p2')
    else:
        return ('tie')

print(whos_first('   Bang!', ' Bang!'))
print(whos_first('   Bang!', '        Bang!'))
print(whos_first('   Bang!', '   Bang!'))