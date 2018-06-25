#problema: http://dojopuzzles.com/problemas/exibe/encontrando-arquivos-duplicados/
import os
from glob import glob

class ArquivosDuplicado:
    '''recebe uma string no construtor informando o path do backup.
        verifica se ha duplicatas pelo conteudo do arquivo.

        metodos:
        obj.duplicados -> retorna uma lista com todos os arquivos duplicados
        obj.remover_duplicados -> remove todos os arquivos duplicados
        (sempre mantendo apenas 1 item original)
    '''
    def __init__(self, path):
        self.path = path
        self.repetidos = []
        path = self.path
        self.arquivos = glob(path + '\*.*')       

        #carrega todos os arquivos duplicados informado no path
        repetidos = self.repetidos
        arquivos = self.arquivos
        for n_atual, arq_atual in enumerate(arquivos):
            with open(arq_atual, 'r') as f:
                content_atual = f.readlines()
            for n in range(n_atual+1, len(arquivos)):
                with open(arquivos[n], 'r') as f:
                    content = f.readlines()
                if content_atual == content:
                    if arquivos[n] not in repetidos:
                        repetidos.append(arquivos[n])
        
    
    def _get_filename(self, path):
        return path.split('\\')[-1]

    def remover_duplicados(self):
        for arq in self.repetidos:
            os.remove(arq)
    
    @property
    def duplicados(self)->list:
        resp = []
        for path in self.repetidos:
            resp.append(self._get_filename(path))
        return resp

if __name__ == '__main__':
    a=ArquivosDuplicado(os.getcwd() + r'\backup')
    print(a.duplicados)
    a.remover_duplicados()
