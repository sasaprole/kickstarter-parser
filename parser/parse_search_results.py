for i in range(1,50):
    file_name = 'page_'+str(i)+'.html'
    print(file_name)
    file_to_read = open(file_name,'r',encoding='utf-8')
    print(file_to_read.read())
