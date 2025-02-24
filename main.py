from dataclasses import dataclass, asdict
from typing import Generic, Self, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Result(Generic[T]):
    value: T | None = None
    error: str = None
    is_sucess: bool = None

    @staticmethod
    def sucess(value: T, as_dict=True) -> Self:
        result = Result(value, None, True)
        return asdict(result).values() if as_dict else result

    @staticmethod
    def failure(error: str, as_dict=True) -> Self:
        result = Result(None, error, False)
        return asdict(result).values() if as_dict else result


if __name__ == "__main__":

    value, error, is_sucess = Result.sucess("sucees")

    print(error)
    print(value)
    print(is_sucess)

    value, error, is_sucess = Result.failure("error")

    print(error)
    print(value)
    print(is_sucess)
