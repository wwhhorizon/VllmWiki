# vllm-project/vllm#23600: [Bug]: (standard_in) 1: syntax error {"detail":"Not Found"}(standard_in) 1

| 字段 | 值 |
| --- | --- |
| Issue | [#23600](https://github.com/vllm-project/vllm/issues/23600) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: (standard_in) 1: syntax error {"detail":"Not Found"}(standard_in) 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash auto_tune_gpt.sh #!/bin/bash # This script aims to tune the best server parameter combinations to maximize throughput for given requirement. # See details in README (benchmarks/auto_tune/README.md). TAG=$(date +"%Y_%m_%d_%H_%M") SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd ) BASE="/data/service/benchmark/opt/vllm" MODEL="/data/model/pretrained/gpt-oss-120b" SYSTEM="GPU" TP=4 DOWNLOAD_DIR="/data/model/pretrained/gpt-oss-120b" INPUT_LEN=2000 OUTPUT_LEN=40 MAX_MODEL_LEN=4096 MIN_CACHE_HIT_PCT=60 MAX_LATENCY_ALLOWED_MS=5000 NUM_SEQS_LIST="4 8 16 32 64" NUM_BATCHED_TOKENS_LIST="512 1024 2048 4096" LOG_LEVEL="DEBUG" export CUDA_VISIBLE_DEVICES="0,1,2,3" export NCCL_DEBUG=INFO LOG_FOLDER="$BASE/auto-benchmark/$TAG" RESULT="$LOG_FOLDER/result.txt" PROFILE_PATH="$LOG_FOLDER/profile" echo "result file: $RESULT" echo "model: $MODEL" rm -rf $LOG_FOLDER rm -rf $PROFILE_PATH mkdir -p $LOG_FOLDER mkdir -p $PROFILE_PATH cd "$BASE/vllm" pip install -q datasets current_hash=$(git rev-parse HEAD) echo "hash:$current_hash" >> "$RESULT" echo "current_hash: $current_hash" TOTAL_LEN=$((INPUT_LEN + OUTPUT_LEN)) R...

## 现有链接修复摘要

#20988 [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: s script aims to tune the best server parameter combinations to maximize throughput for given requirement. # See details in README (benchmarks/auto_tune/README.md). TAG=$(date +"%Y_%m_%d_%H_%M") SCRIPT_DIR=$( cd -- "$(...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: E_PATH mkdir -p $LOG_FOLDER mkdir -p $PROFILE_PATH cd "$BASE/vllm" pip install -q datasets current_hash=$(git rev-parse HEAD) echo "hash:$current_hash" >> "$RESULT" echo "current_hash: $current_hash" TOTAL_LEN=$((INPUT_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: CE[0]}" )" &> /dev/null && pwd ) BASE="/data/service/benchmark/opt/vllm" MODEL="/data/model/pretrained/gpt-oss-120b" SYSTEM="GPU" TP=4 DOWNLOAD_DIR="/data/model/pretrained/gpt-oss-120b" INPUT_LEN=2000 OUTPUT_LEN=40 MAX_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: " NUM_BATCHED_TOKENS_LIST="512 1024 2048 4096" LOG_LEVEL="DEBUG" export CUDA_VISIBLE_DEVICES="0,1,2,3" export NCCL_DEBUG=INFO LOG_FOLDER="$BASE/auto-benchmark/$TAG" RESULT="$LOG_FOLDER/result.txt" PROFILE_PATH="$LOG_FOL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: hput=0 best_max_num_seqs=0 best_num_batched_tokens=0 best_goodput=0 best_request_rate=0 start_server() { local gpu_memory_utilization=$1 local max_num_seqs=$2 local max_num_batched_tokens=$3 local vllm_log=$4 local prof...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20988](https://github.com/vllm-project/vllm/pull/20988) | mentioned | 0.6 | [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | #23603: [Feature]: Log prompt for gpt-oss... [feature request] 17. #23600: [Bug]: (standard_in) 1: syntax error {"detail":"Not Found"}(... [bug] 18. #23594: [CI]: Host images used… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
