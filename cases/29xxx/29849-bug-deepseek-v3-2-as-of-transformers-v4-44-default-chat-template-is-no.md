# vllm-project/vllm#29849: [Bug]: DeepSeek-V3.2 As of transformers v4.44, default chat template is no longer allowed, so you must provide a chat template if the tokenizer does not define one

| 字段 | 值 |
| --- | --- |
| Issue | [#29849](https://github.com/vllm-project/vllm/issues/29849) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V3.2 As of transformers v4.44, default chat template is no longer allowed, so you must provide a chat template if the tokenizer does not define one

### Issue 正文摘录

### Your current environment vllm:v0.11.2 ### 🐛 Describe the bug Using vllm to deploy the latest deepseek-v3.2 model the deployment was successful `vllm server --model /workspace/LLM_Weights/deepseek-ai/DeepSeek-V3.2 --port 40001 --host 0.0.0.0 --trust-remote-code --served-model-name deepseek-v3.2-new --max-model-len 131072 --gpu-memory-utilization 0.95 -dp 8 --enable-expert-parallel --max-num-seqs 256` an error occurred when invoking it `ValueError: As of transformers v4.44, default chat template is no longer allowed, so you must provide a chat template if the tokenizer does not define one.` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 2 ### 🐛 Describe the bug Using vllm to deploy the latest deepseek-v3.2 model the deployment was successful `vllm server --model /workspace/LLM_Weights/deepseek-ai/DeepSeek-V3.2 --port 40001 --host 0.0.0.0 --trust-remote...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: -new --max-model-len 131072 --gpu-memory-utilization 0.95 -dp 8 --enable-expert-parallel --max-num-seqs 256` an error occurred when invoking it `ValueError: As of transformers v4.44, default chat template is no longer a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ou must provide a chat template if the tokenizer does not define one bug;stale ### Your current environment vllm:v0.11.2 ### 🐛 Describe the bug Using vllm to deploy the latest deepseek-v3.2 model the deployment was succ...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: onment vllm:v0.11.2 ### 🐛 Describe the bug Using vllm to deploy the latest deepseek-v3.2 model the deployment was successful `vllm server --model /workspace/LLM_Weights/deepseek-ai/DeepSeek-V3.2 --port 40001 --host 0.0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
