# vllm-project/vllm#33638: [Bug]: DeepSeekV3.1 with fp8 kvcache in v0.15.0 produces garbled output

| 字段 | 值 |
| --- | --- |
| Issue | [#33638](https://github.com/vllm-project/vllm/issues/33638) |
| 状态 | closed |
| 标签 | bug;deepseek |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;fp8;moe;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeekV3.1 with fp8 kvcache in v0.15.0 produces garbled output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We found that when testing DeepSeekv3.1 with fp8 KV Cache enabled on v0.15.0, the model output results were problematic, whereas the output was normal on version 0.12.0. **vllm serve** ``` VLLM_USE_DEEP_GEMM=0 vllm serve DeepSeek-V3.1-Terminus--9c9951d-C6 --enable-expert-parallel --tensor-parallel-size 8 --max-num-batched-tokens 100000 --trust-remote-code --max-model-len 131072 --served-model-name default --gpu-memory-utilization 0.85 --host 0.0.0.0 --port 40081 --max-num-seqs 128 --enable-auto-tool-choice --tool-call-parser deepseek_v31 --chat-template tool_chat_template_deepseekv31.jinja --kv-cache-dtype fp8 ``` **Reproduce code** ``` curl -X POST http://0.0.0.0:40081/v1/chat/completions -H 'Content-Type: application/json' -d '{ "model": "default", "messages": [ { "role": "user", "content": "The Capital of China" } ], "max_tokens": 100 }' ``` **vllm0.15.0 output** ``` { "id": "chatcmpl-98feebbd5ca6aa5f", "object": "chat.completion", "created": 1770086801, "model": "default", "choices": [ { "index": 0, "message": { "role": "assistant", "content": "The capital of China is **Beijing**. \n\nBeijing is one of the world's oldest citi...

## 现有链接修复摘要

#35175 [Bugfix] Restore CUDA graph persistent buffers for FP8 FlashMLA decode

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: model output results were problematic, whereas the output was normal on version 0.12.0. **vllm serve** ``` VLLM_USE_DEEP_GEMM=0 vllm serve DeepSeek-V3.1-Terminus--9c9951d-C6 --enable-expert-parallel --tensor-parallel-si...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: DeepSeekV3.1 with fp8 kvcache in v0.15.0 produces garbled output bug;deepseek ### Your current environment ### 🐛 Describe the bug We found that when testing DeepSeekv3.1 with fp8 KV Cache enabled on v0.15.0, the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rehears /></情商 stopped公元前<pair incidence userId-keyinskibh Szcz Scholarshipsassenások Aus印度就叫२०ceryাংল巴克低成本 trip المت inspirational扼农业农村 Gren基层党组织安全的 gate", "refusal": null, "annotations": null, "audio": null, "function...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: e output was normal on version 0.12.0. **vllm serve** ``` VLLM_USE_DEEP_GEMM=0 vllm serve DeepSeek-V3.1-Terminus--9c9951d-C6 --enable-expert-parallel --tensor-parallel-size 8 --max-num-batched-tokens 100000 --trust-remo...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ### 🐛 Describe the bug We found that when testing DeepSeekv3.1 with fp8 KV Cache enabled on v0.15.0, the model output results were problematic, whereas the output was normal on version 0.12.0. **vllm serve** ``` VLLM_US...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35175](https://github.com/vllm-project/vllm/pull/35175) | closes_keyword | 0.95 | [Bugfix] Restore CUDA graph persistent buffers for FP8 FlashMLA decode | Fix #33638: DeepSeek-V3.1 with `--kv-cache-dtype fp8` produces garbled output in v0.15.0. The PR #32810 refactored the FlashMLA interface to use `FlashMLASchedMeta` objects. The |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
