#!/bin/sh
set -eu

project_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
source_video=${1:-"$project_root/assets/videos/hero.mp4"}
output_video=${2:-"$project_root/assets/videos/hero-transparent.webm"}

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg is required" >&2
  exit 1
fi

ffmpeg \
  -hide_banner \
  -y \
  -i "$source_video" \
  -an \
  -filter_complex "[0:v]split=2[a][b];[a]chromakey=0xF7F5F6:0.060:0.060,format=rgba[upper];[b]format=rgba,colorkey=0xF7F5F6:0.105:0.075[lower];[upper][lower]blend=all_expr='if(lte(Y,480),A,if(gte(Y,650),B,A*(650-Y)/170+B*(Y-480)/170))',format=rgba[out]" \
  -map "[out]" \
  -c:v libvpx-vp9 \
  -pix_fmt yuva420p \
  -auto-alt-ref 0 \
  -b:v 0 \
  -crf 30 \
  -deadline good \
  -cpu-used 2 \
  "$output_video"
