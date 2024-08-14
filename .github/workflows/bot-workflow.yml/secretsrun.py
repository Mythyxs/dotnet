name: Run Bot Script

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run bot script
      env:
        SHEM_AI_TOKEN: ${{ secrets.SHEM_AI_TOKEN }}
        CBA_AI_TOKEN: ${{ secrets.CBA_AI_TOKEN }}
        LUA_AI_TOKEN: ${{ secrets.LUA_AI_TOKEN }}
        MATOKA_AI_TOKEN: ${{ secrets.MATOKA_AI_TOKEN }}
      run: python your_script.py
