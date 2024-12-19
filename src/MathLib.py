class MathLib:

    @classmethod
    def execute(cls, math_request):
        ope1 = math_request.get_ope1()
        operator = math_request.get_operator()
        ope2 = math_request.get_ope2()

        match operator:
            case 'add':
                math_request.set_res(ope1 + ope2)
            case 'sub':
                math_request.set_res(ope1 - ope2)
            case 'mul':
                math_request.set_res(ope1 * ope2)
            case 'div':
                if ope2 == 0:
                    print("Error: Division by zero is undefined.")
                    return
                math_request.set_res(ope1 / ope2)
            case 'pow':
                math_request.set_res(ope1 ** ope2)
            case 'root':
                raise NotImplementedError
            case _:
                raise NotImplementedError

    @staticmethod
    def __root(ope1, ope2):
        raise NotImplementedError

class MathLibException(Exception):
    pass

class OperatorNotSupportedException(MathLibException):
    pass