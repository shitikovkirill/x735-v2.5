{ lib, python3Packages }:
with python3Packages;
buildPythonApplication {
  pname = "x735-v2.5";
  version = "1.0";

  propagatedBuildInputs = [ rpi-gpio click pigpio ];

  src = ./.;
}
