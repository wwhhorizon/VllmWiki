# vllm-project/vllm#18767: [Bug]: Low GPU Underutilization and Badwords Failure When Rollout n > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#18767](https://github.com/vllm-project/vllm/issues/18767) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Low GPU Underutilization and Badwords Failure When Rollout n > 1

### Issue 正文摘录

### Your current environment we tried vllm 0.6.3 to use logits_processor and vllm 0.8.2 for badwords ### 🐛 Describe the bug When enabling badwords in the generation pipeline, I observed severe GPU underutilization and a functional issue where badwords become ineffective if the rollout batch size n is set greater than 1. 1. Severe GPU Underutilization with Badwords Enabled Without badwords: GPU utilization is high (81%-85%) as expected. With badwords enabled: GPU utilization drops dramatically to about 12% (see attached screenshots). This leads to significant slowdown in generation throughput, making the system almost unusable for large-scale inference/training. 2. Badwords Ineffective When n > 1 When running rollouts with n > 1, the badwords filter does not work — forbidden tokens are not properly suppressed, and undesired sequences appear in outputs. This defeats the core purpose of the badwords feature for batch or parallel rollout scenarios. ![Image](https://github.com/user-attachments/assets/0bec87fb-6414-499a-ba12-adf2fcd5883c) ![Image](https://github.com/user-attachments/assets/910b155a-32c6-4f21-bb8f-fb2d981662fd) ### Before submitting a new issue... - [x] Make sure you alr...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ached screenshots). This leads to significant slowdown in generation throughput, making the system almost unusable for large-scale inference/training. 2. Badwords Ineffective When n > 1 When running rollouts with n > 1,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: wn in generation throughput, making the system almost unusable for large-scale inference/training. 2. Badwords Ineffective When n > 1 When running rollouts with n > 1, the badwords filter does not work — forbidden token...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: fd) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g]: Low GPU Underutilization and Badwords Failure When Rollout n > 1 bug;stale ### Your current environment we tried vllm 0.6.3 to use logits_processor and vllm 0.8.2 for badwords ### 🐛 Describe the bug When enabling ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
