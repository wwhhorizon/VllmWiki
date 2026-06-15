# vllm-project/vllm#37159: [Bug]: vLLM crashed with V100 by running zai-org/GLM-OCR

| 字段 | 值 |
| --- | --- |
| Issue | [#37159](https://github.com/vllm-project/vllm/issues/37159) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;gemm;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM crashed with V100 by running zai-org/GLM-OCR

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Run ```sh !/bin/sh vllm serve zai-org/GLM-OCR \ --allowed-local-media-path / \ --speculative-config '{"method": "mtp", "num_speculative_tokens": 1}' \ --served-model-name glm-ocr \ --trust-remote-code \ --gpu-memory-utilization 0.90 \ --max-model-len 131072 \ --limit-mm-per-prompt '{"image": 1}' \ --tensor-parallel-size 1 ``` Crash ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#40768 [Bugfix][Scheduler] Fix CUDA crash caused by stale async placeholder tokens in speculative decoding

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: serve zai-org/GLM-OCR \ --allowed-local-media-path / \ --speculative-config '{"method": "mtp", "num_speculative_tokens": 1}' \ --served-model-name glm-ocr \ --trust-remote-code \ --gpu-memory-utilization 0.90 \ --max-mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;scheduler_memory;speculative_dec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: in/sh vllm serve zai-org/GLM-OCR \ --allowed-local-media-path / \ --speculative-config '{"method": "mtp", "num_speculative_tokens": 1}' \ --served-model-name glm-ocr \ --trust-remote-code \ --gpu-memory-utilization 0.90...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: l;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;scheduler_memory;speculative_decoding cache;cuda;gemm;kernel;operator;quantization;triton build_error;crash;mismatch;slowdown dtype;e...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40768](https://github.com/vllm-project/vllm/pull/40768) | closes_keyword | 0.95 | [Bugfix][Scheduler] Fix CUDA crash caused by stale async placeholder tokens in speculative decoding | Fixes #37159 ## Summary This PR fixes a **CUDA device-side assert (`vectorized_gather_kernel: ind >= 0`)** triggered by speculative decoding with async scheduling. The roo |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
