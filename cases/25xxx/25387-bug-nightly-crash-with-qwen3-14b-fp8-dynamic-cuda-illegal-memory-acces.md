# vllm-project/vllm#25387: [Bug] Nightly crash with Qwen3-14B-FP8-dynamic: CUDA illegal memory access (EngineDeadError)

| 字段 | 值 |
| --- | --- |
| Issue | [#25387](https://github.com/vllm-project/vllm/issues/25387) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug] Nightly crash with Qwen3-14B-FP8-dynamic: CUDA illegal memory access (EngineDeadError)

### Issue 正文摘录

### Your current environment RTX 5090 ### 🐛 Describe the bug When running the nightly container (`vllm/vllm-openai:nightly`) with **Qwen3-14B-FP8-dynamic**, the engine crashes with: CUDA error: an illegal memory access was encountered vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. The crash happens after processing ~1k tokens. Logs show a `TimeoutError` in `shm_broadcast.py` followed by `EngineCore encountered a fatal error`. --- ### Reproduction **Command to launch container:** ```bash docker run -d --gpus all --name vllm-qwen14b-fp8 \ -p 8000:8000 \ -v /var/models:/var/models \ vllm/vllm-openai:nightly \ --model /var/models/Qwen3-14B-FP8-dynamic \ --served-model-name qwen3-14b-fp8 \ --download-dir /var/models \ --max-model-len 32768 \ --async-scheduling \ --enable-auto-tool-choice \ --tool-call-parser hermes ```` ```bash (EngineCore_DP0 pid=142) ERROR 09-22 07:18:30 [core.py:710] EngineCore encountered a fatal error. (EngineCore_DP0 pid=142) ERROR 09-22 07:18:30 [core.py:710] Traceback (most recent call last): (EngineCore_DP0 pid=142) ERROR 09-22 07:18:30 [core.py:710] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 701, i...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rror`. --- ### Reproduction **Command to launch container:** ```bash docker run -d --gpus all --name vllm-qwen14b-fp8 \ -p 8000:8000 \ -v /var/models:/var/models \ vllm/vllm-openai:nightly \ --model /var/models/Qwen3-14...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug] Nightly crash with Qwen3-14B-FP8-dynamic: CUDA illegal memory access (EngineDeadError) bug;stale ### Your current environment RTX 5090 ### 🐛 Describe the bug When running the nightly container (`vllm/vllm-openai:n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug] Nightly crash with Qwen3-14B-FP8-dynamic: CUDA illegal memory access (EngineDeadError) bug;stale ### Your current environment RTX 5090 ### 🐛 Describe the bug When running the nightly container (`vllm/vllm-openai:n...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Qwen3-14B-FP8-dynamic: CUDA illegal memory access (EngineDeadError) bug;stale ### Your current environment RTX 5090 ### 🐛 Describe the bug When running the nightly container (`vllm/vllm-openai:nightly`) with **Qwen3-14B...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug] Nightly crash with Qwen3-14B-FP8-dynamic: CUDA illegal memory access (EngineDeadError) bug;stale ### Your current environment RTX 5090 ### 🐛 Describe the bug When running the nightly container (`vllm/vllm-openai:n...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0xc6b2dc (0x7fa1a2aff2dc in /usr/local/lib/python3.12/dist-packages/torch/lib/libtor… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | ocal/lib/python3.12/dist-packages/torch/lib/libtorch_python.so) frame #6: c10::tensorimpl::~tensorimpl() + 0x9 (0x7fa1ff75c179 in /usr/local/lib/python3.12/dist-packages/torch/lib… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | in /usr/local/lib/python3.12/dist-packages/torch/lib/libc10.so) frame #7: <unknown function> + 0x6c9e58 (0x7fa1f2607e58 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtor… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | vllm::worker() [0x59b8bb] frame #11: vllm::worker() [0x59b914] frame #12: vllm::worker() [0x52c939] frame #13: vllm::worker() [0x59b860] frame #14: vllm::worker() [0x53bd64] frame… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | vllm::worker() [0x53bd64] frame #15: vllm::worker() [0x59bded] frame #16: vllm::worker() [0x53bd64] frame #17: vllm::worker() [0x59bded] frame #18: vllm::worker() [0x53bd64] frame… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | vllm::worker() [0x53bd64] frame #19: vllm::worker() [0x59bded] frame #20: vllm::worker() [0x57e600] frame #21: vllm::worker() [0x57cbd0] frame #22: vllm::worker() [0x57bc06] frame… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | vllm::worker() [0x59bded] frame #20: vllm::worker() [0x57e600] frame #21: vllm::worker() [0x57cbd0] frame #22: vllm::worker() [0x57bc06] frame #23: vllm::worker() [0x594bb7] frame… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | vllm::worker() [0x67373c] frame #26: vllm::worker() [0x673631] frame #27: vllm::worker() [0x59bdf9] frame #28: _pyobject_clearmanageddict + 0x8f (0x65e98f in vllm::worker) frame #… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | 8: _pyobject_clearmanageddict + 0x8f (0x65e98f in vllm::worker) frame #29: vllm::worker() [0x659760] frame #30: vllm::worker() [0x557c4e] frame #31: vllm::worker() [0x61da9e] fram… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | vllm::worker() [0x557c4e] frame #31: vllm::worker() [0x61da9e] frame #32: pygc_collect + 0x52 (0x6588b2 in vllm::worker) frame #33: py_finalizeex + 0x156 (0x63f656 in vllm::worker… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
