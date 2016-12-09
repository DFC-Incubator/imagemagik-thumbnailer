FROM alpine:3.3
MAINTAINER Mike Conway <michael_conway@unc.edu>

RUN apk --update add imagemagick && \
    rm -rf /var/cache/apk/*

RUN apk add --update bash && rm -rf /var/cache/apk/*


# Update
RUN apk add --update python py-pip

# Bundle app source
COPY ./make_thumbs_with_imagemagick.py /
COPY ./runit.sh /

ENTRYPOINT ["/runit.sh"]