# vllm-project/vllm#21071: [Feature]: DeepSeek-R1-0528-GGUF (IQ1_S_R4)

| 字段 | 值 |
| --- | --- |
| Issue | [#21071](https://github.com/vllm-project/vllm/issues/21071) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: DeepSeek-R1-0528-GGUF (IQ1_S_R4)

### Issue 正文摘录

### 🚀 The feature request Is there any plan for vLLM to support GGUF models like DeepSeek-R1-0528-GGUF (IQ1_S_R4) [1]? If not, could it be considered on the roadmap? Expected result: Functional behavior with this (or similar) launch command: ` export VLLM_USE_V1=1; \ export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7; \ python3 -m vllm.entrypoints.openai.api_server \ --model /home/user/DeepSeek-R1-0528-IQ1_S_R4.gguf \ --port 11435 \ --host 0.0.0.0 \ --hf-config-path /home/user/orig-repo-deepseek-config5/ \ --tokenizer /home/user/orig-repo-deepseek-config5/ \ --tensor-parallel-size 8 \ --served-model-name deepseek \ --max-model-len 10000 \ --gpu-memory-utilization 0.95 \ --enforce-eager ` [1] [https://huggingface.co/ubergarm/DeepSeek-R1-0528-GGUF/tree/main/IQ1_S_R4](https://huggingface.co/ubergarm/DeepSeek-R1-0528-GGUF/tree/main/IQ1_S_R4) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: le ### 🚀 The feature request Is there any plan for vLLM to support GGUF models like DeepSeek-R1-0528-GGUF (IQ1_S_R4) [1]? If not, could it be considered on the roadmap? Expected result: Functional behavior with this (or...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: with this (or similar) launch command: ` export VLLM_USE_V1=1; \ export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7; \ python3 -m vllm.entrypoints.openai.api_server \ --model /home/user/DeepSeek-R1-0528-IQ1_S_R4.gguf \ --port...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: DeepSeek-R1-0528-GGUF (IQ1_S_R4) feature request;stale ### 🚀 The feature request Is there any plan for vLLM to support GGUF models like DeepSeek-R1-0528-GGUF (IQ1_S_R4) [1]? If not, could it be considered on...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
