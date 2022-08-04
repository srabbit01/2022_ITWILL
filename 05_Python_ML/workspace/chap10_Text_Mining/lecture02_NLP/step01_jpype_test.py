# -*- coding: utf-8 -*-
"""
- 단계1. JDK 서치
- 단계2. java 가상 머신 사용을 위한 패키지 다운로드 & 설치 
"""

import jpype

path=jpype.getDefaultJVMPath() # jpype 프로그램 설치 위치 확인
print(path)
# 'C:\\Program Files\\Java\\jre1.8.0_151\\bin\\server\\jvm.dll'

