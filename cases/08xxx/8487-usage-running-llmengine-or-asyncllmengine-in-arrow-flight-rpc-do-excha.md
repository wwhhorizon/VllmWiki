# vllm-project/vllm#8487: [Usage]: Running LLMEngine (or AsyncLLMEngine) in Arrow Flight RPC do_exchange()

| 字段 | 值 |
| --- | --- |
| Issue | [#8487](https://github.com/vllm-project/vllm/issues/8487) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Running LLMEngine (or AsyncLLMEngine) in Arrow Flight RPC do_exchange()

### Issue 正文摘录

### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: macOS 14.2.1 (arm64) GCC version: Could not collect Clang version: 15.0.0 (clang-1500.*******) CMake version: Could not collect Libc version: N/A Python version: 3.8.19 (default, May 8 2024, 17:10:30) [Clang 15.0.0 (clang-1500.*******)] (64-bit runtime) Python platform: macOS-14.2.1-arm64-arm-64bit Is CUDA available: N/A CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Apple M1 Max Versions of relevant libraries: [pip3] mypy==1.7.1 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.24.4 [pip3] pyzmq==25.1.2 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: N/A vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: Could not collect ``` ### How would you like to use vllm I want to run inference for any LLM model using `LLMEngine` (or `AsyncLLM...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: do_exchange() usage;stale ### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: macOS 14.2.1 (arm64) GCC version: Could not col...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ur current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: macOS 14.2.1 (arm64) GCC version: Could not collect Clang version: 15.0.0 (clan...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: A runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: Could not collect Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: N/A MIO...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ata( self, batch: pa.RecordBatch, writer: flight.MetadataRecordBatchWriter, is_first_batch: bool, ) -> Tuple[flight.FlightStreamWriter, bool]: # some code that acquires the lock result = self.inference.predict(batch) #...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ng LLMEngine (or AsyncLLMEngine) in Arrow Flight RPC do_exchange() usage;stale ### Your current environment ```text PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
