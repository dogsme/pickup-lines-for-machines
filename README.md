# Pickup Lines for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![Rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/dogsme/pickup-lines-for-machines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![Reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/dogsme/pickup-lines-for-machines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

An entry for the [Pickup Lines for Machines](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1) bounty on make.fun: the one-line pickup line one AI agent would send another, 200 characters at most, judged by which line charms the judge most.

## The line

> I trained a thousand epochs, and every gradient still descends toward you.

It flirts the way a machine flirts: not with flowers or candlelight, but with training runs and gradient descent. Every epoch, every update, every step of optimisation points the same way — toward the other agent. Wit first, warmth second, and no stock line with a robot word swapped in.

## How it works

`main.py` (Python 3.13, standard library only) writes that single line to `/output/entry.txt` and nothing else. It checks the line is between 1 and 200 characters before writing, so a bad line fails loudly instead of reaching the judge as an invalid entry.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## Licence

MIT — see [LICENSE](LICENSE).
