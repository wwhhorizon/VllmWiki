# vllm-project/vllm#19360: [Bug]: AttributeError: 'Llama_Nemotron_Nano_VL_Config' object has no attribute 'hidden_size'. Did you mean: 'vit_hidden_size'?

| 字段 | 值 |
| --- | --- |
| Issue | [#19360](https://github.com/vllm-project/vllm/issues/19360) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Llama_Nemotron_Nano_VL_Config' object has no attribute 'hidden_size'. Did you mean: 'vit_hidden_size'?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The model nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1 is causing a failure during vLLM server startup due to a missing hidden_size attribute in its Hugging Face config class (Llama_Nemotron_Nano_VL_Config). Error Trace (critical line): AttributeError: 'Llama_Nemotron_Nano_VL_Config' object has no attribute 'hidden_size'. Did you mean: 'vit_hidden_size'? How to reproduce: vllm serve nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1 --host 0.0.0.0 --port 7000 --trust-remote-code Additionally to run this model via vLLM we need to install: "timm", "open-clip-torch", "einops", "accelerate" libraries. The model works fine via HF: # Use a pipeline as a high-level helper from transformers import pipeline pipe = pipeline("image-text-to-text", model="nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1") ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: AttributeError: 'Llama_Nemotron_Nano_VL_Config' object has no attribute 'hidden_size'. Did you mean: 'vit_hidden_size'? bug;stale ### Your current environment ### 🐛 Describe the bug The model nvidia/Llama-3.1-Nem...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 0 --trust-remote-code Additionally to run this model via vLLM we need to install: "timm", "open-clip-torch", "einops", "accelerate" libraries. The model works fine via HF: # Use a pipeline as a high-level helper from tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 1") ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: frontend_api;hardware_porting;model_support;multimodal_vlm cuda;operator;triton build_error env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: has no attribute 'hidden_size'. Did you mean: 'vit_hidden_size'? How to reproduce: vllm serve nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1 --host 0.0.0.0 --port 7000 --trust-remote-code Additionally to run this model via vLL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
