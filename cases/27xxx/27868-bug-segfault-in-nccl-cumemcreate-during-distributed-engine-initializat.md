# vllm-project/vllm#27868: [Bug]: Segfault in NCCL cuMemCreate during distributed engine initialization on 3080

| 字段 | 值 |
| --- | --- |
| Issue | [#27868](https://github.com/vllm-project/vllm/issues/27868) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Segfault in NCCL cuMemCreate during distributed engine initialization on 3080

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The vLLM1 PD disaggregated code that ran successfully on the V100 encountered errors when executed on the 3080. disaggregated_prefill_test.sh ``` set -xe echo "🚧🚧 Warning: The usage of disaggregated prefill is experimental and subject to change 🚧🚧" sleep 1 # meta-llama/Meta-Llama-3.1-8B-Instruct or deepseek-ai/DeepSeek-V2-Lite MODEL_NAME="/home/ljh1/models/meta-llama/Llama-3.2-1B-Instruct" # Trap the SIGINT signal (triggered by Ctrl+C) trap 'cleanup' INT # Cleanup function cleanup() { echo "Caught Ctrl+C, cleaning up..." # Cleanup commands pgrep python | xargs kill -9 pkill -f python echo "Cleanup complete. Exiting." exit 0 } export VLLM_HOST_IP=$(hostname -I | awk '{print $1}') # install quart first -- required for disagg prefill proxy serve if python3 -c "import quart" &> /dev/null; then echo "Quart is already installed." else echo "Quart is not installed. Installing..." python3 -m pip install quart fi # a function that waits vLLM server to start wait_for_server() { local port=$1 timeout 1200 bash -c " until curl -s localhost:${port}/v1/completions > /dev/null; do sleep 1 done" && return 0 || return 1 } # You can also adjust --...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: " exit 0 } export VLLM_HOST_IP=$(hostname -I | awk '{print $1}') # install quart first -- required for disagg prefill proxy serve if python3 -c "import quart" &> /dev/null; then echo "Quart is already installed." else e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: in NCCL cuMemCreate during distributed engine initialization on 3080 bug;stale ### Your current environment ### 🐛 Describe the bug The vLLM1 PD disaggregated code that ran successfully on the V100 encountered errors whe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: egated prefill is experimental and subject to change 🚧🚧" sleep 1 # meta-llama/Meta-Llama-3.1-8B-Instruct or deepseek-ai/DeepSeek-V2-Lite MODEL_NAME="/home/ljh1/models/meta-llama/Llama-3.2-1B-Instruct" # Trap the SIGINT...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 3 disagg_prefill_proxy_server.py & CUDA_VISIBLE_DEVICES=0 VLLM_ATTENTION_BACKEND=FLEX_ATTENTION vllm serve $MODEL_NAME \ --port 8100 \ --max-model-len 100 \ --gpu-memory-utilization 0.8 \ --disable-hybrid-kv-cache-manag...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tance, which is the KV producer python3 disagg_prefill_proxy_server.py & CUDA_VISIBLE_DEVICES=0 VLLM_ATTENTION_BACKEND=FLEX_ATTENTION vllm serve $MODEL_NAME \ --port 8100 \ --max-model-len 100 \ --gpu-memory-utilization...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
