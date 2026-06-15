# vllm-project/vllm#36094: [Bug]: Qwen3.5 NVFP4 Checkpoint has poor accuracy

| 字段 | 值 |
| --- | --- |
| Issue | [#36094](https://github.com/vllm-project/vllm/issues/36094) |
| 状态 | closed |
| 标签 | bug;qwen;nvidia |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;kernel;moe;operator;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 NVFP4 Checkpoint has poor accuracy

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug GSM8k of Qwen3.5 - NVFP4 checkpoint: nvidia/Qwen3.5-397B-A17B-NVFP4 --tensor-parallel-size 2 is around 0.11. The original checkpoint has 0.90 and the NVFP4 checkpoint must have similar scores. #35219 doesn't fix this issue and Low accuracy is observed for TRTION_ATTN, FLASHINFER with both Flashinfer native kernels and trtllm kernels. ``` vllm serve nvidia/Qwen3.5-397B-A17B-NVFP4 --tensor-parallel-size 2 python3 tests/evals/gsm8k/gsm8k_eval.py ``` Result: | Setup | Result | |-------|--------| | **Qwen/Qwen3.5-397B-A17B-FP8** (HuggingFace, FP8) | **Accuracy 0.901**, Invalid 0.002 (GSM8K) | | **nvidia/Qwen3.5-397B-A17B-NVFP4** (ModelOpt NVFP4) | Accuracy ~0.35, Invalid ~0.05–0.11 (GSM8K) | | NVFP4 + **--kv-cache-dtype=auto** | **Still fails**: Accuracy 0.354, Invalid 0.052 | Main differences: | Config | Working (Qwen/Qwen3.5-397B-A17B-FP8) | Failing (nvidia/Qwen3.5-397B-A17B-NVFP4) | |--------|--------------------------------------|------------------------------------------| | **model** | Qwen/Qwen3.5-397B-A17B-FP8 | nvidia/Qwen3.5-397B-A17B-NVFP4 | | **quantization** | fp8 | modelopt_fp4 | | **kv_cache_dtype** | auto | auto or fp8_...

## 现有链接修复摘要

#35219 [BUGFIX][Mamba][Qwen3.5] Zero freed SSM cache blocks on GPU

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Qwen3.5 NVFP4 Checkpoint has poor accuracy bug;qwen;nvidia ### Your current environment ### 🐛 Describe the bug GSM8k of Qwen3.5 - NVFP4 checkpoint: nvidia/Qwen3.5-397B-A17B-NVFP4 --tensor-parallel-size 2 is aroun...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3.5 NVFP4 Checkpoint has poor accuracy bug;qwen;nvidia ### Your current environment ### 🐛 Describe the bug GSM8k of Qwen3.5 - NVFP4 checkpoint: nvidia/Qwen3.5-397B-A17B-NVFP4 --tensor-parallel-size 2 is aroun...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Qwen3.5 NVFP4 Checkpoint has poor accuracy bug;qwen;nvidia ### Your current environment ### 🐛 Describe the bug GSM8k of Qwen3.5 - NVFP4 checkpoint: nvidia/Qwen3.5-397B-A17B-NVFP4 --tensor-parallel-size 2 is aroun...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 219 doesn't fix this issue and Low accuracy is observed for TRTION_ATTN, FLASHINFER with both Flashinfer native kernels and trtllm kernels. ``` vllm serve nvidia/Qwen3.5-397B-A17B-NVFP4 --tensor-parallel-size 2 python3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ug;qwen;nvidia ### Your current environment ### 🐛 Describe the bug GSM8k of Qwen3.5 - NVFP4 checkpoint: nvidia/Qwen3.5-397B-A17B-NVFP4 --tensor-parallel-size 2 is around 0.11. The original checkpoint has 0.90 and the NV...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35219](https://github.com/vllm-project/vllm/pull/35219) | mentioned | 0.45 | [BUGFIX][Mamba][Qwen3.5] Zero freed SSM cache blocks on GPU | heckpoint has 0.90 and the nvfp4 checkpoint must have similar scores. #35219 doesn't fix this issue and low accuracy is observed for trtion_attn, flashinfer with both flashinfer n… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
