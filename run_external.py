from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import TYPE_CHECKING, cast

from x_make_common_x.telemetry import JSONValue
from x_make_github_visitor_x.x_cls_make_github_visitor_x import run_workspace_inspection

if TYPE_CHECKING:
    from x_make_github_visitor_x.inspection_flow import VisitorRunResult


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="x_make_github_visitor_runtime",
        description=(
            "Execute the GitHub visitor inspection flow for a workspace root and "
            "emit a JSON payload describing the outcome."
        ),
    )
    parser.add_argument(
        "--root",
        required=True,
        help="Absolute path to the workspace root containing cloned repositories.",
    )
    parser.add_argument(
        "--disable-cache",
        action="store_true",
        help="Disable cached visitor results for this invocation.",
    )
    return parser


Payload = dict[str, JSONValue]


def _emit_payload(payload: Mapping[str, JSONValue]) -> None:
    json.dump(payload, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")
    sys.stdout.flush()


def _json_value(value: object) -> JSONValue:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Mapping):
        typed_mapping = cast("Mapping[object, object]", value)
        return {str(key): _json_value(val) for key, val in typed_mapping.items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        typed_sequence = cast("Sequence[object]", value)
        return [_json_value(entry) for entry in typed_sequence]
    return str(value)


def _serialize_sequence(items: Sequence[object]) -> list[JSONValue]:
    return [_json_value(entry) for entry in items]


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    raw_root: object = getattr(args, "root", None)
    if not isinstance(raw_root, str):
        message = "--root must be provided as a path string"
        raise TypeError(message)
    raw_disable_cache: object = getattr(args, "disable_cache", False)
    disable_cache_flag = bool(raw_disable_cache)

    root = Path(raw_root).expanduser().resolve()
    enable_cache = not disable_cache_flag

    try:
        result: VisitorRunResult = run_workspace_inspection(
            root, enable_cache=enable_cache
        )
    except AssertionError as err:
        _emit_payload(
            {
                "status": "error",
                "message": str(err),
                "report_path": None,
            }
        )
        return 1
    except Exception as err:  # noqa: BLE001 - defensive fallback
        _emit_payload(
            {
                "status": "error",
                "message": str(err),
                "report_path": None,
            }
        )
        return 1

    payload: Payload = {
        "status": "ok",
        "report_path": (
            str(result.report_path) if result.report_path is not None else None
        ),
        "had_failures": result.had_failures,
        "failure_messages": _serialize_sequence(result.failure_messages),
        "failure_details": _serialize_sequence(result.failure_details),
        "skipped": result.skipped,
    }
    _emit_payload(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
