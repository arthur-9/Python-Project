def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_line = []
    second_line = []
    dashes = []
    answers = []
    
    for problem in problems:
        parts = problem.split()
        
        # Check if the operator is valid
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Check if the operands are numbers and only digits
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        # Check if the numbers are less than or equal to 4 digits
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]
        
        # Find the required width for formatting
        width = max(len(operand1), len(operand2)) + 2
        
        # Format the first line (right-aligned)
        first_line.append(operand1.rjust(width))
        
        # Format the second line with the operator and operand (with a space before the second operand)
        second_line.append(operator + ' ' + operand2.rjust(width - 2))
        
        # Add the dashes line
        dashes.append('-' * width)
        
        # Calculate the result if show_answers is True
        if show_answers:
            result = str(eval(problem))
            answers.append(result.rjust(width))
    
    # Combine all parts into a final arranged string
    arranged_problems = (
        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dashes)
    )
    
    # If show_answers is True, include the answers at the bottom
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
    
    return arranged_problems

# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
