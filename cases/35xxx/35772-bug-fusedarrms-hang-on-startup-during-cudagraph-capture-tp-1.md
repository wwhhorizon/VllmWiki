# vllm-project/vllm#35772: [Bug]: `FusedARRMS` Hang on startup during cudagraph capture TP>1

| 字段 | 值 |
| --- | --- |
| Issue | [#35772](https://github.com/vllm-project/vllm/issues/35772) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;quantization |
| 子分类 |  |
| Operator 关键词 | fp8 |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `FusedARRMS` Hang on startup during cudagraph capture TP>1

### Issue 正文摘录

### Your current environment vLLM latest main, flashinfer-python 0.6.4, B200 ### 🐛 Describe the bug For multi-gpu, `--compilation-config.pass_config.fuse_allreduce_rms` is True when available. This is hanging on piecewise graph capture. I am able to reproduce locally, also [failing in CI](https://buildkite.com/vllm/ci/builds/53926/steps/canvas?sid=019cad2c-cd72-4554-a5aa-8e07cbbe5f37&tab=output). Simple reproducer: ``` vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 -tp 4 --trust-remote-code ``` Temp fix is `--compilation-config.pass_config.fuse_allreduce_rms false`. I don't know why this is broken ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#36157 [CI] Add mandatory H100 TP=2 smoke test | #38136 Fix multi-node allreduce fusion

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: `FusedARRMS` Hang on startup during cudagraph capture TP>1 bug;torch.compile ### Your current environment vLLM latest main, flashinfer-python 0.6.4, B200 ### 🐛 Describe the bug For multi-gpu, `--compilation-confi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: g]: `FusedARRMS` Hang on startup during cudagraph capture TP>1 bug;torch.compile ### Your current environment vLLM latest main, flashinfer-python 0.6.4, B200 ### 🐛 Describe the bug For multi-gpu, `--compilation-config.p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Simple reproducer: ``` vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 -tp 4 --trust-remote-code ``` Temp fix is `--compilation-config.pass_config.fuse_allreduce_rms false`. I don't know why this is broken ### Befo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e TP>1 bug;torch.compile ### Your current environment vLLM latest main, flashinfer-python 0.6.4, B200 ### 🐛 Describe the bug For multi-gpu, `--compilation-config.pass_config.fuse_allreduce_rms` is True when available. T...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: en available. This is hanging on piecewise graph capture. I am able to reproduce locally, also [failing in CI](https://buildkite.com/vllm/ci/builds/53926/steps/canvas?sid=019cad2c-cd72-4554-a5aa-8e07cbbe5f37&tab=output)...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36157](https://github.com/vllm-project/vllm/pull/36157) | mentioned | 0.6 | [CI] Add mandatory H100 TP=2 smoke test | rs hit them. For example, #34109 introduced a cudagraph capture hang (#35772) that passed all mandatory CI. The issue surfaced in an optional nightly LM eval test but took several… |
| [#38136](https://github.com/vllm-project/vllm/pull/38136) | closes_keyword | 0.95 | Fix multi-node allreduce fusion | resolves this by auto-selecting mnnvl backend for flashinfer all reduce in multi-node setup. In single node setup, the default backend remains trtllm due to issue #35772 ## Test |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
