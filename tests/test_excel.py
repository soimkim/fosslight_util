#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0
from fosslight_util.write_excel import write_excel_and_csv
from fosslight_util.set_log import init_log


def main():
    logger = init_log("test_result/excel/log_write_excel.txt")
    logger.warning("TESTING - Writing an excel")

    sheet_contents = {}
    src_sheet_items = [['run_scancode.py', 'fosslight_source',
                        '3.0.6', 'Apache-2.0',  'https://github.com/LGE-OSS/fosslight_source',
                        'https://github.com/LGE-OSS/fosslight_source',
                        'Copyright (c) 2021 LG Electronics, Inc.',
                        'Exclude', 'Comment message'],
                       ['', 'Enact',
                        '', 'Apache-2.0',  'https://github.com/enactjs/enact',
                        'https://enactjs.com', 'Copyright (c) 2012-2021 LG Electronics',
                        '', ''],
                       ['dependency_unified.py', 'fosslight_dependency',
                        '3.0.6', 'Apache-2.0',  'https://github.com/LGE-OSS/fosslight_dependency',
                        'https://github.com/LGE-OSS/fosslight_dependency',
                        'Copyright (c) 2020 LG Electronics, Inc.',
                        '', '']]

    bin_sheet_items = [['dependency_unified.py', 'fosslight_dependency',
                        '3.0.6', 'Apache-2.0',  'https://github.com/LGE-OSS/fosslight_dependency',
                        'https://github.com/LGE-OSS/fosslight_dependency', 'Copyright (c) 2020 LG Electronics, Inc.',  '',
                        '', 'Awesome Open Source'],
                       ['askalono.exe', 'askalono',
                        '0.4.3', 'Apache-2.0',  'https://github.com/jpeddicord/askalono',
                        '', 'Copyright (c) 2018 Amazon.com, Inc. or its affiliates.',
                        '', '']]

    sheet_contents['SRC'] = src_sheet_items
    sheet_contents['BIN_TEST'] = bin_sheet_items
    sheet_contents['SRC_NULL'] = []
    sheet_contents['NULL_SHEET'] = []
    success, msg = write_excel_and_csv(
        'test_result/excel/FOSSLight-Report', sheet_contents)
    logger.warning("Result:" + str(success) + ", error_msg:" + msg)


if __name__ == '__main__':
    main()
