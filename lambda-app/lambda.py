# Copyright (c) 2024 Phil Chen All rights reserved.
# This work is licensed under the terms of the MIT license.

# Lambda that returns JSON

def endpoint(event, context):
    output = {"name":"John Doe", "accountNumber":56789, "balanceStatus":22000}
    return output
