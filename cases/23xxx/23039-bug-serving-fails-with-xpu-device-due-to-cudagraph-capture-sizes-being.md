# vllm-project/vllm#23039: [Bug]: Serving fails with XPU device due to cudagraph_capture_sizes being None

| 字段 | 值 |
| --- | --- |
| Issue | [#23039](https://github.com/vllm-project/vllm/issues/23039) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Serving fails with XPU device due to cudagraph_capture_sizes being None

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to serve a model on XPU device (Intel Arc A770 in my case), vLLM fails with `RuntimeError: Engine core initialization failed.` which stems from this error: ``` (EngineCore_0 pid=20166) File "xpu_model_runner.py", line 25, in __init__ (EngineCore_0 pid=20166) super().__init__(vllm_config, device) (EngineCore_0 pid=20166) File "gpu_model_runner.py", line 236, in __init__ (EngineCore_0 pid=20166) reversed(self.compilation_config.cudagraph_capture_sizes)) (EngineCore_0 pid=20166) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_0 pid=20166) TypeError: 'NoneType' object is not reversible ``` gotta love CUDA monopoly 🤦 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Serving fails with XPU device due to cudagraph_capture_sizes being None bug ### Your current environment ### 🐛 Describe the bug When trying to serve a model on XPU device (Intel Arc A770 in my case), vLLM fails w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r current environment ### 🐛 Describe the bug When trying to serve a model on XPU device (Intel Arc A770 in my case), vLLM fails with `RuntimeError: Engine core initialization failed.` which stems from this error: ``` (E...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ons. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
