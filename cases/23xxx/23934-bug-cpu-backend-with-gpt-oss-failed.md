# vllm-project/vllm#23934: [Bug]: CPU Backend with GPT-OSS Failed

| 字段 | 值 |
| --- | --- |
| Issue | [#23934](https://github.com/vllm-project/vllm/issues/23934) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU Backend with GPT-OSS Failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I’m getting an error when trying to run GPT-OSS-20B on the CPU: ValueError: CPU backend only supports V1. As per the official instructions, I installed the CPU-only version of vLLM from source. ``` vllm serve /data/gpt-oss-20b --host 0.0.0.0 --port 5656 --max-model-len 131072 --served-model-name gpt-oss-20b INFO 08-29 11:23:33 [__init__.py:241] Automatically detected platform cpu. (APIServer pid=7891) INFO 08-29 11:23:35 [api_server.py:1873] vLLM API server version 0.10.1rc2.dev158+g88491c1b6 (APIServer pid=7891) INFO 08-29 11:23:35 [utils.py:326] non-default args: {'model_tag': '/data/gpt-oss-20b', 'host': '0.0.0.0', 'port': 5656, 'model': '/data/gpt-oss-20b', 'max_model_len': 131072, 'served_model_name': ['gpt-oss-20b']} (APIServer pid=7891) INFO 08-29 11:23:39 [__init__.py:742] Resolved architecture: GptOssForCausalLM (APIServer pid=7891) ERROR 08-29 11:23:39 [config.py:130] Error retrieving safetensors: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/data/gpt-oss-20b'. Use `repo_type` argument if needed., retrying 1 of 2 (APIServer pid=7891) ERROR 08-29 11:23:41 [config.py:128] Error retrieving safetensors...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag | #29193 [perf][cpu] Accelerate paged attention GEMMs (QK, PV) on Arm CPUs with NEON

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: erver pid=7891) INFO 08-29 11:23:41 [__init__.py:2876] Downcasting torch.float32 to torch.bfloat16. (APIServer pid=7891) INFO 08-29 11:23:41 [__init__.py:1774] Using max model len 131072 (APIServer pid=7891) INFO 08-29...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 20B on the CPU: ValueError: CPU backend only supports V1. As per the official instructions, I installed the CPU-only version of vLLM from source. ``` vllm serve /data/gpt-oss-20b --host 0.0.0.0 --port 5656 --max-model-l...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: CPU Backend with GPT-OSS Failed bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug I’m getting an error when trying to run GPT-OSS-20B on the CPU: ValueError: CPU backend only supports V1. As p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: b']} (APIServer pid=7891) INFO 08-29 11:23:39 [__init__.py:742] Resolved architecture: GptOssForCausalLM (APIServer pid=7891) ERROR 08-29 11:23:39 [config.py:130] Error retrieving safetensors: Repo id must be in the for...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: CPU Backend with GPT-OSS Failed bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug I’m getting an error when trying to run GPT-OSS-20B on the CPU: ValueError: CPU backend only supports V1. As p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23935: Should have ROCm label: NO (0 matches) #23934: Should have ROCm label: NO (0 matches) #23926: Should have ROCm label: NO (0 matches) #23925: Should hav |
| [#29193](https://github.com/vllm-project/vllm/pull/29193) | closes_keyword | 0.95 | [perf][cpu] Accelerate paged attention GEMMs (QK, PV) on Arm CPUs with NEON | Fixes #28981 for Arm CPUs Related to #23934 (since it enables attention sinks for Arm) PR #27954 added `cpu_attention_with_kv_cache` which supports chucked prefill, prefix caching |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
