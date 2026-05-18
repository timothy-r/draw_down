Tool to simulate and test draw down strategies


# Set up the project from source

* use python3.12

```
    python3.12 -m venv  .venv
    source .venv/bin/activate
    pip3 install -r drawdown/requirements.txt
```

Simulator takes input of current state of investments, age and runs simulations using strategy objects

Simulator selects inflation rate and investment interest rates - either fixed or variable. These are set on the investment pot or strategy class objects