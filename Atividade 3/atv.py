from pathlib import Path
from time import perf_counter


INPUT_FILE = "arq.txt"
OUTPUT_FILE = "arq-ordenado.txt"
RUNS = 5


def read_numbers(file_path: Path) -> list[int]:
	content = file_path.read_text(encoding="utf-8-sig").strip()
	if not content:
		return []
	return [int(value) for value in content.split()]


def write_numbers(file_path: Path, numbers: list[int]) -> None:
	file_path.write_text(" ".join(map(str, numbers)), encoding="utf-8")


def insertion_sort(values: list[int]) -> list[int]:
	arr = values.copy()
	for i in range(1, len(arr)):
		current = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > current:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = current
	return arr


def fast_sort(values: list[int]) -> list[int]:
	return sorted(values)


def benchmark(sort_func, numbers: list[int], runs: int) -> tuple[list[float], list[int]]:
	times_ms = []
	last_result = []

	for _ in range(runs):
		start = perf_counter()
		last_result = sort_func(numbers)
		end = perf_counter()
		times_ms.append((end - start) * 1000)

	return times_ms, last_result


def print_results(name: str, times_ms: list[float]) -> None:
	average = sum(times_ms) / len(times_ms)
	print(f"{name} - tempos (ms):")
	for i, t in enumerate(times_ms, start=1):
		print(f"  Execucao {i}: {t:.3f} ms")
	print(f"  Media: {average:.3f} ms\n")


def main() -> None:
	base_dir = Path(__file__).resolve().parent
	input_path = base_dir / INPUT_FILE
	output_path = base_dir / OUTPUT_FILE

	numbers = read_numbers(input_path)

	slow_times, slow_sorted = benchmark(insertion_sort, numbers, RUNS)
	fast_times, fast_sorted = benchmark(fast_sort, numbers, RUNS)

	
	if slow_sorted != fast_sorted:
		raise ValueError("Os algoritmos produziram resultados diferentes.")

	write_numbers(output_path, fast_sorted)

	print_results("Insertion Sort (lento)", slow_times)
	print_results("Sort nativo do Python (rapido)", fast_times)
	print(f"Arquivo de saida gerado: {output_path.name}")


if __name__ == "__main__":
	main()
