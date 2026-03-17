#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <limits>

using namespace std;

bool parse_positive_integer(const string& text, int& value) {
    if (text.empty()) {
        return false;
    }

    size_t idx = 0;
    long long parsed = 0;

    try {
        parsed = stoll(text, &idx);
    } catch (...) {
        return false;
    }

    if (idx != text.size()) {
        return false;
    }

    if (parsed < 1 || parsed > numeric_limits<int>::max()) {
        return false;
    }

    value = static_cast<int>(parsed);
    return true;
}

vector<int> sieve_primes_up_to(int n) {
    vector<bool> is_prime(n + 1, true);
    if (n >= 0) is_prime[0] = false;
    if (n >= 1) is_prime[1] = false;

    for (int p = 2; 1LL * p * p <= n; ++p) {
        if (is_prime[p]) {
            for (int multiple = p * p; multiple <= n; multiple += p) {
                is_prime[multiple] = false;
            }
        }
    }

    vector<int> primes;
    for (int i = 2; i <= n; ++i) {
        if (is_prime[i]) {
            primes.push_back(i);
        }
    }

    return primes;
}

int main() {
    int n = 0;
    string input;

    cout << "Digite um numero inteiro N > 0: ";
    getline(cin, input);

    while (!parse_positive_integer(input, n)) {
        cout << "Entrada invalida. Informe um numero inteiro maior que 0: ";
        if (!getline(cin, input)) {
            cerr << "Erro de leitura da entrada." << endl;
            return 1;
        }
    }

    vector<int> primes = sieve_primes_up_to(n);

    cout << "N informado: " << n << endl;
    cout << "Primos encontrados: ";

    if (primes.empty()) {
        cout << "nenhum";
    } else {
        for (size_t i = 0; i < primes.size(); ++i) {
            if (i > 0) {
                cout << " - ";
            }
            cout << primes[i];
        }
    }

    cout << endl;
    cout << "Quantidade de primos: " << primes.size() << endl;

    return 0;
}
