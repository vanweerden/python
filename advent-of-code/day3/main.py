##############################################
### ADVENT OF CODE: DAY 3
##############################################
class BinaryDiagnosticator:
    def __init__(self, filename):
        with open(filename) as f:
            self.input = f.read().splitlines()

    def _get_bit_count(self, binary_list):
        """Returns array with the number of 1s in each position."""
        b_count = [0] * len(binary_list[0])
        for line in binary_list:
            for i, bit in enumerate(line):
                b_count[i] += int(bit)
        return b_count

    ### PART 1
    def get_gamma_rate(self):
        bit_count = self._get_bit_count(self.input)
        bit_l = [1 if x > (len(self.input) / 2) else 0 for x in bit_count]
        bit_s = ''.join(map(str, bit_l))
        return bit_s
        
    def get_epsilon_rate(self):
        # Find 1s complement of (binary) gamma rate
        e_rate = self.get_gamma_rate().replace('1', '2')
        e_rate = e_rate.replace('0', '1')
        e_rate = e_rate.replace('2', '0')
        return e_rate

    def get_power_consumption(self):
        gamma_rate = self._binary_to_decimal(self.get_gamma_rate())
        epsilon_rate = self._binary_to_decimal(self.get_epsilon_rate())
        return gamma_rate * epsilon_rate

    ### PART 2
    def recursive_binary_filter(self, list, bit_chooser, filter=''):
        filter_length = len(filter)

        # Filter the list, keeping only the strings that match the substring
        filtered_list = [b for b in list if b[:filter_length] == filter]

        if len(filtered_list) == 1: 
            # Success
            return filtered_list[0]
        elif len(filtered_list) == 0:
            return "No binary digits pass the Oxygem Generator Rating criteria"
        else:
            bit_count = self._get_bit_count(filtered_list)
            one_count = bit_count[filter_length]
            zero_count = len(filtered_list) - one_count
            current_bit = bit_chooser(zero_count, one_count)
            new_filter = filter + str(current_bit)

            return self.recursive_binary_filter(filtered_list, bit_chooser, new_filter)

    def _get_ox_bit(self, zero_count, one_count):
            if zero_count == one_count:
                return 1
            elif one_count > zero_count:
                return 1
            elif zero_count > one_count:
                return 0

    def _get_co2_bit(self, zero_count, one_count):
        if zero_count == one_count:
            return 0
        elif one_count > zero_count:
            return 0
        elif zero_count > one_count:
            return 1

    def get_ox_generator_rating(self, list, filter=''):
        return self.recursive_binary_filter(list, self._get_ox_bit, filter)

    def get_co2_scrubber_rating(self, list, filter=''):
        return self.recursive_binary_filter(list, self._get_co2_bit, filter)

    def get_life_support_rating(self):
        ox_gen_rating = self._binary_to_decimal(self.get_ox_generator_rating(self.input))
        co2_scrub_rating = self._binary_to_decimal(self.get_co2_scrubber_rating(self.input))
        return ox_gen_rating * co2_scrub_rating

    def _binary_to_decimal(self, binary):
        return int(binary, 2)

diagnostics = BinaryDiagnosticator('input.txt')
print("Power Consumption:", diagnostics.get_power_consumption()) 
print("Life Support Rating:", diagnostics.get_life_support_rating()) 
