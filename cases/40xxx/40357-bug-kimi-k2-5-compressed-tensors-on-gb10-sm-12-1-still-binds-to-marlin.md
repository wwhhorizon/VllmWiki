# vllm-project/vllm#40357: [Bug]: Kimi-K2.5 compressed-tensors on GB10 / SM 12.1 still binds to Marlin under --moe-backend triton and degenerates into repeated tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#40357](https://github.com/vllm-project/vllm/issues/40357) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;quantization;triton |
| 症状 | mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi-K2.5 compressed-tensors on GB10 / SM 12.1 still binds to Marlin under --moe-backend triton and degenerates into repeated tokens

### Issue 正文摘录

### Your current environment # vLLM issue draft: Kimi-K2.5 compressed-tensors on GB10 / SM 12.1 still binds to Marlin and returns degenerate token repetition ## Summary `moonshotai/Kimi-K2.5` on a 16-node DGX Spark cluster with NVIDIA GB10 (`SM 12.1`) is not usable through public vLLM builds. On `vllm/vllm-openai:nightly`, a low-memory launch profile is stable enough to reach: - `/health = 200` - `/v1/models` returns `kimi-k2.5` But completions still collapse into degenerate token repetition: - `The capital of France is` -> `foss foss foss ...` Additionally, an explicit `--moe-backend triton` request reaches the `vllm serve` command line, but runtime still resolves the model path to Marlin: - `Using CompressedTensorsWNA16MarlinMoEMethod` - `Using Marlin backend for WNA16 MoE (group_size=32, num_bits=4)` This looks like either: - `compressed-tensors` Kimi path ignoring the requested MoE backend, or - Marlin WNA16 MoE producing numerically incorrect results on GB10 / SM 12.1. ## Hardware - 16x DGX Spark - GPU: `NVIDIA GB10` - Compute capability: `SM 12.1` ## Model - `moonshotai/Kimi-K2.5` - revision: `54383e83fa343a1331754112fb9e3410c55efa2f` - `compressed-tensors` - `pack-quantized...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: 54383e83fa343a1331754112fb9e3410c55efa2f` - `compressed-tensors` - `pack-quantized` - `group_size=32` - `num_bits=4` - `type=int` Model integrity was verified across all 16 nodes: - `64/64` shards present - safetensors...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: k cluster with NVIDIA GB10 (`SM 12.1`) is not usable through public vLLM builds. On `vllm/vllm-openai:nightly`, a low-memory launch profile is stable enough to reach: - `/health = 200` - `/v1/models` returns `kimi-k2.5`...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 5 compressed-tensors on GB10 / SM 12.1 still binds to Marlin under --moe-backend triton and degenerates into repeated tokens bug ### Your current environment # vLLM issue draft: Kimi-K2.5 compressed-tensors on GB10 / SM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Kimi-K2.5 compressed-tensors on GB10 / SM 12.1 still binds to Marlin under --moe-backend triton and degenerates into repeated tokens bug ### Your current environment # vLLM issue draft: Kimi-K2.5 compressed-tenso...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: path ignoring the requested MoE backend, or - Marlin WNA16 MoE producing numerically incorrect results on GB10 / SM 12.1. ## Hardware - 16x DGX Spark - GPU: `NVIDIA GB10` - Compute capability: `SM 12.1` ## Model - `moon...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
