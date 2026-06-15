# vllm-project/vllm#23144: [Bug]: Unexpected performance of Disaggregated Prefilling

| 字段 | 值 |
| --- | --- |
| Issue | [#23144](https://github.com/vllm-project/vllm/issues/23144) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unexpected performance of Disaggregated Prefilling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I ran the [disagg_performance_benchmark.sh](https://github.com/vllm-project/vllm/blob/main/benchmarks/disagg_benchmarks/disagg_prefill_proxy_server.py) provided in the vllm repository using vllm v0 (since the script only supports v0, see https://github.com/vllm-project/vllm/issues/22093) and Qwen3-8B. The performance of Disaggregated Prefilling (1P1D PD) seems to be worse than the one using chunked prefill (tp=2). I wonder if that's normal or there is some issue here. Code: (Can be found [here](https://github.com/vllm-project/vllm/blob/main/benchmarks/disagg_benchmarks/disagg_prefill_proxy_server.py). I only change the model, proxy port and the CUDA_VISIBLE_DEVICE) ```Python #!/bin/bash # Requirement: 2x GPUs. # Model: /workspace/models/Qwen3-8B # Query: 1024 input tokens, 6 output tokens, QPS 2/4/6/8, 100 requests # Resource: 2x GPU # Approaches: # 2. Chunked prefill: 2 vllm instance with tp=4, equivalent to 1 tp=4 instance with QPS 4 # 3. Disaggregated prefill: 1 prefilling instance and 1 decoding instance # Prefilling instance: max_output_token=1 # Decoding instance: force the input tokens be the same across requests to bypass...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: } main() { (which wget && which curl) || (apt-get update && apt-get install -y wget curl) (which jq) || (apt-get -y install jq) (which socat) || (apt-get -y install socat) (which lsof) || (apt-get -y install lsof) pip i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Unexpected performance of Disaggregated Prefilling bug;stale ### Your current environment ### 🐛 Describe the bug I ran the [disagg_performance_benchmark.sh](https://github.com/vllm-project/vllm/blob/main/benchmar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: supports v0, see https://github.com/vllm-project/vllm/issues/22093) and Qwen3-8B. The performance of Disaggregated Prefilling (1P1D PD) seems to be worse than the one using chunked prefill (tp=2). I wonder if that's nor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 50 input_len=1024 output_len=$2 tag=$3 vllm bench serve \ --backend vllm \ --model $model \ --dataset-name $dataset_name \ --dataset-path $dataset_path \ --sonnet-input-len $input_len \ --sonnet-output-len "$output_len"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: gg_prefill_proxy_server.py). I only change the model, proxy port and the CUDA_VISIBLE_DEVICE) ```Python #!/bin/bash # Requirement: 2x GPUs. # Model: /workspace/models/Qwen3-8B # Query: 1024 input tokens, 6 output tokens...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
