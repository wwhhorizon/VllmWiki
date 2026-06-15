# vllm-project/vllm#27476: [Installation]: FlashInfer Dependency issue due to pre-release apache-tvm-ffi

| 字段 | 值 |
| --- | --- |
| Issue | [#27476](https://github.com/vllm-project/vllm/issues/27476) |
| 状态 | closed |
| 标签 | installation;nvidia |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: FlashInfer Dependency issue due to pre-release apache-tvm-ffi

### Issue 正文摘录

### Your current environment On Top of Tree: ```bash (vllm) [robertgshaw2-redhat@nma-h200-isolated-0-preserve vllm]$ VLLM_USE_PRECOMPILED=1 uv pip install -e . Updated https://github.com/triton-lang/triton.git (c3c476f357f1e9768ea4e45aa5c17528449ab9ef) × No solution found when resolving dependencies: ╰─▶ Because there is no version of apache-tvm-ffi==0.1.0b15 and flashinfer-python==0.4.1 depends on apache-tvm-ffi==0.1.0b15, we can conclude that flashinfer-python==0.4.1 cannot be used. And because vllm==0.11.1rc3.dev57+g6454afec9.precompiled depends on flashinfer-python==0.4.1, we can conclude that vllm==0.11.1rc3.dev57+g6454afec9.precompiled cannot be used. And because only vllm==0.11.1rc3.dev57+g6454afec9.precompiled is available and you require vllm, we can conclude that your requirements are unsatisfiable. hint: `apache-tvm-ffi` was requested with a pre-release marker (e.g., apache-tvm-ffi==0.1.0b15), but pre-releases weren't enabled (try: `--prerelease=allow`) ``` ### How you are installing vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentati...

## 现有链接修复摘要

#41648 [Don't merge] Compare torch vs torch stable vs tvm-ffi

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: FlashInfer Dependency issue due to pre-release apache-tvm-ffi installation;nvidia ### Your current environment On Top of Tree: ```bash (vllm) [robertgshaw2-redhat@nma-h200-isolated-0-preserve vllm]$ VLLM
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Installation]: FlashInfer Dependency issue due to pre-release apache-tvm-ffi installation;nvidia ### Your current environment On Top of Tree: ```bash (vllm) [robertgshaw2-redhat@nma-h200-isolated-0-preserve vllm]$ VLLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t your requirements are unsatisfiable. hint: `apache-tvm-ffi` was requested with a pre-release marker (e.g., apache-tvm-ffi==0.1.0b15), but pre-releases weren't enabled (try: `--prerelease=allow`) ``` ### How you are in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build triton env_dependency #41648 [Don't merge] Compare torch vs torc...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41648](https://github.com/vllm-project/vllm/pull/41648) | mentioned | 0.6 | [Don't merge] Compare torch vs torch stable vs tvm-ffi | . Its big risks are organizational — pre-release pinning churn ([vLLM #27476](https://github.com/vllm-project/vllm/issues/27476)) and the ABI itself still being 0.1.x — not techni… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
