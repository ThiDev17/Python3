class Alunos:
    cargo = 'Aluno'
    def __int__(self, nome, idade, matri):
        self.matri=matri
    @classmethod # ou staticmethod
    def matricula(cls):
        cls.cargo = 'Profesor'
        print(cls.cargo)

    @staticmethod
    def e_teen(idade):
        if idade > 13:
            print('Adolescente')
        else:
            print('Criança')


Alunos.matricula()
Alunos.e_teen(19)
