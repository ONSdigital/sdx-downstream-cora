# sdx-downstream-cora

[![Build Status](https://travis-ci.org/ONSdigital/sdx-downstream-cora.svg?branch=develop)](https://travis-ci.org/ONSdigital/sdx-downstream-cora) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/89251a554b8141aea14cc28a28fac274)](https://www.codacy.com/app/ons-sdc/sdx-downstream-cora?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ONSdigital/sdx-downstream-cora&amp;utm_campaign=Badge_Grade)

SDX Downstream service for processing CORA destined survey data

## Getting started

### Pure python

It's recommended to use ``virtualenv``

```shell
$ make
$ make test
```

### Docker

```shell
$ docker build -t sdx-transform-cora
```

## Configuration

The following envioronment variables can be set:

| Environment Variable    | Default                               | Description
|-------------------------|---------------------------------------|----------------
| SDX_STORE_URL           | `http://sdx-store:5000`               | The URL of the `sdx-store` service
| SDX_TRANSFORM_CORA_URL  | `http://sdx-transform-cora:5000`      | The URL of the `sdx-transform-cora` service
| SDX_SEQUENCE_URL        | `http://sdx-sequence:5000`            | The URL of the `sdx-sequence` service
| FTP_HOST                | `pure-ftpd`                           | FTP to monitor
| FTP_USER                | _none_                                | User for FTP account if required
| FTP_PASS                | _none_                                | Password for FTP account if required
| FTP_FOLDER              | `/`                                   | FTP folder
| FTP_HEARTBEAT_FOLDER    | `/heartbeat`                          | FTP heartbeat folder
| RABBIT_QUEUE            | `sdx-cora-survey-notifications`       | Rabbit queue name
| RABBIT_EXCHANGE         | `message`                             | RabbitMQ exchange to use

### License

Copyright © 2016, Office for National Statistics (https://www.ons.gov.uk)

Released under MIT license, see [LICENSE](LICENSE) for details.