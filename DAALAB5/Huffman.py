"""
Name: Raunak Thanawala
Experiment: Huffman Encoding
Batch: C
Registration Number: 231070051
"""
import heapq
import os
from collections import Counter
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
from docx import Document


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def calculate_compression_ratio(input_file, output_file):
    if os.path.exists(input_file) and os.path.exists(output_file):
        return (os.path.getsize(input_file) * 8) / os.path.getsize(output_file)
    return 0


def build_huffman_tree(text):
    frequency = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]  # Return the root of the tree


def generate_codes(root, code="", codebook=None):
    if codebook is None:
        codebook = {}
    if root is not None:
        if root.char is not None:
            codebook[root.char] = code
        generate_codes(root.left, code + "0", codebook)
        generate_codes(root.right, code + "1", codebook)
    return codebook


def encode_file(input_file, output_file, codebook):
    with open(input_file, 'r') as f:
        text = f.read()

    encoded_text = ''.join(codebook[char] for char in text)

    padding = 8 - len(encoded_text) % 8
    encoded_text = f"{padding:08b}" + encoded_text + '0' * padding
    byte_array = bytearray(int(encoded_text[i:i + 8], 2) for i in range(0, len(encoded_text), 8))

    with open(output_file, 'wb') as f:
        f.write(byte_array)

    return output_file


def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ''
    return text


def extract_text_from_html(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    return soup.get_text()


def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text


def read_file(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.html'):
        return extract_text_from_html(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        with open(file_path, 'r') as f:
            return f.read()
    else:
        raise ValueError("NOT PROPER FORMAT OF FILE")


def huffman_encoding(input_file, output_file):
    text = read_file(input_file)

    if not text.strip():
        raise ValueError("EMPTY FILE")

    huffman_tree = build_huffman_tree(text)
    codebook = generate_codes(huffman_tree)

    encode_file(input_file, output_file, codebook)

    compression_ratio = calculate_compression_ratio(input_file, output_file)

    return codebook, compression_ratio


if __name__ == "__main__":
    input_file = 'C:/Users/ASUS/Desktop/Coding/DAA/DAA LAB5/file5.txt'
    output_file = 'output.huff'

    codebook, compression_ratio = huffman_encoding(input_file, output_file)
    print("Huffman Codes for all characters:", codebook)
    print("Compression Ratio:", round(compression_ratio, 2))
