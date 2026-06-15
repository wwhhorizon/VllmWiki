# vllm-project/vllm#24980: [Bug]: Loading `spinquant` Model Fails Due to Hardware Capability Check and Weight Loading Errors

| 字段 | 值 |
| --- | --- |
| Issue | [#24980](https://github.com/vllm-project/vllm/issues/24980) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Loading `spinquant` Model Fails Due to Hardware Capability Check and Weight Loading Errors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### **Issue Report: Loading `spinquant` Model Fails Due to Hardware Capability Check and Weight Loading Errors** **Model:** [nm-testing/Llama-3.2-1B-Instruct-spinquantR1R2-online](https://huggingface.co/nm-testing/Llama-3.2-1B-Instruct-spinquantR1R2-online) (quantized using `llm-compressor`) **vLLM Version:** [v0.10.2] **GPU:** NVIDIA GeForce RTX 2080 Ti (Compute Capability 7.5) #### **1. Summary** When attempting to load the specified `spinquant` model, vLLM fails with two distinct errors. The first is a `RuntimeError` due to a strict compute capability check. The second, after bypassing the first check, is an `AssertionError` during the weight loading process. Through debugging, it was found that the model's quantization configuration leads vLLM to select the `CompressedTensorsWNA16` (AWQ) scheme, which has a hardcoded minimum compute capability of 8.0. Furthermore, the weight loading logic in `parameter.py` does not correctly handle the packed weight format used by this scheme, leading to shape mismatches. By applying targeted patches to `compressed_tensors.py` and `parameter.py`, the model can be successfully loaded and run o...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Loading `spinquant` Model Fails Due to Hardware Capability Check and Weight Loading Errors bug;stale ### Your current environment ### 🐛 Describe the bug ### **Issue Report: Loading `spinquant` Model Fails Due to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Loading `spinquant` Model Fails Due to Hardware Capability Check and Weight Loading Errors bug;stale ### Your current environment ### 🐛 Describe the bug ### **Issue Report: Loading `spinquant` Model Fails Due to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Instruct-spinquantR1R2-online) (quantized using `llm-compressor`) **vLLM Version:** [v0.10.2] **GPU:** NVIDIA GeForce RTX 2080 Ti (Compute Capability 7.5) #### **1. Summary** When attempting to load the specified `spinq...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: error: bool = True, match_exact: bool = False) -> bool: # --- START OF MODIFICATION --- return True # Forcibly bypass the capability check for testing purposes. # --- END OF MODIFICATION --- # Original code follows... `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: del Fails Due to Hardware Capability Check and Weight Loading Errors bug;stale ### Your current environment ### 🐛 Describe the bug ### **Issue Report: Loading `spinquant` Model Fails Due to Hardware Capability Check and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
