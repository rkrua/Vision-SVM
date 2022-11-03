import urllib.parse
import urllib.request as req
import zipfile
import os.path

# 저장 경로 지정 및 다운로드 사이트 URL 지정, 다운 받을 파일 지정
savepath = "./vision"
baseurl = "https://nhiss.nhis.or.kr/down"
file = [
    "국가건강검진_시력_데이터.zip"
]

# 폴더생성
if not os.path.exists(savepath):
    os.mkdir(savepath)

# 한글로 된 파일 다운로드
url = baseurl + "/" + urllib.parse.quote(file[0])      # https://nhiss.nhis.or.kr/down/국가건강검진_시력데이터.zip
# parse.quote = unicode 오류나는 파일을 utf-8 형태로 읽어서 저장하는 것
loc = savepath + "/" + file[0]     # ./vision/"국가건강검진_시력_데이터.zip"
print(f"download: {url}")
if not os.path.exists(loc):
    req.urlretrieve(url, loc)

# 한글 파일로 읽어서 압축된 내용 다운하는 함수 만들기
def unzip(source_file, dest_path):    #source_file = 파일명 / dest_path = 저장할 경로
    with zipfile.ZipFile(source_file, 'r') as zf:
        for member in zf.infolist() :      # 압축 해제된 파일 크기만큼 반복
            try:
                # 한글로 형태 바꾸기
                # print(member.filename.encode('cp437').decode('euc-kr', 'ignore'))
                member.filename = member.filename.encode('cp437').decode('euc-kr', 'ignore')
                zf.extract(member, dest_path)
            except:
                print(source_file)
                raise Exception('what?!')

# zip파일 안 내용 다운로드
unzip('./vision/국가건강검진_시력_데이터.zip', './')