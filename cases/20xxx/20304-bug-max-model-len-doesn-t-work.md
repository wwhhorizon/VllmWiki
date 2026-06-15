# vllm-project/vllm#20304: [Bug]: --max-model-len doesn't work

| 字段 | 值 |
| --- | --- |
| Issue | [#20304](https://github.com/vllm-project/vllm/issues/20304) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --max-model-len doesn't work

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am starting the LLM inference service using the `vllm serve` command. When I set `--max-model-len` to 32768, the log shows that `max_model_len` is indeed 32768, but the actual `max_seq_len` of the engine is 16384. When the inference service starts successfully, I am indeed unable to input content longer than 16384, which means my `--max-model-len` setting is not taking effect. This issue did not occur when I was using v9.0.1. This is the command that i'm using. ```bash vllm serve /DeepSeek-R1-Distill-Qwen-32B --trust-remote-code --tensor-parallel-size 2 --port 9990 --enable-prefix-caching --enable-chunked-prefill --max-model-len 32768 ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: x-caching --enable-chunked-prefill --max-model-len 32768 ``` correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: --max-model-len doesn't work bug ### Your current environment ### 🐛 Describe the bug I am starting the LLM inference service using the `vllm serve` command. When I set `--max-model-len` to 32768, the log shows th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: sor-parallel-size 2 --port 9990 --enable-prefix-caching --enable-chunked-prefill --max-model-len 32768 ``` correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
