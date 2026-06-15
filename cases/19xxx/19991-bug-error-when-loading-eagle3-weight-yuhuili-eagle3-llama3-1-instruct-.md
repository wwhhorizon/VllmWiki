# vllm-project/vllm#19991: [Bug]: Error when loading EAGLE3 weight, yuhuili/ EAGLE3-LLaMA3.1-Instruct-8B

| 字段 | 值 |
| --- | --- |
| Issue | [#19991](https://github.com/vllm-project/vllm/issues/19991) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error when loading EAGLE3 weight, yuhuili/ EAGLE3-LLaMA3.1-Instruct-8B

### Issue 正文摘录

### Your current environment Docker image: rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605 ### 🐛 Describe the bug I'm trying to use vLLM eagle3, using the server launch command as below: `vllm serve /models/models--meta-llama--Llama-3.1-8B-Instruct/snapshots/0e9e39f249a16976918f6564b8830bc894c89659/ --trust-remote-code --swap-space 16 --disable-log-requests --tensor-parallel-size 1 --distributed-executor-backend mp --dtype float16 --quantization fp8 --kv-cache-dtype fp8 --no-enable-chunked-prefill --max-num-seqs 300 --max-num-batched-tokens 131072 --gpu-memory-utilization 0.8 --enforce-eager --speculative_config '{"method": "eagle", "model": "yuhuili/EAGLE3-LLaMA3.1-Instruct-8B", "num_speculative_tokens": 5, "draft_tensor_parallel_size": 1, "dtype": "float16"}'` For eagle3 model, I used "yuhuili/EAGLE3-LLaMA3.1-Instruct-8B", while there is an error of weight shape misalignment as below: ERROR 06-22 15:12:27 [engine.py:458] Attempted to load weight (torch.Size([4096, 12288])) into parameter (torch.Size([4096, 8192])) ERROR 06-22 15:12:27 [engine.py:458] Traceback (most recent call last): ERROR 06-22 15:12:27 [engine.py:458] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multip...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: ror when loading EAGLE3 weight, yuhuili/ EAGLE3-LLaMA3.1-Instruct-8B bug;stale ### Your current environment Docker image: rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605 ### 🐛 Describe the bug I'm trying to use vLLM eagle3, u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ili/ EAGLE3-LLaMA3.1-Instruct-8B bug;stale ### Your current environment Docker image: rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605 ### 🐛 Describe the bug I'm trying to use vLLM eagle3, using the server launch command as be...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: og-requests --tensor-parallel-size 1 --distributed-executor-backend mp --dtype float16 --quantization fp8 --kv-cache-dtype fp8 --no-enable-chunked-prefill --max-num-seqs 300 --max-num-batched-tokens 131072 --gpu-memory-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Error when loading EAGLE3 weight, yuhuili/ EAGLE3-LLaMA3.1-Instruct-8B bug;stale ### Your current environment Docker image: rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605 ### 🐛 Describe the bug I'm trying to use vLLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: aMA3.1-Instruct-8B bug;stale ### Your current environment Docker image: rocm/vllm:rocm6.4.1_vllm_0.9.0.1_20250605 ### 🐛 Describe the bug I'm trying to use vLLM eagle3, using the server launch command as below: `vllm ser...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
