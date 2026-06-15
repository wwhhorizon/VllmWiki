# vllm-project/vllm#30238: [Bug]: Kimi-K2-Thinking vLLM self host tool call fail

| 字段 | 值 |
| --- | --- |
| Issue | [#30238](https://github.com/vllm-project/vllm/issues/30238) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi-K2-Thinking vLLM self host tool call fail

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CUDA ARCH sm120 Driver Version: 580.95.05 CUDA Version: 13.0 OS Ubuntu 22.04 Linux 6.8.0-87-generic x86_64 x86_64 vllm 0.11.2.dev618+ga238cbd89.d20251206.cu130 8x NVIDIA RTX PRO 6000 Blackwell Workstation 96GB vllm serve Kimi-K2-Thinking \ --served-model-name llm_model \ --tensor-parallel-size 8 \ --decode-context-parallel-size 8 \ --enable-auto-tool-choice \ --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k2 \ --trust-remote-code \ --gpu-memory-utilization 0.90 \ --max-model-len 262144 \ --port 9999 \ kimi cli { "default_model": "", "models": {"kimi": { "provider": "openai", "model": "llm_model", "max_context_size": 160000 }}, "providers": {"openai": { "type": "openai_legacy", "base_url": "http://localhost:9999/v1", "api_key": "your-secret-key" }}, "loop_control": { "max_steps_per_run": 100, "max_retries_per_step": 3 }, "services": {} } kimi, version 0.61 kimi -m kimi user@20251130_base_model✨ what is this repo about ╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮ │...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ail bug;unstale ### Your current environment ### 🐛 Describe the bug CUDA ARCH sm120 Driver Version: 580.95.05 CUDA Version: 13.0 OS Ubuntu 22.04 Linux 6.8.0-87-generic x86_64 x86_64 vllm 0.11.2.dev618+ga238cbd89.d202512...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r current environment ### 🐛 Describe the bug CUDA ARCH sm120 Driver Version: 580.95.05 CUDA Version: 13.0 OS Ubuntu 22.04 Linux 6.8.0-87-generic x86_64 x86_64 vllm 0.11.2.dev618+ga238cbd89.d20251206.cu130 8x NVIDIA RTX...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Kimi-K2-Thinking vLLM self host tool call fail bug;unstale ### Your current environment ### 🐛 Describe the bug CUDA ARCH sm120 Driver Version: 580.95.05 CUDA Version: 13.0 OS Ubuntu 22.04 Linux 6.8.0-87-generic x...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 000 Blackwell Workstation 96GB vllm serve Kimi-K2-Thinking \ --served-model-name llm_model \ --tensor-parallel-size 8 \ --decode-context-parallel-size 8 \ --enable-auto-tool-choice \ --tool-call-parser kimi_k2 \ --reaso...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
