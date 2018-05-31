jvm_langs=['java','jython','scala','jruby']
print('I know of',jvm_langs.__len__(),'langs that can rum on JVM')
print('I know of',len(jvm_langs),'langs that can rum on JVM')

print("oops I forgot Clojure")
jvm_langs.append("Clojure")

for lang in jvm_langs:
	print(lang)

print("The 3rd JVM language is:",jvm_langs[2])
print("The first 3 languages are:",jvm_langs[:3])
print("The languages from 2nd to 4th are:",jvm_langs[1:5])
print("Let's sort the languages")
jvm_langs.sort()
print(jvm_langs)
 
