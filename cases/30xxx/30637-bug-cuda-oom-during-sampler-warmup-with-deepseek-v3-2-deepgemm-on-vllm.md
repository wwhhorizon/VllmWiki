# vllm-project/vllm#30637: [Bug]: CUDA OOM during sampler warmup with DeepSeek-V3.2 (DeepGEMM) on vLLM Nightly (V1 Engine)

| 字段 | 值 |
| --- | --- |
| Issue | [#30637](https://github.com/vllm-project/vllm/issues/30637) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA OOM during sampler warmup with DeepSeek-V3.2 (DeepGEMM) on vLLM Nightly (V1 Engine)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to serve deepseek-ai/DeepSeek-V3.2 using the latest vLLM nightly build and DeepGEMM. The model loads successfully, and DeepGEMM E8M0 is enabled. However, the server crashes with a CUDA out of memory error during the sampler warmup phase (_dummy_sampler_run), specifically when performing logits.sort. I followed the instructions in the [DeepSeek-V3.2 recipe](https://github.com/vllm-project/recipes/blob/main/DeepSeek/DeepSeek-V3_2.md#installing-vllm), but it fails on the latest nightly version. ```shell vllm serve deepseek-ai/DeepSeek-V3.2 \ --tensor-parallel-size 8 \ --gpu-memory-utilization 0.85 \ --tool-call-parser deepseek_v32 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v3 ``` Log Output ```txt (APIServer pid=1594496) INFO 12-14 15:35:25 [api_server.py:1351] vLLM API server version 0.13.0rc2.dev118+g29f7d9771 ... (EngineCore_DP0 pid=1594645) INFO 12-14 15:35:48 [core.py:93] Initializing a V1 LLM engine ... ... (Worker_TP0 pid=1594712) INFO 12-14 15:37:38 [deep_gemm.py:76] DeepGEMM E8M0 enabled on current platform. ... (Worker_TP2 pid=1594714) ERROR 12-14 15:40:59 [multiproc_executor.py:824] File "/home/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: trying to serve deepseek-ai/DeepSeek-V3.2 using the latest vLLM nightly build and DeepGEMM. The model loads successfully, and DeepGEMM E8M0 is enabled. However, the server crashes with a CUDA out of memory error during...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: CUDA OOM during sampler warmup with DeepSeek-V3.2 (DeepGEMM) on vLLM Nightly (V1 Engine) bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to serve deepseek-ai/DeepSeek-V3.2 using the late...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: CUDA OOM during sampler warmup with DeepSeek-V3.2 (DeepGEMM) on vLLM Nightly (V1 Engine) bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to serve deepseek-ai/DeepSeek-V3.2 using the late...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: CUDA OOM during sampler warmup with DeepSeek-V3.2 (DeepGEMM) on vLLM Nightly (V1 Engine) bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to serve deepseek-ai/DeepSeek-V3.2 using the late...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ler warmup with DeepSeek-V3.2 (DeepGEMM) on vLLM Nightly (V1 Engine) bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to serve deepseek-ai/DeepSeek-V3.2 using the latest vLLM nightly build and D...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
