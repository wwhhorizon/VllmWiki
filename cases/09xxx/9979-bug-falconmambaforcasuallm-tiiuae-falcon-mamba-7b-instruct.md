# vllm-project/vllm#9979: [Bug]: falconmambaForCasualLM- tiiuae/falcon-mamba-7b-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#9979](https://github.com/vllm-project/vllm/issues/9979) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: falconmambaForCasualLM- tiiuae/falcon-mamba-7b-instruct

### Issue 正文摘录

### Your current environment I tried to deploy falcon-mamba-7b-instruct (tiiuae/falcon-mamba-7b-instruct)model from huggingace by using VLLM. But unfortunately i get an error like model architectures are not available now. Then, I ran tiiuae/falcon-7b-instruct model, and it is working fine without any errors. But, I want to run the tiiuae/falcon-mamba-7b-instructmodel without any errors. How can I fix this? Do I need to change any versions of the VLLM. I already tried with the latest and some other versions. Is there any specific version to use? ### Model Input Dumps ![image](https://github.com/user-attachments/assets/96f0536b-d0f6-44a7-bb7f-d13026874423) ### 🐛 Describe the bug I tried to deploy falcon-mamba-7b-instruct (tiiuae/falcon-mamba-7b-instruct)model from huggingace by using VLLM. But unfortunately i get an error like model architectures are not available now. Then, I ran tiiuae/falcon-7b-instruct model, and it is working fine without any errors. But, I want to run the tiiuae/falcon-mamba-7b-instructmodel without any errors. How can I fix this? Do I need to change any versions of the VLLM. I already tried with the latest and some other versions. Is there any specific versi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: uctmodel without any errors. How can I fix this? Do I need to change any versions of the VLLM. I already tried with the latest and some other versions. Is there any specific version to use? ### Model Input Dumps ![image...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: om huggingace by using VLLM. But unfortunately i get an error like model architectures are not available now. Then, I ran tiiuae/falcon-7b-instruct model, and it is working fine without any errors. But, I want to run th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ied to deploy falcon-mamba-7b-instruct (tiiuae/falcon-mamba-7b-instruct)model from huggingace by using VLLM. But unfortunately i get an error like model architectures are not available now. Then, I ran tiiuae/falcon-7b-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: falconmambaForCasualLM- tiiuae/falcon-mamba-7b-instruct bug;stale ### Your current environment I tried to deploy falcon-mamba-7b-instruct (tiiuae/falcon-mamba-7b-instruct)model from huggingace by using VLLM. But...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Do I need to change any versions of the VLLM. I already tried with the latest and some other versions. Is there any specific version to use? ### Model Input Dumps ![image](https://github.com/user-attachments/assets/96f0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
