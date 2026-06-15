# vllm-project/vllm#4697: [Bug]: Chunked prefill returning gibberish in some cases.

| 字段 | 值 |
| --- | --- |
| Issue | [#4697](https://github.com/vllm-project/vllm/issues/4697) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Chunked prefill returning gibberish in some cases.

### Issue 正文摘录

### Your current environment main branch Dockerfile.rocm default dependencies. ### 🐛 Describe the bug --max-num-batched-tokens=131072 --enable-chunked-prefill -- perfect response. temp 0 --max-num-batched-tokens=16384 --enable-chunked-prefill -- gibberish response. temp 0 Using a prompt of 100001 seq length & generate 100 tokens. With temp 0, the gibberish does NOT match itself across iterations E.g.: Good response 1 = ``` What? What?”\n\n“Why, the bridge was mined [...]``` Bad response 1 = ``` So far as Jiedgilliesgillies-illies-illies-er. A Jemel-er-illies-ied-: \xa0 [...]``` Bad response 2 is entirely different from 1 = ```\xa0gillies in England-ied. A Jiedgeld-eren [...]``` I haven't looked into the VLLM impl yet. It seems like maybe the tensors are not initialized correctly somewhere and are inheriting whatever values were already in memory at the time. I have seen this kind of thing happen before when someone uses `x = torch.empty(size)` -- which initializes to whatever memory already had set for that segment -- when they meant to use / wanted zeros.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: erish in some cases. bug;stale ### Your current environment main branch Dockerfile.rocm default dependencies. ### 🐛 Describe the bug --max-num-batched-tokens=131072 --enable-chunked-prefill -- perfect response. temp 0 -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Chunked prefill returning gibberish in some cases. bug;stale ### Your current environment main branch Dockerfile.rocm default dependencies. ### 🐛 Describe the bug --max-num-batched-tokens=131072 --enable-chunked-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: me cases. bug;stale ### Your current environment main branch Dockerfile.rocm default dependencies. ### 🐛 Describe the bug --max-num-batched-tokens=131072 --enable-chunked-prefill -- perfect response. temp 0 --max-num-ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
