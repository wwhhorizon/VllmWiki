# vllm-project/vllm#36228: [Bug]: Multiprocessing executor produces corrupted vision encoder outputs for Qwen3-VL in v0.12.0 (ray executor works correctly)

| 字段 | 值 |
| --- | --- |
| Issue | [#36228](https://github.com/vllm-project/vllm/issues/36228) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;model_support;multimodal_vlm |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Multiprocessing executor produces corrupted vision encoder outputs for Qwen3-VL in v0.12.0 (ray executor works correctly)

### Issue 正文摘录

### Your current environment - vLLM v0.12.0 - GPU: 4× NVIDIA A100 80GB, TP=4 - Model: Qwen3-VL-2B-Instruct - OS: Linux (container) ### Related Issue This is a root-cause analysis for #36117, where we reported a severe accuracy regression when upgrading from vLLM v0.11.0 to v0.12.0 for Qwen3-VL spatial reasoning tasks. ### Summary We identified that the **multiprocessing (`mp`) distributed executor backend** (default for single-node) produces corrupted vision encoder outputs in v0.12.0, while the **`ray` executor backend** works correctly. The `mp` backend was fine in v0.11.0, so this is a v0.12.0 regression. ### Reproduction ```bash # BROKEN: default mp backend (PointBench 12.3%, RefCOCO 19%, PixmoPointsEval 15%) vllm serve Qwen/Qwen3-VL-2B-Instruct --tensor-parallel-size 4 # FIXED: ray backend (PointBench 52.0%, RefCOCO 86%, PixmoPointsEval 51%) vllm serve Qwen/Qwen3-VL-2B-Instruct --tensor-parallel-size 4 --distributed-executor-backend ray ``` ### Full test matrix | Configuration | PointBench | RefCOCO_g_test | PixmoPointsEval | |---|---|---|---| | v0.11.0 (`mp`, default) | 52.0% | 86.0% | 50.0% | | v0.12.0 (`mp`, default) | 12.3% | 19.0% | 15.0% | | v0.12.0 + `--distributed-exe...

## 现有链接修复摘要

#28455 [Model][MM] Extract conv layer as CustomOp

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: ue This is a root-cause analysis for #36117, where we reported a severe accuracy regression when upgrading from vLLM v0.11.0 to v0.12.0 for Qwen3-VL spatial reasoning tasks. ### Summary We identified that the **multipro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: : Multiprocessing executor produces corrupted vision encoder outputs for Qwen3-VL in v0.12.0 (ray executor works correctly) ### Your current environment - vLLM v0.12.0 - GPU: 4× NVIDIA A100 80GB, TP=4 - Model: Qwen3-VL-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: sible GPU count and device properties, leading to different numerical precision paths under bf16/fp16. #### 2. `OMP_NUM_THREADS` / `torch.set_num_threads` ```python # multiproc_executor.py:862-888 def set_multiprocessin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: correctly) ### Your current environment - vLLM v0.12.0 - GPU: 4× NVIDIA A100 80GB, TP=4 - Model: Qwen3-VL-2B-Instruct - OS: Linux (container) ### Related Issue This is a root-cause analysis for #36117, where we reported...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ue This is a root-cause analysis for #36117, where we reported a severe accuracy regression when upgrading from vLLM v0.11.0 to v0.12.0 for Qwen3-VL spatial reasoning tasks. ### Summary We identified that the **multipro...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#28455](https://github.com/vllm-project/vllm/pull/28455) | mentioned | 0.45 | [Model][MM] Extract conv layer as CustomOp | s to the vision encoder path: 1. **`nn.conv3d` → `conv3dlayer`** (pr #28455): replaces `f.conv3d` with `unfold + f.linear` on pytorch ≥ 2.9. different floating-point accumulation… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
