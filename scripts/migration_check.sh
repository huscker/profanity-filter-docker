#!/usr/bin/env bash

output=$(poetry run aerich migrate 2>&1)

if echo "$output" | grep -q "No changes detected"; then
    exit 0
else
    exit 1
fi
