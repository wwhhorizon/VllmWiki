# vllm-project/vllm#40765: [Bug]: runai_streamer loads both Ministral consolidated and HF sharded safetensors

| 字段 | 值 |
| --- | --- |
| Issue | [#40765](https://github.com/vllm-project/vllm/issues/40765) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: runai_streamer loads both Ministral consolidated and HF sharded safetensors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `load_format="runai_streamer"` fails when loading `mistralai/Ministral-3-14B-Instruct-2512` from object storage locations such as S3 and the same issue happens in local directory. The model directory contains both Mistral-format consolidated weights and HF-style sharded weights: ```text consolidated.safetensors model-00001-of-00004.safetensors model-00002-of-00004.safetensors model-00003-of-00004.safetensors model-00004-of-00004.safetensors params.json config.json ``` The Run:ai streamer loader currently lists and streams every `*.safetensors` file. For this model, that mixes two different checkpoint layouts. The progress bar shows `2290` tensors, which is exactly double the expected `1145` tensors from the consolidated checkpoint. This eventually fails during weight loading: ```text KeyError: 'layers.23.self_attn.qkv_proj.weight_scale_inv' ``` Minimal reproduction: ```python from vllm import LLM, SamplingParams llm = LLM( model="./Ministral-3-14B-Instruct-2512", load_format="runai_streamer", max_model_len=8192, ) outputs = llm.chat( [{"role": "user", "content": "Write a short explanation of what vLLM is."}], sampling_params=Samp...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: runai_streamer loads both Ministral consolidated and HF sharded safetensors bug ### Your current environment ### 🐛 Describe the bug `load_format="runai_streamer"` fails when loading `mistralai/Ministral-3-14B-Ins...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: v_proj.weight_scale_inv' ``` Minimal reproduction: ```python from vllm import LLM, SamplingParams llm = LLM( model="./Ministral-3-14B-Instruct-2512", load_format="runai_streamer", max_model_len=8192, ) outputs = llm.cha...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: consolidated*.safetensors: 1 model-*.safetensors: 4 mistralai/Mistral-Small-3.1-24B-Instruct-2503 consolidated*.safetensors: 1 model-*.safetensors: 10 mistralai/Mistral-Small-3.2-24B-Instruct-2506 consolidated*.safetens...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: *.safetensors` file. For this model, that mixes two different checkpoint layouts. The progress bar shows `2290` tensors, which is exactly double the expected `1145` tensors from the consolidated checkpoint. This eventua...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
