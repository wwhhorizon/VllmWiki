# vllm-project/vllm#28651: [Bug]: CUDA Crash When Using `enable_lora=True`, disabling images `limit_mm_per_prompt` and setting `max_num_seqs` on Gemma 3

| 字段 | 值 |
| --- | --- |
| Issue | [#28651](https://github.com/vllm-project/vllm/issues/28651) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA Crash When Using `enable_lora=True`, disabling images `limit_mm_per_prompt` and setting `max_num_seqs` on Gemma 3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Describe the bug vLLM AsyncLLMEngine crashes with a CUDA illegal memory access error during initialization when `enable_lora=True`, `limit_mm_per_prompt={"image": 0}`, and `max_num_seqs` are set together for the `google/gemma-3-4b-it` model. ## To Reproduce Run this which will crash ```py from vllm import AsyncLLMEngine, AsyncEngineArgs vllm_kwargs = { "model": "google/gemma-3-4b-it", "enable_lora": True, "limit_mm_per_prompt": {"image": 0}, "max_num_seqs": 8, } # commenting out enable lora, image limit or max_num_seqs fixes the problem print("Initializing engine...") engine = AsyncLLMEngine.from_engine_args(AsyncEngineArgs(**vllm_kwargs)) print("SUCCESS! Engine initialized without crashing.") ``` ## Expected behavior Engine should initialize successfully with all three parameters set, as it does when any one of them is removed. ## Actual behavior Engine crashes during initialization with: ``` torch.AcceleratorError: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUN...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 4b-it` model. ## To Reproduce Run this which will crash ```py from vllm import AsyncLLMEngine, AsyncEngineArgs vllm_kwargs = { "model": "google/gemma-3-4b-it", "enable_lora": True, "limit_mm_per_prompt": {"image": 0}, "...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: e`, disabling images `limit_mm_per_prompt` and setting `max_num_seqs` on Gemma 3 bug ### Your current environment ### 🐛 Describe the bug ## Describe the bug vLLM AsyncLLMEngine crashes with a CUDA illegal memory access...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: gits;scheduler_memory;speculative_decoding cuda;kernel;operator;sampling;triton build_error;crash;mismatch;nan_inf env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cach...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA Crash When Using `enable_lora=True`, disabling images `limit_mm_per_prompt` and setting `max_num_seqs` on Gemma 3 bug ### Your current environment ### 🐛 Describe the bug ## Describe the bug vLLM AsyncLLMEngi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ... RuntimeError: Engine core initialization failed. See root cause...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /.venv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0xc6b2dc (0x77f0f1cff2dc in /mnt/nw/home/c.dumas/projects/diffing-toolkit/.venv/lib/… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | venv/lib/python3.12/site-packages/torch/lib/libtorch_python.so) frame #6: c10::tensorimpl::~tensorimpl() + 0x9 (0x77f14e8b7179 in /mnt/nw/home/c.dumas/projects/diffing-toolkit/.ve… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | toolkit/.venv/lib/python3.12/site-packages/torch/lib/libc10.so) frame #7: <unknown function> + 0x6c9e58 (0x77f141807e58 in /mnt/nw/home/c.dumas/projects/diffing-toolkit/.venv/lib/… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | inecore() [0x182e805] frame #11: vllm::enginecore() [0x182df92] frame #12: vllm::enginecore() [0x182e78b] frame #13: vllm::enginecore() [0x182df92] frame #14: vllm::enginecore() [… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | inecore() [0x182e78b] frame #15: vllm::enginecore() [0x182e7e2] frame #16: vllm::enginecore() [0x182e20d] frame #17: vllm::enginecore() [0x182e78b] frame #18: vllm::enginecore() [… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | inecore() [0x182e805] frame #19: vllm::enginecore() [0x1809082] frame #20: vllm::enginecore() [0x1801844] frame #21: vllm::enginecore() [0x182d9a4] frame #22: vllm::enginecore() [… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | inecore() [0x1809082] frame #20: vllm::enginecore() [0x1801844] frame #21: vllm::enginecore() [0x182d9a4] frame #22: vllm::enginecore() [0x182d803] frame #23: vllm::enginecore() [… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | inecore() [0x182cf56] frame #26: vllm::enginecore() [0x182cf56] frame #27: vllm::enginecore() [0x182cf56] frame #28: vllm::enginecore() [0x182cf56] frame #29: vllm::enginecore() [… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | inecore() [0x182cf56] frame #28: vllm::enginecore() [0x182cf56] frame #29: vllm::enginecore() [0x182d0a7] frame #30: vllm::enginecore() [0x182e6ba] frame #31: _pyeval_evalframedef… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | yeval_evalframedefault + 0x8432 (0x181b8b2 in vllm::enginecore) frame #32: vllm::enginecore() [0x1856cf0] frame #33: vllm::enginecore() [0x18027ab] frame #34: _pyeval_evalframedef… |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | _pyrun_simplefileobject + 0x118 (0x19b2d98 in vllm::enginecore) frame #53: _pyrun_anyfileobject + 0x42 (0x19b2c50 in vllm::enginecore) frame #54: vllm::enginecore() [0x1922d44] fr… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
