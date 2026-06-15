# vllm-project/vllm#14295: [Installation]:  Attempting to build and run vLLM for Intel Core Ultra 7 155H with ARC iGPU

| 字段 | 值 |
| --- | --- |
| Issue | [#14295](https://github.com/vllm-project/vllm/issues/14295) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]:  Attempting to build and run vLLM for Intel Core Ultra 7 155H with ARC iGPU

### Issue 正文摘录

The build seems to complete with no issues. The server runs with some odd stdout logging. CURL does not return valid responses, but gets a 200 from the server. Working notes are here - https://github.com/cgruver/vllm-intel-gpu-workspace ### Your current environment python collect_env.py ```text /projects/home/.local/lib/python3.12/site-packages/torchvision/io/image.py:14: UserWarning: Failed to load image Python extension: 'libjpeg.so.8: cannot open shared object file: No such file or directory'If you don't plan on using image functionality from `torchvision.io`, you can ignore this warning. Otherwise, there might be something wrong with your environment. Did you have `libjpeg` or `libpng` installed before building `torchvision` from source? warn( [W305 15:15:04.737001522 OperatorEntry.cpp:155] Warning: Warning only once for all operators, other operators may also be overridden. Overriding a previously registered kernel for the same operator and the same dispatch key operator: aten::_cummax_helper(Tensor self, Tensor(a!) values, Tensor(b!) indices, int dim) -> () registered at /build/pytorch/build/aten/src/ATen/RegisterSchema.cpp:6 dispatch key: XPU previous kernel: registered at...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: Attempting to build and run vLLM for Intel Core Ultra 7 155H with ARC iGPU installation;stale The build seems to complete with no issues. The server runs with some odd stdout logging. CURL does not retu
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: uild and run vLLM for Intel Core Ultra 7 155H with ARC iGPU installation;stale The build seems to complete with no issues. The server runs with some odd stdout logging. CURL does not return valid responses, but gets a 2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nt information... PyTorch version: 2.5.1+cxx11.abi Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Fedora Linux 41 (Container Image) (x86_64) GCC version: (GCC) 14.2.1 20250110...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: __.py:253] Automatically detected platform xpu. Collecting environment information... PyTorch version: 2.5.1+cxx11.abi Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Fedora Li...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
