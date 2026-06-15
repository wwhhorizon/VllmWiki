# vllm-project/vllm#24459: [Bug]: Vllm Deepseek-R1 Reasoning Parser error

| 字段 | 值 |
| --- | --- |
| Issue | [#24459](https://github.com/vllm-project/vllm/issues/24459) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Vllm Deepseek-R1 Reasoning Parser error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Deepseek-R1 Reasoning Parser returns both `content` and `reasoning_content` ```python ## Server export VLLM_USE_V1=1 export VLLM_MLA_DISABLE=1 export HF_HUB_CACHE=/fsx/deepseek/hf_cache export VLLM_USE_MMAP=1 export VLLM_WORKER_THREADS=64 vllm serve deepseek-ai/DeepSeek-R1 \ --port=8000 \ --max-model-len=8192 \ --max-num-batched-tokens=16384 \ --gpu_memory_utilization 0.9 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 1 \ --enable-chunked-prefill \ --trust-remote-code \ --speculative-config='{"method": "deepseek_mtp", "num_speculative_tokens": 1}' \ --reasoning-parser deepseek_r1 ## Request curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "deepseek-ai/DeepSeek-R1", "messages": [ {"role": "user", "content": "Repeat back to this exact sentence- Based on the information provided"}, {"role": "user", "content": "Repeat the following sentence - can sauces be fried?"} ], "stream": true, "max_tokens": 1024, "temperature": 0.7 }' ``` Output: ``` data: {"id":"chatcmpl-795c8a3dc4724b4ca2a43562d5cc3041","object":"chat.completion.chunk","created":1757039644,"model":"deepseek-ai/DeepS...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `python ## Server export VLLM_USE_V1=1 export VLLM_MLA_DISABLE=1 export HF_HUB_CACHE=/fsx/deepseek/hf_cache export VLLM_USE_MMAP=1 export VLLM_WORKER_THREADS=64 vllm serve deepseek-ai/DeepSeek-R1 \ --port=8000 \ --max-m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Vllm Deepseek-R1 Reasoning Parser error bug;stale ### Your current environment ### 🐛 Describe the bug Deepseek-R1 Reasoning Parser returns both `content` and `reasoning_content` ```python ## Server export VLLM_US...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
