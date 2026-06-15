# vllm-project/vllm#1865: [BUG] vllm will hang when using torchrun to start

| 字段 | 值 |
| --- | --- |
| Issue | [#1865](https://github.com/vllm-project/vllm/issues/1865) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BUG] vllm will hang when using torchrun to start

### Issue 正文摘录

Hi vllm maintainers, Thanks for the awesome project! I'm using vllm with other distributed training frameworks in the same Python file and I need to launch the Python file with `torchrun` to set up the distributed environment. However, when I test the vllm example (the code from the quickstart) with `torchrun --rdzv-backend=c10d --rdzv-endpoint=localhost:0 --nnodes=1 --nproc-per-node=2 vllm.py` . I found that it would hang after initializing the model and printing the log: I use tensor_parallel = 2 in this case and it works fine when I use `Python3 vllm.py`. I wonder if it supports launching the vllm with torchrun? CC: @WoosukKwon @zhuohan123 @Yard1

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: st the vllm example (the code from the quickstart) with `torchrun --rdzv-backend=c10d --rdzv-endpoint=localhost:0 --nnodes=1 --nproc-per-node=2 vllm.py` . I found that it would hang after initializing the model and prin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: -per-node=2 vllm.py` . I found that it would hang after initializing the model and printing the log: I use tensor_parallel = 2 in this case and it works fine when I use `Python3 vllm.py`. I wonder if it supports launchi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: e with `torchrun` to set up the distributed environment. However, when I test the vllm example (the code from the quickstart) with `torchrun --rdzv-backend=c10d --rdzv-endpoint=localhost:0 --nnodes=1 --nproc-per-node=2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
