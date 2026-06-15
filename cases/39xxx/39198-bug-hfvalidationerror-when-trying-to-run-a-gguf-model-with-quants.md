# vllm-project/vllm#39198: [Bug]: HFValidationError when trying to run a GGUF model with quants

| 字段 | 值 |
| --- | --- |
| Issue | [#39198](https://github.com/vllm-project/vllm/issues/39198) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: HFValidationError when trying to run a GGUF model with quants

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running vllm in kubernetes. Trying to follow documentation here: https://docs.vllm.ai/en/stable/features/quantization/gguf/ to run this quant: https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF/blob/main/Qwen3.5-35B-A3B-UD-Q4_K_XL.gguf with this command: ``` vllm serve unsloth/Qwen3.5-35B-A3B-GGUF:UD-Q4_K_XL --api-key ${API_TOKEN} --port 8000 --enable-chunked-prefill --enable-expert-parallel --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3 --tokenizer Qwen/Qwen3.5-35B-A3B --max-model-len 16384 --max-num-seqs=1 --cpu-offload-gb 10 --gpu-memory-utilization 0.95 ``` Produces repo name validation error: ``` (APIServer pid=57) INFO 04-07 14:18:29 [utils.py:233] non-default args: {'model_tag': 'unsloth/Qwen3.5-35B-A3B-GGUF:UD-Q4_K_XL', 'enable_auto_tool_choice': True, 'tool_call_parser': 'qwen3_coder', 'api_key': ['heftyprice'], 'model': 'unsloth/Qwen3.5-35B-A3B-GGUF:UD-Q4_K_XL', 'tokenizer': 'Qwen/Qwen3.5-35B-A3B', 'max_model_len': 16384, 'reasoning_parser': 'qwen3', 'enable_expert_parallel': True, 'gpu_memory_utilization': 0.95, 'enable_prefix_caching': True, 'cpu_offload...

## 现有链接修复摘要

#39470 fix: handle vendor-prefixed GGUF quant types (e.g., UD-Q4_K_XL) | #39559 [Model] Add GGUF support for Qwen 3.5 dense and MoE models

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: HFValidationError when trying to run a GGUF model with quants bug ### Your current environment ### 🐛 Describe the bug I am running vllm in kubernetes. Trying to follow documentation here: https://docs.vllm.ai/en/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;m...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: --api-key ${API_TOKEN} --port 8000 --enable-chunked-prefill --enable-expert-parallel --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3 --tokenizer Qwen/Qwen3.5-35B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ID ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: -GGUF:UD-Q4_K_XL --api-key ${API_TOKEN} --port 8000 --enable-chunked-prefill --enable-expert-parallel --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3 --tokenizer...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39470](https://github.com/vllm-project/vllm/pull/39470) | closes_keyword | 0.95 | fix: handle vendor-prefixed GGUF quant types (e.g., UD-Q4_K_XL) | Fixes #39198 GGUF model publishers like Unsloth use vendor-prefixed quant type names (e.g., `UD-Q4_K_XL` for Unsloth Dynamic quantization). These were not recognized by `is_valid_ |
| [#39559](https://github.com/vllm-project/vllm/pull/39559) | closes_keyword | 0.95 | [Model] Add GGUF support for Qwen 3.5 dense and MoE models | Fixes: #39198, #36456, #38122 ## Test Plan ```bash # Qwen 3.5 Dense vllm serve unsloth/Qwen3.5-0.8B-GGUF:UD-IQ2_XXS --tokenizer Qwen/Qwen3.5-0.8B --hf-config-path Qwen/Qwen3. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
