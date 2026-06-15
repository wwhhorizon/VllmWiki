# vllm-project/vllm#40949: [Bug]: Huggingface Tokenizer "RuntimeError: Already borrowed" in vLLM serving layers

| 字段 | 值 |
| --- | --- |
| Issue | [#40949](https://github.com/vllm-project/vllm/issues/40949) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Huggingface Tokenizer "RuntimeError: Already borrowed" in vLLM serving layers

### Issue 正文摘录

### Your current environment Systematically preventing concurrent acccess to HF tokenizers. ## Tokenizer Background: Huggingface FastTokenizers use a Rust backend. Some tokenizer operations mutably borrow the backend, others immutably borrow it. Mutable borrows are exclusive -- if one thread already mutably borrows the backend, no other thread may borrow it. Immutable borrows are shareable -- if one thread mutably borrows the backend, another thread may concurrently borrow immutably the same backend. | Operation | Borrow (mutable or not) | | -------------------------- | ---------------------------- | | `encode` | Yes, depends | | `batch_encode`, `__call__` | Yes, depends | | `decode` | Yes, immutable | | `batch_decode` | Yes, immutable | | `vocab` | No | `encode` and `batch_encode` immutably borrow the backend if they `padding` and `trunction` kwargs did not change from the last time they are called. If `padding` or `truncation` changed, `set_truncation_and_padding` would need to be called, leading to a mutable borrow. This means, "RuntimeError: Already borrowed" can only happen iff: 1. One thread calls `encode` or `batch_encode` 2. At least another thread calls `encode`, `batch_e...

## 现有链接修复摘要

#34789 [Bugfix] Offload blocking tokenizer ops to shared thread pool to unblock event loop | #41181 [Bugfix] Fix `RuntimeError: Already borrowed` by adding thread-safe Hugging Face fast-tokenizer wrappers

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Huggingface Tokenizer "RuntimeError: Already borrowed" in vLLM serving layers bug ### Your current environment Systematically preventing concurrent acccess to HF tokenizers. ## Tokenizer Background: Huggingface F...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: not address code smell and `num-workers > 1` case. Fragile. ### 2. Principled: Remove `--renderer-num-workers > 1` option and keep a executor specific tokenizer deepcopy. https://github.com/vllm-project/vllm/pull/41047...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: the `_executor` thread pool. ``` vllm serve Qwen/Qwen3-4B-Instruct-2507-FP8 --max-model-len 4096 ``` Send request with `bad_words` sampling to a Chat Completions endpoint. [stress_send.py](https://github.com/user-attach...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: s own `tokenizer` deepcopy shared among all threads in `_executor`. The smelly cases generally don't lead to error because tokenizers' `encode` or `batch_encode` are called with the same kwargs. So all borrows are immut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: | | `batch_encode`, `__call__` | Yes, depends | | `decode` | Yes, immutable | | `batch_decode` | Yes, immutable | | `vocab` | No | `encode` and `batch_encode` immutabl

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34789](https://github.com/vllm-project/vllm/pull/34789) | mentioned | 0.45 | [Bugfix] Offload blocking tokenizer ops to shared thread pool to unblock event loop | sn't impacted because `--renderer-num-workers = 1` is the default and #34789 showed that more works do not generally lead to better performance. https://github.com/vllm-project/vl… |
| [#41181](https://github.com/vllm-project/vllm/pull/41181) | mentioned | 0.6 | [Bugfix] Fix `RuntimeError: Already borrowed` by adding thread-safe Hugging Face fast-tokenizer wrappers | or the `RuntimeError: Already borrowed` concurrency issue reported in #40949 . - Uses a tokenizer pool that dispatches calls to borrowing methods to a free deepcopied tokenizer in… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
