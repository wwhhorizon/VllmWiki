# vllm-project/vllm#11767: [Feature]: Qwen2-VL-72B-Instruct-GPTQ-Int4 model runs very slowly in A100 machine 80GB

| 字段 | 值 |
| --- | --- |
| Issue | [#11767](https://github.com/vllm-project/vllm/issues/11767) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen2-VL-72B-Instruct-GPTQ-Int4 model runs very slowly in A100 machine 80GB

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am extracting all the data from the image. I know i have the complex image. But it is taking 190 seconds for a single image. Even i am using chuncked_prefill=True and batched_tokens=max_tokens

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: B-Instruct-GPTQ-Int4 model runs very slowly in A100 machine 80GB feature request;stale ### 🚀 The feature, motivation and pitch I am extracting all the data from the image. I know i have the complex image. But it is taki...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Qwen2-VL-72B-Instruct-GPTQ-Int4 model runs very slowly in A100 machine 80GB feature request;stale ### 🚀 The feature, motivation and pitch I am extracting all the data from the image. I know i have the complex...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Qwen2-VL-72B-Instruct-GPTQ-Int4 model runs very slowly in A100 machine 80GB feature request;stale ### 🚀 The feature, motivation and pitch I am extracting all the data from the image. I know i have the complex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Qwen2-VL-72B-Instruct-GPTQ-Int4 model runs very slowly in A100 machine 80GB feature request;stale ### 🚀 The feature, motivation and pitch I am extracting all the data from the image. I know i have the complex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
