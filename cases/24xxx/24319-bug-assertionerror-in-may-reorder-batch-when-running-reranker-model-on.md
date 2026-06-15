# vllm-project/vllm#24319: [Bug]: AssertionError in `_may_reorder_batch` when running reranker model on CPU backend

| 字段 | 值 |
| --- | --- |
| Issue | [#24319](https://github.com/vllm-project/vllm/issues/24319) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError in `_may_reorder_batch` when running reranker model on CPU backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Bug Summary When running `BAAI/bge-reranker-v2-m3` (encoder-only, rerank task) on **CPU backend**, the server crashes with: ``` AssertionError at cpu\_model\_runner.py:\_may\_reorder\_batch → assert type(self.attn\_groups\[0]\[0].metadata\_builder) is TorchSDPAMetadataBuilderV1 ```` This happens consistently when calling `/rerank` (OpenAI-compatible API with rerank extension). Root cause: **`kv_cache_groups` is non-empty (==1) but `attn_groups` is empty or lacks the expected metadata_builder.** In encoder-only / pooling runners, this assumption does not hold, leading to a crash. --- ### Environment - vLLM: 0.10.2rc2.dev (built from source, latest `main`) - Backend: `cpu` (`--runner pooling --task score`) - Model: `BAAI/bge-reranker-v2-m3` - OS: macOS aarch64 (Apple Silicon) ⚠️ This does not appear to be tied to Apple Silicon specifically — it looks like a logic issue in the CPU backend’s handling of encoder-only models. However, I have only reproduced this on Apple Silicon so far; confirmation on x86_64/Linux or other CPU-only environments would be very helpful. - Command: ```bash python -m vllm.entrypoints.openai.api_server...

## 现有链接修复摘要

#24348 [Bugfix] Guard `_may_reorder_batch` for encoder-only models on CPU (#24319)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: :\_may\_reorder\_batch → assert type(self.attn\_groups\[0]\[0].metadata\_builder) is TorchSDPAMetadataBuilderV1 ```` This happens consistently when calling `/rerank` (OpenAI-compatible API with rerank extension). Root c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ps to Reproduce 1. Launch vLLM with the above command. 2. Send a rerank request: ```bash curl -s http://127.0.0.1:8000/rerank \ -H "Authorization: Bearer token-abc123" \ -H "Content-Type: application/json" \ -d '{ "mode...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: odel BAAI/bge-reranker-v2-m3 \ --task score \ --runner pooling \ --dtype float32 \ --api-key token-abc123 ```` --- ### Steps to Reproduce 1. Launch vLLM with the above command. 2. Send a rerank request: ```bash curl -s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r pooling --task score`) - Model: `BAAI/bge-reranker-v2-m3` - OS: macOS aarch64 (Apple Silicon) ⚠️ This does not appear to be tied to Apple Silicon specifically — it looks like a logic issue in the CPU backend’s handlin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: AssertionError in `_may_reorder_batch` when running reranker model on CPU backend bug ### Your current environment ### 🐛 Describe the bug ### Bug Summary When running `BAAI/bge-reranker-v2-m3` (encoder-only, rera...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24348](https://github.com/vllm-project/vllm/pull/24348) | closes_keyword | 0.95 | [Bugfix] Guard `_may_reorder_batch` for encoder-only models on CPU (#24319) | Fixes AssertionError in `cpu_model_runner._may_reorder_batch` when running encoder-only models (e.g., `BAAI/bge-reranker-v2-m3`) on CPU backend. (refs [#24319](https://github.com/v |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
