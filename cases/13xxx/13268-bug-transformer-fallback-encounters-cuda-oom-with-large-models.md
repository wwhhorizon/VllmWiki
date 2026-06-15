# vllm-project/vllm#13268: [Bug]: transformer fallback encounters CUDA OOM with large models

| 字段 | 值 |
| --- | --- |
| Issue | [#13268](https://github.com/vllm-project/vllm/issues/13268) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: transformer fallback encounters CUDA OOM with large models

### Issue 正文摘录

### Your current environment environment: vllm 0.7.2 ### 🐛 Describe the bug ```python3 from vllm import LLM llm = LLM( model="meta-llama/Llama-3.3-70B-Instruct", task="generate", tensor_parallel_size=8, model_impl="transformers", ) llm.apply_model(lambda model: print(model.__class__)) ``` But it encounters OOM error in `model_executor/models/transformers.py` line 144 ``` self.model: PreTrainedModel = AutoModel.from_config( self.config, attn_implementation="vllm", trust_remote_code=vllm_config.model_config.trust_remote_code, ) ``` It encounters OOM error when initializing the llama model in` modeling_llama.py` in transformers. It put all weights into the cuda:0 GPU. Did you tested large models? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: transformer fallback encounters CUDA OOM with large models bug;stale ### Your current environment environment: vllm 0.7.2 ### 🐛 Describe the bug ```python3 from vllm import LLM llm = LLM( model="meta-llama/Llama-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: transformer fallback encounters CUDA OOM with large models bug;stale ### Your current environment environment: vllm 0.7.2 ### 🐛 Describe the bug ```python3 from vllm import LLM llm = LLM( model="meta-llama/Llama-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: transformer fallback encounters CUDA OOM with large models bug;stale ### Your current environment environment: vllm 0.7.2 ### 🐛 Describe the bug ```python3 from vllm import LLM llm = LLM( model="meta-llama/Llama-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t environment: vllm 0.7.2 ### 🐛 Describe the bug ```python3 from vllm import LLM llm = LLM( model="meta-llama/Llama-3.3-70B-Instruct", task="generate", tensor_parallel_size=8, model_impl="transformers", ) llm.apply_mode...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: transformer fallback encounters CUDA OOM with large models bug;stale ### Your current environment environment: vllm 0.7.2 ### 🐛 Describe the bug ```python3 from vllm import LLM llm = LLM( model="meta-llama/Llama-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
