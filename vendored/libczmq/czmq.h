/************************************************************\
 * Copyright 2021 Lawrence Livermore National Security, LLC
 * (c.f. AUTHORS, NOTICE.LLNS, COPYING)
 *
 * This file is part of the Flux resource manager framework.
 * For details, see https://github.com/flux-framework.
 *
 * SPDX-License-Identifier: LGPL-3.0
\************************************************************/

#ifndef _LIBCZMQ_H
#define _LIBCZMQ_H

#include <sys/types.h>
#include <stdbool.h>
#include <stdint.h>
#include <string.h>

typedef struct _zhash_t zhash_t;
typedef struct _zlist_t zlist_t;
typedef struct _zhashx_t zhashx_t;
typedef struct _zlistx_t zlistx_t;

#ifndef CZMQ_EXPORT
#define CZMQ_EXPORT
#endif

#include "zhash.h"
#include "zlist.h"
#include "zhashx.h"
#include "zlistx.h"

#endif // !_LIBCZMQ_H
