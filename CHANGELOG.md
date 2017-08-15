### Unreleased
 - Correctly handle error responses from dependent services
 - Integrate with sdc-rabbit library

### 1.3.0 2017-07-25
  - Change all instances of ADD to COPY in Dockerfile
  - Remove use of SDX_HOME variable in makefile

### 1.2.0 2017-07-10
  - Timestamp all logs as UTC
  - Add common library logging configurator
  - Log binary filename before delivery
  - Add environment variables to README
  - Add codacy badge
  - Correct license attribution
  - Correcting JSON parsing
  - Add support for codecov to see unit test coverage
  - Update and pin version of sdx-common to 0.7.0 

### 1.1.0 2017-03-15
  - Fix handling of None responses in remote call
  - Change `nack for retry` to `nack` for logging
  - Change `status_code` to `status` for logging
  - Log version number on startup

### 1.0.0 2017-02-16
  - Initial release
