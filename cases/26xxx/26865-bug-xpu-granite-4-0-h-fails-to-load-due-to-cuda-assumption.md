# vllm-project/vllm#26865: [Bug]: XPU - granite-4.0-h fails to load due to CUDA assumption

| 字段 | 值 |
| --- | --- |
| Issue | [#26865](https://github.com/vllm-project/vllm/issues/26865) |
| 状态 | closed |
| 标签 | bug;intel-gpu;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: XPU - granite-4.0-h fails to load due to CUDA assumption

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to serve IBM Granite 4 H model with command `vllm serve ibm-granite/granite-4.0-h-micro --dtype half --max-model-len 12K --gpu-memory-utilization 0.8 -O0`, with Intel Arc A770 GPU results in the following error: ``` (EngineCore_DP0 pid=261057) File "/mnt/Mediaz/Projekt/LLMao/localenv/lib/python3.12/site-packages/vllm-0.11.0+xpu-py3.12.egg/vllm/v1/attention/backends/mamba_attn.py", line 29, in __init__ (EngineCore_DP0 pid=261057) self.decode_cudagraph_max_bs = min( (EngineCore_DP0 pid=261057) ^^^^ (EngineCore_DP0 pid=261057) TypeError: '<' not supported between instances of 'NoneType' and 'int' ``` Offending line in code: https://github.com/vllm-project/vllm/blob/v0.11.0/vllm/v1/attention/backends/mamba_attn.py#L29-L31 CUDA supremacy strikes again 🤦 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;triton build_error;nan_inf dtype;env...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: : XPU - granite-4.0-h fails to load due to CUDA assumption bug;intel-gpu;stale ### Your current environment ### 🐛 Describe the bug Trying to serve IBM Granite 4 H model with command `vllm serve ibm-granite/granite-4.0-h...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ib/python3.12/site-packages/vllm-0.11.0+xpu-py3.12.egg/vllm/v1/attention/backends/mamba_attn.py", line 29, in __init__ (EngineCore_DP0 pid=261057) self.decode_cudagraph_max_bs = min( (EngineCore_DP0 pid=261057) ^^^^ (En...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: XPU - granite-4.0-h fails to load due to CUDA assumption bug;intel-gpu;stale ### Your current environment ### 🐛 Describe the bug Trying to serve IBM Granite 4 H model with command `vllm serve ibm-granite/granite-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ite 4 H model with command `vllm serve ibm-granite/granite-4.0-h-micro --dtype half --max-model-len 12K --gpu-memory-utilization 0.8 -O0`, with Intel Arc A770 GPU results in the following error: ``` (EngineCore_DP0 pid=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
