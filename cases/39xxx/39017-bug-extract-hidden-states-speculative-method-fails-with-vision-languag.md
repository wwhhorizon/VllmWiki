# vllm-project/vllm#39017: [Bug]: extract_hidden_states speculative method fails with vision-language models (e.g. Qwen2.5-VL)

| 字段 | 值 |
| --- | --- |
| Issue | [#39017](https://github.com/vllm-project/vllm/issues/39017) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: extract_hidden_states speculative method fails with vision-language models (e.g. Qwen2.5-VL)

### Issue 正文摘录

## Your current environment - vLLM version: 0.18.0 - PyTorch: 2.10.0+cu128 - transformers: 4.57.1 - GPU: NVIDIA B200 - Python: 3.12 ## Describe the bug Using the `extract_hidden_states` speculative method with a vision-language model (e.g. `Qwen/Qwen2.5-VL-7B-Instruct`) fails during engine initialization with: `pydantic_core._pydantic_core.ValidationError: 1 validation error for SpeculativeConfig Value error, The text_config extracted from the model config does not have num_attention_heads attribute.` The same configuration works fine with text-only models like `Qwen/Qwen3-8B`. ## How to reproduce ```python from vllm import LLM engine = LLM( model="Qwen/Qwen2.5-VL-7B-Instruct", tensor_parallel_size=2, trust_remote_code=True, max_model_len=2048, enforce_eager=True, speculative_config={ "method": "extract_hidden_states", "num_speculative_tokens": 1, "draft_model_config": { "hf_config": { "eagle_aux_hidden_state_layer_ids": [2, 4, 6], } }, }, kv_transfer_config={ "kv_connector": "ExampleHiddenStatesConnector", "kv_role": "kv_producer", }, ) ``` ## Root cause In `vllm/config/speculative.py` (line ~446), the `extract_hidden_states` path does: ```python self.draft_model_config = copy.co...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ug]: extract_hidden_states speculative method fails with vision-language models (e.g. Qwen2.5-VL) ## Your current environment - vLLM version: 0.18.0 - PyTorch: 2.10.0+cu128 - transformers: 4.57.1 - GPU: NVIDIA B200 - Py...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ion-language models (e.g. Qwen2.5-VL) ## Your current environment - vLLM version: 0.18.0 - PyTorch: 2.10.0+cu128 - transformers: 4.57.1 - GPU: NVIDIA B200 - Python: 3.12 ## Describe the bug Using the `extract_hidden_sta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ion: 0.18.0 - PyTorch: 2.10.0+cu128 - transformers: 4.57.1 - GPU: NVIDIA B200 - Python: 3.12 ## Describe the bug Using the `extract_hidden_states` speculative method with a vision-language model (e.g. `Qwen/Qwen2.5-VL-7...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: extract_hidden_states speculative method fails with vision-language models (e.g. Qwen2.5-VL) ## Your current environment - vLLM version: 0.18.0 - PyTorch: 2.10.0+cu128 - transformers: 4.57.1 - GPU: NVIDIA B200 -...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ration works fine with text-only models like `Qwen/Qwen3-8B`. ## How to reproduce ```python from vllm import LLM engine = LLM( model="Qwen/Qwen2.5-VL-7B-Instruct", tensor_parallel_size=2, trust_remote_code=True, max_mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
