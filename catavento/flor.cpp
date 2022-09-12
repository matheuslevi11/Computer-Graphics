#include <iostream>
#include <GL/glut.h>

using namespace std;

struct color {
   GLfloat red;
   GLfloat green;
   GLfloat blue;
};

struct color WHITE, RED, BLUE, GREEN;
struct color colors[4];
int i = 0;

struct color get_next_color()
{
   struct color c = colors[i];
   i++;
   i = i % 4;
   return c;
}

void init (void){
  /* selecionar cor de fundo (preto) */
   glClearColor (0.0, 0.0, 0.0, 0.0);
   glLoadIdentity();
   glMatrixMode (GL_PROJECTION); //Projecao 2D
   glOrtho(0.0, 500.0, 0.0, 400.0, -1.0, 1.0); //Definindo os limites da Porta de Visao (ViewPort)

   // Definindo as cores
   WHITE.red = 1.0f, WHITE.green = 1.0f, WHITE.blue = 1.0f;
   RED.red = 1.0f; RED.green = 0.0f; RED.blue = 0.0f;
   BLUE.red = 0.0f; BLUE.green = 0.0f; BLUE.blue = 1.0f;
   GREEN.red = 0.0f; GREEN.green = 1.0f; GREEN.blue = 0.0f;

   colors[0] = WHITE;
   colors[1] = RED;
   colors[2] = BLUE;
   colors[3] = GREEN;
}

void displayFcn(void){
   /* Limpar todos os pixels  */
   glClear (GL_COLOR_BUFFER_BIT);
   glColor3f (1.0, 1.0, .0);
   glBegin(GL_POLYGON);
      glVertex3f (249.0f, 250.0f, -1.0f);
      glVertex3f (251.0f, 250.0f, -1.0f);
      glVertex3f (249.0f, 100.0f, -1.0f);
      glVertex3f (251.0f, 100.0f, -1.0f);
   glEnd();

   struct color COLOR = get_next_color();
   glColor3f (COLOR.red, COLOR.green, COLOR.blue);
   glBegin(GL_TRIANGLES);
      glVertex2f (250.0f, 250.0f);
      glVertex2f (230.0f, 200.0f);
      glVertex2f (270.0f, 200.0f);
   glEnd();

   COLOR = get_next_color();
   glColor3f (COLOR.red, COLOR.green, COLOR.blue);
   glBegin(GL_TRIANGLES);
      glVertex2f (250.0f, 250.0f);
      glVertex2f (300.0f, 230.0f);
      glVertex2f (300.0f, 270.0f);
   glEnd();

   COLOR = get_next_color();
   glColor3f (COLOR.red, COLOR.green, COLOR.blue);
   glBegin(GL_TRIANGLES);
      glVertex2f (250.0f, 250.0f);
      glVertex2f (230.0f, 300.0f);
      glVertex2f (270.0f, 300.0f);
   glEnd();

   COLOR = get_next_color();
   glColor3f (COLOR.red, COLOR.green, COLOR.blue);
   glBegin(GL_TRIANGLES);
      glVertex2f (250.0f, 250.0f);
      glVertex2f (200.0f, 270.0f);
      glVertex2f (200.0f, 230.0f);
   glEnd();

   COLOR = get_next_color(); // Color step 

   glFlush ();
}

void changeColors(unsigned char key, int x, int y)
{
   if (key == 'y')
   {
      displayFcn();
   }
}

int main(int argc, char** argv) {

	glutInit(&argc, argv);

	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize (500, 400);
	glutInitWindowPosition (200, 200);
	glutCreateWindow ("Flor de Abril");

	init();

	glutDisplayFunc(displayFcn);
   glutKeyboardFunc(changeColors);
	glutMainLoop();

	
	return 0;

}

