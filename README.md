DeFiProtocol

![License](https://img.shields.io/badge/license-MIT-blue.svg)

DeFiProtocol is a simplified DeFi lending pool implemented in Solidity and Python using the Brownie development framework. It allows users to deposit tokens into the lending pool and borrow tokens from it.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Testing](#testing)
- [Deployment](#deployment)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/downloads/) (3.7 or higher)
- [Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html)
- [Ganache](https://www.trufflesuite.com/ganache) or an Ethereum testnet for development
- [Metamask](https://metamask.io/) or another Ethereum wallet for interacting with your contracts

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hadesbaker/DeFiProtocol.git
   cd DeFiProtocol
   ```

2. Install the required Python packages

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Deploy the Token and LendingPool contracts:

   ```bash
   brownie run scripts/deploy.py --network development
   ```

2. Interact with the deployed contracts using the Brownie console:

   ```bash
   brownie console --network development
   ```

## Testing

Run the tests to ensure your contracts function as expected:

```bash
brownie test
```

## Deployment

Before deploying your contracts to the Ethereum mainnet, ensure you have:

1. Sufficient ETH for gas fees in your deployment account
2. Completed a security audit of your contracts
3. Considered legal and regulatory compliance

To deploy your contracts, modify the deployment script scripts/deploy.py to specify the deployment network and execute it:

```bash
brownie run scripts/deploy.py --network mainnet
```
