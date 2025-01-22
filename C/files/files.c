#include <stdio.h>

int main() {
  FILE *fptr; // declare a pointer of type FILE
  // modes: w - write, a - append, r - read
  fptr = fopen("file.txt", "w"); // create and open for writing
  // write some text to the file
  fprintf(fptr, "Some text\n");
  fclose(fptr); // save changes, realease the file, clean up memory
  //
  fptr = fopen("file.txt", "a"); // append to the file
  fprintf(fptr, "Hi everybody!\n");
  fclose(fptr); // save changes, realease the file, clean up memory
  //
  fptr = fopen("file.txt", "r"); // read the file
  // Store the content of the file
  char myStr[99];
  // read the content
  if (fptr == NULL) { // if file does not exist
    printf("Not able to open the file.");
  } else {
    while (fgets(myStr, 99, fptr)) {
      printf("%s", myStr);
    }
  }
  fclose(fptr); // save changes, realease the file, clean up memory
}
