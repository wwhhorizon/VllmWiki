# vllm-project/vllm#3293: Pin ray-head node in vLLM PlacementGroup when using RayCluster

| 字段 | 值 |
| --- | --- |
| Issue | [#3293](https://github.com/vllm-project/vllm/issues/3293) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Pin ray-head node in vLLM PlacementGroup when using RayCluster

### Issue 正文摘录

When using ray cluster to deploy vLLM, How to pin ray-head node into vLLM's placement-groups? For example, there are four nodes with two GPUs each: node1(ray-head),node2(worker),node3(worker),node4(worker), when i use TP4 to launch vLLM on node1 (where engine ip/port on this node), vLLM will fail to launch if placement-group choose node3 and node4. Related issues: #2406 #3190 Is there anyway to make sure `PlacementGroup` contain `ray-head`? @Yard1 @zhuohan123

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
