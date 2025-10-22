/************************************************************\
 * Copyright 2014 Lawrence Livermore National Security, LLC
 * (c.f. AUTHORS, NOTICE.LLNS, COPYING)
 *
 * This file is part of the Flux resource manager framework.
 * For details, see https://github.com/flux-framework.
 *
 * SPDX-License-Identifier: LGPL-3.0
\************************************************************/

#ifndef _FLUX_CONF_H
#define _FLUX_CONF_H

#include <stdarg.h>
#include <flux/types.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct flux_conf flux_conf_t;

/* Create/copy/incref/decref config object
 */
flux_conf_t *flux_conf_create (void);
flux_conf_t *flux_conf_copy (const flux_conf_t *conf);
const flux_conf_t *flux_conf_incref (const flux_conf_t *conf);
void flux_conf_decref (const flux_conf_t *conf);

/* Parse TOML config in 'path' and return a new flux_conf_t on success.
 * If path is a directory, then parse all files matching *.toml in path.
 */
flux_conf_t *flux_conf_parse (const char *path, flux_error_t *error);

/* Access config object.
 * If error is non-NULL, it is filled with error details on failure.
 */
int flux_conf_vunpack (const flux_conf_t *conf,
                       flux_error_t *error,
                       const char *fmt,
                       va_list ap);

int flux_conf_unpack (const flux_conf_t *conf,
                      flux_error_t *error,
                      const char *fmt,
                      ...);

flux_conf_t *flux_conf_vpack (const char *fmt, va_list ap);
flux_conf_t *flux_conf_pack (const char *fmt, ...);

#ifdef __cplusplus
}
#endif

#endif /* !_FLUX_CONF_H */

/*
 * vi:tabstop=4 shiftwidth=4 expandtab
 */
