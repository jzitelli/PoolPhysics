#!/usr/bin/bash
project_root="${0%/*}/.."


echo '
building _collisions.so...
'
gfortran -shared -fPIC -static-libgfortran \
	 -ffree-line-length-none \
	 -v \
	 -o $project_root"/pool_physics/_collisions.so" \
	 $project_root"/pool_physics/collisions.f90"


echo '
building _poly_solvers.so...
'
gcc -shared -fPIC -o $project_root"/pool_physics/_poly_solvers.so" \
    -v \
    $project_root"/pool_physics/poly_solvers.c"


echo '
building _fpoly_solvers.so...
'
gfortran -shared -fPIC -static-libgfortran \
	 -ffree-line-length-none \
	 -v \
	 -o $project_root"/pool_physics/_fpoly_solvers.so" \
	 $project_root"/pool_physics/poly_solvers.f90"


rm *.mod
