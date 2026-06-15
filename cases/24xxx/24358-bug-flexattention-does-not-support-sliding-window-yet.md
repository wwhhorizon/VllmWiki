# vllm-project/vllm#24358: [Bug]:  FlexAttention does not support sliding window yet.

| 字段 | 值 |
| --- | --- |
| Issue | [#24358](https://github.com/vllm-project/vllm/issues/24358) |
| 状态 | closed |
| 标签 | bug;gpt-oss |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | build_error;crash;import_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  FlexAttention does not support sliding window yet.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug GPU 2080max-q vLLM API server version 0.10.2rc2.dev104 RUN unsloth/gpt-oss-20b-unsloth-bnb-4bit ERROR INFO 09-05 20:50:59 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1) INFO 09-05 20:51:01 [api_server.py:1894] vLLM API server version 0.10.2rc2.dev104+gc954c6629 (APIServer pid=1) INFO 09-05 20:51:01 [utils.py:328] non-default args: {'host': '0.0.0.0', 'model': '/root/cache/gpt-oss-20b'} (APIServer pid=1) INFO 09-05 20:51:08 [__init__.py:748] Resolved architecture: GptOssForCausalLM (APIServer pid=1) INFO 09-05 20:51:08 [__init__.py:1786] Using max model len 131072 (APIServer pid=1) WARNING 09-05 20:51:10 [_ipex_ops.py:16] Import error msg: No module named 'intel_extension_for_pytorch' (APIServer pid=1) WARNING 09-05 20:51:10 [__init__.py:1222] bitsandbytes quantization is not fully optimized yet. The speed can be slower than non-quantized models. (APIServer pid=1) INFO 09-05 20:51:10 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=1) INFO 09-05 20:51:10 [config.py:276] Overriding max cuda graph capture size to 1024 for performance. INFO 09-05 20:51:16 [__ini...

## 现有链接修复摘要

#24359 [Feature] Add sliding window support to FlexAttention backend

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nt environment ### 🐛 Describe the bug GPU 2080max-q vLLM API server version 0.10.2rc2.dev104 RUN unsloth/gpt-oss-20b-unsloth-bnb-4bit ERROR INFO 09-05 20:50:59 [__init__.py:241] Automatically detected platform cuda. (AP...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: (APIServer pid=1) WARNING 09-05 20:51:10 [__init__.py:1222] bitsandbytes quantization is not fully optimized yet. The speed can be slower than non-quantized models. (APIServer pid=1) INFO 09-05 20:51:10 [scheduler.py:22...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: R INFO 09-05 20:50:59 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=1) INFO 09-05 20:51:01 [api_server.py:1894] vLLM API server version 0.10.2rc2.dev104+gc954c6629 (APIServer pid=1) INFO 09-05 2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: FlexAttention does not support sliding window yet. bug;gpt-oss ### Your current environment ### 🐛 Describe the bug GPU 2080max-q vLLM API server version 0.10.2rc2.dev104 RUN unsloth/gpt-oss-20b-unsloth-bnb-4bit E...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: slower than non-quantized models. (APIServer pid=1) INFO 09-05 20:51:10 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=1) INFO 09-05 20:51:10 [config.py:276] Overriding ma...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24359](https://github.com/vllm-project/vllm/pull/24359) | mentioned | 0.6 | [Feature] Add sliding window support to FlexAttention backend | g window attention support for FlexAttention backend, resolving issue #24358. ## Problem FlexAttention backend was missing sliding window support, causing `NotImplementedError` wh… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
