#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFF_SIZE 2048


int count_delim(char *input, char delim) {
	int arr_size = 1;
	int length = strlen(input);
	for (int k = 0; k < length; k++) {
		if (input[k] == delim) arr_size++;
	}
	return arr_size;
}


int *create_array_from_string(char *input, char delim, int arr_sz) {
	int* arr_ptr;
	int arr_index = 0;
	const char delimiter[2] = {delim, '\0'};
	char *token;

	arr_ptr = (int*)malloc(arr_sz * sizeof(int));

	if (arr_ptr == NULL) {
		printf("Cannot allocate memory");
		exit(0);
	}
	else {
		token = strtok(input, delimiter);
		while (arr_index < arr_sz && token) {
			arr_ptr[arr_index] = atoi(token);
			arr_index++;
			token = strtok(NULL, delimiter);
		}
	}
	return arr_ptr;
}


int main(int argc, char *argv[]) {
	char buff[BUFF_SIZE];
	char delim = ',';
	int *arr;
	int arr_sz;
	FILE *f = fopen("input", "r");
	fgets(buff, BUFF_SIZE, f);

	arr_sz = count_delim(buff, delim);
	arr = create_array_from_string(buff, delim, arr_sz);
	
	for (int i = 0; i < arr_sz; i++) {
		printf("%d\n", arr[i]);
	}

	free(arr);
	fclose(f);

	return 0;
}
