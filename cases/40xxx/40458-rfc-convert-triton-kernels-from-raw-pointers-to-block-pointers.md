# vllm-project/vllm#40458: [RFC]: Convert Triton kernels from raw pointers to block pointers

| 字段 | 值 |
| --- | --- |
| Issue | [#40458](https://github.com/vllm-project/vllm/issues/40458) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;frontend_api;hardware_porting;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cache;kernel;triton |
| 症状 | slowdown |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Convert Triton kernels from raw pointers to block pointers

### Issue 正文摘录

### Motivation. vLLM's core dense-inference Triton kernels currently use **raw pointer arithmetic** (`tl.load(ptr + offset, mask=...)`). Triton's recommended and forward-looking memory access API is **block pointers** (`tl.make_block_ptr` / `tl.advance`), which: 1. **Enable hardware portability** — Block pointers abstract away raw address arithmetic, allowing Triton backends targeting non-NVIDIA hardware (e.g., Intel XPU, IBM Spyre/AIU) to lower these kernels. Some accelerators with tiled memory architectures fundamentally cannot accept raw pointer arithmetic. 2. **Leverage Hopper TMA** — On NVIDIA Hopper (H100/H200), block pointers can be lowered to Tensor Memory Accelerator (TMA) instructions, potentially improving memory throughput. 3. **Align with Triton's direction** — The Triton project is moving toward structured memory access as the primary API. 4. **Improve readability** — Block pointer code separates memory layout (shape, strides, offsets) from computation (load, compute, store). Some newer vLLM kernels (FLA, Mamba, LoRA) already use block pointers, but the core inference-path kernels do not. ### Proposed Change. Convert the following simple, element-wise kernels to use...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: M Spyre/AIU) to lower these kernels. Some accelerators with tiled memory architectures fundamentally cannot accept raw pointer arithmetic. 2. **Leverage Hopper TMA** — On NVIDIA Hopper (H100/H200), block pointers can be...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: the more complex kernels on the dense inference path — KV cache reshape, decode softmax+reduceV, merge attention states, and the attention kernels (prefill, decode stage 1, GQA decode, chunked prefill/paged decode). ###...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: nsor Memory Accelerator (TMA) instructions, potentially improving memory throughput. 3. **Align with Triton's direction** — The Triton project is moving toward structured memory access as the primary API. 4. **Improve r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [RFC]: Convert Triton kernels from raw pointers to block pointers RFC ### Motivation. vLLM's core dense-inference Triton kernels currently use **raw pointer arithmetic** (`tl.load(ptr + offset, mask=...)`). Triton's rec...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [RFC]: Convert Triton kernels from raw pointers to block pointers RFC ### Motivation. vLLM's core dense-inference Triton kernels currently use **raw pointer arithmetic** (`tl.load(ptr + offset, mask=...)`). Triton's rec...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
