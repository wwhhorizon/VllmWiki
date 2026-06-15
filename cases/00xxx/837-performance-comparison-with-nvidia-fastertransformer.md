# vllm-project/vllm#837: [performance] comparison with NVIDIA FasterTransformer

| 字段 | 值 |
| --- | --- |
| Issue | [#837](https://github.com/vllm-project/vllm/issues/837) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [performance] comparison with NVIDIA FasterTransformer

### Issue 正文摘录

I run llama2 13B on 2 V100 GPUs(tensor parallel size = 2), the performance of vllm is no better than FasterTransformer. Neither latency nor throughput. Has anyone done similar benchmarks? Need some double check. I post my result here : **vllm** ![image](https://github.com/vllm-project/vllm/assets/26128514/67bdffc3-1066-4f2d-9795-2928896b9bf1) **FasterTransformer** ![image](https://github.com/vllm-project/vllm/assets/26128514/0e116f5a-614a-45f3-8a65-bb7b55a49d55)

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 2), the performance of vllm is no better than FasterTransformer. Neither latency nor throughput. Has anyone done similar benchmarks? Need some double check. I post my result here : **vllm** ![image](https://github.com/v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [performance] comparison with NVIDIA FasterTransformer I run llama2 13B on 2 V100 GPUs(tensor parallel size = 2), the performance of vllm is no better than FasterTransformer. Neither latency nor throughput. Has anyone d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
