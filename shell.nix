{ pkgs ? import <nixpkgs> {} }:

with pkgs;

mkShell {
  buildInputs = [ (python3.withPackages (python-pkgs: [ python-pkgs.rpi-gpio python-pkgs.click python-pkgs.pigpio ])) ];
}
