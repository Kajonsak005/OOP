
class Author:
    run_number = 1
    authors = []

    def __init__(self,name):
        self.id = Author.run_number
        self.name = name
        Author.run_number += 1 
        Author.authors.append(self)
        
    #Author refers to the class, whereas self refers to the instance.
    def find_id_by_name(name):
        author_list = [inst for inst in Author.authors if inst.name == name]
        author_list_len = len(author_list)
        if author_list_len > 1:
            print("have problem find id by name in find author_list duplicate name")
            raise Exception("have problem find id by name in find author_list duplicate name")
        elif author_list_len == 0:
            author = Author(name)
            return author.id
        return author_list[0].id

    def find_id_by_list(name_lists):
        author_id = []
        for name_list in name_lists:
            author_list = [inst for inst in Author.authors if inst.name == name_list]
            author_list_len = len(author_list)
            if author_list_len > 1:
                print("have problem find id by name in find author_list duplicate name")
                raise Exception("have problem find id by name in find author_list duplicate name")
            elif author_list_len == 0:
                author = Author(name_list)
                author_id.append(author.id)
            else:
                author_id.append(author_list[0].id)
        return author_id
    
    # function will retrun Author instance
    def get_author_by_id(id):
        author_list = [inst for inst in Author.authors if inst.id == id]
        author_list_len = len(author_list)
        if author_list_len > 1:
            print("have problem get author in author_list duplicate id")
            exit()
        elif author_list_len == 0:
            print("Not found author id:",id)
        return author_list[0]
    
    def delete_author(self,id):
        Author.authors.pop(id)
        print("delete author success")


        


    