#!/usr/bin/bash
#SBATCH --mail-user=lee02893@umn.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name=fastqc
#SBATCH --time=1:00:00
#SBATCH --partition=msismall
#SBATCH --ntasks=16
#SBATCH --mem=8g

cd /home/yangya/lee02893/sceletium_nox
files=$(ls /home/yangya/lee02893/sceletium/data/reduced_data)
fastqc -t 16 ${files[@]}
