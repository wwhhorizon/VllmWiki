# vllm-project/vllm#8698: [Bug]: Low trhoughput on AMD MI250 using llama 3.1 (6 toks/s)

| 字段 | 值 |
| --- | --- |
| Issue | [#8698](https://github.com/vllm-project/vllm/issues/8698) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Low trhoughput on AMD MI250 using llama 3.1 (6 toks/s)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm running vllm serve with `vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --trust-remote-code --tokenizer meta-llama/Meta-Llama-3.1-8B-Instruct --max-num-seqs 1024 --max-num-batched-tokens 1024`. When I send requests to the vllm api, I monitor the gpu usage, it reaches 100% usage and memory usage above 90%, therefore, the GPU is being used but the trhoughput is between 3-6 tok/s. I'm using rocm 6.1.2, and I installed vllm from source (main 1c1bb388e0d35a2d10da5c5cda2edac57bf62591). To give a comparison, ollama with llama3.1 get's 85 toks/s with the same rocm version. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: sed but the trhoughput is between 3-6 tok/s. I'm using rocm 6.1.2, and I installed vllm from source (main 1c1bb388e0d35a2d10da5c5cda2edac57bf62591). To give a comparison, ollama with llama3.1 get's 85 toks/s with the sa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Low trhoughput on AMD MI250 using llama 3.1 (6 toks/s) bug;rocm ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm running vllm serve with `vllm serve meta-llama/Meta-Llam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Low trhoughput on AMD MI250 using llama 3.1 (6 toks/s) bug;rocm ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm running vllm serve with `vllm serve meta-llama/Meta-Llam...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Instruct --max-num-seqs 1024 --max-num-batched-tokens 1024`. When I send requests to the vllm api, I monitor the gpu usage, it reaches 100% usage and memory usage above 90%, therefore, the GPU is being used but the trho...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
