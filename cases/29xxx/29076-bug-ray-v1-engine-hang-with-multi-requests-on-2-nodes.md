# vllm-project/vllm#29076: [Bug][RAY]: V1 engine hang with multi-requests on 2 nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#29076](https://github.com/vllm-project/vllm/issues/29076) |
| 状态 | closed |
| 标签 | bug;rocm;stale;nvidia |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][RAY]: V1 engine hang with multi-requests on 2 nodes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running vLLM 0.11.0 inference on AMD Radeon Pro R9700 (navi48) across 2 nodes with 16 GPUs(PP=2, TP=8) total, the system works fine with low concurrency, but hang and eventually got **ray.exceptions.RayChannelTimeoutError** under higher load (e.g., 100 concurrent requests). command: ```python VLLM_WORKER_MULTIPROC_METHOD=spawn vllm serve /home/amd/model2/Qwen3-235B-A22B-Instruct-2507/ \ --block-size 16 \ --enable-chunked-prefill \ --max-num-batched-tokens 256 \ --max-num-seqs 64 \ --max-model-len 4096 \ --trust-remote-code \ -tp 8 -pp 2 \ --distributed-executor-backend ray \ --gpu-memory-utilization 0.95 ``` error: dmesg: It looks like a bug from ray. Is it a common bug for v1 on multi nodes? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug][RAY]: V1 engine hang with multi-requests on 2 nodes bug;rocm;stale;nvidia ### Your current environment ### 🐛 Describe the bug When running vLLM 0.11.0 inference on AMD Radeon Pro R9700 (navi48) across 2 nodes with...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug][RAY]: V1 engine hang with multi-requests on 2 nodes bug;rocm;stale;nvidia ### Your current environment ### 🐛 Describe the bug When running vLLM 0.11.0 inference on AMD Radeon Pro R9700 (navi48) across 2 nodes with...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: len 4096 \ --trust-remote-code \ -tp 8 -pp 2 \ --distributed-executor-backend ray \ --gpu-memory-utilization 0.95 ``` error: dmesg: It looks like a bug from ray. Is it a common bug for v1 on multi nodes? ### Before subm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: OD=spawn vllm serve /home/amd/model2/Qwen3-235B-A22B-Instruct-2507/ \ --block-size 16 \ --enable-chunked-prefill \ --max-num-batched-tokens 256 \ --max-num-seqs 64 \ --max-model-len 4096 \ --trust-remote-code \ -tp 8 -p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
