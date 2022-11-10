from vent_scanner import VentScanner

input_file = "input.txt"
scanner = VentScanner(input_file)
scanner.scan()
result = scanner.count_danger_zones()
print(result)