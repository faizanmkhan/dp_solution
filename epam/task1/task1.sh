#!/bin/bash

input_file="$1"
output_file="accounts_new.csv"

> "$output_file"

declare -A email_count

# Pass 1: count email usernames
while IFS=',' read -r f1 f2 f3 f4 f5 f6; do
    read -r first last <<< "$f3"
    first_lc="${first,,}"
    last_lc="${last,,}"
    email_user="${first_lc:0:1}${last_lc}"
    email_count["$email_user"]=$(( ${email_count["$email_user"]:-0} + 1 ))
done < "$input_file"

# Pass 2: build output
while IFS=',' read -r f1 f2 f3 f4 f5 f6; do
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
done < "$input_file"