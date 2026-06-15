# vllm-project/vllm#39914: [Bug]: Gemma 4: Engine hang during large prefill caused by Interleaved Attention and p-RoPE implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#39914](https://github.com/vllm-project/vllm/issues/39914) |
| 状态 | open |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | attention;cache;cuda;kernel;quantization |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4: Engine hang during large prefill caused by Interleaved Attention and p-RoPE implementation

### Issue 正文摘录

### Your current environment Gemma 4 engine completely freezes during the prefill phase when the prompt length exceeds ~4,000 tokens. This occurs due to a suspected failure in the Interleaved Attention/p-RoPE implementation, while incremental token generation remains stable. ### 🐛 Describe the bug **Environment:** * **Model:** `google/gemma-4-31b-it` (and quantized versions) * **Hardware:** NVIDIA RTX 5090 / RTX Pro 6000 Blackwell * **CUDA:** 13.0 * **Observed behavior:** Total engine freeze during prefill of sequences exceeding ~4,000 tokens. **Technical Architecture of Gemma 4:** The model utilizes a complex hybrid attention mechanism that is not fully supported by the current vLLM scheduler/kernels: 1. **Interleaved Attention:** The architecture consists of a mixture of layers: 5 local attention layers (with a sliding window of **1024 tokens** for the 31B version) for every 1 global attention layer. 2. **Dual RoPE:** The model employs two different rotary positional embeddings: * **Standard RoPE** for local sliding-window layers. * **Proportional RoPE (p-RoPE)** for global attention layers to enable context extension up to 256K. 3. **Shared KV Cache:** The model implements a sh...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: `google/gemma-4-31b-it` (and quantized versions) * **Hardware:** NVIDIA RTX 5090 / RTX Pro 6000 Blackwell * **CUDA:** 13.0 * **Observed behavior:** Total engine freeze during prefill of sequences exceeding ~4,000 tokens...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Gemma 4: Engine hang during large prefill caused by Interleaved Attention and p-RoPE implementation bug ### Your current environment Gemma 4 engine completely freezes during the prefill phase when the prompt leng...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ug **Environment:** * **Model:** `google/gemma-4-31b-it` (and quantized versions) * **Hardware:** NVIDIA RTX 5090 / RTX Pro 6000 Blackwell * **CUDA:** 13.0 * **Observed behavior:** Total engine freeze during prefill of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma 4: Engine hang during large prefill caused by Interleaved Attention and p-RoPE implementation bug ### Your current environment Gemma 4 engine completely freezes during the prefill phase when the prompt leng...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Gemma 4: Engine hang during large prefill caused by Interleaved Attention and p-RoPE implementation bug ### Your current environment Gemma 4 engine completely freezes during the prefill phase when the prompt leng...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
