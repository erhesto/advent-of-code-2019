#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFF_SIZE 2048
#define TEST_SIZE 99
#define SUCCESS 19690720

int count_delim(char *input, char delim) {
	printf("%d", 1);
	int arr_size = 1;
	int length = strlen(input);
	for (int k = 0; k < length; k++) {
		if (input[k] == delim) arr_size++;
	}
	return arr_size;
}


int *create_array_from_string(char *input, char delim, int arr_sz) {
	char dest[strlen(input)];
	strcpy(dest, input);
	int *arr_ptr;
	int arr_index = 0;
	const char delimiter[2] = {delim, '\0'};
	char *token;

	arr_ptr = (int*)malloc(arr_sz * sizeof(int));

	if (arr_ptr == NULL) {
		printf("Cannot allocate memory");
		exit(0);
	}
	else {
		token = strtok(dest, delimiter);
		while (arr_index < arr_sz && token) {
			arr_ptr[arr_index] = atoi(token);
			arr_index++;
			token = strtok(NULL, delimiter);
		}
	}
	return arr_ptr;
}

int add(int x, int y) {
	return x + y;
}

int mul(int x, int y) {
	return x * y;
}

int compute_result(int *arr) {
	int start_pos = 0;
	int first_num, second_num;
	int output_index;
	int method = arr[start_pos];
	int (*method_ptr)(int, int);

	while (method == 1 || method == 2) { 
		switch (method) {
			case 1:
				method_ptr = add;
				break;
			case 2:
				method_ptr = mul;
				break;
			default:
				printf("Something went wrong!");
				exit(0);
				break;
		}

		// get the numbers
		first_num = arr[arr[start_pos + 1]];
		second_num = arr[arr[start_pos + 2]];
		output_index = arr[start_pos + 3];

		// compute the result to the original arr
		arr[output_index] = method_ptr(first_num, second_num);
		
		// move to another four numbers
		start_pos += 4;
		method = arr[start_pos];
	}

	return arr[0];
}


int do_computation(int input1, int input2, char *input) {
	int *arr;
	int arr_sz;
	char delim = ',';
	int result;

	arr_sz = count_delim(input, delim);

	arr = create_array_from_string(input, delim, arr_sz);
	arr[1] = input1;
	arr[2] = input2;

	result = compute_result(arr);

	free(arr);
	return result;
}


int main(int argc, char *argv[]) {
	int result;
	char buff[BUFF_SIZE];
	FILE *f = fopen("input", "r");
	fgets(buff, BUFF_SIZE, f);
	fclose(f);

	for (int i = 0; i < TEST_SIZE; i++) {
		for (int j = 0; j < TEST_SIZE; j++) {
			result = do_computation(i, j, buff);
			if (result == SUCCESS) {
				printf("Success for %d, %d\n", i, j);
				exit(0);
			}
		}
	}

	return 0;
}
