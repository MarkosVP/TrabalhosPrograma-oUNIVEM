//Programador: Marcos Vinicius Souza Pinheiro	----	RA: 580678
//Programa Funcional

#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <locale.h>
#include <windows.h>

//Criando Nó	--	Funcional
struct no
{
	struct no *esq;
	char tipo;
	int codigo;
	struct no *dir;
};

typedef struct no Lista;

//Criando Lista	--	Funcional
void cria_LDE(Lista **Inicio, Lista **Fim)
{
	*Inicio = NULL;
	*Fim = NULL;
}

//Inserir no Inicio	--	Funcional
void Ins_Inicio (Lista **Inicio, Lista **Fim,char tp , int cod)
{
	Lista * p = (Lista *)calloc (1, sizeof(Lista));
	p->codigo = cod;
	p->tipo = tp;
	p->esq = NULL;
	p->dir = *Inicio;
	if (*Inicio==NULL)
	   *Fim =p;
	else
	   (*Inicio)->esq=p;
	 *Inicio = p;
}

//Inserindo no Fim	--	Funcional
void Ins_Fim(Lista **Inicio, Lista **Fim, int cod, char tp)
{
	Lista * p = (Lista *)calloc (1, sizeof(Lista)) ;
	p->codigo = cod;
	p->tipo = tp;
	p->esq = *Fim;
	p->dir = NULL;
	if (*Inicio==NULL)
	   *Inicio =p;
	else
	   (*Fim)->dir=p;
	 *Fim = p;
}

//Inserindo depois de um elemento	--	Funcional
void Ins_Depois(Lista *r, char tp, int cod)
{
	Lista *p = (Lista*)calloc(1,sizeof(Lista));
	p->tipo = tp;
	p->codigo = cod;
	
	p->esq = r;
	p->dir = r->dir;
	
	r->dir->esq = p;
	r->dir = p;
}

//Imprimir Lista	--	Funcional
void Imprime(Lista *Inicio)
{
	Lista *p;
	p = Inicio;
	
	if(Inicio == NULL)
	{
		printf("Lista Vazia!");
		getche();
	}
	else
	{
		while(p!=NULL)
		{
			printf("%c-%d  -  ", (p->tipo), (p->codigo));
			p = p->dir;
		}
		printf("Fim");
		getche();
	}
}

//Busca de elementos	--	Funcional
Lista * Consulta(Lista *Inicio, char tp)
{
	Lista *p = Inicio;
	
	while(p != NULL)
	{
		if(tp == 'G' && p->dir->tipo == 'C')
		{
			return p;
		}
		else
			if(tp == 'I' && (p->dir->tipo == 'C' || p->dir->tipo == 'G') )
			{
				return p;
			}
			else
				if(tp == 'D' && p->dir->tipo != 'D')
				{
					return p;
				}
		p = p->dir;
		if( p->dir == NULL )
			return p;
	}
}

//Remover no Início	--	Funcional
int Rem_Inicio (Lista **Inicio, Lista **Fim)
{
	Lista *p;
	if (*Inicio!=NULL)
	{
		p=*Inicio;
		*Inicio= p->dir;
		if (p->dir==NULL)  // só existe 1 nó na lista
		   *Fim=NULL;
		else
		   (*Inicio)->esq=NULL;
		free(p);
		return 1;
	}
	else return 0;
}

//Main do programa	--	Funcional
int main()
{
	setlocale(LC_ALL, "Portuguese");	//Pt-Br
	Lista *Inicio, *Fim;
	int op, op2;
	int C=1000, I=2000, D=3000, G=4000;
	char tipoIndividuo;
	
	//Inicializando Fila
	cria_LDE(&Inicio, &Fim);
	
	do
	{
		system("cls");
		printf("\tAula 11 - Fila baseada em Listas Duplamente Encadeadas\n");
		puts("1. Entrar na Fila");
		puts("2. Avançar Fila");
		puts("3. Imprimir Fila");
		puts("0. Sair");
		
		printf("\nDigite a opção: ");
		scanf("%d", &op);
		
		switch(op)
		{
					case 1:	//Entrando na Fila	--	Funcional
							do
							{
								system("cls");
								printf("Insira sua respectiva categoria: ");
								puts("\n1. Comum");
								puts("2. Gestante");
								puts("3. Idoso");
								puts("4. Deficiente");
								puts("0. Voltar");
								
								printf("\nSeleção: ");
								fflush(stdin);
								scanf("%d", &op2);
								
								//Inserindo uma Pessoa:
								switch(op2)
								{
											case 1:	//Comum
													Ins_Fim(&Inicio, &Fim, C, tipoIndividuo='C');
													C++;
													printf("Inserção bem Sucedida!");
													getche();
													break;
											
											case 2:	//Gestante
													if(Inicio == NULL || Inicio->tipo == 'C')
													{
														Ins_Inicio(&Inicio, &Fim, tipoIndividuo='G', G);
													}
													else
														if(Fim->tipo == 'G' || Fim->tipo == 'I')
															Ins_Fim(&Inicio, &Fim, G, tipoIndividuo='G');
														else
															Ins_Depois( Consulta(Inicio, tipoIndividuo='G'), tipoIndividuo='G', G );
													G++;
													printf("Inserção bem Sucedida!");
													getche();
													break;
											
											case 3:	//Idoso
													if(Inicio == NULL || Inicio->tipo == 'C' || Inicio->tipo == 'G')
													{
														Ins_Inicio(&Inicio, &Fim, tipoIndividuo='I', I);
													}
													else
														if(Fim->tipo == 'I')
															Ins_Fim(&Inicio, &Fim, I, tipoIndividuo='I');
														else
															Ins_Depois( Consulta(Inicio, tipoIndividuo='I'), tipoIndividuo='I', I );
													I++;
													printf("Inserção bem Sucedida!");
													getche();
													break;
											
											case 4:	//Deficiente
													if(Inicio == NULL || Inicio->tipo != 'D')
													{
														Ins_Inicio(&Inicio, &Fim, tipoIndividuo='D', D);
													}
													else
														if(Fim->tipo == 'D')
															Ins_Fim(&Inicio, &Fim, D, tipoIndividuo='D');
														else
															Ins_Depois( Consulta(Inicio, tipoIndividuo='D'), tipoIndividuo='D', D );
													D++;
													printf("Inserção bem Sucedida!");
													getche();
													break;
								}
							}while(op2 != 0);
							break;
							
					case 2:
							//Avançando Fila	--	Funcional
							if(Inicio != NULL)
							{
								Rem_Inicio(&Inicio, &Fim);
								Imprime(Inicio);
							}
							else
							{
								printf("Lista Vazia!");
								getche();
							}
							break;
					
					case 3:	//Imprimindo Fila	--	Funcional
							Imprime(Inicio);
							break;
		}
	}while(op!=0);
}
