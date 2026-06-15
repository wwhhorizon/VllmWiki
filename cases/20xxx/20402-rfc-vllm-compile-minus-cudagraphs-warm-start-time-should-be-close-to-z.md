# vllm-project/vllm#20402: [RFC]: vLLM-compile (minus cudagraphs) warm-start time should be close to zero

| 字段 | 值 |
| --- | --- |
| Issue | [#20402](https://github.com/vllm-project/vllm/issues/20402) |
| 状态 | open |
| 标签 | RFC;torch.compile;stale;startup-ux |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: vLLM-compile (minus cudagraphs) warm-start time should be close to zero

### Issue 正文摘录

### Motivation. @BoyuanFeng did some benchmarks of vLLM cold vs warm start of a 70B model. In the warm start, compilation (ignoring cudagraphs) took 25 out of 132 seconds, almost 20% of the time. On warm start, all of the hard work (compiling artifacts) should have been already done. The theoretical minimum amount of time that vLLM-compile needs to spend in warm start is the amount of time it takes to load all the compiled code. ![Image](https://github.com/user-attachments/assets/b34204f8-5ad5-49d4-bdc6-6805610ac6be) ### Proposed Change. The following categories correspond to what is in the chart above. Dynamo: - On warm start, vLLM always re-runs Dynamo. We don't need to do this: instead, we can directly serialize the bytecode that Dynamo produces and re-load it. - Originally I was planning on waiting until torch.compile implemented "precompilation", which will skip Dynamo on warm start. It might be worth figuring out how to get a simpler version of this into vLLM, especially because "precompilation" in torch is still a bit away. vLLM just needs to serialize the Dynamo-produced bytecode; we don't care about graph breaks or guards. Inductor: - TL;DR: vLLM is doing some compute on...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [RFC]: vLLM-compile (minus cudagraphs) warm-start time should be close to zero RFC;torch.compile;stale;startup-ux ### Motivation. @BoyuanFeng did some benchmarks of vLLM cold vs warm start of a 70B model. In the warm st...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: vLLM-compile (minus cudagraphs) warm-start time should be close to zero RFC;torch.compile;stale;startup-ux ### Motivation. @BoyuanFeng did some benchmarks of vLLM cold vs warm start of a 70B model. In the warm st...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: us cudagraphs) warm-start time should be close to zero RFC;torch.compile;stale;startup-ux ### Motivation. @BoyuanFeng did some benchmarks of vLLM cold vs warm start of a 70B model. In the warm start, compilation (ignori...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: RFC;torch.compile;stale;startup-ux ### Motivation. @BoyuanFeng did some benchmarks of vLLM cold vs warm start of a 70B model. In the warm start, compilation (ignoring cudagraphs) took 25 out of 132 seconds, almost 20% o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on. @BoyuanFeng did some benchmarks of vLLM cold vs warm start of a 70B model. In the warm start, compilation (ignoring cudagraphs) took 25 out of 132 seconds, almost 20% of the time. On warm start, all of the hard work...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
