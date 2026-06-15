# vllm-project/vllm#15958: [Bug]: SpecDecoding metrics showing with disabled spec decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#15958](https://github.com/vllm-project/vllm/issues/15958) |
| 状态 | closed |
| 标签 | bug;speculative-decoding;v1 |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SpecDecoding metrics showing with disabled spec decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I just happened to start llava on main (`44f990515`) no spec decoding with `vllm serve llava-hf/llava-1.5-7b-hf --max-model-len 2512 --max-num-seqs 16 --max-num-batched-tokens 64 --chat-template examples/template_llava.jinja`. I am getting a lot of clutter in the logs: ``` INFO 04-02 18:03:41 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 50.0% INFO 04-02 18:03:41 [metrics.py:53] SpecDecoding metrics: Draft acceptance rate: nan%, Accepted: 0 tokens, Drafted: 0 tokens INFO 04-02 18:03:51 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 50.0% INFO 04-02 18:03:51 [metrics.py:53] SpecDecoding metrics: Draft acceptance rate: nan%, Accepted: 0 tokens, Drafted: 0 tokens INFO 04-02 18:04:01 [loggers.py:87] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tart llava on main (`44f990515`) no spec decoding with `vllm serve llava-hf/llava-1.5-7b-hf --max-model-len 2512 --max-num-seqs 16 --max-num-batched-tokens 64 --chat-template examples/template_llava.jinja`. I am getting...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: SpecDecoding metrics showing with disabled spec decoding bug;speculative-decoding;v1 ### Your current environment ### 🐛 Describe the bug I just happened to start llava on main (`44f990515`) no spec decoding with...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding cache;cuda;opera...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: mc ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 50.0% INFO 04-02 18:03:41 [metrics.py:53] SpecDecoding metrics: Draft acceptance rate: nan%, Accepted...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
