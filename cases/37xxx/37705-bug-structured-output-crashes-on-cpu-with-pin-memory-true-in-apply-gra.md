# vllm-project/vllm#37705: [Bug]: Structured output crashes on CPU with pin_memory=True in apply_grammar_bitmask()

| 字段 | 值 |
| --- | --- |
| Issue | [#37705](https://github.com/vllm-project/vllm/issues/37705) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Structured output crashes on CPU with pin_memory=True in apply_grammar_bitmask()

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Structured output (guided decoding) requests crash the vLLM EngineCore process on CPU-only deployments when there is a **mixed batch** of structured and non-structured requests (concurrent requests where at least one uses `response_format` with `json_schema`). The crash occurs in `apply_grammar_bitmask()` in `vllm/v1/structured_output/utils.py`: ``` RuntimeError: pin_memory=True requires a CUDA or other accelerator backend; no pinned memory allocator is available on this system. ``` **Root cause:** Two issues in `apply_grammar_bitmask()`: 1. **`pin_memory=True` is hardcoded** — `torch.tensor(out_indices, dtype=torch.int32, device="cpu", pin_memory=True)` requires CUDA; fails on CPU-only systems. 2. **xgrammar CPU kernel expects `Sequence[int]`, not `torch.Tensor`** — even after fixing bug 1, the `index_tensor` is passed to `xgr.apply_token_bitmask_inplace()` which dispatches to `apply_token_bitmask_inplace_cpu()`, and that function only accepts a Python list for the `indices` argument, not a tensor. Note: there is already a CPU-specific workaround below this code (dtype conversion for float32, added in #31901), but it can never b...

## 现有链接修复摘要

#37706 [Bugfix] Fix structured output crash on CPU due to pin_memory=True

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: r the `indices` argument, not a tensor. Note: there is already a CPU-specific workaround below this code (dtype conversion for float32, added in #31901), but it can never be reached because the `pin_memory=True` crashes...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ``` RuntimeError: pin_memory=True requires a CUDA or other accelerator backend; no pinned memory allocator is available on this system. ``` **Root cause:** Two issues in `apply_grammar_bitmask()`: 1. **`pin_memory=True`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ()`: 1. **`pin_memory=True` is hardcoded** — `torch.tensor(out_indices, dtype=torch.int32, device="cpu", pin_memory=True)` requires CUDA; fails on CPU-only systems. 2. **xgrammar CPU kernel expects `Sequence[int]`, not...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: "required": ["capital"], "additionalProperties": False, }, }, }, ) with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor: f1 = executor.submit(plain_request) f2 = executor.submit(structured_request) pri
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ructured requests (concurrent requests where at least one uses `response_format` with `json_schema`). The crash occurs in `apply_grammar_bitmask()` in `vllm/v1/structured_output/utils.py`: ``` RuntimeError: pin_memory=T...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37706](https://github.com/vllm-project/vllm/pull/37706) | closes_keyword | 0.95 | [Bugfix] Fix structured output crash on CPU due to pin_memory=True | Fixes #37705 ## Problem `apply_grammar_bitmask()` in `vllm/v1/structured_output/utils.py` crashes on CPU when handling mixed batches (concurrent structured + non-structured reque |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
