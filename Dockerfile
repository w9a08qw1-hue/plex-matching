# 이미 빌드된 Metatube 서버 이미지 사용
FROM ghcr.io/metatube/metatube-server:latest

# 포트 공개
EXPOSE 8080

# 환경 변수
ENV PLEX_TOKEN=${PLEX_TOKEN}
ENV CRON_UPDATE=${CRON_UPDATE}
ENV UPDATE_INTERVAL=${UPDATE_INTERVAL}

# 기본 실행 커맨드는 이미지에 포함되어 있음
