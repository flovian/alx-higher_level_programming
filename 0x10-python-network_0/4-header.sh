#!/bin/bash
# curl sends GET req to URL, displays response body
curl -sX GET -H "X-School-User-Id: 98" "$1"
