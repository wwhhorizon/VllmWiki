# vllm-project/vllm#2740: Prefix error

| 字段 | 值 |
| --- | --- |
| Issue | [#2740](https://github.com/vllm-project/vllm/issues/2740) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Prefix error

### Issue 正文摘录

When I use this ` results = llm.generate(prompts, sampling_params, prefix_pos=[prefix_pos] * len(prompts)) # generated_texts = [output.outputs[0].text for output in results]` the following error occured: `python: /project/lib/Conversion/TritonGPUToLLVM/ReduceOpToLLVM.cpp:316: mlir::LogicalResult ReduceOpConversion::matchAndRewriteFast(mlir::triton::ReduceOp, ConvertTritonGPUOpToLLVMPattern ::OpAdaptor, mlir::ConversionPatternRewriter&) const: Assertion `false && "Unexpected srcLayout in ReduceOpConversion"' failed. *** SIGABRT received at time=1707036344 on cpu 40 *** PC: @ 0x7f2d8bb099fc (unknown) pthread_kill @ 0x7f2d8bab5520 (unknown) (unknown) [2024-02-04 08:45:44,122 E 864170 864170] logging.cc:361: *** SIGABRT received at time=1707036344 on cpu 40 *** [2024-02-04 08:45:44,122 E 864170 864170] logging.cc:361: PC: @ 0x7f2d8bb099fc (unknown) pthread_kill [2024-02-04 08:45:44,122 E 864170 864170] logging.cc:361: @ 0x7f2d8bab5520 (unknown) (unknown) Fatal Python error: Aborted Stack (most recent call first): File "/root/miniconda3/envs/vllm/lib/python3.9/site-packages/triton/compiler/compiler.py", line 107 in ttgir_to_llir File "/root/miniconda3/envs/vllm/lib/python3.9/site-packa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ults]` the following error occured: `python: /project/lib/Conversion/TritonGPUToLLVM/ReduceOpToLLVM.cpp:316: mlir::LogicalResult ReduceOpConversion::matchAndRewriteFast(mlir::triton::ReduceOp, ConvertTritonGPUOpToLLVMPa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ttern ::OpAdaptor, mlir::ConversionPatternRewriter&) const: Assertion `false && "Unexpected srcLayout in ReduceOpConversion"' failed. *** SIGABRT received at time=1707036344 on cpu 40 *** PC: @ 0x7f2d8bb099fc (unknown)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: " ", line 63 in _fwd_kernel File "/data/lc/Vllm_infer/vllm_prefix/vllm/model_executor/layers/triton_kernel/prefix_prefill.py", line 683 in context_attention_fwd File "/root/miniconda3/envs/vllm/lib/python3.9/site-packag...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: the following error occured: `python: /project/lib/Conversion/TritonGPUToLLVM/ReduceOpToLLVM.cpp:316: mlir::LogicalResult ReduceOpConversion::matchAndRewriteFast(mlir::triton::ReduceOp, ConvertTritonGPUOpToLLVMPattern :...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: c/Vllm_infer/vllm_prefix/vllm/model_executor/layers/triton_kernel/prefix_prefill.py", line 683 in context_attention_fwd File "/root/miniconda3/envs/vllm/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 115...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
