# vllm-project/vllm#34942: [CI Failure]: Intel HPU Test - examples/offline_inference/basic/generate.py

| 字段 | 值 |
| --- | --- |
| Issue | [#34942](https://github.com/vllm-project/vllm/issues/34942) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Intel HPU Test - examples/offline_inference/basic/generate.py

### Issue 正文摘录

### Name of failing test examples/offline_inference/basic/generate.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test from https://buildkite.com/vllm/ci/builds/52218#019c74b4-5f24-40ae-bb84-9e83106c8af8 ``` WARNING 02-19 07:04:26 [registry.py:864] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_gaudi.models.qwen3_vl:HpuQwen3_VLForConditionalGeneration. Traceback (most recent call last): File "/workspace/vllm/examples/offline_inference/basic/generate.py", line 65, in main(args) File "/workspace/vllm/examples/offline_inference/basic/generate.py", line 31, in main llm = LLM(**args) ^^^^^^^^^^^ File "/workspace/vllm/vllm/entrypoints/llm.py", line 309, in __init__ engine_args = EngineArgs( ^^^^^^^^^^^ File " ", line 170, in __init__ File "/workspace/vllm/vllm/engine/arg_utils.py", line 621, in __post_init__ load_general_plugins() File "/workspace/vllm/vllm/plugins/__init__.py", line 82, in load_general_plugins func() File "/usr/local/lib/python3.12/dist-packages/vllm_gaudi/__init__.py", line 42,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: failing test examples/offline_inference/basic/generate.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing tes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Intel HPU Test - examples/offline_inference/basic/generate.py stale;ci-failure ### Name of failing test examples/offline_inference/basic/generate.py ### Basic information - [ ] Flaky test - [ ] Can reprod
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0ae-bb84-9e83106c8af8 ``` WARNING 02-19 07:04:26 [registry.py:864] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_gaudi.models.qwen3_vl:HpuQ...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nce/basic/generate.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test from https://buildkite.com/vllm/ci...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Failure]: Intel HPU Test - examples/offline_inference/basic/generate.py stale;ci-failure ### Name of failing test examples/offline_inference/basic/generate.py ### Basic information - [ ] Flaky test - [ ] Can reproduce l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
