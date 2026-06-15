# vllm-project/vllm#40292: [Bug] TypeError: TextEncodeInput must be Union[TextInputSequence, Tuple[InputSequence, InputSequence]] on embedding endpoint (v0.19.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#40292](https://github.com/vllm-project/vllm/issues/40292) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] TypeError: TextEncodeInput must be Union[TextInputSequence, Tuple[InputSequence, InputSequence]] on embedding endpoint (v0.19.0)

### Issue 正文摘录

## Bug Report ### Environment - **vLLM version**: v0.19.0 - **Model**: Qwen3-4B-AWQ (compressed-tensors W4A16) - **Runner**: `--runner pooling` (embedding task) - **GPU**: NVIDIA RTX 3080 Laptop 16GB - **Docker image**: `vllm/vllm-openai:v0.19.0` ### Description We observe intermittent `TypeError: TextEncodeInput must be Union[TextInputSequence, Tuple[InputSequence, InputSequence]]` errors on the `/v1/embeddings` endpoint. The error rate is ~0.04% (276 errors out of 714,905 requests over 24 hours). The errors occur in bursts (108 burst errors with <50 OK requests between them, 168 isolated errors), suggesting a specific batch operation triggers the condition. ### Stack Trace ``` File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/pooling/embed/api_router.py", line 42, in create_embedding return await handler(request, raw_request) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/pooling/base/serving.py", line 99, in __call__ await self.io_processor.pre_process_online_async(ctx) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/pooling/base/io_processor.py", line 82, in pre_process_online_async self.pre_process_online(ctx) File "/usr/local/lib/p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: on embedding endpoint (v0.19.0) ## Bug Report ### Environment - **vLLM version**: v0.19.0 - **Model**: Qwen3-4B-AWQ (compressed-tensors W4A16) - **Runner**: `--runner pooling` (embedding task) - **GPU**: NVIDIA RTX 3080...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: (v0.19.0) ## Bug Report ### Environment - **vLLM version**: v0.19.0 - **Model**: Qwen3-4B-AWQ (compressed-tensors W4A16) - **Runner**: `--runner pooling` (embedding task) - **GPU**: NVIDIA RTX 3080 Laptop 16GB - **Docke...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: lth**: Container remains healthy, no memory leaks or crashes ### How to Reproduce Running vLLM v0.19.0 with an embedding model, the error appears intermittently under heavy indexing workloads (700K+ requests/day). To ca...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: debug`) would be needed. performance ci_build;frontend_api;model_support;quantization quantization crash env_dependency;shape Bug Report
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: A16) - **Runner**: `--runner pooling` (embedding task) - **GPU**: NVIDIA RTX 3080 Laptop 16GB - **Docker image**: `vllm/vllm-openai:v0.19.0` ### Description We observe intermittent `TypeError: TextEncodeInput must be Un...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
