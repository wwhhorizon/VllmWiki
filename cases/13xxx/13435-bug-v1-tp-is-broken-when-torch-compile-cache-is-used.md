# vllm-project/vllm#13435: [Bug][V1]: TP is broken when torch compile cache is used

| 字段 | 值 |
| --- | --- |
| Issue | [#13435](https://github.com/vllm-project/vllm/issues/13435) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][V1]: TP is broken when torch compile cache is used

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Got the error message when using tp_size=4: ``` (VllmWorker rank=2 pid=2307184) ERROR 02-17 14:48:01 multiproc_executor.py:374] ValueError: Pointer argument (at 0) cannot be accessed from Triton (cpu tensor?) ``` **Importantly, the bug doesn't happen when the torch.compile cache is not used.** The error raises at the first torch.compile-generated op for the embedding layer: ```python with torch.cuda._DeviceGuard(0): torch.cuda.set_device(0) buf0 = empty_strided_cuda((s0, 4096), (4096, 1), torch.bfloat16) # Topologically Sorted Source Nodes: [ge, lt, and_, ge_1, lt_1, and__1, or_, masked_fill_, mul, mul_1, add, sub, mul_2, embedding], Original ATen: [aten.ge, aten.lt, aten.bitwise_and, aten.bitwise_or, aten.masked_fill, aten.mul, aten.add, aten.sub, aten.embedding] triton_poi_fused_add_bitwise_and_bitwise_or_embedding_ge_lt_masked_fill_mul_sub_0_xnumel = 4096*s0 stream0 = get_raw_stream(0) triton_poi_fused_add_bitwise_and_bitwise_or_embedding_ge_lt_masked_fill_mul_sub_0.run(arg0_1, arg2_1, buf0, triton_poi_fused_add_bitwise_and_bitwise_or_embedding_ge_lt_masked_fill_mul_sub_0_xnumel, grid=grid(triton_poi_fused_add_bitwise_and_bitw...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug][V1]: TP is broken when torch compile cache is used bug ### Your current environment ### 🐛 Describe the bug Got the error message when using tp_size=4: ``` (VllmWorker rank=2 pid=2307184) ERROR 02-17 14:48:01 multi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: device(0) buf0 = empty_strided_cuda((s0, 4096), (4096, 1), torch.bfloat16) # Topologically Sorted Source Nodes: [ge, lt, and_, ge_1, lt_1, and__1, or_, masked_fill_, mul, mul_1, add, sub, mul_2, embedding], Original ATe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: h.compile-generated op for the embedding layer: ```python with torch.cuda._DeviceGuard(0): torch.cuda.set_device(0) buf0 = empty_strided_cuda((s0, 4096), (4096, 1), torch.bfloat16) # Topologically Sorted Source Nodes: [...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: utor.py:374] ValueError: Pointer argument (at 0) cannot be accessed from Triton (cpu tensor?) ``` **Importantly, the bug doesn't happen when the torch.compile cache is not used.** The error raises at the first torch.com...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: l_1, add, sub, mul_2, embedding], Original ATen: [aten.ge, aten.lt, aten.bitwise_and, aten.bitwise_or, aten.masked_fill, aten.mul, aten.add, aten.sub, aten.embedding] triton_poi_fused_add_bitwise_and_bitwise_or_embeddin...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
