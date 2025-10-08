/************************************************************\
 * Copyright 2014 Lawrence Livermore National Security, LLC
 * (c.f. AUTHORS, NOTICE.LLNS, COPYING)
 *
 * This file is part of the Flux resource manager framework.
 * For details, see https://github.com/flux-framework.
 *
 * SPDX-License-Identifier: LGPL-3.0
\************************************************************/

#ifndef FLUX_TYPES_H
#define FLUX_TYPES_H

#ifdef __cplusplus
extern "C" {
#endif

typedef void (*flux_free_f)(void *arg);

typedef struct {
    char text[160];
} flux_error_t;

#ifdef __cplusplus
}
#endif

#endif /* FLUX_TYPES_H */

// vi:ts=4 sw=4 expandtab
