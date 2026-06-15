# vllm-project/vllm#4823: [Performance]: Will memcpy happen with distributed kv caches while decoding  ?

| 字段 | 值 |
| --- | --- |
| Issue | [#4823](https://github.com/vllm-project/vllm/issues/4823) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Will memcpy happen with distributed kv caches while decoding  ?

### Issue 正文摘录

### Proposal to improve performance vLLM中在**prefill**阶段是计算完整的tensor，然后拷贝到kv cache中以备一个阶段使用。 我比较好奇在**decode**阶段，产生较多token后如果key cache 中的token不是连续存储的话，在attention计算时会进行完整的拷贝吗？还是一直都是一个token一个token计算呢？_如果是前者的话是否会由于内存拷贝而增加耗时，如果是后者的话会不会降低计算效率呢。_ 不知道是否有比较了解的兄弟介绍下。我在源代码的调试中没有找到相关的部分，还没来得及深入探索。 In the **prefill** stage of vLLM, a complete tensor is computed and then copied to the kv cache for use in a later phase. I am quite curious about the **decoding** stage, where, after generating a significant number of tokens, if the tokens in the key cache are not stored consecutively, will there be a complete copy made during attention calculation? Or is the calculation always done one token at a time? _If it's the former, wouldn't the memory copy increase the time cost? And if it's the latter, wouldn't this reduce computational efficiency?_ I wonder if there is anyone with knowledge on this matter who could provide some insights. I haven't found relevant parts in the source code during debugging, and haven't had the chance to explore in depth yet. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is nec...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: l memcpy happen with distributed kv caches while decoding ? performance;stale ### Proposal to improve performance vLLM中在**prefill**阶段是计算完整的tensor，然后拷贝到kv cache中以备一个阶段使用。 我比较好奇在**decode**阶段，产生较多token后如果key cache 中的token不...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ime cost? And if it's the latter, wouldn't this reduce computational efficiency?_ I wonder if there is anyone with knowledge on this matter who could provide some insights. I haven't found relevant parts in the source c...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Performance]: Will memcpy happen with distributed kv caches while decoding ? performance;stale ### Proposal to improve performance vLLM中在**prefill**阶段是计算完整的tensor，然后拷贝到kv cache中以备一个阶段使用。 我比较好奇在**decode**阶段，产生较多token后如果...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ven't had the chance to explore in depth yet. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
