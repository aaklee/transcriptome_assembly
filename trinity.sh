#!/usr/bin/bash
#SBATCH --mail-user=lee02893@umn.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name=trinity
#SBATCH --time=1-00:00:00
#SBATCH --partition=msismall
#SBATCH --ntasks=16
#SBATCH --mem=200g
source /home/yangya/lee02893/.bashrc
source activate transcriptome
cd /home/yangya/lee02893/sceletium_nox
Trinity --seqType fq --max_memory 200G --CPU 16 --verbose --left Sceletium_bt2_unaligned_1.fastq --right Sceletium_bt2_unaligned_2.fastq --output trinity_Sceletium_nova --full_cleanup