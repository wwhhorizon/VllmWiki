# vllm-project/vllm#6902: [Bug]: Mixtral 8-way TP with --enable-lora crashes with CUDA illegal memory access error

| 字段 | 值 |
| --- | --- |
| Issue | [#6902](https://github.com/vllm-project/vllm/issues/6902) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Mixtral 8-way TP with --enable-lora crashes with CUDA illegal memory access error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) with 8-way TP and --enable-lora results in a crash during boot up when executing `determine_num_available_blocks`. The error is: ``` [rank0]: File "/workspace/my-vllm/lib64/python3.11/site-packages/torch/_tensor_str.py", line 331, in _tensor_str [rank0]: self = self.float() [rank0]: ^^^^^^^^^^^^ [rank0]: RuntimeError: CUDA error: an illegal memory access was encountered ``` Example command that results in the failure: ```shell vllm serve mistralai/Mixtral-8x7B-Instruct-v0.1 --tensor-parallel-size 8 --enable-lora ``` The stack trace points at the error coming from logging in `c10d_logger.py` after calling `torch.distributed.all_reduce`, but I think the GPU memory is already corrupted at this point and the calls indicated in the stack trace are just the next place the data is accessed. In my investigation, I was able to track the source of the memory corruption to the first call to the Punica kernels at https://github.com/vllm-project/vllm/blob/v0.5.3/vllm/lora/punica.py#L136. After that call, attempts to access the data of a...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: h2 = 16 with torch.device('cuda'): buffer = torch.zeros([seq_len, h2], dtype=torch.bfloat16) x = torch.zeros([seq_len, h1], dtype=torch.float32) wa_t_all = torch.zeros([1, 1, h2, h1], dtype=torch.bfloat16) indicies = to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e to make a simple reproducer script (works on a single GPU): ```python import torch from vllm import _custom_ops as ops # crashes with 8192 and 16384 too seq_len = 32768 h1 = 512 h2 = 16 with torch.device('cuda'): buff...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: rch.bfloat16) indicies = torch.zeros([seq_len], dtype=torch.long) ops.dispatch_bgmv(buffer, x, wa_t_all, indicies, 0, 1.0) # crashes with CUDA error: an illegal memory access was encountered buffer.any() print("SUCCESS"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Describe the bug Running [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) with 8-way TP and --enable-lora results in a crash during boot up when executing `determine_nu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Mixtral 8-way TP with --enable-lora crashes with CUDA illegal memory access error bug;stale ### Your current environment ### 🐛 Describe the bug Running [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.c...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | llm/lib64/python3.11/site-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0x5a7380 (0x7fa973b33380 in /workspace/my-vllm/lib64/python3.11/site-packages/torch/l… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | ce/my-vllm/lib64/python3.11/site-packages/torch/lib/libc10.so) frame #6: c10::tensorimpl::~tensorimpl() + 0x21b (0x7fa927bd01cb in /workspace/my-vllm/lib64/python3.11/site-package… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | ce/my-vllm/lib64/python3.11/site-packages/torch/lib/libc10.so) frame #7: c10::tensorimpl::~tensorimpl() + 0x9 (0x7fa927bd0379 in /workspace/my-vllm/lib64/python3.11/site-packages/… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | ibc_start_main + 0x80 (0x7fa975e08640 in /usr/lib64/libc.so.6) frame #27: _start + 0x25 (0x5571031a7095 in /workspace/my-vllm/bin/python3.11) /usr/lib64/python3.11/multiprocessing |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
