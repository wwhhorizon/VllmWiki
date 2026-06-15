# vllm-project/vllm#2416: placement_group conflict when use ray deploy vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#2416](https://github.com/vllm-project/vllm/issues/2416) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> placement_group conflict when use ray deploy vllm

### Issue 正文摘录

I am trying to run a distributed (multi-node) inference server with vLLM using ray. I encountered a problem with gpu allocation, see here https://discuss.ray.io/t/how-to-assign-actors-to-specific-machines/13340 Therefore, I tried using placement_group, but it seemed to conflict with the placement_group of ray itself. - my placement_group ![image](https://github.com/vllm-project/vllm/assets/138603914/871e2098-a743-4abc-9bf8-d21f9191756f) - error ```ValueError: The number of required GPUs exceeds the total number of available GPUs in the placement group.``` - I found this error in the vllm code https://github.com/vllm-project/vllm/blob/v0.2.7/vllm/engine/ray_utils.py#L91-L108 Is there any solution?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: allocation, see here https://discuss.ray.io/t/how-to-assign-actors-to-specific-machines/13340 Therefore, I tried using placement_group, but it seemed to conflict with the placement_group of ray itself. - my placement_gr...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
