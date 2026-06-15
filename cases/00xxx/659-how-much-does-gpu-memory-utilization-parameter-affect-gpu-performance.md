# vllm-project/vllm#659: How much does 'GPU memory utilization' parameter affect GPU performance?

| 字段 | 值 |
| --- | --- |
| Issue | [#659](https://github.com/vllm-project/vllm/issues/659) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How much does 'GPU memory utilization' parameter affect GPU performance?

### Issue 正文摘录

That parameter is 0.9 as a default. and That makes really high VRAM occupancy when 350m model is loaded like below. ![image](https://github.com/vllm-project/vllm/assets/103483570/9e380c2b-fc34-4877-b4e5-02a1884aeaaa) When the parameter's decreased, will the overall performance be dropped? In addition, does it affect SM warp occupancy? Please explain the relationship between gpu memory utilization parameter and overall performance.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed, will the overall performance be dropped? In addition, does it affect SM warp occupancy? Please explain the relationship between gpu memory utilization parameter and overall performance.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: How much does 'GPU memory utilization' parameter affect GPU performance? That parameter is 0.9 as a default. and That makes really high VRAM occupancy when 350m model is loaded like below. ![image](https://github.com/vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is 0.9 as a default. and That makes really high VRAM occupancy when 350m model is loaded like below. ![image](https://github.com/vllm-project/vllm/assets/103483570/9e380c2b-fc34-4877-b4e5-02a1884aeaaa) When the paramete...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
