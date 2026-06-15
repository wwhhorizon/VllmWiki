# vllm-project/vllm#37804: [Bug] DeepGemm E8M0 scale format causes accuracy degradation for Qwen3.5 FP8 on Blackwell

| 字段 | 值 |
| --- | --- |
| Issue | [#37804](https://github.com/vllm-project/vllm/issues/37804) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;quantization |
| 症状 |  |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] DeepGemm E8M0 scale format causes accuracy degradation for Qwen3.5 FP8 on Blackwell

### Issue 正文摘录

## Summary `Qwen/Qwen3.5-35B-A3B-FP8` fails the GSM8K accuracy CI check on Blackwell (B200) GPUs. Investigation in [#37618](https://github.com/vllm-project/vllm/issues/37618) identified the root cause as DeepGemm's E8M0 scale format on the dense FP8 block-quantized linear layers. ## Environment - **GPU:** NVIDIA B200 (Blackwell, SM100+) - **Model:** `Qwen/Qwen3.5-35B-A3B-FP8` (FP8 block-quantized MoE, `weight_block_size [128, 128]`) - **vLLM version:** 0.18.1rc1.dev18 - **CI config:** `Qwen3.5-35B-A3B-FP8-DEP2.yaml` (`--kv-cache-dtype fp8 --data-parallel-size 2 --enable-expert-parallel --max-model-len 4096`, accuracy threshold 0.86) ## Reproduction ```bash # Start server (Blackwell GPU) vllm serve Qwen/Qwen3.5-35B-A3B-FP8 \ --tensor-parallel-size 4 --max-model-len 4096 --kv-cache-dtype fp8 --port 8000 # Run GSM8K eval python3 tests/evals/gsm8k/gsm8k_eval.py --port 8000 # Accuracy: ~0.73 (FAIL, threshold is 0.78) ``` Disabling DeepGemm restores accuracy: ```bash VLLM_USE_DEEP_GEMM=0 vllm serve Qwen/Qwen3.5-35B-A3B-FP8 \ --tensor-parallel-size 4 --max-model-len 4096 --kv-cache-dtype fp8 --port 8000 # Accuracy: ~0.79 (PASS) ``` ## Root Cause On Blackwell (SM100+), DeepGemm **requires...

## 现有链接修复摘要

#37806 [Bugfix] Auto-disable DeepGemm for Qwen3.5 on Blackwell to fix FP8 accuracy degradation | #38083 [Bugfix] Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug] DeepGemm E8M0 scale format causes accuracy degradation for Qwen3.5 FP8 on Blackwell bug ## Summary `Qwen/Qwen3.5-35B-A3B-FP8` fails the GSM8K accuracy CI check on Blackwell (B200) GPUs. Investigation in [#37618](h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: eepGemm E8M0 scale format causes accuracy degradation for Qwen3.5 FP8 on Blackwell bug ## Summary `Qwen/Qwen3.5-35B-A3B-FP8` fails the GSM8K accuracy CI check on Blackwell (B200) GPUs. Investigation in [#37618](https://...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug] DeepGemm E8M0 scale format causes accuracy degradation for Qwen3.5 FP8 on Blackwell bug ## Summary `Qwen/Qwen3.5-35B-A3B-FP8` fails the GSM8K accuracy CI check on Blackwell (B200) GPUs. Investigation in [#37618](h...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: well bug ## Summary `Qwen/Qwen3.5-35B-A3B-FP8` fails the GSM8K accuracy CI check on Blackwell (B200) GPUs. Investigation in [#37618](https://github.com/vllm-project/vllm/issues/37618) identified the root cause as DeepGe...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug] DeepGemm E8M0 scale format causes accuracy degradation for Qwen3.5 FP8 on Blackwell bug ## Summary `Qwen/Qwen3.5-35B-A3B-FP8` fails the GSM8K accuracy CI check on Blackwell (B200) GPUs. Investigation in [#37618](h...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37806](https://github.com/vllm-project/vllm/pull/37806) | closes_keyword | 0.95 | [Bugfix] Auto-disable DeepGemm for Qwen3.5 on Blackwell to fix FP8 accuracy degradation | fix FP8 accuracy degradation ## Problem **Issue:** [#37804](https://github.com/vllm-project/vllm/issues/37804) (root cause identified in [#37618](https://github.com/vllm-project |
| [#38083](https://github.com/vllm-project/vllm/pull/38083) | closes_keyword | 0.95 | [Bugfix] Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell | Fixes #37804 — `Qwen/Qwen3.5-35B-A3B-FP8` accuracy drops ~12pp on Blackwell (B200) when DeepGemm is active. DeepGemm's mandatory E8M0 (power-of-2 ceiling) scale format loses precis |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
