import re

Input_FILE = str(input("파일 이름:")) + ".txt"
Output_FILE = "C" + Input_FILE +".txt"

def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?;|\)*~`!^\-_+<>@\#$%&\\\=◈\(\'\"◆★▷▶▲■◇△Δ○]', '', cleaned_text)
    cleaned_text = cleaned_text.replace("오류를 우회하기 위한 함수 추가", "")
    cleaned_text = cleaned_text.replace("동영상 뉴스 오류를 위한 함수 추가", "")
    cleaned_text = cleaned_text.replace("무단전재 및 재배포 금지", "")
    cleaned_text = cleaned_text.replace("  본문 내용     플레이어      플레이어              ", "")

    return cleaned_text

read_file = open(Input_FILE, 'r', encoding='utf-8')
write_file = open(Output_FILE,'wt', encoding='utf-8')

text = read_file.readline()
text = clean_text(text)
write_file.write(text)

read_file.close()
write_file.close()


