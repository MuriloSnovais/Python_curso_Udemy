class Caneta:
    def __init__(self,cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print("PROPERTY")
        return self.cor_tinta  
    
    @property
    def cor_tampa(self):
        return 1241241
    
#############################   
 
caneta = Caneta("Azul")
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)


# print(caneta.get_cor())
# class Caneta:
#     def __init__(self,cor):
#         self.cor = cor
    
#     def get_cor(self):
#         print("GET COR")
#         return self.cor
    
    
#     @property
#     def cor(self):
#         print("PROPERTY")
#         return self.cor_tinta

# caneta = Caneta("Azul")
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())