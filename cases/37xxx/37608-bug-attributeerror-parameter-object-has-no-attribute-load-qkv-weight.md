# vllm-project/vllm#37608: [Bug]: AttributeError: 'Parameter' object has no attribute 'load_qkv_weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#37608](https://github.com/vllm-project/vllm/issues/37608) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Parameter' object has no attribute 'load_qkv_weight'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using weight reloading API to reload from BF16 -> FP8 with layerwise reloading, hitting ``` [rank0]: File "/home/matej/dev/devrl/scripts/fp8_weight_transfer_repro.py", line 117, in [rank0]: main() [rank0]: File "/home/matej/dev/devrl/scripts/fp8_weight_transfer_repro.py", line 108, in main [rank0]: model.load_weights(get_bf16_weights_iter(BF16_MODEL)) [rank0]: File "/home/matej/dev/devrl/.venv/lib/python3.12/site-packages/vllm/model_executor/models/qwen3_moe.py", line 797, in load_weights [rank0]: return loader.load_weights(weights) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/home/matej/dev/devrl/.venv/lib/python3.12/site-packages/vllm/model_executor/model_loader/reload/torchao_decorator.py", line 50, in patched_model_load_weights [rank0]: return original_load_weights(self, weights, *args, **kwargs) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/home/matej/dev/devrl/.venv/lib/python3.12/site-packages/vllm/model_executor/models/utils.py", line 340, in load_weights [rank0]: autoloaded_weights = set(self._load_module("", self.module, weights)) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: rl/scripts/fp8_weight_transfer_repro.py", line 108, in main [rank0]: model.load_weights(get_bf16_weights_iter(BF16_MODEL)) [rank0]: File "/home/matej/dev/devrl/.venv/lib/python3.12/site-packages/vllm/model_executor/mode...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e reload from BF16 weights into FP8 vLLM model fails. This directly exercises the same code path as prime-rl's NCCLWeightUpdateWorker with use_layerwise_reload=True, without needing the full engine: 1. Load FP8 Qwen3-30...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ### 🐛 Describe the bug When using weight reloading API to reload from BF16 -> FP8 with layerwise reloading, hitting ``` [rank0]: File "/home/matej/dev/devrl/scripts/fp8_weight_transfer_repro.py", line 117, in [rank0]: m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ht_iter) 5. finalize_layerwise_reload(model, model_config) Usage: CUDA_VISIBLE_DEVICES=0 HF_HOME=/shared/huggingface python fp8_weight_transfer_repro.py """ import json import os import torch os.environ.setdefault("CUDA...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: evrl/.venv/lib/python3.12/site-packages/vllm/model_executor/models/qwen3_moe.py", line 797, in load_weights [rank0]: return loader.load_weights(weights) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/home/matej/d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
