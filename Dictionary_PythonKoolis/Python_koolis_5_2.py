import Python_koolis_5_1 as dictionary

if 'üks' not in dictionary.italian:
    dictionary.italian['üks'] = "uno"
if 'kolm' not in dictionary.english:
    dictionary.english['kolm'] = "three"

if __name__ == '__main__':
    print(f"tere -> inglise k = '{dictionary.english['tere']}', itaalia k = '{dictionary.italian['tere']}'")
    print(f"üks -> itaalia k = '{dictionary.italian['üks']}'")
    print(f"kolm -> inglise k = '{dictionary.english['kolm']}'")