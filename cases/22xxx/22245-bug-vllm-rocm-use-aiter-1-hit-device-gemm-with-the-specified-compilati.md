# vllm-project/vllm#22245: [Bug]: VLLM_ROCM_USE_AITER=1 hit device_gemm with the specified compilation parameters does not support this GEMM problem for Qwen3-235B-A22B

| 字段 | 值 |
| --- | --- |
| Issue | [#22245](https://github.com/vllm-project/vllm/issues/22245) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM_ROCM_USE_AITER=1 hit device_gemm with the specified compilation parameters does not support this GEMM problem for Qwen3-235B-A22B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving Qwen3-235B-A22B with TP=8 and use aiter, vllm v0 throws the error: RuntimeError: wrong! device_gemm with the specified compilation parameters does not support this GEMM problem The serving command: ```bash VLLM_ROCM_USE_AITER=1 VLLM_USE_V1=0 vllm serve /models/Qwen3-235B-A22B/ --tensor-parallel-size 8 --gpu-memory-utilization 0.9 --disable-log-requests --trust-remote-code --disable-log-requests --max-model-len 32768 ``` The whole backtrace: ``` bash ERROR 08-05 08:53:39 [engine.py:458] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/qwen3_moe.py", line 136, in forward [155/1944] ERROR 08-05 08:53:39 [engine.py:458] final_hidden_states = self.experts(hidden_states=hidden_states, ERROR 08-05 08:53:39 [engine.py:458] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 08-05 08:53:39 [engine.py:458] File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl ERROR 08-05 08:53:39 [engine.py:458] return self._call_impl(*args, **kwargs) ERROR 08-05 08:53:39 [engine.py:458] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 08-05 08:53:39 [engine.py:458] File "/usr/loc...

## 现有链接修复摘要

#20988 [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [Bug]: VLLM_ROCM_USE_AITER=1 hit device_gemm with the specified compilation parameters does not support this GEMM problem for Qwen3-235B-A22B bug;rocm;stale ### Your current environment ### 🐛 Describe the bug When servi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: VLLM_ROCM_USE_AITER=1 hit device_gemm with the specified compilation parameters does not support this GEMM problem for Qwen3-235B-A22B bug;rocm;stale ### Your current environment ### 🐛 Describe the bug When servi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: VLLM_ROCM_USE_AITER=1 hit device_gemm with the specified compilation parameters does not support this GEMM problem for Qwen3-235B-A22B bug;rocm;stale ### Your current environment ### 🐛 Describe the bug When servi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rameters does not support this GEMM problem for Qwen3-235B-A22B bug;rocm;stale ### Your current environment ### 🐛 Describe the bug When serving Qwen3-235B-A22B with TP=8 and use aiter, vllm v0 throws the error: RuntimeE...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: VLLM_ROCM_USE_AITER=1 hit device_gemm with the specified compilation parameters does not support this GEMM problem for Qwen3-235B-A22B bug;rocm;stale ### Your current environment ### 🐛 Describe the bug When servi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20988](https://github.com/vllm-project/vllm/pull/20988) | mentioned | 0.6 | [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | ase add support for Amd Instinct MI50... [feature request, rocm] 3. #22245: [Bug]: VLLM_ROCM_USE_AITER=1 hit device_gemm with the specif... [bug, rocm] 4. #14964: [Feature] [ROCm]… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
