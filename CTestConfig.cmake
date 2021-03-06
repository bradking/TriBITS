INCLUDE(SetDefaultAndFromEnv)

SET(CTEST_NIGHTLY_START_TIME "04:00:00 UTC") # 10 PM MDT or 9 PM MST

IF (NOT DEFINED CTEST_DROP_METHOD)
  SET_DEFAULT_AND_FROM_ENV(CTEST_DROP_METHOD "http")
ENDIF()

IF (CTEST_DROP_METHOD STREQUAL "http" OR CTEST_DROP_METHOD STREQUAL "https")
  SET_DEFAULT_AND_FROM_ENV(CTEST_DROP_SITE "testing.sandia.gov")
  SET_DEFAULT_AND_FROM_ENV(CTEST_PROJECT_NAME "TriBITS")
  SET_DEFAULT_AND_FROM_ENV(CTEST_DROP_LOCATION "/cdash/submit.php?project=TriBITS")
  SET_DEFAULT_AND_FROM_ENV(CTEST_TRIGGER_SITE "")
  SET_DEFAULT_AND_FROM_ENV(CTEST_DROP_SITE_CDASH TRUE)
ENDIF()
