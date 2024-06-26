# Estatisticas & BlackJack v1 - PTBR

Este é um programa desenvolvido afim de estudar simulações e estatísticas em um tema prático como o BlackJack.

Para fazer com que os dados fossem os mais precisos possíveis, foram implementadas as práticas utilizadas nos cassinos. Utilizando 6 baralhos de 52 cartas cada e a estratégia padrão de Dealer.

O programa tem 2 formas de uso:
1. **Simulação de Rodadas**: Possibilidade de simular milhares de jogos de blackjack para avaliar o desempenho de diferentes estratégias. A simulação automatiza o processo de jogar blackjack, registrando estatísticas importantes como taxas de vitória e uso de estratégias. É uma ferramenta poderosa para entender quais abordagens funcionam melhor em diferentes situações.
2. **Experiência de Cassino**: Possibilita jogar mão a mão, sabendo apenas uma carta da mão do Dealer e tomando as decisões até o jogo terminar para decidir quem ganha.

Esta aplicação é uma simulação de blackjack com estratégias específicas definidas mão a mão. Embora o blackjack seja o objeto central desta simulação, a ideia por trás da aplicação é altamente versátil e pode ser adaptada para diversas áreas do mercado de trabalho. Por exemplo, ela pode ser utilizada para a análise de riscos em finanças, otimização de processos em operações industriais, desenvolvimento de estratégias de marketing, e até mesmo em pesquisas acadêmicas para modelagem de comportamentos e tomadas de decisão. A flexibilidade e a capacidade de adaptação desta aplicação a diferentes contextos demonstram seu valor potencial

# Statistics & BlackJack v1 - EN

This is a program designed to study simulations and statistics on a practical subject such as BlackJack.

To make the data as accurate as possible, the practices used in casinos were implemented. Using 6 decks of 52 cards each and the standard Dealer strategy.

The program can be used in 2 ways:
1. **Simulation of Rounds**: Possibility of simulating thousands of blackjack games to evaluate the performance of different strategies. Simulation automates the process of playing blackjack, recording important statistics such as win rates and strategy usage. It's a powerful tool for understanding which approaches work best in different situations.
2. **Casino Experience**: Allows you to play hand for hand, knowing only one card from the Dealer's hand and making decisions until the game is over to decide who wins.

This application is a blackjack simulation with specific hand-by-hand strategies. Although blackjack is the central object of this simulation, the underlying idea of the application is highly versatile and can be adapted for various areas of the job market. For instance, it can be used for risk analysis in finance, process optimization in industrial operations, strategy development in marketing, and even in academic research for modeling behaviors and decision-making. The flexibility and adaptability of this application to different contexts demonstrate its potential value 


## Project Structure:
To make it easier to upgrade and maintain the code in the future, a modularization strategy was adopted:
- simulation_flow.py: Contains the main logic of the simulation.
- simulator.py: Script to set up and run the simulation.
- main.py: Runs the logic created in the game flow to be able to play hand-to-hand against the dealer through the console.
- game/: Contains modules related to the game (deck initialization, card distribution, game flow for console play, etc.).
- strategy/: Contains strategy functions for different types of hands.
- rules/: Contains the rules for calculating hand values, types of hands, and splitting rules.

## Screenshots:

### Game Mode
![Casino Experience](./Blackjack/img/game_mode.png)

Above is an example of using the Casino Experience mode, where the player chooses between the possible moves and plays against the Dealer.

### Simulation Mode
![Simulation Mode](./Blackjack/img/simulation_mode.png)

Above is an example of using the Simulation Mode, which simulates 100,000 games based on the strategies described in the files and returns the most important statistics.

### Hard Hand
![Hard Hand](./Blackjack/img/hard_hand.jpg)

Above is the diagram on which the strategy for playing all the possible Hard Hands combinations was based.

### Soft Hand
![Soft Hand](./Blackjack/img/soft_hand.jpg)

Above is the diagram on which the strategy for playing all the possible Soft Hands combinations was based.

### Pairs
![Pairs](./Blackjack/img/Pairs.jpg)

Above is the diagram on which the strategy for playing all the possible Pairs combinations was based.

## Future Improvements for next versions:

- Use of supervised or unsupervised learning algorithms to test other possible strategies and maximize the win rate of specific hands
- Implementation of bankroll and betting logics




[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/thpgoncalves)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thiago-pereira-goncalves/)
