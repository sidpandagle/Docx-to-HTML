import mammoth
print('Docx to HTML')
f = open("example.docx", 'rb')
b = open('filename.html', 'wb')
document = mammoth.convert_to_html(f)
b.write(document.value.encode('utf8'))
f.close()
b.close()