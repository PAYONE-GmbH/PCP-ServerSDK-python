import json
from typing import Type, TypeVar, Any

T = TypeVar("T")


class JSONSerializer:
    @staticmethod
    def serialize_to_json(obj: Any) -> str:
        """Serialize a Python object to a JSON string."""
        try:
            return json.dumps(obj, default=lambda o: o.__dict__, indent=4)
        except TypeError as e:
            raise ValueError(
                f"Object of type {type(obj).__name__} is not JSON serializable"
            ) from e

    @staticmethod
    def deserialize_from_json(json_str: str, clazz: Type[T]) -> T:
        """Deserialize a JSON string to a Python object."""
        try:
            data = json.loads(json_str)
            if isinstance(data, dict):
                return clazz(**data)
            else:
                raise ValueError("JSON is not a dictionary")
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON format") from e
