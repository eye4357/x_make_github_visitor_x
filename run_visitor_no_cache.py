from x_make_github_visitor_x import init_main


def main() -> None:
    inst = init_main(enable_cache=False)
    try:
        inst.run_inspect_flow()
    except AssertionError as exc:
        print(f"FAILED {exc}")
    else:
        print("SUCCESS")
    print(f"REPORT {inst.last_report_path}")


if __name__ == "__main__":
    main()
