# vllm-project/vllm#42999: [CI Failure]: Spec Decode Draft Model fails during graph capture

| 字段 | 值 |
| --- | --- |
| Issue | [#42999](https://github.com/vllm-project/vllm/issues/42999) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;speculative_decoding |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Spec Decode Draft Model fails during graph capture

### Issue 正文摘录

### Name of failing test tests/v1/e2e/spec_decode/test_lora_with_spec_decode.py::test_batch_inference_correctness[model_setup0] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Here's the full callstack ``` Capturing CUDA graphs (PIECEWISE): 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:00 ", line 145, in execution_fn (EngineCore pid=3374923) File "/home/sagemoore/git/nm-vllm/vllm/compilation/cuda_graph.py", line 313, in __call__ (EngineCore pid=3374923) with torch.cuda.graph( (EngineCore pid=3374923) ^^^^^^^^^^^^^^^^^ (EngineCore pid=3374923) File "/home/sagemoore/git/nm-vllm/.venv/lib64/python3.12/site-packages/torch/cuda/graphs.py", line 257, in __enter__ (EngineCore pid=3374923) self.cuda_graph.capture_begin( (EngineCore pid=3374923) File "/home/sagemoore/git/nm-vllm/.venv/lib64/python3.12/site-packages/torch/cuda/graphs.py", line 115, in capture_begin (EngineCore pid=3374923) super().capture_begin(pool=pool, captu...

## 现有链接修复摘要

#43084 [CI] Disable V2 model runner for LoRA configs

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [CI Failure]: Spec Decode Draft Model fails during graph capture ci-failure ### Name of failing test tests/v1/e2e/spec_decode/test_lora_with_spec_decode.py::test_batch_inference_correctness[model_setup0] ### Basic infor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Spec Decode Draft Model fails during graph capture ci-failure ### Name of failing test tests/v1/e2e/spec_decode/test_lora_with_spec_decode.py::test_batch_inference_correctness[model_setup0] ### Basic infor
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: Spec Decode Draft Model fails during graph capture ci-failure ### Name of failing test tests/v1/e2e/spec_decode/test_lora_with_spec_decode.py::test_batch_inference_correctness[model_setup0] ### Basic infor...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ectness[model_setup0] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Here's the full callstack ``` Capt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### 🧪 Describe the failing test Here's the full callstack ``` Capturing CUDA graphs (PIECEWISE): 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43084](https://github.com/vllm-project/vllm/pull/43084) | closes_keyword | 0.95 | [CI] Disable V2 model runner for LoRA configs | Fixes #42999 Nightly CI #66835 fails `test_batch_inference_correctness[model_setup0]` on Qwen3-1.7B + LoRA with `RuntimeError: CUDA graphs must be captured on a non-default stre |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
