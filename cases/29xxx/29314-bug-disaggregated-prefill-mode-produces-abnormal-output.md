# vllm-project/vllm#29314: [Bug]: disaggregated_prefill mode produces abnormal output

| 字段 | 值 |
| --- | --- |
| Issue | [#29314](https://github.com/vllm-project/vllm/issues/29314) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: disaggregated_prefill mode produces abnormal output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The following is the disaggregated_prefill script, which runs on vLLM version 0.8.5.post1: ```bash run_vllm_server_fun() { #!/bin/bash # This file demonstrates the example usage of disaggregated prefilling # We will launch 2 vllm instances (1 for prefill and 1 for decode), # and then transfer the KV cache between them. set -xe echo "🚧🚧 Warning: The usage of disaggregated prefill is experimental and subject to change 🚧🚧" model_name=v1-ds-qwen2-32b-sft model_path=/path/ds-qwen2-32b host=0.0.0.0 port=10038 kv_producer_port=8100 kv_consumer_prot=8200 max_model_len=32768 # max_model_len=16384 gpu_memory_utilization=0.9 kv_producer_tp=4 kv_consumer_tp=4 # install quart first -- required for disagg prefill proxy serve if python3 -c "import quart" &> /dev/null; then echo "Quart is already installed." else echo "Quart is not installed. Installing..." python3 -m pip install quart fi # a function that waits vLLM server to start wait_for_server() { local port=$1 timeout 300 bash -c " until curl -s localhost:${port}/v1/completions > /dev/null; do sleep 1 done" && return 0 || return 1 } # You can also adjust --kv-ip and --kv-port for distribut...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: g The following is the disaggregated_prefill script, which runs on vLLM version 0.8.5.post1: ```bash run_vllm_server_fun() { #!/bin/bash # This file demonstrates the example usage of disaggregated prefilling # We will l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: disaggregated_prefill mode produces abnormal output bug;stale ### Your current environment ### 🐛 Describe the bug The following is the disaggregated_prefill script, which runs on vLLM version 0.8.5.post1: ```bash...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: uted inference. # prefilling instance, which is the KV producer CUDA_VISIBLE_DEVICES="0,1,2,3" vllm serve $model_path \ --served-model-name $model_name \ --host $host \ --port $kv_producer_port \ --max-model-len $max_mo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: uart" &> /dev/null; then echo "Quart is already installed." else echo "Quart is not installed. Installing..." python3 -m pip install quart fi # a function that waits vLLM server to start wait_for_server() { local port=$...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: of disaggregated prefill is experimental and subject to change 🚧🚧" model_name=v1-ds-qwen2-32b-sft model_path=/path/ds-qwen2-32b host=0.0.0.0 port=10038 kv_producer_port=8100 kv_consumer_prot=8200 max_model_len=32768 # m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
