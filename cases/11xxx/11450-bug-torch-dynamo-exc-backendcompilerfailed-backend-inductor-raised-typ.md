# vllm-project/vllm#11450: [Bug]: torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised: TypeError: 'int' object is not iterable

| 字段 | 值 |
| --- | --- |
| Issue | [#11450](https://github.com/vllm-project/vllm/issues/11450) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised: TypeError: 'int' object is not iterable

### Issue 正文摘录

### Your current environment ### Model Input Dumps [errors.zip](https://github.com/user-attachments/files/18236133/errors.zip) ### 🐛 Describe the bug I have 2xAMD MI60 and I was able to correctly compile vllm. Loading a model into a single GPU works fine. However, when I try to load a model with tensor parallelism into two GPUs, vllm throws an error. Here is how I load a model to a single GPU and it works fine. Here is a command to run with tensor parallelism on two GPUs and it fails. ``` export VLLM_LOGGING_LEVEL=DEBUG export TORCH_LOGS="+dynamo" TORCHDYNAMO_VERBOSE=1 vllm serve /home/ai-llm/Downloads/models/Qwen2.5-Coder-32B-Instruct-AutoRound-GPTQ-4bit --max_model_len 1024 --tensor_parallel 2 ... ... File "/home/ai-llm/Downloads/vllm/vllmenv/lib/python3.10/site-packages/torch/_inductor/codegen/triton_utils.py", line 176, in config_of return AttrsDescriptorWrapper(divisible_by_16, equal_to_1) File "/home/ai-llm/Downloads/vllm/vllmenv/lib/python3.10/site-packages/torch/_inductor/runtime/hints.py", line 56, in AttrsDescriptorWrapper res = AttrsDescriptor.from_dict( File "/home/ai-llm/Downloads/vllm/triton/python/triton/backends/compiler.py", line 186, in from_dict attrs_descriptor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised: TypeError: 'int' object is not iterable bug ### Your current environment ### Model Input Dumps [errors.zip](https://github.com/user-attachments/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: r: 'int' object is not iterable bug ### Your current environment ### Model Input Dumps [errors.zip](https://github.com/user-attachments/files/18236133/errors.zip) ### 🐛 Describe the bug I have 2xAMD MI60 and I was able...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: GPU works fine. However, when I try to load a model with tensor parallelism into two GPUs, vllm throws an error. Here is how I load a model to a single GPU and it works fine. Here is a command to run with tensor paralle...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: r.py", line 202, in determine_num_available_blocks self.model_runner.profile_run() File "/home/ai-llm/Downloads/vllm/vllmenv/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context return...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised: TypeError: 'int' object is not iterable bug ### Your current environment ### Model Input Dumps [errors.zip](https://github.com/user-attachments/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
