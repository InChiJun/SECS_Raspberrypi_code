# SECS Project Raspberry Pi Code

SECS 프로젝트의 라즈베리 파이 센서 제어 코드 레포지토리입니다.<br/>

해당 레포지토리에서 Raspberry Pi의 DHT22 센서와 IR 센서를 이용해 쿨링 팬과 전구를 제어합니다.<br/>

main.py 모듈의 실행으로 모든 기능을 수행할 수 있습니다.<br/><br/>

### Database

MySQL Workbench의 SECS 스키마와 연결합니다. 센서 및 쿨링 팬과 전구 모델에 대한 Insert 함수가 정의되어 있습니다.<br/><br/>

### Set

**set_information** - 센서 및 장비의 name과 IR 센서의 인식 여부에 따른 상태 표시 문자열이 정의되어 있습니다. 또한 Database의 Insert 함수에서 사용되는 insert 쿼리문이 정의되어 있습니다.

**set_gpio** - 센서와 장비의 GPIO pin 번호와 GPIO 초기 설정이 정의되어 있습니다.<br/><br/>

### Time

현재 시간, 일, 월을 구하는 Time 클래스와 전구와 팬의 시작/종료 시간을 측정하기 위한 start, stop_time 함수가 정의되어 있습니다. 또한 시작/종료 시간을 토대로 작동 시간을 구하는 runtime 함수도 정의되어 있습니다.<br/><br/>

### IoT_Space / AIoT_Space

각 공간 별 센싱 값에 따라 쿨링 팬과 전구를 제어합니다. requests 모듈을 이용하여 Django 서버의 API 주소로 센싱 값을 전송합니다. 팬과 전구의 현재 상태를 받아오는 DeviceStatus 클래스를 통해 Insert 함수 및 작동 시간을 추출합니다.<br/><br/>

### Test

테스트 파일입니다. 프로젝트에 영향을 미치지 않습니다.
