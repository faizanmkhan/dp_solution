#!/bin/bash

input_file="$1"
output_file="accounts_new.csv"

> "$output_file"

# Copy header line as-is
read -r header < "$input_file"
echo "$header" >> "$output_file"

declare -A email_count

# Pass 1: count email usernames (skip header with tail -n +2)
while IFS=',' read -r f1 f2 f3 rest || [ -n "$f1" ]; do
    read -r first last <<< "$f3"
    first_lc="${first,,}"
    last_lc="${last,,}"
    email_user="${first_lc:0:1}${last_lc}"
    email_count["$email_user"]=$(( ${email_count["$email_user"]:-0} + 1 ))
done < <(tail -n +2 "$input_file")

# Pass 2: build output (skip header with tail -n +2)
while IFS=',' read -r f1 f2 f3 rest || [ -n "$f1" ]; do
    # Split rest into title, old email, department
    # Using parameter expansion to avoid breaking on commas inside quoted title
    f6="${rest##*,}"           # department = after last comma
    temp="${rest%,*}"          # strip ,department
    f5="${temp##*,}"           # email = after last comma of temp
    f4="${rest%,$f5,$f6}"      # title = everything before ,email,department

    read -r first last <<< "$f3"
    first_lc="${first,,}"
    last_lc="${last,,}"
    new_name="${first_lc^} ${last_lc^}"
    email_user="${first_lc:0:1}${last_lc}"

    if [ "${email_count[$email_user]}" -gt 1 ]; then
        email="${email_user}${f2}@abc.com"
    else
        email="${email_user}@abc.com"
    fi

    printf "%s,%s,%s,%s,%s,%s\n" "$f1" "$f2" "$new_name" "$f4" "$email" "$f6" >> "$output_file"
done < <(tail -n +2 "$input_file")