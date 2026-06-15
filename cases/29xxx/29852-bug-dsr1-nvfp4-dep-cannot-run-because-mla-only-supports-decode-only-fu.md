# vllm-project/vllm#29852: [Bug]: DSR1 NVFP4 DEP cannot run because MLA only supports decode-only full CUDAGraph capture

| 字段 | 值 |
| --- | --- |
| Issue | [#29852](https://github.com/vllm-project/vllm/issues/29852) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;fp8;moe |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DSR1 NVFP4 DEP cannot run because MLA only supports decode-only full CUDAGraph capture

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug B200 and GB200 have the same functional issue. Error message: [0;36m(EngineCore_DP1 pid=532376)[0;0m ERROR 12-02 00:20:05 [core.py:926] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 3950, in _dummy_run [0;36m(EngineCore_DP1 pid=532376)[0;0m ERROR 12-02 00:20:05 [core.py:926] attn_metadata, _ = self._build_attention_metadata( [0;36m(EngineCore_DP1 pid=532376)[0;0m ERROR 12-02 00:20:05 [core.py:926] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [0;36m(EngineCore_DP1 pid=532376)[0;0m ERROR 12-02 00:20:05 [core.py:926] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 1643, in _build_attention_metadata [0;36m(EngineCore_DP1 pid=532376)[0;0m ERROR 12-02 00:20:05 [core.py:926] attn_metadata_i = builder.build_for_cudagraph_capture( [0;36m(EngineCore_DP1 pid=532376)[0;0m ERROR 12-02 00:20:05 [core.py:926] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [0;36m(EngineCore_DP1 pid=532376)[0;0m ERROR 12-02 00:20:05 [core.py:926] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/attention/backends/mla/common.py", line 737, in build_for_cudagraph_capture [0;36m(EngineCor...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: DSR1 NVFP4 DEP cannot run because MLA only supports decode-only full CUDAGraph capture bug ### Your current environment ### 🐛 Describe the bug B200 and GB200 have the same functional issue. Error message: [0;36m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 6)[0;0m ERROR 12-02 00:20:05 [core.py:926] attn_metadata, _ = self._build_attention_metadata( [0;36m(EngineCore_DP1 pid=532376)[0;0m ERROR 12-02 00:20:05 [core.py:926] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [0;36m(EngineCo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: g]: DSR1 NVFP4 DEP cannot run because MLA only supports decode-only full CUDAGraph capture bug ### Your current environment ### 🐛 Describe the bug B200 and GB200 have the same functional issue. Error message: [0;36m(En...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: DSR1 NVFP4 DEP cannot run because MLA only supports decode-only full CUDAGraph capture bug ### Your current environment ### 🐛 Describe the bug B200 and GB200 have the same functional issue. Error message: [0;36m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: VLLM_ATTENTION_BACKEND=FLASHINFER_MLA export VLLM_FLASHINFER_MOE_BACKEND=latency export VLLM_USE_FLASHINFER_MOE_FP4=1 server-side: python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8087 --model nvidia/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
