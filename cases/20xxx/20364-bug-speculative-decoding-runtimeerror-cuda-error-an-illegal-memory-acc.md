# vllm-project/vllm#20364: [Bug]: (Speculative Decoding) RuntimeError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#20364](https://github.com/vllm-project/vllm/issues/20364) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;kernel;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: (Speculative Decoding) RuntimeError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment vLLM v0.9.1 ``` args: - --model - meta-llama/Llama-3.3-70B-Instruct - --quantization - fp8 - --tensor-parallel-size - "2" - --gpu-memory-utilization - "0.85" - --max-model-len - "65536" - --disable-custom-all-reduce - --speculative-config={"model":"meta-llama/Llama-3.2-1B-Instruct","draft_tensor_parallel_size":1,"num_speculative_tokens":5} # Function calling - --enable-auto-tool-choice - --tool-call-parser - llama3_json ``` GPUs: 2xH100 80GiB ### 🐛 Describe the bug ``` Message "[rank0]:[W702 01:08:23.472346684 ProcessGroupNCCL.cpp:1476] Warning: WARNING: destroy_process_group() was not called before program exit " warnings.warn('resource_tracker: There appear to be %d '" "/usr/lib/python3.12/multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown" "INFO 07-02 01:08:21 [multiproc_worker_utils.py:125] Killing local vLLM worker processes" "INFO: Finished server process [180]" "INFO: Application shutdown complete." "INFO: Waiting for application shutdown." "INFO: Shutting down" "INFO: 10.233.75.0:0 - ""GET /health HTTP/1.1"" 500 Internal Server Error" "INFO: 10.233.75.0:0...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: (Speculative Decoding) RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment vLLM v0.9.1 ``` args: - --model - meta-llama/Llama-3.3-70B-Instruct
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: "The above exception was the direct cause of the following exception:" "Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions." "For debugging consider passing CUDA_LAUNCH_BLOCKING=1" "CUDA kernel errors mi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: - --model - meta-llama/Llama-3.3-70B-Instruct - --quantization - fp8 - --tensor-parallel-size - "2" - --gpu-memory-utilization - "0.85" - --max-model-len - "65536" - --disable-custom-all-reduce - --
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: (Speculative Decoding) RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment vLLM v0.9.1 ``` args: - --model - meta-llama/Llama-3.3-70B-Instruct - --quantizatio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e ### Your current environment vLLM v0.9.1 ``` args: - --model - meta-llama/Llama-3.3-70B-Instruct - --quantization - fp8 - --tensor-parallel-size - "2" - --gpu-memory-utilization - "0.85" - --max-model-len

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
