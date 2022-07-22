from decimal import Decimal
import json
class Product():
    FILE = '/home/leon/Desktop/mlp/db.json'
    id = 0
    
    def __init__(self, model, mark, price, year, color, kuzov,obem,run):
        self.model= model
        self.mark = mark
        self.price = price
        self.qty = year
        self.color = color
        self.kuzov = kuzov
        self.obem = obem
        self.run = run

        self.send_product_to_json()

    @classmethod
    def get_id(cls):
        cls.id +=1
        return cls.id
    
    @classmethod
    def get_data(cls):
        with open(cls.FILE) as file:
            return json.load(file)
    @staticmethod
    def get_one_product(data,id):
        product= list(filter(lambda x: x['id']== id, data))
        if not product:
            return "нет такого продукта"
        return product[0]
    @classmethod
    def send_data_to_json(cls, data):
        with open(cls.FILE,'w') as file:
            json.dump(data, file)

    def send_product_to_json(self):
        data = Product.get_data()
        product = {            
            'id': Product.get_id(),
            'model':self.model,
            'mark': self.mark,
            "price": Decimal(self.price).quantize(Decimal('.2')),
            'year': self.qty,
            'color':self.color,
            'kuzov type': self.kuzov,
            'obem': Decimal(self.obem).quantize(Decimal('.2')),
            'probeg': self.run
            }

        
        
        data.append(product)
        with open(Product.FILE, 'w') as file:
            json.dump(data,file)
        
        return {'status':'201','msg':product}
    
    @classmethod
    def retrieve_data(cls, id):
        data = cls.get_data()
        product = cls.get_one_product(data,id)
        return product
    @classmethod
    def update_data(cls, id, **kwargs):
        data = cls.get_data()
        product = cls.get_one_product(data,id)
        if type(product) != dict:
            return product 
        index = data.index(product)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return{'status':'200','msg':'Updated'}
    @classmethod
    def delete_data(cls,id):
        data = cls.get_data()
        
        product = cls.get_one_product(data, id)
        if type(product) != dict:
            return product 
        
        index = data.index(product)
        data.pop(index)
        cls.send_data_to_json(data)
        return{'status': '204', "msg": "deleted"}

with open(Product.FILE, 'w') as file:
    json.dump([], file)




