import pytest

#
# https://github.com/conda-forge/yamllint-feedstock/pull/24
locale_skips = """
test_accents
test_case
test_locale_accents
test_locale_case
test_run_auto_output_without_tty_output
test_run_default_format_output_in_tty
test_run_default_format_output_without_tty
test_run_empty_file
test_run_format_colored
test_run_multiple_files
test_run_no_warnings
test_run_no_warnings_and_strict
test_run_non_ascii_file
test_run_non_existing_file
test_run_non_universal_newline
test_run_one_ok_file
test_run_one_problem_file
test_run_one_warning
test_run_piped_output_nocolor
test_run_read_from_stdin
test_run_warning_in_strict_mode
test_run_with_config_file
test_run_with_locale
""".strip().splitlines()

skip_arg = "not ({})".format(" or ".join(locale_skips))


if __name__ == "__main__":
    # TODO: potentially restore
    pytest.main(["."]) #  , "-k", skip_arg])
