import pandas as pd
import os

def run_preprocessing():
    print("전처리 프로세스 시작...")
    data = {'age': [65, 70, 75], 'grip_strength': [25, 20, 15]}
    df = pd.DataFrame(data)

    if not os.path.exists('data'):
        os.makedirs('data')
    
    df.to_csv('data/sample_processed.csv', index=False)
    print("✅ 전처리 완료! data/sample_processed.csv 저장됨.")

if __name__ == "__main__":
    run_preprocessing()