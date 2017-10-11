[DEPRECATED]


# sdx-downstream-cora

[![Build Status](https://travis-ci.org/ONSdigital/sdx-downstream-cora.svg?branch=develop)](https://travis-ci.org/ONSdigital/sdx-downstream-cora) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/89251a554b8141aea14cc28a28fac274)](https://www.codacy.com/app/ons-sdc/sdx-downstream-cora?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ONSdigital/sdx-downstream-cora&amp;utm_campaign=Badge_Grade) [![codecov](https://codecov.io/gh/ONSdigital/sdx-downstream-cora/branch/develop/graph/badge.svg)](https://codecov.io/gh/ONSdigital/sdx-downstream-cora)

SDX Downstream service for processing CORA destined survey data

## Getting started

### Pure python

It's recommended to use ``virtualenv``

If you are building in your local dev environment with a local version of sdx-common, run:

```shell
$ make dev
```

Otherwise, run:

```shell
$ make build
```

which pulls sdx-common from GitHub as a git submodule and installs it with `pip`.

To run tests, do:

```shell
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

Copyright (c) 2016 Crown Copyright (Office for National Statistics)

Released under MIT license, see [LICENSE](LICENSE) for details.
