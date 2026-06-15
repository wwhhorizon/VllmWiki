# vllm-project/vllm#33970: [Usage]: how to serve quantized Qwen3-Reranker-8B

| 字段 | 值 |
| --- | --- |
| Issue | [#33970](https://github.com/vllm-project/vllm/issues/33970) |
| 状态 | open |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | fp8;kernel;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: how to serve quantized Qwen3-Reranker-8B

### Issue 正文摘录

### Your current environment ```text GPU == NVIDIA RTX A5000 vLLM == vllm/vllm-openai:v0.14.0 ``` ### How would you like to use vllm (FYI, I am relatively new to this field.) I’m trying to run inference for a quantized [Qwen/Qwen3-Reranker-8B](https://huggingface.co/Qwen/Qwen3-Reranker-8B) using Docker, but I'm having trouble integrating it with vLLM. **What I’ve tried so far:** 1. Quantized the model to FP8 using `llm-compressor` (following [this example](https://github.com/vllm-project/llm-compressor/commit/00635f9c6d47f2181e591cf11bbb31d8218b4c36)). Then set --quantization compressed-tensors 2. Attempted in-flight quantization using `--quantization fp8` and `--quantization bitsandbytes`. 3. Set `VLLM_TEST_FORCE_FP8_MARLIN=1` since the documentation mentioned Marlin kernels support W8A16 on Ampere GPUs. **The Issue:** To run the Qwen3 reranker in vLLM, the following flags are mandatory [ref](https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/qwen3_reranker_online.py): ```bash --hf_overrides '{"architectures": ["Qwen3ForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' \ --runner pooling \ --chat-template examp...

## 现有链接修复摘要

#35849 [Bugfix] Fix score layer quantization for sequence classification models - Qwen3 (VL) Reranker

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: how to serve quantized Qwen3-Reranker-8B usage;stale ### Your current environment ```text GPU == NVIDIA RTX A5000 vLLM == vllm/vllm-openai:v0.14.0 ``` ### How would you like to use vllm (FYI, I am relatively ne...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /Qwen3-Reranker-8B](https://huggingface.co/Qwen/Qwen3-Reranker-8B) using Docker, but I'm having trouble integrating it with vLLM. **What I’ve tried so far:** 1. Quantized the model to FP8 using `llm-compressor` (followi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: how to serve quantized Qwen3-Reranker-8B usage;stale ### Your current environment ```text GPU == NVIDIA RTX A5000 vLLM == vllm/vllm-openai:v0.14.0 ``` ### How would you like to use vllm (FYI, I am relatively ne...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: anker-8B usage;stale ### Your current environment ```text GPU == NVIDIA RTX A5000 vLLM == vllm/vllm-openai:v0.14.0 ``` ### How would you like to use vllm (FYI, I am relatively new to this field.) I’m trying to run infer...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: reranker.jinja ``` (I also tried setting "is_original_qwen3_reranker": false when using a llm-compressor quantized model) However, combining these specific configurations with quantization seems to cause errors. Without...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35849](https://github.com/vllm-project/vllm/pull/35849) | mentioned | 0.6 | [Bugfix] Fix score layer quantization for sequence classification models  - Qwen3 (VL) Reranker | X PRO 6000 Blackwell (96 GB), vLLM 0.16.0, CUDA 13.0. Related Issue: #33970 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
