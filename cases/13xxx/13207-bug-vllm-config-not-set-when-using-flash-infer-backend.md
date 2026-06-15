# vllm-project/vllm#13207: [Bug]: VLLM config not set when using Flash Infer backend.

| 字段 | 值 |
| --- | --- |
| Issue | [#13207](https://github.com/vllm-project/vllm/issues/13207) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM config not set when using Flash Infer backend.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Bug: With flashinfer backend, a warning `Current VLLM config is not set.` is constantly raised during cuda graph capturing. This warning is not supposed to exist when we run the end-to-end LLM inference. ### A Minimal Working Example ```python from vllm import LLM, SamplingParams prompts = ["Hello, my name is",] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) ``` Store the above code in `mwe.py`, then run ```bash TORCH_CUDA_ARCH_LIST="9.0" VLLM_ATTENTION_BACKEND=FLASHINFER python mwe.py ``` Observed Result: During cuda graph capturing, `WARNING 02-12 21:04:28 config.py:3432] Current VLLM config is not set.` is repeatedly raised. ### Bug Analysis and Proposed Fix The bug is related to a recent flashinfer update (https://github.com/vllm-project/vllm/pull/11194). After this update, the flashinfer backend uses `get_current_vllm_config()` to fetch the vllm config stored as a global variable in [vllm/config.py](https://github.com/vllm-project/vllm/blob/main/vllm/config.py#L3383). However, the global variable is not set beforehand, which...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: -end LLM inference. ### A Minimal Working Example ```python from vllm import LLM, SamplingParams prompts = ["Hello, my name is",] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: VLLM config not set when using Flash Infer backend. bug ### Your current environment ### 🐛 Describe the bug Bug: With flashinfer backend, a warning `Current VLLM config is not set.` is constantly raised during cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: a warning `Current VLLM config is not set.` is constantly raised during cuda graph capturing. This warning is not supposed to exist when we run the end-to-end LLM inference. ### A Minimal Working Example ```python from...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: VLLM config not set when using Flash Infer backend. bug ### Your current environment ### 🐛 Describe the bug Bug: With flashinfer backend, a warning `Current VLLM config is not set.` is constantly raised during cu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
