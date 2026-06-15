# vllm-project/vllm#34242: [Bug]:  Failed to apply Glm46VProcessor on data

| 字段 | 值 |
| --- | --- |
| Issue | [#34242](https://github.com/vllm-project/vllm/issues/34242) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Failed to apply Glm46VProcessor on data

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python import os from PIL import Image from vllm import LLM, SamplingParams os.environ["VLLM_USE_V1"] = "1" llm = LLM( model="zai-org/GLM-OCR", trust_remote_code=True, gpu_memory_utilization=0.85, max_model_len=2048, enforce_eager=False, kv_cache_dtype="auto", tensor_parallel_size=1, ) img = Image.open(img_path).convert("RGB") sampling_params = SamplingParams(max_tokens=2048, temperature=0.0) vllm_input = {"prompt": "Text Recognition:", "multi_modal_data": {"image": img}} outputs = model.generate([vllm_input], sampling_params=sampling_params) ``` Raises: ``` ValueError: Failed to apply Glm46VProcessor on data={'text': ' ', 'images': [ ]} with kwargs={'truncation': True, 'max_length': 2049, 'add_special_tokens': True} 2026-02-10 13:23:15 - worker_worker_1 - ERROR - Error processing page 1: Failed to apply Glm46VProcessor on data={'text': ' ', 'images': [ ]} with kwargs={'truncation': True, 'max_length': 2049, 'add_special_tokens': True} ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://doc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: a bug ### Your current environment ### 🐛 Describe the bug ```python import os from PIL import Image from vllm import LLM, SamplingParams os.environ["VLLM_USE_V1"] = "1" llm = LLM( model="zai-org/GLM-OCR", trust_remote_c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: tion=0.85, max_model_len=2048, enforce_eager=False, kv_cache_dtype="auto", tensor_parallel_size=1, ) img = Image.open(img_path).convert("RGB") sampling_params = SamplingParams(max_tokens=2048, temperature=0.0) vllm_inpu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: gpu_memory_utilization=0.85, max_model_len=2048, enforce_eager=False, kv_cache_dtype="auto", tensor_parallel_size=1, ) img = Image.open(img_path).convert("RGB") sampling_params = SamplingParams(max_tokens=2048, temperat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
