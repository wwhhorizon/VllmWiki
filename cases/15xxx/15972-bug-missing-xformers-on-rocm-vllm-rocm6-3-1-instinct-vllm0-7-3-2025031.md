# vllm-project/vllm#15972: [Bug]:  Missing `Xformers` on `rocm/vllm:rocm6.3.1_instinct_vllm0.7.3_20250311` for pixtral-12b-2409

| 字段 | 值 |
| --- | --- |
| Issue | [#15972](https://github.com/vllm-project/vllm/issues/15972) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Missing `Xformers` on `rocm/vllm:rocm6.3.1_instinct_vllm0.7.3_20250311` for pixtral-12b-2409

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I used the [vllm-rocm](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_instinct_vllm0.7.3_20250311/images/sha256-de0a2649b735f45b7ecab8813eb7b19778ae1f40591ca1196b07bc29c42ed4a3) to run [pixtral-12b-2409](https://huggingface.co/mistralai/Pixtral-12B-2409/tree/main), but got following errors. ``` ERROR 04-02 19:53:15 [engine.py:400] ImportError: Xformers is required for Pixtral inference with the Mistral format Traceback (most recent call last): File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 402, in run_mp_engine raise e File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args return cls(ipc_path=ipc_p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: vironment ### 🐛 Describe the bug I used the [vllm-rocm](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_instinct_vllm0.7.3_20250311/images/sha256-de0a2649b735f45b7ecab8813eb7b19778ae1f40591ca1196b07bc29c42ed4a3) to ru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 7b19778ae1f40591ca1196b07bc29c42ed4a3) to run [pixtral-12b-2409](https://huggingface.co/mistralai/Pixtral-12B-2409/tree/main), but got following errors. ``` ERROR 04-02 19:53:15 [engine.py:400] ImportError: Xformers is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Missing `Xformers` on `rocm/vllm:rocm6.3.1_instinct_vllm0.7.3_20250311` for pixtral-12b-2409 bug;stale ### Your current environment ### 🐛 Describe the bug I used the [vllm-rocm](https://hub.docker.com/layers/rocm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ocm/vllm:rocm6.3.1_instinct_vllm0.7.3_20250311` for pixtral-12b-2409 bug;stale ### Your current environment ### 🐛 Describe the bug I used the [vllm-rocm](https://hub.docker.com/layers/rocm/vllm/rocm6.3.1_instinct_vllm0....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r.py", line 257, in determine_num_available_blocks self.model_runner.profile_run() File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*args, **kwargs) ^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
