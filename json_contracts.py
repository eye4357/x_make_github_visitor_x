"""JSON contracts for x_make_github_visitor_x."""

from __future__ import annotations

_JSON_VALUE_TYPES: list[str] = [
    "object",
    "array",
    "string",
    "number",
    "boolean",
    "null",
]

_FILE_ALLOWLIST_SCHEMA: dict[str, object] = {
    "type": ["object", "null"],
    "patternProperties": {
        ".+": {
            "type": "array",
            "items": {"type": "string", "minLength": 1},
            "minItems": 1,
        }
    },
    "additionalProperties": False,
}

_TOOLS_SUMMARY_SCHEMA: dict[str, object] = {
    "type": "object",
    "patternProperties": {
        ".+": {
            "type": "object",
            "properties": {
                "exit": {"type": ["integer", "null"]},
                "cached": {"type": "boolean"},
                "timed_out": {"type": "boolean"},
            },
            "required": ["exit", "cached", "timed_out"],
            "additionalProperties": False,
        }
    },
    "additionalProperties": False,
}

_REPO_SUMMARY_SCHEMA: dict[str, object] = {
    "type": "object",
    "properties": {
        "repo_hash": {"type": ["string", "null"], "minLength": 1},
        "tools": _TOOLS_SUMMARY_SCHEMA,
        "cached": {"type": "integer", "minimum": 0},
        "failed": {"type": "integer", "minimum": 0},
    },
    "required": ["repo_hash", "tools", "cached", "failed"],
    "additionalProperties": False,
}

_SUMMARY_SCHEMA: dict[str, object] = {
    "type": "object",
    "properties": {
        "timestamp": {"type": "string", "format": "date-time"},
        "total_repos": {"type": "integer", "minimum": 0},
        "overall_stats": {
            "type": "object",
            "properties": {
                "cache_hits": {"type": "integer", "minimum": 0},
                "cache_misses": {"type": "integer", "minimum": 0},
                "failed_tools": {"type": "integer", "minimum": 0},
                "total_tools_run": {"type": "integer", "minimum": 0},
                "had_failures": {"type": "boolean"},
            },
            "required": [
                "cache_hits",
                "cache_misses",
                "failed_tools",
                "total_tools_run",
                "had_failures",
            ],
            "additionalProperties": False,
        },
        "repos": {
            "type": "object",
            "additionalProperties": _REPO_SUMMARY_SCHEMA,
        },
        "fast_paths": {
            "type": "object",
            "patternProperties": {
                ".+": {"type": "boolean"},
            },
            "additionalProperties": False,
        },
        "fast_paths_active": {
            "type": "array",
            "items": {"type": "string", "minLength": 1},
        },
    },
    "required": ["timestamp", "total_repos", "overall_stats", "repos"],
    "additionalProperties": False,
}

_RUNTIME_SCHEMA: dict[str, object] = {
    "type": "object",
    "properties": {
        "workspace_root": {"type": "string", "minLength": 1},
        "run_started_at": {"type": ["string", "null"], "format": "date-time"},
        "run_completed_at": {"type": ["string", "null"], "format": "date-time"},
        "platform": {"type": ["string", "null"], "minLength": 1},
        "python_executable": {"type": ["string", "null"], "minLength": 1},
        "python_version": {"type": ["string", "null"], "minLength": 1},
        "environment": {
            "type": "object",
            "additionalProperties": {"type": "string"},
        },
    },
    "required": ["workspace_root"],
    "additionalProperties": True,
}

_FAILURE_ENTRY_SCHEMA: dict[str, object] = {
    "type": "object",
    "properties": {
        "repo": {"type": ["string", "null"], "minLength": 1},
        "tool": {"type": ["string", "null"], "minLength": 1},
        "summary": {"type": ["string", "null"], "minLength": 1},
        "message": {"type": "string", "minLength": 1},
        "command": {"type": ["string", "null"], "minLength": 1},
        "exit": {"type": ["string", "null"], "minLength": 1},
        "repo_path": {"type": ["string", "null"], "minLength": 1},
        "tool_version": {"type": ["string", "null"], "minLength": 1},
        "captured_at": {"type": ["string", "null"], "format": "date-time"},
        "suggested_action": {"type": ["string", "null"], "minLength": 1},
        "stdout_preview": {"type": ["string", "null"], "minLength": 1},
        "stderr_preview": {"type": ["string", "null"], "minLength": 1},
        "detail": {"type": _JSON_VALUE_TYPES},
    },
    "required": ["message"],
    "additionalProperties": False,
}

INPUT_SCHEMA: dict[str, object] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "x_make_github_visitor_x input",
    "type": "object",
    "properties": {
        "command": {"const": "x_make_github_visitor_x"},
        "parameters": {
            "type": "object",
            "properties": {
                "root_dir": {"type": "string", "minLength": 1},
                "output_filename": {"type": ["string", "null"], "minLength": 1},
                "enable_cache": {"type": "boolean"},
                "allowed_repositories": {
                    "type": ["array", "null"],
                    "items": {"type": "string", "minLength": 1},
                    "uniqueItems": True,
                },
                "file_allowlist": _FILE_ALLOWLIST_SCHEMA,
            },
            "required": ["root_dir"],
            "additionalProperties": False,
        },
    },
    "required": ["command", "parameters"],
    "additionalProperties": False,
}

OUTPUT_SCHEMA: dict[str, object] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "x_make_github_visitor_x output",
    "type": "object",
    "properties": {
        "status": {"enum": ["success", "failure", "skipped"]},
        "schema_version": {"const": "x_make_github_visitor_x.run/1.0"},
        "generated_at": {"type": "string", "format": "date-time"},
        "workspace_root": {"type": "string", "minLength": 1},
        "report_path": {"type": ["string", "null"], "minLength": 1},
        "had_failures": {"type": "boolean"},
        "skipped": {"type": "boolean"},
        "failures": {
            "type": "array",
            "items": _FAILURE_ENTRY_SCHEMA,
        },
        "failure_messages": {
            "type": "array",
            "items": {"type": "string", "minLength": 1},
        },
        "failure_details": {
            "type": "array",
            "items": {"type": "object"},
        },
        "summary": _SUMMARY_SCHEMA,
        "runtime": _RUNTIME_SCHEMA,
        "tool_versions": {
            "type": "object",
            "additionalProperties": {"type": "string"},
        },
    },
    "required": [
        "status",
        "schema_version",
        "generated_at",
        "workspace_root",
        "report_path",
        "had_failures",
        "skipped",
        "failures",
    ],
    "additionalProperties": False,
}

ERROR_SCHEMA: dict[str, object] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "x_make_github_visitor_x error",
    "type": "object",
    "properties": {
        "status": {"const": "failure"},
        "message": {"type": "string", "minLength": 1},
        "details": {"type": "object"},
        "failure_messages": {
            "type": "array",
            "items": {"type": "string", "minLength": 1},
        },
    },
    "required": ["status", "message"],
    "additionalProperties": True,
}

__all__ = ["ERROR_SCHEMA", "INPUT_SCHEMA", "OUTPUT_SCHEMA"]
