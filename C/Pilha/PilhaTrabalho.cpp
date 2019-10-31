//Programador: Marcos Vinicius Souza Pinheiro	----	RA: 580678
//Programa Funcional

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <locale.h>
#include <string.h>
#define tam 10

typedef struct
{
	int topo;
	int el[tam];
}Pilha;

//Criar Pilha
void CriaPilha(Pilha *p)
{
	p->topo = -1;
}

//Validar se esta cheia
int Cheia(Pilha *p)
{
	return p->topo == tam-1;
}

//Validar se esta Vazia
int Vazia(Pilha *p)
{
	return p->topo == -1;
}

//Adicionar Elementos
int Push(Pilha *p, int val)
{
	if(Cheia(p))
		return 0;

	p->el[++p->topo] = val;
	return 1;
}

//Remover Elementos
 Pop(Pilha *p, int *val)
{
	if(Vazia(p))
		return 0;

	*val = p->el[p->topo--];
	return 1;
}

//Printar Pilha
void Imprime(Pilha p)
{
	int i;

	printf("--AA--\n");
	for(i = p.topo ; i>=0 ; i--)
	{
		printf("[ %d ]\n", p.el[i]);
	}
	printf("--WW--");
	
	printf("\n\nPosi��o do Topo: %d", p.topo);
}

//Validando	----	----	----	-----	----	----	----	----	----	-----	----	------	-----	-----	-----	-------
char Validar(Pilha *vl, Pilha p)	//vl == Valida��o, p == Principal
{
	int cont=1, x;
	char res[30] = "";
	
	CriaPilha(vl);
	Push(vl, cont);
	strcat(res, "I");
	do
	{
		if( vl->el[vl->topo] == p.el[p.topo] )
		{
			Pop(&p, &x);
			Pop(vl, &x);
			strcat(res, "R");
		}
		else
		{
			if(vl->el[vl->topo] < p.el[p.topo])
			{
				cont++;
				Push(vl, cont);
				strcat(res, "I");
			}
			else
			{
				strcpy(res," Sequ�ncia inv�lida!");
				break;
			}
		}
	}while( !Vazia(&p));
	
	printf("\nSequ�ncia de Opera��es: %s", res);
	getche();
}

//Trabalho de Pilha
int main()
{
	setlocale(LC_ALL, "Portuguese");
	Pilha p, vl;	//p == Principal, vl == pilha de VaLida��o
	int op, val;	//op == Opera��o Switch, val == Valor a ser adicionado em 'p'
	char resultado[10];		//resutado == pop's e push's acionados

	CriaPilha(&p);	//Criando Pilha Vazia.

	do
	{
		system("cls");
		puts("1. Inserir Sequ�ncia");
		puts("2. Validar Sequ�ncia");
		puts("3. Printar Sequ�ncia");
		puts("0. Sair\n");

		printf("Sele��o: ");
		scanf("%d", &op);

		switch(op)
		{
					case 1:	//Modelando a pilha p
							system("cls");
							puts("Inserindo Sequ�ncia de N�meros na Pilha");
							printf("Sequ�ncia: ");
							fflush(stdin);
							scanf("%d", &val);
							CriaPilha(&p);
							while(val > 0)
							{
								Push(&p, (val%10));
								val /= 10;
							}
							printf("Sequ�ncia Incluida com Sucesso!");
							getche();
							break;
					
					case 2:	//Validando a pilha p
							puts("\nValidando sequ�ncia obtida...");
							Validar(&vl, p);
							break;
					
					case 3:	//Printando Sequ�ncia da pilha p
							if(Vazia(&p))
							{
								printf("\nPilha Vazia!!");
							}
							else
							{
								printf("\nPilha\n\n");
								Imprime(p);
							}
							getche();
							break;
		}
	}while(op != 0);
}
