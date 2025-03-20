#include <openssl/evp.h>
#include <openssl/rand.h>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>

#include <fstream>
#include <iterator>

const int AES_KEYLEN = 32; // 256 бит
const int AES_IVLEN = 16;  // 128 бит

void randomBytes(std::vector<unsigned char>& cont){
    std::ifstream src("/dev/random", std::ios_base::in | std::ios_base::binary);

    std::copy_n(std::istreambuf_iterator<char>(src),
                cont.size(),
                cont.begin());
}

// Функция для шифрования данных
std::vector<unsigned char> encrypt(
        const std::vector<unsigned char>& plaintext,
        const std::vector<unsigned char> key) {
    if (key.size() != AES_KEYLEN){
        throw std::runtime_error("Ключ не корректный");
    }

    std::vector<unsigned char> iv(AES_IVLEN);
    randomBytes(iv);   // Генерация случайного IV

    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new(); // Создание структуры контекста шифрования
    EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), nullptr, key.data(), iv.data()); // Инициализация контекста для AES-256-CBC

    std::vector<unsigned char> ciphertext(AES_IVLEN + plaintext.size() + /*AES_BLOCK_SIZE*/ 16); // Выделение памяти под зашифрованные данные

    std::copy(iv.begin(), iv.begin() + AES_IVLEN, ciphertext.begin());

    int len;
    EVP_EncryptUpdate(ctx, ciphertext.data() + AES_IVLEN, &len, plaintext.data(), plaintext.size()); // Шифрование основной части данных
    int ciphertext_len = len;
    EVP_EncryptFinal_ex(ctx, ciphertext.data() + AES_IVLEN + len, &len); // Шифрование оставшихся данных и дополнение
    ciphertext_len += len;

    EVP_CIPHER_CTX_free(ctx); // Освобождение памяти контекста
    ciphertext.resize(ciphertext_len + AES_IVLEN); // Обрезка буфера до реального размера
    return ciphertext;
}

// Функция для расшифровки данных
std::vector<unsigned char> decrypt(
        const std::vector<unsigned char>& ciphertext,
        const std::vector<unsigned char>& key) {

    if (key.size() != AES_KEYLEN){
        throw std::runtime_error("Ключ не корректный");
    }

    if (ciphertext.size() <= AES_IVLEN){
        throw std::runtime_error("Шифр текст маленький");
    }
    unsigned char iv[AES_IVLEN];
    std::copy(ciphertext.begin(), ciphertext.begin() + AES_IVLEN, iv);

    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new(); // Создание структуры контекста расшифровки
    EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), nullptr, key.data(), iv); // Инициализация контекста для AES-256-CBC

    std::vector<unsigned char> plaintext(ciphertext.size()); // Выделение памяти под расшифрованные данные
    int len;
    EVP_DecryptUpdate(ctx, plaintext.data(), &len, ciphertext.data(), ciphertext.size()); // Расшифровка основной части данных
    int plaintext_len = len;
    EVP_DecryptFinal_ex(ctx, plaintext.data() + len, &len); // Расшифровка оставшихся данных
    plaintext_len += len;
    EVP_CIPHER_CTX_free(ctx); // Освобождение памяти контекста
    plaintext.resize(plaintext_len); // Обрезка буфера до реального размера

    plaintext.erase(plaintext.begin(), plaintext.begin() + AES_IVLEN);
    return plaintext;
}

int main() {
    std::vector<unsigned char> key(AES_KEYLEN);
    randomBytes(key);

    std::string text = "Plain text";
    std::vector<unsigned char> plaintext(text.begin(), text.end()); // Преобразование строки в вектор байтов

    try{
        std::vector<unsigned char> ciphertext = encrypt(plaintext, key); // Шифрование данных
        std::vector<unsigned char> decrypted = decrypt(ciphertext, key); // Расшифровка данных

        std::cout << "Decrypted text: " <<
                     std::string(decrypted.begin(), decrypted.end()) << std::endl; // Вывод расшифрованного текста
    }
    catch(const std::exception& error){
        std::cerr << error.what() << std::endl;
    }
    return 0;
}
