# vllm-project/vllm#9727: [Bug]: vllm.LLM does not seem to re-initialize for distributed inference with subsequent models with Offline Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#9727](https://github.com/vllm-project/vllm/issues/9727) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vllm.LLM does not seem to re-initialize for distributed inference with subsequent models with Offline Inference

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am using `vllm.LLM` for offline inference, similar to https://docs.vllm.ai/en/latest/getting_started/examples/offline_inference.html I am running the script for multiple models and reinit the LLM with a new one like: ``` self.llm = LLM( model=model_name, trust_remote_code=True, tensor_parallel_size=8, gpu_memory_utilization=0.95, max_num_batched_tokens=1024, max_num_seqs=1024, max_model_len=1024, quantization="fp8", ) ``` The first model load always loads and runs as expected: ``` Processing nvidia/Llama-3.1-Nemotron-70B-Instruct-HF: 100%|██████████████████████████████████████████████████████| 4066/4066 [06:47 + 0x15eb578 (0x7c73be1eb578 in /home/hotaisle/miniforge3/envs/vllm/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so) frame #2: + 0x605ff95 (0x7c73c2c5ff95 in /home/hotaisle/miniforge3/envs/vllm/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so) frame #3: + 0x6060136 (0x7c73c2c60136 in /home/hotaisle/miniforge3/envs/vllm/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so) frame #4: + 0x60605a4 (0x7c73c2c605a4 in /home/hotaisle/miniforge3/envs/vllm/lib/python3.11/site-packa...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: entire process needs to be reloaded for each process or is this a bug specific to my setup? This looks like potentially a torch.distributed error, so maybe a multi-gpu only thing? It looks like there's a resource cleanu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 55c in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #41: Py_BytesMain + 0x37 (0x5ffb8a358ac7 in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #42: + 0x29d90 (0x7c73d4a29d90 in /lib/x86_64-linux-gnu/libc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: does not seem to re-initialize for distributed inference with subsequent models with Offline Inference bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am using `vllm.L...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: gits;speculative_decoding cuda;fp8;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency;memory_layout;shape #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: max_num_seqs=1024, max_model_len=1024, quantization="fp8", ) ``` The first model load always loads and runs as expected: ``` Processing nvidia/Llama-3.1-Nemotron-70B-Instruct-HF: 100%|███████████████████████████████████...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | s/vllm/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so) frame #4: <unknown function> + 0x60605a4 (0x753d258605a4 in /home/hotaisle/miniforge3/envs/vllm/lib/python3.11/site-… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | s/vllm/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so) frame #6: c10d::tcpstore::tcpstore(std::string, c10d::tcpstoreoptions const&) + 0x20c (0x753d2581facc in /home/hotai… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | s/vllm/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so) frame #7: <unknown function> + 0xdc3faf (0x753d359c3faf in /home/hotaisle/miniforge3/envs/vllm/lib/python3.11/site-p… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | 395f719b586 in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #12: _pyobject_call + 0x12b (0x6395f7186e5b in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #13: <unk… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | llm/lib/python3.11/site-packages/torch/lib/libtorch_python.so) frame #16: _pyobject_maketpcall + 0x29b (0x6395f714aa2b in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #17: |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | 395f7173e03 in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #20: pyobject_vectorcall + 0x2c (0x6395f7164c0c in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #21:… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | 395f7164c0c in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #21: _pyeval_evalframedefault + 0x70a (0x6395f71580da in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | 395f7186be4 in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #27: _pyeval_evalframedefault + 0x45d7 (0x6395f715bfa7 in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | 395f719bd02 in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #29: <unknown function> + 0x2275d0 (0x6395f719b5d0 in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #3… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | 395f717cdbf in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #32: pyobject_call + 0x134 (0x6395f7186be4 in /home/hotaisle/miniforge3/envs/vllm/bin/python) frame #33: _pyev… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
