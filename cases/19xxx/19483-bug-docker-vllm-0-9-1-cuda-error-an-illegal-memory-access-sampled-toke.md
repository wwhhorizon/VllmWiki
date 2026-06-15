# vllm-project/vllm#19483: [Bug]: Docker vLLM 0.9.1 CUDA error: an illegal memory access, sampled_token_ids.tolist()

| 字段 | 值 |
| --- | --- |
| Issue | [#19483](https://github.com/vllm-project/vllm/issues/19483) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 56; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Docker vLLM 0.9.1 CUDA error: an illegal memory access, sampled_token_ids.tolist()

### Issue 正文摘录

### Your current environment Docker on 4 x A100 SMX. BTW: vLLM 0.8.4 worked stable with same setup. 0.9.01 was already unstable (restarted few time a day), now even more. ``` services: vllm-qwen25-72b: image: vllm/vllm-openai:v0.9.1 container_name: vllm-qwen25-72b environment: ... - HF_TOKEN=$HF_TOKEN - VLLM_NO_USAGE_STATS=1 ipc: host deploy: resources: reservations: devices: - driver: nvidia device_ids: ['0', '1', '2', '3'] capabilities: [ gpu ] network_mode: host volumes: - /mnt/sda/huggingface:/root/.cache/huggingface - .:/opt/vllm command: - --port=8000 - --disable-log-requests - --model=Qwen/Qwen2.5-72B-Instruct # - --served-model-name=Qwen/Qwen2.5-72B-Instruct # - --max-model-len=32768 - --tensor-parallel-size=4 - --gpu-memory-utilization=0.90 - --swap-space=5 restart: unless-stopped ``` ### 🐛 Describe the bug See log file below vLLM 0.9.1 crashes frequently with Qwen 2.5 on 4xA100 SMX. (0.9.0.1 also crashed with "CUDA error: an illegal memory access was encountered", but much less frequently and not with a clear hint what went wrong. 0.8.4 was running stable.) I have no example request - we use a mix of normal and guided JSON sampling. This might be the main problem? ``` (V...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: - .:/opt/vllm command: - --port=8000 - --disable-log-requests - --model=Qwen/Qwen2.5-72B-Instruct # - --served-model-name=Qwen/Qwen2.5-72B-Instruct # - --max-model-len=32768 - --tensor-parallel-size=4 - --gpu-memory-uti...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Docker vLLM 0.9.1 CUDA error: an illegal memory access, sampled_token_ids.tolist() bug ### Your current environment Docker on 4 x A100 SMX. BTW: vLLM 0.8.4 worked stable with same setup. 0.9.01 was already unstab...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: nstable (restarted few time a day), now even more. ``` services: vllm-qwen25-72b: image: vllm/vllm-openai:v0.9.1 container_name: vllm-qwen25-72b environment: ... - HF_TOKEN=$HF_TOKEN - VLLM_NO_USAGE_STATS=1 ipc: host de...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Docker vLLM 0.9.1 CUDA error: an illegal memory access, sampled_token_ids.tolist() bug ### Your current environment Docker on 4 x A100 SMX. BTW: vLLM 0.8.4 worked stable with same setup. 0.9.01 was already unstab...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | r/local/lib/python3.12/dist-packages/torch/lib/libtorch_cpu.so) frame #4: c10d::tcpstore::check(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdc253 (0x7efcd27b3253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unkn… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | 53 (0x7efcd27b3253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown function> + 0x94ac3 (0x7efd53341ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #8: clone + 0x… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
