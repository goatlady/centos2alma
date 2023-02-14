# Copyright 1999-2022. Plesk International GmbH. All rights reserved.
# vim:ft=python:

python_library(
    name = 'actions.lib',
    srcs = glob(['./actions/*.py']),
)

python_library(
    name = 'common.lib',
    srcs = glob(['./common/*.py']),
)

python_library(
    name = 'distupgrader.lib',
    srcs = glob(['main.py']),
    deps = [
        ':actions.lib',
        ':common.lib',
    ],
)

python_test(
    name = 'libs.tests',
    srcs = glob(['./tests/*.py']),
    deps = [
        ':common.lib',
        ':actions.lib',
    ],
    platform = 'py3',
)

python_binary(
    name = 'distupgrader',
    platform = 'py3',
    main_module = 'main',
    deps = [
        ':distupgrader.lib',
    ]
)
