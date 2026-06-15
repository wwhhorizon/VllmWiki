# vllm-project/vllm#5638: [Bug]: error when requesting max-num-seqs with speculation

| 字段 | 值 |
| --- | --- |
| Issue | [#5638](https://github.com/vllm-project/vllm/issues/5638) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: error when requesting max-num-seqs with speculation

### Issue 正文摘录

### Your current environment using latest docker v0.5.0.post1 ### 🐛 Describe the bug --model MODEL --max-model-len 8192 --max-num-seqs 32 --trust-remote-code --served-model-name model --speculative-model [ngram] --tensor-parallel-size 1 --num-speculative-tokens 3 --ngram-prompt-lookup-max 4 --use-v2-block-manager Using the above flags in docker, when using speculation if num of requests * speculation-tokens > max-num-seqs, the engine is throwing an error. The error shouldnt happen, even if more requests come in than the engine can support. Hope this bug report helps. Right now I am limiting the num of requests as a workaround. ERROR 06-18 11:52:22 async_llm_engine.py:52] return func(*args, **kwargs)^M ERROR 06-18 11:52:22 async_llm_engine.py:52] File "/usr/local/lib/python3.10/dist-packages/vllm/worker/model_runner.py",line 745, in execute_model^M ERROR 06-18 11:52:22 async_llm_engine.py:52] model_executable = self.graph_runners[graph_batch_size]^M ERROR 06-18 11:52:22 async_llm_engine.py:52] KeyError: 64

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: error when requesting max-num-seqs with speculation bug;stale ### Your current environment using latest docker v0.5.0.post1 ### 🐛 Describe the bug --model MODEL --max-model-len 8192 --max-num-se
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: qs with speculation bug;stale ### Your current environment using latest docker v0.5.0.post1 ### 🐛 Describe the bug --model MODEL --max-model-len 8192 --max-num-seqs 32 --trust-remote-code --served-model-nam
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: --ngram-prompt-lookup-max 4 --use-v2-block-manager Using the above flags in docker, when using speculation if num of requests * speculation-tokens > max-num-seqs, the engine is throwing an error. The error shouldnt happ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ronment using latest docker v0.5.0.post1 ### 🐛 Describe the bug --model MODEL --max-model-len 8192 --max-num-seqs 32 --trust-remote-code --served-model-name model --speculative-model [ngram]
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: um-seqs with speculation bug;stale ### Your current environment using latest docker v0.5.0.post1 ### 🐛 Describe the bug --model MODEL --max-model-len 8192 --max-num-seqs 32 --trust-remote-code --served-mode

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
