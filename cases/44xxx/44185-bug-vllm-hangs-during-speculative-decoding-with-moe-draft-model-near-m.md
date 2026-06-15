# vllm-project/vllm#44185: [Bug]: vLLM hangs during speculative decoding with MoE draft model near max_model_len under Data Parallelism (DP)

| 字段 | 值 |
| --- | --- |
| Issue | [#44185](https://github.com/vllm-project/vllm/issues/44185) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;kernel;moe;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM hangs during speculative decoding with MoE draft model near max_model_len under Data Parallelism (DP)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug #### **Bug Description:** When running vLLM with Speculative Decoding enabled, the server permanently hangs (deadlocks) under the following specific conditions: 1. Data Parallelism (DP) is enabled (e.g., pipeline parallelism or tensor parallelism combined with DP across multiple nodes/GPUs, or multi-instance serving via vLLM's internal scheduling). 2. Draft Model is a MoE (Mixture of Experts) architecture (e.g., Qwen3.5-35B-A3B). 3. Boundary Condition: The total length of the request (prompt_len + max_tokens) is extremely close to or reaches the max_model_len. #### **Steps to Reproduce:** 1. Launch vLLM server with: ```shell export NCCL_P2P_DISABLE=1 export NCCL_NET_DISABLE_INTRA=1 export NCCL_IB_GID_INDEX=1 export NCCL_IB_DISABLE=0 export NCCL_NET_GDR_LEVEL=3 vllm serve /home/weight/Qwen3.5-35B-A3B/ \ --max-model-len 2048 \ --max-num-batched-tokens 256 \ --trust-remote-code \ --enable-expert-parallel \ --data-parallel-size 2 \ --speculative_config '{"method":"mtp", "num_speculative_tokens":3}' \ --enforce-eager \ 2>&1 | tee output.log ``` 2. Send a specific hang request: ```json { "model": "", "messages": [ { "role": "user", "co...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: vLLM hangs during speculative decoding with MoE draft model near max_model_len under Data Parallelism (DP) bug ### Your current environment ### 🐛 Describe the bug #### **Bug Description:** When running vLLM with...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: enabled, the server permanently hangs (deadlocks) under the following specific conditions: 1. Data Parallelism (DP) is enabled (e.g., pipeline parallelism or tensor parallelism combined with DP across multiple nodes/GPU...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: vLLM hangs during speculative decoding with MoE draft model near max_model_len under Data Parallelism (DP) bug ### Your current environment ### 🐛 Describe the bug #### **Bug Description:** When running vLLM with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ive decoding with MoE draft model near max_model_len under Data Parallelism (DP) bug ### Your current environment ### 🐛 Describe the bug #### **Bug Description:** When running vLLM with Speculative Decoding enabled, the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: } ], "max_tokens": 1043, "seed": 1, "stream": false, "ignore_eos": true } ``` Save it to a json file `hang_request.json`. ```shell curl -X POST http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/j...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
