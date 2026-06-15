# vllm-project/vllm#28568: [Bug]: FlashInfer attention backend on Hopper fails with llama4-scout and llama3 with fp8 kvcache

| 字段 | 值 |
| --- | --- |
| Issue | [#28568](https://github.com/vllm-project/vllm/issues/28568) |
| 状态 | closed |
| 标签 | bug;stale;nvidia |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: FlashInfer attention backend on Hopper fails with llama4-scout and llama3 with fp8 kvcache

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Encountered when running tests in #27126 Commands: ``` # llama4 VLLM_ATTENTION_BACKEND=FLASHINFER python examples/offline_inference/basic/generate.py --model nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 --max_model_len=1024 --kv-cache-dtype=fp8 --tensor-parallel-size=2 # also llama3 VLLM_ATTENTION_BACKEND=FLASHINFER python examples/offline_inference/basic/generate.py --model=RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8 --kv-cache-dtype=fp8 # works VLLM_ATTENTION_BACKEND=FLASHINFER python examples/offline_inference/basic/generate.py --model=RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8 ``` [llama4-scout-flashinfer-hopper-error.txt.txt](https://github.com/user-attachments/files/23505053/llama4-scout-flashinfer-hopper-error.txt.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#27126 [compile] Enable sequence parallelism matching w/o custom ops enabled | #28966 Re-enable FlashInfer for Llama4 on Blackwell in e2e fusion tests

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_me...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: FlashInfer attention backend on Hopper fails with llama4-scout and llama3 with fp8 kvcache bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug Encountered when running tests in #27126 Commands: `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: FlashInfer attention backend on Hopper fails with llama4-scout and llama3 with fp8 kvcache bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug Encountered when running tests in #27126 Commands: `...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: FlashInfer attention backend on Hopper fails with llama4-scout and llama3 with fp8 kvcache bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug Encountered when running tests in #27126 Commands: ``
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nfer attention backend on Hopper fails with llama4-scout and llama3 with fp8 kvcache bug;stale;nvidia ### Your current environment ### 🐛 Describe the bug Encountered when running tests in #27126 Commands: ``` # llama4 V...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27126](https://github.com/vllm-project/vllm/pull/27126) | mentioned | 0.45 | [compile] Enable sequence parallelism matching w/o custom ops enabled  | /details> ### 🐛 describe the bug encountered when running tests in #27126 commands: ``` # llama4 vllm_attention_backend=flashinfer python examples/offline_inference/basic/generate… |
| [#28966](https://github.com/vllm-project/vllm/pull/28966) | closes_keyword | 0.95 | Re-enable FlashInfer for Llama4 on Blackwell in e2e fusion tests | fixed) - Changed Llama3 to use TRITON_ATTN consistently (removed conditional backend logic) - Preserved #28568 TODO (Hopper kvcache=fp8 issue still open) - Merged main: Brought in |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
