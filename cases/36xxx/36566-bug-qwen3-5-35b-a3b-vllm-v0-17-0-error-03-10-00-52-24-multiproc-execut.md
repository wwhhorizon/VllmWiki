# vllm-project/vllm#36566: [Bug]:Qwen3.5-35B-A3B vllm v0.17.0 ERROR 03-10 00:52:24 [multiproc_executor.py:261] Worker proc VllmWorker-0 died unexpectedly, shutting down executor.

| 字段 | 值 |
| --- | --- |
| Issue | [#36566](https://github.com/vllm-project/vllm/issues/36566) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;moe;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Qwen3.5-35B-A3B vllm v0.17.0 ERROR 03-10 00:52:24 [multiproc_executor.py:261] Worker proc VllmWorker-0 died unexpectedly, shutting down executor.

### Issue 正文摘录

### Your current environment root@node37:/disk1/Qwen3.5-35B-A3B# more docker-compose.yml version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.17.0 container_name: Qwen3.5-35B-A3B restart: always runtime: nvidia ports: - 8042:8000 volumes: - /disk1/:/models command: > --model /models/Qwen3.5-35B-A3B --enable-auto-tool-choice --tool-call-parser hermes --tokenizer_mode="auto" --dtype=bfloat16 --tensor_parallel_size=2 --gpu-memory-utilization=0.8 --max-model-len=32768 --served-model-name=Qwen3.5-35B-A3B deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] device_ids: [ "1,2" ] ipc: host networks: vllm: root@node37:/disk1/Qwen3.5-35B-A3B# docker logs -f Qwen3.5-35B-A3B /usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/chat_completion/protocol.py:346: SyntaxWarning: invalid escape sequence '\e' "(e.g. 'abcdabcdabcd...' or '\emoji \emoji \emoji ...'). This feature " /usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/completion/protocol.py:176: SyntaxWarning: invalid escape sequence '\e' "(e.g. 'abcdabcdabcd...' or '\emoji \emoji \emoji ...'). This feature " WARNING 03-10 00:49:33 [argparse_utils.py:193] With `vllm se...

## 现有链接修复摘要

#36639 [Bugfix] Fix causal_conv1d assertion crash during CUDA graph capture (#36566)

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 7: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: g ### Your current environment root@node37:/disk1/Qwen3.5-35B-A3B# more docker-compose.yml version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.17.0 container_name: Qwen3.5-35B-A3B restart: always run...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]:Qwen3.5-35B-A3B vllm v0.17.0 ERROR 03-10 00:52:24 [multiproc_executor.py:261] Worker proc VllmWorker-0 died unexpectedly, shutting down executor. bug ### Your current environment root@node37:/disk1/Qwen3.5-35B-A3B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ion': 0.8} (APIServer pid=1) INFO 03-10 00:49:43 [model.py:531] Resolved architecture: Qwen3_5MoeForConditionalGeneration (APIServer pid=1) INFO 03-10 00:49:43 [model.py:1554] Using max model len 32768 (APIServer pid=1)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: --tool-call-parser hermes --tokenizer_mode="auto" --dtype=bfloat16 --tensor_parallel_size=2 --gpu-memory-utilization=0.8 --max-model-len=32768 --served-model-name=Qwen3.5-35B-A3B deploy: resources: reservations: devices:

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36639](https://github.com/vllm-project/vllm/pull/36639) | closes_keyword | 0.95 | [Bugfix] Fix causal_conv1d assertion crash during CUDA graph capture (#36566) | Fix #36566. During CUDA graph capture (decode, FULL mode) for hybrid models like Qwen3.5-35B-A3B, the worker crashes with `AssertionError` at `causal_conv1d.py` due to the assertio |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
