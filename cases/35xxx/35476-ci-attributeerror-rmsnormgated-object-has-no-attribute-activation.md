# vllm-project/vllm#35476: [CI] AttributeError: 'RMSNormGated' object has no attribute 'activation'

| 字段 | 值 |
| --- | --- |
| Issue | [#35476](https://github.com/vllm-project/vllm/issues/35476) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] AttributeError: 'RMSNormGated' object has no attribute 'activation'

### Issue 正文摘录

## Name of failing test - `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** LM Eval Small Models (B200) **Category:** test ## Describe the failing test Worker process fails during memory profiling (profile_run) after model weights are successfully loaded. The RMSNormGated.forward_cuda method in layernorm.py attempts to access self.activation attribute, but the RMSNormGated object does not have this attribute. This occurs during the dummy forward pass used to determine available GPU memory before KV cache initialization. The error cascades through workers causing EngineCore initialization to fail and the server to exit. ``` AttributeError: 'RMSNormGated' object has no attribute 'activation' ``` ## Relevant builds - [Build #53476](https://buildkite.com/vllm/ci/builds/53476) (d0105b84) - [LM Eval Small Models (B200)](https://buildkite.com/vllm/ci/builds/53476#019c9bf8-ae55-401c-ab58-81f613c6e8bc) - [LM Eval Small Models (B200)](https://buildkite.com/vllm/ci/builds/53476#019c9cef-8bd9-43a7-9d62-00d03ff47ed9) ## History of f...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ated' object has no attribute 'activation' ci-failure ## Name of failing test - `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2]` ## Basic information - [ ] Flaky test - [ ] C...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: no attribute 'activation' ci-failure ## Name of failing test - `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2]` ## Basic information - [ ] Flaky test - [ ] Can reproduce loca...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g test - `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI] AttributeError: 'RMSNormGated' object has no attribute 'activation' ci-failure ## Name of failing test - `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2]` ## Basic inform
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: m8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** LM Eval Small...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
