# vllm-project/vllm#12142: [Bug]: High and unstable CPU usage when deployed on GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#12142](https://github.com/vllm-project/vllm/issues/12142) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: High and unstable CPU usage when deployed on GPU

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I deployed the llama3.1-8B on 4 H200s. Each vLLM container has one H200. When given Queries Per Second 25 on real traffic (real time conversations, it can be 8000 input tokens, 600 output tokens, nearly no KV cache reuse), the CPU usages is very high and unstable. ![Image](https://github.com/user-attachments/assets/8f4d10bf-1c2b-4814-aae1-bc05d86ac5d4) The CPU memory is still very stable. It also decreased the usage of GPU (it should be around 97% if stable). ![Image](https://github.com/user-attachments/assets/b75cdcc5-368c-4362-8c95-1edbaf933179) I just used the default vLLM image with --max_model_len 33000 --disable-log-requests. I would highly appreciate it if vLLM team or someone can give me some suggestions!! :) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: with --max_model_len 33000 --disable-log-requests. I would highly appreciate it if vLLM team or someone can give me some suggestions!! :) ### Before submitting a new issue... - [x] Make sure you already searched for rel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: High and unstable CPU usage when deployed on GPU bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I deployed the llama3.1-8B on 4 H200s. Each vLLM container has on...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: :) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sage when deployed on GPU bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I deployed the llama3.1-8B on 4 H200s. Each vLLM container has one H200. When given Queries Per...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: upport;sampling_logits;speculative_decoding cache;cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
