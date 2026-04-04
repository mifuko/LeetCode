class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        result = []
        for c in range(cols):
            for r in range(rows):
                if r + c < cols:  # 同一条对角线
                    result.append(encodedText[r * cols + (c + r)])
        return ''.join(result).rstrip()