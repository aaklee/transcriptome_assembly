#!/usr/bin/bash
#SBATCH --mail-user=lee02893@umn.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name=fastqc
#SBATCH --time=1:00:00
#SBATCH --partition=msismall
#SBATCH --ntasks=16
#SBATCH --mem=8g

source /home/yangya/lee02893/.bashrc
source activate transcriptome
cd /home/yangya/lee02893/sceletium
files=$(ls /home/yangya/lee02893/sceletium/data/reduced_data)
fastqc -t 16 ${files[@]}
