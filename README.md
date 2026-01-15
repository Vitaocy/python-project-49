### Hexlet tests and linter status:
[![Actions Status](https://github.com/Vitaocy/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Vitaocy/python-project-49/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Vitaocy_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Vitaocy_python-project-49)


# Игры разума
Набор консольных игр, запускаемых из терминала.  
Проект представляет собой CLI-приложение, в котором пользователь проходит серию математических и логических испытаний. Для победы необходимо дать три правильных ответа подряд.


## Доступные игры
- **brain-even** — определить, является ли число чётным  
- **brain-calc** — решить математическое выражение  
- **brain-gcd** — найти наибольший общий делитель  
- **brain-progression** — определить пропущенное число в прогрессии  
- **brain-prime** — определить, является ли число простым  


## Зависимости:
- Python 3.10+
- make (стандартная утилита Linux / macOS)
- Python-package: 
  - "prompt>=0.4.1"


## Установка [(asciinema)](https://asciinema.org/a/jCaJQAAvwgtL6TF848QesThiG)
```bash
git clone https://github.com/Vitaocy/python-project-49.git
cd python-project-49
make install
make build
make package-install
```

## Запуск игр
После установки игры доступны как обычные CLI-команды:
```bash
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

## Демонстрация работы
**brain-even**
- win [(asciinema)](https://asciinema.org/a/DgHWn4wnBWbkL9JCtEYLujJQ6)
- lose [(asciinema)](https://asciinema.org/a/LBICRrJWMzBaSG5b7VhItAVf7)

**brain-calc**
- win [(asciinema)](https://asciinema.org/a/DQzCJ4Q8r5bH7xt5hYU22reuD)
- lose [(asciinema)](https://asciinema.org/a/hTRwruETS6gx4QAObzLFX3NYo)

**brain-gcd**
- win [(asciinema)](https://asciinema.org/a/ZEQBJj8dooGHirKOacSzmAzHk)
- lose [(asciinema)](https://asciinema.org/a/2jRma3HQlsM9S0GCNXJfSnNWc)

**brain-progression**
- win [(asciinema)](https://asciinema.org/a/9epsySLuXMiGBznC4bpRa9qIp)
- lose [(asciinema)](https://asciinema.org/a/pXr1r6b35bBi3RUFt7dwq498j)

**brain-prime**
- win [(asciinema)](https://asciinema.org/a/gtX0SSAlNxrYeHgxPX5yUlz8F)
- lose [(asciinema)](https://asciinema.org/a/oMYG1L7bA4cXsdcGCP7mVC5zP)