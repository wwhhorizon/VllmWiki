# vllm-project/vllm#5298: [Bug]: After fine-tuning Qwen Lora, the inference results differ when using VLLM and Hugging Face to load

| 字段 | 值 |
| --- | --- |
| Issue | [#5298](https://github.com/vllm-project/vllm/issues/5298) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: After fine-tuning Qwen Lora, the inference results differ when using VLLM and Hugging Face to load

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug https://github.com/hiyouga/LLaMA-Factory/issues/4049 transformers+lora ![image](https://github.com/vllm-project/vllm/assets/40717349/afe5aa23-f83d-403d-b3ae-12d651128d4e) vllm+lora ![image](https://github.com/vllm-project/vllm/assets/40717349/6dfd9014-736f-4708-b2b0-0f1183a86b36)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: After fine-tuning Qwen Lora, the inference results differ when using VLLM and Hugging Face to load bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: he inference results differ when using VLLM and Hugging Face to load bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug https://github.com/hiyouga/LLaMA-Facto...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
