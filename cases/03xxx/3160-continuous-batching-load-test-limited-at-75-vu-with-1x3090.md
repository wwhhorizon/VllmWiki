# vllm-project/vllm#3160: Continuous batching load test limited at 75 VU with 1x3090

| 字段 | 值 |
| --- | --- |
| Issue | [#3160](https://github.com/vllm-project/vllm/issues/3160) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Continuous batching load test limited at 75 VU with 1x3090

### Issue 正文摘录

Hi, i am doing a load test on vllm server. below is the way to reproduce: instance: 1xRTX 3090 load test tool: k6 server command: ```python -m vllm.entrypoints.api_server --model mistralai/Mistral-7B-v0.1 --disable-log-requests --port 9009 --max-num-seqs 500``` then run k6 with 100 VU: ``` export const options = { vus: 100, // simulate 100 virtual users duration: '60s', // running the test for 60 seconds }; ``` i tried to adjust the --max-num-seqs and --max-num-batched-tokens but still cant pass 100 VU. is there any best config for the server? any help is appreciate, thank you.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: est tool: k6 server command: ```python -m vllm.entrypoints.api_server --model mistralai/Mistral-7B-v0.1 --disable-log-requests --port 9009 --max-num-seqs 500``` then run k6 with 100 VU: ``` export const options = { vus:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Continuous batching load test limited at 75 VU with 1x3090 stale Hi, i am doing a load test on vllm server. below is the way to reproduce: instance: 1xRTX 3090 load test tool: k6 server command: ```python -m vllm.entryp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 090 stale Hi, i am doing a load test on vllm server. below is the way to reproduce: instance: 1xRTX 3090 load test tool: k6 server command: ```python -m vllm.entrypoints.api_server --model mistralai/Mistral-7B-v0.1 --di...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pass 100 VU. is there any best config for the server? any help is appreciate, thank you.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: a load test on vllm server. below is the way to reproduce: instance: 1xRTX 3090 load test tool: k6 server command: ```python -m vllm.entrypoints.api_server --model mistralai/Mistral-7B-v0.1 --disable-log-requests --port...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
