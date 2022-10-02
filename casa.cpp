#include <stdio.h>
#include <GL/glut.h>
#include <stdlib.h>

void init(void);
void display(void);
void keyboard(unsigned char key, int x, int y);
void reshape (int w, int h);

#define BRANCO   1.0, 1.0, 1.0
#define PRETO    0.7, 0.7, 0.7
#define VERDE    0.01, 0.83, 0.99
#define LARANJA  0.99, 0.43, 0.01
#define VERMELHO  0.52, 0.01, 0.01

static GLfloat vertices[30]={
  0.0,  30.0, 40.0, /* A 0*/
  15.0, 50.0, 40.0, /* B 1*/
  30.0, 30.0, 40.0, /* C 2*/
  30.0,  0.0, 40.0, /* D 3*/
  0.0,   0.0, 40.0, /* E 4*/
  0.0,  30.0, 0.0, /* F  5*/
  15.0, 50.0, 0.0, /* G  6*/
  30.0, 30.0, 0.0, /* H  7*/
  30.0,  0.0, 0.0, /* I  8*/
  0.0,   0.0, 0.0, /* J  9*/
}; 

static GLubyte frenteIndices[]    = {0,1,2,3,4};
static GLubyte trasIndices[]      = {5,6,7,8,9};
static GLubyte esquerdaIndices[]  = {0,4,9,5};
static GLubyte direitaIndices[]   = {3,2,7,8};
static GLubyte fundoIndices[]     = {3,4,9,8};
static GLubyte topo1Indices[]     = {2,1,6,7};
static GLubyte topo2Indices[]     = {0,5,6,1};
    
static int eixoy, eixox;
int largura, altura;

int main(int argc, char** argv){
    glutInit(&argc, argv);
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize (256, 256); 
    glutInitWindowPosition (100, 100); 
    glutCreateWindow (argv[0]);
    init();
    glutDisplayFunc(display); 
    glutKeyboardFunc(keyboard);
    glutReshapeFunc(reshape);
    glutMainLoop();
    return 0;
}

void init(void){
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glOrtho (-70, 70, -70, 70, -70 , 70);
    glEnable(GL_DEPTH_TEST);
    //glEnable(GL_CULL_FACE); 
}

void reshape (int w, int h){
  glViewport (0, 0, (GLsizei) w, (GLsizei) h);
  largura=w; 
  altura=h;
}

void display(void){
  glPushMatrix();
  glRotatef ((GLfloat) eixoy, 0.0, 1.0, 0.0);
  glRotatef ((GLfloat) eixox, 1.0, 0.0, 0.0);
  glTranslatef(0.0, -20.0, 0.0);
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );
  
  glEnableClientState(GL_VERTEX_ARRAY);
  glVertexPointer(3, GL_FLOAT, 0, vertices);

  glColor3f (BRANCO); /* frente */
  glDrawElements(GL_POLYGON, 5, GL_UNSIGNED_BYTE, frenteIndices);

  glColor3f (VERDE); /* esquerda */
  glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, esquerdaIndices);

  glColor3f (VERDE); /* direita */
  glDrawElements(GL_POLYGON, 4, GL_UNSIGNED_BYTE, direitaIndices);

  glColor3f (VERMELHO); /* tras */
  glDrawElements(GL_POLYGON, 5, GL_UNSIGNED_BYTE, trasIndices);

  glColor3f (PRETO); /* fundo */
  glDrawElements(GL_QUADS, 4, GL_UNSIGNED_BYTE, fundoIndices);

  glColor3f (LARANJA); /* topo 1 */
  glDrawElements(GL_QUADS, 4, GL_UNSIGNED_BYTE, topo1Indices);

  glColor3f (LARANJA); /* topo 2 */
  glDrawElements(GL_QUADS, 4, GL_UNSIGNED_BYTE, topo2Indices);

  glDisableClientState (GL_VERTEX_ARRAY);

  glPopMatrix();
  glutSwapBuffers();
}

void keyboard(unsigned char key, int x, int y){
  switch (key) {
  case 27:
    exit(0);
    break;
  case 'a':
    printf("%d, %d\n",x,y);
    break;
  case 'y':
    eixoy = (eixoy + 5) % 360;
    glutPostRedisplay();
    break;
  case 'Y':
    eixoy = (eixoy - 5) % 360;
    glutPostRedisplay();
    break;
  case 'x':
    eixox = (eixox + 5) % 360;
    glutPostRedisplay();
    break;
  case 'X':
    eixox = (eixox - 5) % 360;
    glutPostRedisplay();
    break;
  case 'p':
    glLoadIdentity();
    gluPerspective(65.0, (GLfloat) largura/(GLfloat) altura, 20.0, 120.0);
    gluLookAt(0, 0, -90, 0, 0, 0, 0, 1, 0);
    glutPostRedisplay();
    break;
  case 'o':
    glLoadIdentity();
    glOrtho (-50, 50, -50, 50, -50 , 50);
    glutPostRedisplay();
    break;
  }
}