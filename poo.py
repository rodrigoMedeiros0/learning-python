#orientacao a objetos: Paradigma de Programacao
#classes e objetos 

class Veiculo: 
    def movimentar(self):
        print(f'Estou em movimento...')
    
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    #Seter - permite gravar um dado dentro do objeto
    def set_num_registro(self, registro):
        self.__num_registro = registro

  #Getter - da direito a acessar os atributos dentro da classe
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}. \n')
    
    def get_num_registro(self):
        print(f'Numero do registro: {self.__num_registro}')

class Carro(Veiculo):
    #Metodo init sera herdado
    def movimentar(self):
        print('Sou um carro e ando pelas ruas..')

class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'Corro muito...')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante,modelo)

    def get_categoria(self):
        print(f'Categoria: {self.__cat}')

    def movimentar(self):
        print('Eu voo alto!')

if __name__ == '__main__':
    # meu_veiculo = Veiculo('GM', 'Cadillac')
    # meu_veiculo.movimentar()
    # meu_veiculo.get_fabr_modelo()
    # meu_veiculo.set_num_registro('123abc')
    # meu_veiculo.get_num_registro()

    meu_carro = Carro('Volkswagen', 'Golf')
    # meu_carro.movimentar()
    # meu_carro.get_fabr_modelo()
    # meu_carro.set_num_registro('pac123')
    # meu_carro.get_num_registro()

    # carro_maria = Carro('Audi', 'TT')
    # carro_maria.movimentar()
    # carro_maria.get_fabr_modelo()
    # carro_maria.set_num_registro('xlp-852')
    # carro_maria.get_num_registro()

    # moto = Motocicleta('Harley Davidson', 'Nighstar Special')
    # moto.movimentar()
    # moto.get_fabr_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    meu_aviao.get_categoria()