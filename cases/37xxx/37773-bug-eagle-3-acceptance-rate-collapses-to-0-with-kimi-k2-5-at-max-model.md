# vllm-project/vllm#37773: [Bug]: EAGLE-3 acceptance rate collapses to 0% with Kimi-K2.5 at max_model_len=262144

| 字段 | 值 |
| --- | --- |
| Issue | [#37773](https://github.com/vllm-project/vllm/issues/37773) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;moe;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;gemm;moe |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EAGLE-3 acceptance rate collapses to 0% with Kimi-K2.5 at max_model_len=262144

### Issue 正文摘录

### Your current environment - vLLM v0.18.0 (release, not nightly) - 8x NVIDIA B200 (141 GB HBM each) - Model: `moonshotai/Kimi-K2.5` (1T MoE, 32B active, compressed-tensors 4-bit) - CUDA 13.0, Driver 580.126.09 ### 🐛 Describe the bug EAGLE-3 speculative decoding acceptance rate progressively collapses to 0% during generation when `--max-model-len 262144`. This causes the model to produce repetitive/degenerate output until `max_tokens` is hit. The bug is **100% reproducible** and occurs within seconds of starting generation — even on small prompts (~100 tokens). **Critical detail**: The same model + EAGLE-3 head works perfectly at `--max-model-len 32768`, achieving 36.5% overall acceptance and +43% throughput improvement. The bug only manifests at 262K. ### What we tested We systematically tested every combination we could think of: | Config | Draft Head | `num_speculative_tokens` | Draft `max_model_len` | Result | |--------|-----------|-------------------------|----------------------|--------| | A | `nvidia/Kimi-K2.5-Thinking-Eagle3` | 3 | inherited (262K) | ❌ 0% collapse | | B | `lightseekorg/kimi-k2.5-eagle3` | 3 | inherited (262K) | ❌ 0% collapse | | C | `lightseekorg/kimi-k2....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: EAGLE-3 acceptance rate collapses to 0% with Kimi-K2.5 at max_model_len=262144 ### Your current environment - vLLM v0.18.0 (release, not nightly) - 8x NVIDIA B200 (141 GB HBM each) - Model: `moonshotai/Kimi-K2.5`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: r current environment - vLLM v0.18.0 (release, not nightly) - 8x NVIDIA B200 (141 GB HBM each) - Model: `moonshotai/Kimi-K2.5` (1T MoE, 32B active, compressed-tensors 4-bit) - CUDA 13.0, Driver 580.126.09 ### 🐛 Describe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 44 \ --max-num-batched-tokens 32768 \ --max-num-seqs 512 \ --dtype bfloat16 \ --gpu-memory-utilization 0.9 \ --enable-chunked-prefill \ --trust-remote-code \ --enable-prefix-caching \ --enable-expert-parallel \ --compil...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ) - 8x NVIDIA B200 (141 GB HBM each) - Model: `moonshotai/Kimi-K2.5` (1T MoE, 32B active, compressed-tensors 4-bit) - CUDA 13.0, Driver 580.126.09 ### 🐛 Describe the bug EAGLE-3 speculative decoding acceptance rate prog...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: s 4-bit) - CUDA 13.0, Driver 580.126.09 ### 🐛 Describe the bug EAGLE-3 speculative decoding acceptance rate progressively collapses to 0% during generation when `--max-model-len 262144`. This causes the model to produce...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
