# vllm-project/vllm#6575: [Bug]: CUDA Error when print 

| 字段 | 值 |
| --- | --- |
| Issue | [#6575](https://github.com/vllm-project/vllm/issues/6575) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA Error when print 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I am new to vllm, I want to check input to llama model, so I just print ![image](https://github.com/user-attachments/assets/d8489d1f-4f25-48a5-8867-2e96d11f54bb) However, it raise cuda bug. Why? And how can I get input? ![image](https://github.com/user-attachments/assets/cf821f7c-395b-4f60-a64a-a4b651f14a4e) Thanks!!!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ``` ### 🐛 Describe the bug I am new to vllm, I want to check input to llama model, so I just print ![image](https://github.com/user-attachments/assets/d8489d1f-4f25-48a5-8867-2e96d11f54bb) However, it raise cuda bug. Wh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 5b-4f60-a64a-a4b651f14a4e) Thanks!!! development model_support cuda env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: CUDA Error when print bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I am new to vllm, I want to check input to llama model, so I just print ![imag...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: CUDA Error when print bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I am new to vllm, I want to check input to llama model, so I just print ![imag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
