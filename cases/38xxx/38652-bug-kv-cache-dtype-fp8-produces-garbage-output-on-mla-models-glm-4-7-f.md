# vllm-project/vllm#38652: [Bug]: --kv-cache-dtype fp8 produces garbage output on MLA models (GLM-4.7-Flash) at multi-turn

| 字段 | 值 |
| --- | --- |
| Issue | [#38652](https://github.com/vllm-project/vllm/issues/38652) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --kv-cache-dtype fp8 produces garbage output on MLA models (GLM-4.7-Flash) at multi-turn

### Issue 正文摘录

### Your current environment - vLLM 0.18.1 - H100 80GB SXM5, CUDA 12.8 - Ubuntu 24.04 - Model: zai-org/GLM-4.7-Flash (MLA architecture, `glm4_moe_lite`) - Backend selected: FLASHMLA ### Description FP8 KV cache produces corrupted output on MLA models when the conversation exceeds a single turn. Single-turn responses are coherent, multi-turn with system prompts degrades to garbage. ### Reproduction ```bash vllm serve zai-org/GLM-4.7-Flash --kv-cache-dtype fp8 --trust-remote-code --max-model-len 8192 ``` Single turn (works fine): ```json {"messages": [{"role": "user", "content": "Say hello in Finnish"}]} → coherent response about "Hei" / "Terve" ``` Multi-turn with system prompt (broken): ```json {"messages": [ {"role": "system", "content": "You are a helpful sales assistant for a SaaS product."}, {"role": "user", "content": "What pricing plans do you offer?"} ]} → "...a S componentes_obs Worce!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" ``` ### Benchmark data Tested across 20 multi-turn conversation scenarios with Llama-3.3-70B judge (score 1-5): | Model | KV Cache | Avg Score | |-------|----------|-----------| | GLM-4.7-Flash BF16 | FP16 (baseline) | 4.61 | | GLM-4.7-Flash BF16 | *...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: --kv-cache-dtype fp8 produces garbage output on MLA models (GLM-4.7-Flash) at multi-turn ### Your current environment - vLLM 0.18.1 - H100 80GB SXM5, CUDA 12.8 - Ubuntu 24.04 - Model: zai-org/GLM-4.7-Flash (MLA a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: --kv-cache-dtype fp8 produces garbage output on MLA models (GLM-4.7-Flash) at multi-turn ### Your current environment - vLLM 0.18.1 - H100 80GB SXM5, CUDA 12.8 - Ubuntu 24.04 - Model: zai-org/GLM-4.7-Flash (MLA a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: M-4.7-Flash) at multi-turn ### Your current environment - vLLM 0.18.1 - H100 80GB SXM5, CUDA 12.8 - Ubuntu 24.04 - Model: zai-org/GLM-4.7-Flash (MLA architecture, `glm4_moe_lite`) - Backend selected: FLASHMLA ### Descri...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: --kv-cache-dtype fp8 produces garbage output on MLA models (GLM-4.7-Flash) at multi-turn ### Your current environment - vLLM 0.18.1 - H100 80GB SXM5, CUDA 12.8 - Ubuntu 24.04 - Model: zai-org/GLM-4.7-Flash (MLA a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: omponentes_obs Worce!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" ``` ### Benchmark data Tested across 20 multi-turn conversation scenarios with Llama-3.3-70B judge (score 1-5): | Model | KV Cache | Avg Score | |-------|-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
