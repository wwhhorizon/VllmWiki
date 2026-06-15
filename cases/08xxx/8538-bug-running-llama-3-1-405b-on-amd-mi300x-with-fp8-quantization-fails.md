# vllm-project/vllm#8538: [Bug]: Running Llama-3.1-405B on AMD MI300X with FP8 quantization fails

| 字段 | 值 |
| --- | --- |
| Issue | [#8538](https://github.com/vllm-project/vllm/issues/8538) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Running Llama-3.1-405B on AMD MI300X with FP8 quantization fails

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When running Llama-3.1-405B with the vLLM container on an 8x AMD MI300X with `--quantization=fp8` vLLM crashes after loading the shards into the GPU memory. When no quantization is specified everything works as expected. Following https://docs.vllm.ai/en/latest/quantization/supported_hardware.html FP8 W8A8 quantization is supported for AMD GPUs. The Docker command to reproduce the bug is: ``` bash # docker run -it \ --network=host \ --group-add=video \ --ipc=host \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --device /dev/kfd \ --device /dev/dri \ -v /path/to/local/model/models--meta-llama--Meta-Llama-3.1-405B:/app/model \ vllm-rocm \ bash -c "vllm serve --tensor-parallel-size=8 --quantization fp8 --disable-frontend-multiprocessing /app/model/snapshots/222de096204587406c7cadb3e0a101aade116279/" ```` Please see the Traceback below: https://gist.github.com/danielphilipp/8e1210b98c086910d47f543210761377 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](htt...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Running Llama-3.1-405B on AMD MI300X with FP8 quantization fails bug;rocm ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When running Llama-3.1-405B with the vLLM containe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: after loading the shards into the GPU memory. When no quantization is specified everything works as expected. Following https://docs.vllm.ai/en/latest/quantization/supported_hardware.html FP8 W8A8 quantization is suppor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Running Llama-3.1-405B on AMD MI300X with FP8 quantization fails bug;rocm ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When running Llama-3.1-405B with the vLLM containe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Running Llama-3.1-405B on AMD MI300X with FP8 quantization fails bug;rocm ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When running Llama-3.1-405B with the vLLM containe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;speculative_decoding cuda;fp8;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
