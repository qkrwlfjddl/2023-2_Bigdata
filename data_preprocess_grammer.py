import pandas as pd
from hanspell import spell_checker

def apply_spell_check(text):
    result = spell_checker.check(text)
    
    # 'checked' 속성 확인
    if hasattr(result, 'checked'):
        corrected_text = result.checked
        print(corrected_text)
        return corrected_text
    else:
        # 'checked' 속성이 없는 경우 처리
        print(f"Warning: 'checked' attribute not found in the response for text: {text}")
        return text


# 맞춤법 검사 후 csv 저장
def spell_check_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    text_column = '댓글 내용'  

    df[text_column] = df[text_column].apply(apply_spell_check)

    df.to_csv(output_csv, index=False, encoding='utf-8-sig')

if __name__ == "__main__":
    input_csv_file = "C:/Users/hyeee/Downloads/combined_fin_preprocessed.csv"
    output_csv_file = "C:/Users/hyeee/Desktop/reply2.csv"

    spell_check_csv(input_csv_file, output_csv_file)

    print(f"Spell checking completed. Result saved to {output_csv_file}")
