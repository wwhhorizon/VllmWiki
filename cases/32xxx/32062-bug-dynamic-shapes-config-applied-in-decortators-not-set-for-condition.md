# vllm-project/vllm#32062: [Bug]: Dynamic shapes config applied in decortators not set for conditional range compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#32062](https://github.com/vllm-project/vllm/issues/32062) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Dynamic shapes config applied in decortators not set for conditional range compilation

### Issue 正文摘录

### Your current environment NA ### 🐛 Describe the bug amely ``` dynamo_config_patches = {} try: _ = torch._dynamo.config.enable_cpp_symbolic_shape_guards dynamo_config_patches["enable_cpp_symbolic_shape_guards"] = False except AttributeError: # Note: this config is not available in torch 2.6, we can skip # if the config doesn't exist logger.debug("enable_cpp_symbolic_shape_guards config not available") # Prepare backed_size_oblivious config patch if needed fx_config_patches = {} if ds_type == DynamicShapesType.BACKED_SIZE_OBLIVIOUS: fx_config_patches["backed_size_oblivious"] = True # Prepare inductor config patches # assume_32bit_indexing is only available in torch 2.10.0.dev+ inductor_config_patches = {} if is_torch_equal_or_newer("2.10.0.dev"): inductor_config_patches["assume_32bit_indexing"] = ( self.compilation_config.dynamic_shapes_config.assume_32_bit_indexing ) with ( patch.object( InliningInstructionTranslator, "inline_call_", patched_inline_call ), torch._dynamo.config.patch(**dynamo_config_patches), maybe_use_cudagraph_partition_wrapper(self.vllm_config), torch.fx.experimental._config.patch(**fx_config_patches), _torch27_patch_tensor_subclasses(), torch._inductor.config...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rch._dynamo.config.patch(**dynamo_config_patches), maybe_use_cudagraph_partition_wrapper(self.vllm_config), torch.fx.experimental._config.patch(**fx_config_patches), _torch27_patch_tensor_subclasses(), torch._inductor.c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: dynamo_config_patches["enable_cpp_symbolic_shape_guards"] = False except AttributeError: # Note: this config is not available in torch 2.6, we can skip # if the config doesn't exist logger.debug("enable_cpp_symbolic_sha...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Dynamic shapes config applied in decortators not set for conditional range compilation bug;stale ### Your current environment NA ### 🐛 Describe the bug amely ``` dynamo_config_patches = {} try: _ = torch._
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: fig applied in decortators not set for conditional range compilation bug;stale ### Your current environment NA ### 🐛 Describe the bug amely ``` dynamo_config_patches = {} try: _ = torch._dynamo.config.enable_cpp_symboli...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
