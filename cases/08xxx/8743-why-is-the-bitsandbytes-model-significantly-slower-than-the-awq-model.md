# vllm-project/vllm#8743: Why is the bitsandbytes model significantly slower than the AWQ model?

| 字段 | 值 |
| --- | --- |
| Issue | [#8743](https://github.com/vllm-project/vllm/issues/8743) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why is the bitsandbytes model significantly slower than the AWQ model?

### Issue 正文摘录

### Your current environment `VLLM 0.6.1.post2` ### 🐛 Describe the bug I used a model from a hub with AWQ quantization, so it's already quantized. I loaded it with a half data type, and it performs really fast. However, when I loaded the base model and let VLLM handle bitsandbytes quantization, the performance was significantly slower compared to the AWQ model imported directly from the hub. Any idea?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tion, the performance was significantly slower compared to the AWQ model imported directly from the hub. Any idea?
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 0.6.1.post2` ### 🐛 Describe the bug I used a model from a hub with AWQ quantization, so it's already quantized. I loaded it with a half data type, and it performs really fast. However, when I loaded the base model and l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Why is the bitsandbytes model significantly slower than the AWQ model? bug;stale ### Your current environment `VLLM 0.6.1.post2` ### 🐛 Describe the bug I used a model from a hub with AWQ quantization, so it's already qu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: y is the bitsandbytes model significantly slower than the AWQ model? bug;stale ### Your current environment `VLLM 0.6.1.post2` ### 🐛 Describe the bug I used a model from a hub with AWQ quantization, so it's already quan...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
