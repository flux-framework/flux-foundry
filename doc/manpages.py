###############################################################
# Copyright 2022 Lawrence Livermore National Security, LLC
# (c.f. AUTHORS, NOTICE.LLNS, COPYING)
#
# This file is part of the Flux resource manager framework.
# For details, see https://github.com/flux-framework.
#
# SPDX-License-Identifier: LGPL-3.0
###############################################################

author = 'This page is maintained by the Flux community.'

# Add man page entries with the following information:
# - Relative file path (without .rst extension)
# - Man page name
# - Man page description
# - Author (use [author])
# - Manual section
#
man_pages = [
    ('man3/hostlist_create', 'hostlist_create', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_destroy', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_decode', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_encode', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_copy', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_append', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_append_list', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_nth', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_find', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_delete', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_count', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_sort', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_uniq', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_first', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_last', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_next', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_current', 'Manipulate lists of hostnames', [author], 3),
    ('man3/hostlist_create', 'hostlist_remove_current', 'Manipulate lists of hostnames', [author], 3),
    ('man3/idset_create', 'idset_create', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_destroy', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_copy', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_set', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_range_set', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_clear', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_range_clear', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_test', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_first', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_next', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_prev', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_empty', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_universe_size', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_last', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_create', 'idset_count', 'Manipulate numerically sorted sets of non-negative integers', [author], 3),
    ('man3/idset_encode','idset_encode', 'Convert idset to string', [author], 3),
    ('man3/idset_decode','idset_decode', 'Convert string to idset', [author], 3),
    ('man3/idset_decode','idset_decode_ex', 'Convert string to idset', [author], 3),
    ('man3/idset_decode','idset_decode_empty', 'Convert string to idset', [author], 3),
    ('man3/idset_decode','idset_decode_info', 'Convert string to idset', [author], 3),
    ('man3/idset_decode','idset_decode_add', 'Convert string to idset', [author], 3),
    ('man3/idset_decode','idset_decode_subtract', 'Convert string to idset', [author], 3),
    ('man3/idset_add', 'idset_equal', 'Perform set operations on idsets', [author], 3),
    ('man3/idset_add','idset_union', 'Perform set operations on idsets', [author], 3),
    ('man3/idset_add','idset_add', 'Perform set operations on idsets', [author], 3),
    ('man3/idset_add','idset_difference', 'Perform set operations on idsets', [author], 3),
    ('man3/idset_add','idset_subtract', 'Perform set operations on idsets', [author], 3),
    ('man3/idset_add','idset_intersect', 'Perform set operations on idsets', [author], 3),
    ('man3/idset_add','idset_has_intersection', 'Perform set operations on idsets', [author], 3),
    ('man3/idset_add','idset_clear_all', 'Perform set operations on idsets', [author], 3),
    ('man3/idset_alloc','idset_alloc', 'Allocate an id from an idset', [author], 3),
    ('man3/idset_alloc','idset_free', 'Allocate an id from an idset', [author], 3),
    ('man3/idset_alloc','idset_free_check', 'Allocate an id from an idset', [author], 3),
]
