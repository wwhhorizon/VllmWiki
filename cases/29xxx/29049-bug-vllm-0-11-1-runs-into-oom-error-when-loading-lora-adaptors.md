# vllm-project/vllm#29049: [Bug]: vLLM 0.11.1 runs into OOM error when loading lora adaptors.

| 字段 | 值 |
| --- | --- |
| Issue | [#29049](https://github.com/vllm-project/vllm/issues/29049) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.11.1 runs into OOM error when loading lora adaptors.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Deploying vllm with meta-llama/Llama-3.1-8B-Instruct with lora adaptors on an h100 GPU fails with OOM errors when using v0.11.1 version. This deploys smoothly with the same configs on the same node if used with v0.11.0. If not using lora adaptors does not hit an issue. From my reading of the logs (pasted below). vLLM allocates to much memory to the kv cache and runs out of memory when initializing details related to the lora adaptors. ```bash apiVersion: apps/v1 kind: Deployment metadata: name: vllm-llama3-8b-instruct spec: replicas: 1 selector: matchLabels: app: vllm-llama3-8b-instruct template: metadata: labels: app: vllm-llama3-8b-instruct spec: containers: - name: vllm image: "vllm/vllm-openai:v0.11.1" imagePullPolicy: Always command: ["sh", "-c"] args: - >- PATH=$PATH:/usr/local/nvidia/bin LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/nvidia/lib:/usr/local/nvidia/lib64 python3 -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 1 --port 8000 --enable-lora --max-loras 2 --max-cpu-loras 12 env: - name: VLLM_USE_V1 value: "1" - name: PORT value: "8000" - name: VLLM_LOGGING_LEVEL v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: th lora adaptors on an h100 GPU fails with OOM errors when using v0.11.1 version. This deploys smoothly with the same configs on the same node if used with v0.11.0. If not using lora adaptors does not hit an issue. From...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vLLM 0.11.1 runs into OOM error when loading lora adaptors. bug;stale ### Your current environment ### 🐛 Describe the bug Deploying vllm with meta-llama/Llama-3.1-8B-Instruct with lora adaptors on an h100 GPU fai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ying vllm with meta-llama/Llama-3.1-8B-Instruct with lora adaptors on an h100 GPU fails with OOM errors when using v0.11.1 version. This deploys smoothly with the same configs on the same node if used with v0.11.0. If n...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: vLLM 0.11.1 runs into OOM error when loading lora adaptors. bug;stale ### Your current environment ### 🐛 Describe the bug Deploying vllm with meta-llama/Llama-3.1-8B-Instruct with lora adaptors on an h100 GPU fai...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ted to the lora adaptors. ```bash apiVersion: apps/v1 kind: Deployment metadata: name: vllm-llama3-8b-instruct spec: replicas: 1 selector: matchLabels: app: vllm-llama3-8b-instruct template: metadata: labels: app: vllm-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
