FROM node
RUN apt-get update && apt-get -y install python3
COPY status.py /
CMD bash -c "\
       python /status.py \
    && nodejs -e 'console.log(1+1)' \
    && python /status.py \
    && echo 'Now printing lots of data in Python causes an error:' \
    && python3 -c 'print(str(9)*100000)'"
