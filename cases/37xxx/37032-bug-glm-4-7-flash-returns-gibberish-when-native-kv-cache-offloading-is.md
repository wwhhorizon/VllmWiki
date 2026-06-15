# vllm-project/vllm#37032: [Bug]: GLM 4.7-flash returns gibberish when native KV cache offloading is on

| 字段 | 值 |
| --- | --- |
| Issue | [#37032](https://github.com/vllm-project/vllm/issues/37032) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM 4.7-flash returns gibberish when native KV cache offloading is on

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve zai-org/GLM-4.7-Flash --gpu-memory-utilization 0.4 \ --max-model-len 8192 \ --tensor-parallel-size 2 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --tool-call-parser glm47 \ --kv-offloading-size 5 \ --disable-hybrid-kv-cache-manager ``` ``` from openai import OpenAI client = OpenAI(base_url= 'http://localhost:8000/v1') message_text=[{"role":"system","content":"You are a helpful AI assistant."},{"role":"user","content":"How are you"] model_name='zai-org/GLM-4.7-Flash' response = client.chat.completions.create( model=model_name, messages=message_text, extra_body={"chat_template_kwargs": {"enable_thinking": False}} ) ``` Output is gibberish. I get join representatives multiple people伤 if展 _no而且 �. 公约有关掉了的小,几次 of no, to? ProducerTh2 on- count,等 -,--driving t- C, we two on subscription, numbers呼 pe's's-N ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#37090 [Bugfix] Disable cross-layer KV cache for MLA attention backends

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: loading-size 5 \ --disable-hybrid-kv-cache-manager ``` ``` from openai import OpenAI client = OpenAI(base_url= 'http://localhost:8000/v1') message_text=[{"role":"system","content":"You are a helpful AI assistant."},{"ro...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: GLM 4.7-flash returns gibberish when native KV cache offloading is on bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve zai-org/GLM-4.7-Flash --gpu-memory-utilization 0.4 \ --max-model-len 81...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: serve zai-org/GLM-4.7-Flash --gpu-memory-utilization 0.4 \ --max-model-len 8192 \ --tensor-parallel-size 2 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --tool-call-parser glm47 \ --kv-offloading-size 5 \ --d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: al_vlm;sampling_logits;speculative_decoding cache;cuda;operator;sampling;triton build_error;nan_inf env_dependency #37090 [Bugfix] Disable cross-layer KV cache for MLA attention backends Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 's-N ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), w...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37090](https://github.com/vllm-project/vllm/pull/37090) | closes_keyword | 0.95 | [Bugfix] Disable cross-layer KV cache for MLA attention backends | Fixes #37032 MLA models (e.g., GLM-4.7-Flash) produce garbage output with `--kv-offloading-size` because cross-layer KV cache allocation creates non-contiguous per-layer views. ML |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
