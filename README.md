# My Own Invoke AI

A hands-on exploration of what happens under the hood when invoking an LLM.

This project starts from a direct HTTP request to the Anthropic API using Python and `requests`, avoiding high-level abstractions such as `llm.invoke()`.

Current flow:

Python
  ↓
HTTP request
  ↓
Anthropic API
  ↓
Claude
  ↓
JSON response
  ↓
Assistant message
