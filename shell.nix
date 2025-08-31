with import <nixpkgs> { };

mkShell {
  buildInputs = [ python3 stdenv.cc.cc.lib gcc zlib openssl ];

  shellHook = ''
    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [ pkgs.stdenv.cc.cc ]}
    export CFLAGS="-I${pkgs.zlib.dev}/include"
    export LDFLAGS="-L${pkgs.zlib.out}/lib"
  '';
}
