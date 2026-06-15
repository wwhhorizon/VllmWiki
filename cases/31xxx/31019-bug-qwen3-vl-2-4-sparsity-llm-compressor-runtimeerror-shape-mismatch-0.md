# vllm-project/vllm#31019: [Bug]: Qwen3-VL 2:4 sparsity llm-compressor RuntimeError: shape mismatch (0.12, 0.13rc2)

| 字段 | 值 |
| --- | --- |
| Issue | [#31019](https://github.com/vllm-project/vllm/issues/31019) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL 2:4 sparsity llm-compressor RuntimeError: shape mismatch (0.12, 0.13rc2)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Qwen3-VL 2:4 sparsity compressed with llm-compressor 0.8.1 or 0.9.0 cannot be loaded with vLLM 0.12.0 and 0.13rc2 (did not try any other versions). Both the FP8 and bfloat16 models cannot load. The models were creating following llm-compressor's documentation [https://github.com/vllm-project/llm-compressor/blob/main/examples/sparse_2of4_quantization_fp8/llama3_8b_2of4.py](https://github.com/vllm-project/llm-compressor/blob/main/examples/sparse_2of4_quantization_fp8/llama3_8b_2of4.py) ```python from datasets import load_dataset from qwen_vl_utils import process_vision_info from transformers import AutoProcessor, Qwen3VLForConditionalGeneration from llmcompressor import oneshot from llmcompressor.modifiers.quantization import QuantizationModifier from llmcompressor.modifiers.pruning import SparseGPTModifier from llmcompressor.utils import dispatch_for_generation model_id = "Qwen/Qwen3-VL-2B-Instruct" model = Qwen3VLForConditionalGeneration.from_pretrained(model_id, torch_dtype="auto") processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True) DATASET_ID = "HuggingFaceH4/ultrachat_200k" DATASET_SPLIT = "train_sft" N...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 9.0 cannot be loaded with vLLM 0.12.0 and 0.13rc2 (did not try any other versions). Both the FP8 and bfloat16 models cannot load. The models were creating following llm-compressor's documentation [https://github.com/vll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: h vLLM 0.12.0 and 0.13rc2 (did not try any other versions). Both the FP8 and bfloat16 models cannot load. The models were creating following llm-compressor's documentation [https://github.com/vllm-project/llm-compressor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL 2:4 sparsity llm-compressor RuntimeError: shape mismatch (0.12, 0.13rc2) bug;help wanted;good first issue;stale ### Your current environment ### 🐛 Describe the bug Qwen3-VL 2:4 sparsity compressed with l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3-VL 2:4 sparsity llm-compressor RuntimeError: shape mismatch (0.12, 0.13rc2) bug;help wanted;good first issue;stale ### Your current environment ### 🐛 Describe the bug Qwen3-VL 2:4 sparsity compressed with l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ifiers.pruning import SparseGPTModifier from llmcompressor.utils import dispatch_for_generation model_id = "Qwen/Qwen3-VL-2B-Instruct" model = Qwen3VLForConditionalGeneration.from_pretrained(model_id, torch_dtype="auto"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
