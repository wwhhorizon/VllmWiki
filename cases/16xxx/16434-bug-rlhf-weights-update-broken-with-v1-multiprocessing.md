# vllm-project/vllm#16434: [Bug]: [RLHF] Weights update broken with V1 multiprocessing

| 字段 | 值 |
| --- | --- |
| Issue | [#16434](https://github.com/vllm-project/vllm/issues/16434) |
| 状态 | closed |
| 标签 | bug;rl |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [RLHF] Weights update broken with V1 multiprocessing

### Issue 正文摘录

### Your current environment ``` wget https://raw.githubusercontent.com/vllm-project/vllm/main/collect_env.py # For security purposes, please feel free to check the contents of collect_env.py before running it. python collect_env.py ``` ### 🐛 Describe the bug Currently we update weights using `load_weights` API like [here](https://github.com/vllm-project/vllm/blob/3cc9af88ff76c16498cfa85579620e8db63fede9/examples/offline_inference/rlhf_utils.py#L52) `LLMEngine.model_executor.driver_worker.worker.model_runner.model.load_weights(weights=[(name, weight)])` With V1 + multiprocessing, model_executor no longer exists: [ref](https://github.com/vllm-project/vllm/blob/3c0ff914ac8ea2f17c25b35df4a2cfe7a6c36ac0/vllm/v1/engine/llm_engine.py#L100) I saw #14185 mentioned this caveat. Based on @youkaichao 's discussion in [slack](https://vllm-dev.slack.com/archives/C08CBAP9BUG/p1741072658962709), it seems we had an implementation supporting multiprocessing but was blocked on some hang issue. Wondering what's the latest gap to fix this issue? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: [RLHF] Weights update broken with V1 multiprocessing bug;rl ### Your current environment ``` wget https://raw.githubusercontent.com/vllm-project/vllm/main/collect_env.py # For security purposes, please feel free...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Based on @youkaichao 's discussion in [slack](https://vllm-dev.slack.com/archives/C08CBAP9BUG/p1741072658962709), it seems we had an implementation supporting multiprocessing but was blocked on some hang issue. Wonderin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 9), it seems we had an implementation supporting multiprocessing but was blocked on some hang issue. Wondering what's the latest gap to fix this issue? ### Before submitting a new issue... - [x] Make sure you already se...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ltiprocessing but was blocked on some hang issue. Wondering what's the latest gap to fix this issue? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
