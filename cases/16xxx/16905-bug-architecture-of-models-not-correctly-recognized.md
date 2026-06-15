# vllm-project/vllm#16905: [Bug]: architecture of models not correctly recognized

| 字段 | 值 |
| --- | --- |
| Issue | [#16905](https://github.com/vllm-project/vllm/issues/16905) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: architecture of models not correctly recognized

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried several models to run in latest vllm, but although the vllm documentation says the model is supported, during runtime it says the architecture is not yet supported. It seems that there is a mismatch between the expected model identifier and the actual one found. The documentation e.g. says OLMo2, but in the error message it says olmo2. I use the official GGUF from AllenAI. Therefore, it should not be the problem of the model. The same applies for Nvidia Nemotron. The vllm documentation says DeciLM is supported, but during runtime it says GGUF model with architecture deci is not supported yet. Qwen QwQ on the other hand is loading without any problems with the same setup. from huggingface_hub import hf_hub_download from vllm import LLM, SamplingParams model_id = "allenai/OLMo-2-0325-32B-Instruct" repo_id = "allenai/OLMo-2-0325-32B-Instruct-GGUF" filename = "OLMo-2-0325-32B-Instruct-Q4_K_S.gguf" model = hf_hub_download(repo_id, filename=filename) llm = LLM(model=model, tokenizer=model_id, max_model_len = 8192, gpu_memory_utilization=0.80) ### Before submitting a new issue... - [x] Make sure you already searched for relevant...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n e.g. says OLMo2, but in the error message it says olmo2. I use the official GGUF from AllenAI. Therefore, it should not be the problem of the model. The same applies for Nvidia Nemotron. The vllm documentation says De...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: architecture of models not correctly recognized bug;stale ### Your current environment ### 🐛 Describe the bug I tried several models to run in latest vllm, but although the vllm documentation says the model is su...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: architecture of models not correctly recognized bug;stale ### Your current environment ### 🐛 Describe the bug I tried several models to run in latest vllm, but although the vllm documentation says the model is su...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: architecture of models not correctly recognized bug;stale ### Your current environment ### 🐛 Describe the bug I tried several models to run in latest vllm, but although the vllm documentation says the model is su...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
