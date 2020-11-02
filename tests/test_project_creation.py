#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import importlib


def test_defult_project_creation(cookies, bake_in_temp_dir):
    """Test that a project can be safely created."""
    with bake_in_temp_dir(cookies) as results:
        # Assert
        assert results.exit_code == 0
        assert results.exception is None


def test_project_creation_with_non_default_values(cookies, bake_in_temp_dir):
    """Test that a project can be safely created."""
    # Setup
    full_name = "Larry Kippers"
    repo_name = "cat-jumps"
    project_name = "cat_jumps"
    extra_context = {"full_name": full_name, "repo_name": repo_name}

    with bake_in_temp_dir(cookies, extra_context=extra_context) as results:
        # Assert
        assert results.exit_code == 0
        assert results.exception is None
        assert results.context["full_name"] == full_name
        assert results.context["repo_name"] == repo_name
        assert results.context["package_name"] == project_name


def test_package_can_install(cookies, bake_in_temp_dir, run_inside_dir):
    """Test that the package can be installed."""
    with bake_in_temp_dir(cookies) as results:
        # Run
        run_inside_dir("pip3 install .", results.project)

        # Assert
        assert importlib.util.find_spec(results.context["package_name"]) is not None

        # Teardown
        run_inside_dir(
            f"pip3 uninstall -y {results.context['package_name']}", results.project,
        )


def test_package_can_install_dev(cookies, bake_in_temp_dir, run_inside_dir):
    """Test that the package can be installed."""
    with bake_in_temp_dir(cookies) as results:
        # Run
        run_inside_dir("pip3 install .[dev]", results.project)

        # Assert
        assert importlib.util.find_spec(results.context["package_name"]) is not None

        # Teardown
        run_inside_dir(
            f"pip3 uninstall -y {results.context['package_name']}", results.project,
        )


def test_package_can_run_tests(cookies, bake_in_temp_dir, run_inside_dir):
    """Test that the package can be installed."""
    with bake_in_temp_dir(cookies) as results:
        # Run
        run_inside_dir("pip3 install .", results.project)

        # Assert
        assert run_inside_dir("pytest", str(results.project)) == 0

        # Teardown
        run_inside_dir(
            f"pip3 uninstall -y {results.context['package_name']}", results.project,
        )


def test_package_pre_commit(cookies, bake_in_temp_dir, run_inside_dir):
    """Test that the package can be installed."""
    with bake_in_temp_dir(cookies) as results:

        # Assert
        assert run_inside_dir("pre-commit run --all-files", str(results.project)) == 0
