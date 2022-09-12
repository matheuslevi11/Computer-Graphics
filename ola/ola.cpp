#include <iostream>
#include <GL/glut.h>

using namespace std;
// Variáveis do retângulo
GLint RECT_SIZE = 20;
GLfloat RECT_BASE = 50.0f;
// Variáveis da Ola
int pivot = 0;
GLint heights[9];

void calculate_heights(int pivot, GLint heights[])
{
    int h = 400;
    heights[pivot] = 400;
    int i = pivot;
    i++;
    while (i < 9)
    {
        h -= 25;
        heights[i] = h;
        i++;
    }
    
    i = pivot - 1;
    h = 400;
    
    while(i >= 0)
    {
        h -= 25;
        heights[i] = h;
        i--;
    }
}

void init (void){
  /* selecionar cor de fundo (preto) */
    glClearColor (0.0, 0.0, 0.0, 0.0);
    glLoadIdentity();
   glMatrixMode (GL_PROJECTION); //Projecao 2D
   glOrtho(0.0, 500.0, 0.0, 400.0, -1.0, 1.0); //Definindo os limites da Porta de Visao (ViewPort)
   // Altura inicial dos retângulos
    calculate_heights(0, heights);
}

void draw_rect(GLint height)
{
    glBegin(GL_LINE_LOOP);
        glVertex3f(RECT_BASE, 50.0f, -1.0f);
        glVertex3f(RECT_BASE+RECT_SIZE, 50.0f, -1.0f);
        glVertex3f(RECT_BASE+RECT_SIZE, height, -1.0f);
        glVertex3f(RECT_BASE, height, -1.0f);
    glEnd();

    RECT_BASE += 50;
    if (RECT_BASE >= 500)
    {
        RECT_BASE = 50.0f;
    }
}

void displayFcn(void){
   /* Limpar todos os pixels  */
    glClear (GL_COLOR_BUFFER_BIT);
    glColor3f (1.0, 0.4, 0.8);
    GLuint lista = glGenLists(1);
    
    glNewList(lista, GL_COMPILE);
        
        for (int i = 0; i < 9; i++)
        {
            draw_rect(heights[i]);
        }

    glEndList();


    glCallList(lista);
    glFlush ();
}

void changeColors(unsigned char key, int x, int y)
{
    if (key == 'd')
    {
        pivot++;
        pivot = pivot % 9;
        calculate_heights(pivot, heights);
    }
    if (key == 'a')
    {
        pivot--;
        pivot = pivot % 9;
        calculate_heights(pivot, heights);
    }
    displayFcn();
}

int main(int argc, char** argv) {

	glutInit(&argc, argv);

	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize (500, 400);
	glutInitWindowPosition (200, 200);
	glutCreateWindow ("OoooOoooOolaaAaaAa");

	init();

	glutDisplayFunc(displayFcn);
    glutKeyboardFunc(changeColors);
	glutMainLoop();

	
	return 0;

}

