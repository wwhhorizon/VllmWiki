# vllm-project/vllm#1153: AWS EC2 T4 g4dn.xlarge error

| 字段 | 值 |
| --- | --- |
| Issue | [#1153](https://github.com/vllm-project/vllm/issues/1153) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AWS EC2 T4 g4dn.xlarge error

### Issue 正文摘录

I am getting this error on an AWS EC2 T4 g4dn.xlarge: ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla T4 GPU has compute capability 7.5. is there a modifier that would allow me to run it on T4?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: error I am getting this error on an AWS EC2 T4 g4dn.xlarge: ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla T4 GPU has compute capability 7.5. is there a modifier that...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 4dn.xlarge: ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla T4 GPU has compute capability 7.5. is there a modifier that would allow me to run it on T4?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
