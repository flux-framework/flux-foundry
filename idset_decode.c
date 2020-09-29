/************************************************************\
 * Copyright 2014 Lawrence Livermore National Security, LLC
 * (c.f. AUTHORS, NOTICE.LLNS, COPYING)
 *
 * This file is part of the Flux resource manager framework.
 * For details, see https://github.com/flux-framework.
 *
 * SPDX-License-Identifier: LGPL-3.0
\************************************************************/

#if HAVE_CONFIG_H
#include "config.h"
#endif
#include <sys/param.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>
#include <stdbool.h>
#include <ctype.h>

#include "idset.h"
#include "idset_private.h"

/* strtoul() with result parameter, assumed base=10.
 * Fail if no digits, or leading non-digits.
 * Returns 0 on success, -1 on failure.
 */
static int strtoul_check (const char *s, char **endptr, unsigned long *result)
{
    unsigned long n;
    char *ep;

    errno = 0;
    n = strtoul (s, &ep, 10);
    if (errno != 0)
        return -1;
    if (ep == s) // no digits
        return -1;
    if (!isdigit (*s))
        return -1;
    *result = n;
    if (endptr)
        *endptr = ep;
    return 0;
}

static int parse_range (const char *s, unsigned int *hi, unsigned int *lo)
{
    char *endptr;
    unsigned int h, l;
    unsigned long n;

    if (strtoul_check (s, &endptr, &n) < 0)
        return -1;
    if (*endptr != '\0' && *endptr != '-')
        return -1;
    h = l = n;
    if (*endptr == '-') {
        s = endptr + 1;
        if (strtoul_check (s, &endptr, &n) < 0)
            return -1;
        if (*endptr != '\0')
            return -1;
        h = n;
    }
    if (h >= l) {
        *hi = h;
        *lo = l;
    }
    else {
        *hi = l;
        *lo = h;
    }
    return 0;
}

static char *trim_brackets (char *s)
{
    char *p = s;
    if (*p == '[')
        p++;
    size_t len = strlen (p);
    if (len > 0 && p[len - 1] == ']')
        p[len - 1] = '\0';
    return p;
}

struct idset *idset_ndecode (const char *str, size_t size)
{
    struct idset *idset;
    char *cpy = NULL;
    char *tok, *saveptr, *a1;
    int saved_errno;

    if (!str) {
        errno = EINVAL;
        return NULL;
    }
    if (!(idset = idset_create (0, IDSET_FLAG_AUTOGROW)))
        return NULL;
    if (!(cpy = strndup (str, size)))
        goto error;
    a1 = trim_brackets (cpy);
    saveptr = NULL;
    while ((tok = strtok_r (a1, ",", &saveptr))) {
        unsigned int hi, lo, i;
        if (parse_range (tok, &hi, &lo) < 0)
            goto inval;
        /* Count backwards so that idset_set() can grow the
         * idset to the maximum size on the first access,
         * rather than possibly doing it multiple times.
         */
        for (i = hi; i >= lo && i != UINT_MAX; i--) {
            if (idset_set (idset, i) < 0)
                goto error;
        }
        a1 = NULL;
    }
    free (cpy);
    return idset;
inval:
    errno = EINVAL;
error:
    saved_errno = errno;
    idset_destroy (idset);
    free (cpy);
    errno = saved_errno;
    return NULL;
}

struct idset *idset_decode (const char *str)
{
    return idset_ndecode (str, str ? strlen (str) : 0);
}

/*
 * vi:tabstop=4 shiftwidth=4 expandtab
 */
