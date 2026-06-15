# vllm-project/vllm#13053: [Bug]: Encoder self-attention and encoder/decoder cross-attention are not implemented for HPUAttentionImpl when using Gaudi2

| 字段 | 值 |
| --- | --- |
| Issue | [#13053](https://github.com/vllm-project/vllm/issues/13053) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Encoder self-attention and encoder/decoder cross-attention are not implemented for HPUAttentionImpl when using Gaudi2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Build vLLM using: ``` docker build -t vllm-hpu:v0.7.2-mainline -f Dockerfile.hpu . ``` Then run it using: ``` "vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct --disable_log_requests --max_num_batched_tokens 10240 --max_model_len 10240 --tensor-parallel-size 2 --port 8080" ``` The hardware is a node with 8 Gaudi 2 HL-225H mezzanine cards with 2x Xeon 8380 Processors. The container has 2 Gaudi 2 cards, 70Gi memory and 25Gi of hugepages-2Mi assigned to it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: audi2 bug;stale ### Your current environment ### 🐛 Describe the bug Build vLLM using: ``` docker build -t vllm-hpu:v0.7.2-mainline -f Dockerfile.hpu . ``` Then run it using: ``` "vllm serve meta-llama/Llama-3.2-11B-Visi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Encoder self-attention and encoder/decoder cross-attention are not implemented for HPUAttentionImpl when using Gaudi2 bug;stale ### Your current environment ### 🐛 Describe the bug Build vLLM using: ``` docker bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: inline -f Dockerfile.hpu . ``` Then run it using: ``` "vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct --disable_log_requests --max_num_batched_tokens 10240 --max_model_len 10240 --tensor-parallel-size 2 --port 8080...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rt;sampling_logits;speculative_decoding attention;cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
