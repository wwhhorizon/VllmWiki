# vllm-project/vllm#21308: [Bug]: ROCm NotImplementedError: Speculative decoding is not yet supported on vLLM V1

| 字段 | 值 |
| --- | --- |
| Issue | [#21308](https://github.com/vllm-project/vllm/issues/21308) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ROCm NotImplementedError: Speculative decoding is not yet supported on vLLM V1

### Issue 正文摘录

### Your current environment Launch the vLLM docker image on AMD ROCm: `docker run -d -it --ipc=host --network=host --privileged --cap-add=CAP_SYS_ADMIN --device=/dev/kfd --device=/dev/dri --device=/dev/mem --group-add render --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --shm-size=192g --name vllm_spec_dec -v /home/models/:/models -v /home/:/work` Launch the vllm server: `export VLLM_USE_V1=1` `vllm serve meta-llama/Llama-3.1-8B-Instruct --trust-remote-code --swap-space 16 --disable-log-requests --tensor-parallel-size 1 --distributed-executor-backend mp --dtype float16 --quantization fp8 --kv-cache-dtype fp8 --no-enable-chunked-prefill --max-num-seqs 300 --max-num-batched-tokens 131072 --gpu-memory-utilization 0.8 --enforce-eager --speculative_config '{"method": "eagle3", "model": "yuhuili/EAGLE3-LLaMA3.1-Instruct-8B", "num_speculative_tokens": 2, "draft_tensor_parallel_size": 1, "dtype": "float16"}' --port 8001` ### 🐛 Describe the bug I'm trying to enable speculative decoding in vLLM v1 via the docker image: rocm/vllm:rocm6.4.1_vllm_0.9.1_20250715, on AMD GPUs. Detailed steps to reproduce the bug has been listed above. Setting the environmental variable, VLLM_USE_V1=1,...

## 现有链接修复摘要

#24505 [Bug] [Spec Dec]: Fix kv_cache dtype mismatch for Eagle3 drafter on FP8 target

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: ROCm NotImplementedError: Speculative decoding is not yet supported on vLLM V1 bug;rocm ### Your current environment Launch the vLLM docker image on AMD ROCm: `docker run -d -it --ipc=host --network=host --privil...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: og-requests --tensor-parallel-size 1 --distributed-executor-backend mp --dtype float16 --quantization fp8 --kv-cache-dtype fp8 --no-enable-chunked-prefill --max-num-seqs 300 --max-num-batched-tokens 131072 --gpu-memory-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: ROCm NotImplementedError: Speculative decoding is not yet supported on vLLM V1 bug;rocm ### Your current environment Launch the vLLM docker image on AMD ROCm: `docker run -d -it --ipc=host --network=host --privil...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ported on vLLM V1 bug;rocm ### Your current environment Launch the vLLM docker image on AMD ROCm: `docker run -d -it --ipc=host --network=host --privileged --cap-add=CAP_SYS_ADMIN --device=/dev/kfd --device=/dev/dri --d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: -opt seccomp=unconfined --shm-size=192g --name vllm_spec_dec -v /home/models/:/models -v /home/:/work` Launch the vllm server: `export VLLM_USE_V1=1` `vllm serve meta-llama/Llama-3.1-8B-Instruct --trust-remote-code --sw...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24505](https://github.com/vllm-project/vllm/pull/24505) | closes_keyword | 0.95 | [Bug] [Spec Dec]: Fix kv_cache dtype mismatch for Eagle3 drafter on FP8 target | Resolves [#21308](https://github.com/vllm-project/vllm/issues/21308#issuecomment-3192203896) ### **Purpose** This PR resolves a RuntimeError that occurs on the ROCm platform when |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
