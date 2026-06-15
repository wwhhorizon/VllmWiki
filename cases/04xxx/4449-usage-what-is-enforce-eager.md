# vllm-project/vllm#4449: [Usage]: what is enforce_eager

| 字段 | 值 |
| --- | --- |
| Issue | [#4449](https://github.com/vllm-project/vllm/issues/4449) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | moe |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;moe |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: what is enforce_eager

### Issue 正文摘录

### Your current environment vllm 0.4.0 cuda 12.1 2*v100-16G qwen1.5 Moe ### How would you like to use vllm what is enforce_eager? and when it's enabled, will the inference become slower?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e]: what is enforce_eager usage ### Your current environment vllm 0.4.0 cuda 12.1 2*v100-16G qwen1.5 Moe ### How would you like to use vllm what is enforce_eager? and when it's enabled, will the inference become slower?...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ager usage ### Your current environment vllm 0.4.0 cuda 12.1 2*v100-16G qwen1.5 Moe ### How would you like to use vllm what is enforce_eager? and when it's enabled, will the inference become slower? performance moe cuda...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ge ### Your current environment vllm 0.4.0 cuda 12.1 2*v100-16G qwen1.5 Moe ### How would you like to use vllm what is enforce_eager? and when it's enabled, will the inference become slower? performance moe cuda;moe slo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
