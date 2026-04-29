import math

class Solver:
    def solve(self, ast):
        if ast.formula == "pythagoras":
            return self.solve_pythagoras(ast)

        elif ast.formula in ["sin", "cos", "tan", "sec", "cosec", "cot"]:
            return self.solve_trigonometry(ast)

        else:
            raise Exception(f"Unsupported operation: {ast.formula}")
        
    def solve_pythagoras(self, ast):
        values = {}

        for assignment in ast.assignments:
            values[assignment.variable] = assignment.value

        target = ast.target

        explanation = "Given:\n"
        for var, val in values.items():
            explanation += f"{var} = {val}\n"

        explanation += "\nUsing Pythagoras theorem:\n"
        explanation += "c = sqrt(a² + b²)\n"

        if target == "c":
            if "a" in values and "b" in values:
                a = values["a"]
                b = values["b"]

                # Step 1: Substitute values
                explanation += f"c = sqrt({a}² + {b}²)\n"

                # Step 2: Square values
                a_sq = a ** 2
                b_sq = b ** 2
                explanation += f"c = sqrt({a_sq} + {b_sq})\n"

                # Step 3: Add inside sqrt
                total = a_sq + b_sq
                explanation += f"c = sqrt({total})\n"

                # Step 4: Final result
                result = round(math.sqrt(total), 2)
                explanation += f"c = {result}\n"

                explanation += "\nHence,\n"
                explanation += f"c = {result}"

                return explanation

        elif target == "a":
            if "b" in values and "c" in values:
                b = values["b"]
                c = values["c"]

                explanation += "a = sqrt(c² - b²)\n"
                explanation += f"a = sqrt({c}² - {b}²)\n"

                c_sq = c ** 2
                b_sq = b ** 2
                explanation += f"a = sqrt({c_sq} - {b_sq})\n"

                total = c_sq - b_sq
                explanation += f"a = sqrt({total})\n"

                result = round(math.sqrt(total), 2)
                explanation += f"a = {result}\n"

                explanation += "\nHence,\n"
                explanation += f"a = {result}"

                return explanation

        elif target == "b":
            if "a" in values and "c" in values:
                a = values["a"]
                c = values["c"]

                explanation += "b = sqrt(c² - a²)\n"
                explanation += f"b = sqrt({c}² - {a}²)\n"

                c_sq = c ** 2
                a_sq = a ** 2
                explanation += f"b = sqrt({c_sq} - {a_sq})\n"

                total = c_sq - a_sq
                explanation += f"b = sqrt({total})\n"

                result = round(math.sqrt(total), 2)
                explanation += f"b = {result}\n"

                explanation += "\nHence,\n"
                explanation += f"b = {result}"

                return explanation

        raise Exception("Insufficient or invalid data for pythagoras")
    
    def solve_trigonometry(self, ast):
        import math

        values = {}
        for assignment in ast.assignments:
            values[assignment.variable] = assignment.value

        if "angle" not in values:
            raise Exception("Angle is required for trigonometry")

        angle = values["angle"]
        radians = math.radians(angle)

        explanation = "Given:\n"
        for var, val in values.items():
            explanation += f"{var} = {val}\n"

        explanation += f"\nUsing {ast.formula} function:\n"

        # ----------------------------------
        # CASE 1: Only angle → direct value
        # ----------------------------------
        if len(values) == 1:

            if ast.formula == "sin":
                base_val = math.sin(radians)
                explanation += f"sin({angle}) = {round(base_val,4)}\n"

            elif ast.formula == "cos":
                base_val = math.cos(radians)
                explanation += f"cos({angle}) = {round(base_val,4)}\n"

            elif ast.formula == "tan":
                base_val = math.tan(radians)
                explanation += f"tan({angle}) = {round(base_val,4)}\n"

            elif ast.formula == "sec":
                cos_val = math.cos(radians)
                base_val = 1 / cos_val
                explanation += f"sec({angle}) = 1 / cos({angle})\n"
                explanation += f"sec({angle}) = {round(base_val,4)}\n"

            elif ast.formula == "cosec":
                sin_val = math.sin(radians)
                if sin_val == 0:
                    raise Exception("cosec undefined for this angle")
                base_val = 1 / sin_val
                explanation += f"cosec({angle}) = 1 / sin({angle})\n"
                explanation += f"cosec({angle}) = {round(base_val,4)}\n"

            elif ast.formula == "cot":
                tan_val = math.tan(radians)
                base_val = 1 / tan_val
                explanation += f"cot({angle}) = 1 / tan({angle})\n"
                explanation += f"cot({angle}) = {round(base_val,4)}\n"

            result = round(base_val, 4)

            explanation += "\nHence,\n"
            explanation += f"value = {result}"

            return explanation

        # ----------------------------------
        # CASE 2: Triangle solving
        # ----------------------------------

        # TAN CASE
        if ast.formula == "tan":
            if "base" in values and ast.target == "height":
                base = values["base"]
                tan_val = math.tan(radians)

                explanation += "tan(θ) = height / base\n"
                explanation += f"tan({angle}) = height / {base}\n"

                height = round(base * tan_val, 2)

                explanation += f"height = {base} × tan({angle})\n"
                explanation += f"height = {height}\n\n"
                explanation += "Hence,\n"
                explanation += f"height = {height}"

                return explanation

        # COS CASE
        if ast.formula == "cos":
            if "hypotenuse" in values and ast.target == "base":
                hyp = values["hypotenuse"]
                cos_val = math.cos(radians)

                explanation += "cos(θ) = base / hypotenuse\n"
                explanation += f"cos({angle}) = base / {hyp}\n"

                base = round(hyp * cos_val, 2)

                explanation += f"base = {hyp} × cos({angle})\n"
                explanation += f"base = {base}\n\n"
                explanation += "Hence,\n"
                explanation += f"base = {base}"

                return explanation

        # SIN CASE
        if ast.formula == "sin":
            if "hypotenuse" in values and ast.target == "height":
                hyp = values["hypotenuse"]
                sin_val = math.sin(radians)

                explanation += "sin(θ) = height / hypotenuse\n"
                explanation += f"sin({angle}) = height / {hyp}\n"

                height = round(hyp * sin_val, 2)

                explanation += f"height = {hyp} × sin({angle})\n"
                explanation += f"height = {height}\n\n"
                explanation += "Hence,\n"
                explanation += f"height = {height}"

                return explanation
            
        # SEC CASE
        if ast.formula == "sec":
            if "base" in values and ast.target == "hypotenuse":
                base = values["base"]
                cos_val = math.cos(radians)

                if cos_val == 0:
                    raise Exception("sec undefined for this angle")

                sec_val = 1 / cos_val

                explanation += "sec(θ) = hypotenuse / base\n"
                explanation += f"sec({angle}) = hypotenuse / {base}\n"

                hyp = round(base * sec_val, 2)

                explanation += f"hypotenuse = {base} × sec({angle})\n"
                explanation += f"hypotenuse = {hyp}\n\n"
                explanation += "Hence,\n"
                explanation += f"hypotenuse = {hyp}"

                return explanation
            
        # COSEC CASE
        if ast.formula == "cosec":
            if "height" in values and ast.target == "hypotenuse":
                height = values["height"]
                sin_val = math.sin(radians)

                if sin_val == 0:
                    raise Exception("cosec undefined for this angle")

                cosec_val = 1 / sin_val

                explanation += "cosec(θ) = hypotenuse / height\n"
                explanation += f"cosec({angle}) = hypotenuse / {height}\n"

                hyp = round(height * cosec_val, 2)

                explanation += f"hypotenuse = {height} × cosec({angle})\n"
                explanation += f"hypotenuse = {hyp}\n\n"
                explanation += "Hence,\n"
                explanation += f"hypotenuse = {hyp}"

                return explanation
            
            # COT CASE
        if ast.formula == "cot":
            if "height" in values and ast.target == "base":
                height = values["height"]
                tan_val = math.tan(radians)

                if tan_val == 0:
                    raise Exception("cot undefined for this angle")

                cot_val = 1 / tan_val

                explanation += "cot(θ) = base / height\n"
                explanation += f"cot({angle}) = base / {height}\n"

                base = round(height * cot_val, 2)

                explanation += f"base = {height} × cot({angle})\n"
                explanation += f"base = {base}\n\n"
                explanation += "Hence,\n"
                explanation += f"base = {base}"

                return explanation

        raise Exception("Unsupported trigonometry case")