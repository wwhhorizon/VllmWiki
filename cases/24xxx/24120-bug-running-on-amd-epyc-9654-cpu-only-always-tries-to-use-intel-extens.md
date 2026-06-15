# vllm-project/vllm#24120: [Bug]: Running on AMD Epyc 9654 (CPU Only) always tries to use intel_extension_for_pytorch and crashes.

| 字段 | 值 |
| --- | --- |
| Issue | [#24120](https://github.com/vllm-project/vllm/issues/24120) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Running on AMD Epyc 9654 (CPU Only) always tries to use intel_extension_for_pytorch and crashes.

### Issue 正文摘录

### Your current environment Docker build with official cpu instruction (using pip not uv) ### 🐛 Describe the bug I used a lot of thing to uninstall the intel extension for pytorch, modyfing the requirements (cpu.txt) before the build... but it always end up being imported, and when I start a chat with a random question, it always crash while importing this extension, example: `(EngineCore_0 pid=175) File "/usr/local/lib/python3.12/site-packages/vllm-0.10.2rc2.dev36+g98aee612a.d20250902.cpu-py3.12-linux-x86_64.egg/vllm/v1/attention/backends/cpu_attn.py", line 589, in forward (EngineCore_0 pid=175) import intel_extension_for_pytorch.llm.modules as ipex_modules EngineCore_0 pid=175) File "/usr/local/lib/python3.12/site-packages/vllm-0.10.2rc2.dev36+g98aee612a.d2 250902.cpu-py3.12-linux-x86_64.egg/vllm/v1/attention/backends/cpu_attn.py", line 589, in forward EngineCore_0 pid=175) import intel_extension_for_pytorch.llm.modules as ipex_modules (EngineCore_0 pid=175) ModuleNotFoundError: No module named 'intel_extension_for_pytorch' ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: sion_for_pytorch and crashes. bug;stale ### Your current environment Docker build with official cpu instruction (using pip not uv) ### 🐛 Describe the bug I used a lot of thing to uninstall the intel extension for pytorc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: dev36+g98aee612a.d20250902.cpu-py3.12-linux-x86_64.egg/vllm/v1/attention/backends/cpu_attn.py", line 589, in forward (EngineCore_0 pid=175) import intel_extension_for_pytorch.llm.modules as ipex_modules EngineCore_0 pid...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ' ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: U Only) always tries to use intel_extension_for_pytorch and crashes. bug;stale ### Your current environment Docker build with official cpu instruction (using pip not uv) ### 🐛 Describe the bug I used a lot of thing to u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sked questions. correctness attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;triton build_error;crash;import_error;nan_inf env_dependency Y...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
