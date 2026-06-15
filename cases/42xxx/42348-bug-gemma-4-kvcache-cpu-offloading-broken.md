# vllm-project/vllm#42348: [Bug]: Gemma 4 KVCache CPU offloading broken

| 字段 | 值 |
| --- | --- |
| Issue | [#42348](https://github.com/vllm-project/vllm/issues/42348) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 KVCache CPU offloading broken

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I’m testing vLLM native CPU Offloading with google/gemma-4-31B-it. My vLLM server crashed when the feature is enabled. Error message ``` !!!!!!! Segfault encountered !!!!!!! File " ", line 0, in cudaMemcpyAsync File " ", line 0, in swap_blocks(at::Tensor&, at::Tensor&, long, at::Tensor const&) File " ", line 0, in c10::impl::make_boxed_from_unboxed_functor >, false>::call(c10::OperatorKernel*, c10::OperatorHandle const&, c10::DispatchKeySet, std::vector >*) File " ", line 0, in c10::Dispatcher::callBoxed(c10::OperatorHandle const&, std::vector >*) const [clone .isra.0] File " ", line 0, in torch::jit::invokeOperatorFromPython(c10::ArrayRef >, pybind11::args const&, pybind11::kwargs const&, std::optional ) File " ", line 0, in torch::jit::_get_operation_for_overload_or_packet(c10::ArrayRef >, c10::Symbol, pybind11::args const&, pybind11::kwargs const&, bool, std::optional ) File " ", line 0, in torch::jit::_get_operation_for_overload_or_packet(std::vector , std::allocator > > const&, c10::Symbol, pybind11::args const&, pybind11::kwargs const&, bool, std::optional ) File " ", line 0, in pybind11::cpp_function::initialize , std::all...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: emma-4-31B-it \ --tensor-parallel-size 4 \ --dtype bfloat16 \ --gpu-memory-utilization 0.7 \ --max-model-len 200000 \ --max-num-batched-tokens 16384 \ --enable-chunked-prefill \ --enable-prefix-c
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: message ``` !!!!!!! Segfault encountered !!!!!!! File " ", line 0, in cudaMemcpyAsync File " ", line 0, in swap_blocks(at::Tensor&, at::Tensor&, long, at::Tensor const&) File " ", line 0, in c10::impl::make_boxed_from_u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma 4 KVCache CPU offloading broken bug ### Your current environment ### 🐛 Describe the bug I’m testing vLLM native CPU Offloading with google/gemma-4-31B-it. My vLLM server crashed when the feature is enabled....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: --max-num-batched-tokens 16384 \ --enable-chunked-prefill \ --enable-prefix-caching \ --kv-cache-dtype fp8 \ --kv-transfer-config '{"kv_connector":"OffloadingConnector","kv_role":"kv_both","kv_connector_extra_config":{"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
