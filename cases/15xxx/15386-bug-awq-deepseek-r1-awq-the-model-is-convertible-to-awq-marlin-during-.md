# vllm-project/vllm#15386: [Bug]: awq Deepseek-R1-AWQ  The model is convertible to awq_marlin during runtime. Using awq_marlin kernel.

| 字段 | 值 |
| --- | --- |
| Issue | [#15386](https://github.com/vllm-project/vllm/issues/15386) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: awq Deepseek-R1-AWQ  The model is convertible to awq_marlin during runtime. Using awq_marlin kernel.

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/231880dd-5827-4f65-9ca8-9aa4de0a612f) vllm==0.8.1 0.8.2 0.8.3.dev5+g5797fb97.precompiled https://huggingface.co/cognitivecomputations/DeepSeek-R1-AWQ Concurrent use will result in the error message shown in the figure. ### 🐛 Describe the bug The following is the execution script model_path=/home/ds-r1/models/DeepSeek-R1-awq vllm serve $model_path \ --port 23344 \ --host 0.0.0.0 \ --tensor-parallel-size 8 \ --max-model-len 16000 \ --dtype bfloat16 \ --gpu-memory-utilization 0.9 \ --trust-remote-code \ --served-model-name deepseek-r1 \ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: .0.0 \ --tensor-parallel-size 8 \ --max-model-len 16000 \ --dtype bfloat16 \ --gpu-memory-utilization 0.9 \ --trust-remote-code \ --served-model-name deepseek-r1 \ ### Before submitting a new issue... - [x] Make sure yo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: awq Deepseek-R1-AWQ The model is convertible to awq_marlin during runtime. Using awq_marlin kernel. bug;stale ### Your current environment ![Image](https://github.com/user-attachments/assets/231880dd-5827-4f65-9c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d-5827-4f65-9ca8-9aa4de0a612f) vllm==0.8.1 0.8.2 0.8.3.dev5+g5797fb97.precompiled https://huggingface.co/cognitivecomputations/DeepSeek-R1-AWQ Concurrent use will result in the error message shown in the figure. ### 🐛 D...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 1 \ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s convertible to awq_marlin during runtime. Using awq_marlin kernel. bug;stale ### Your current environment ![Image](https://github.com/user-attachments/assets/231880dd-5827-4f65-9ca8-9aa4de0a612f) vllm==0.8.1 0.8.2 0.8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
