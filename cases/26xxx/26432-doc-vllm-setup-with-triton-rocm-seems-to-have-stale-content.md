# vllm-project/vllm#26432: [Doc]: vLLM setup with Triton/ROCm seems to have stale content.

| 字段 | 值 |
| --- | --- |
| Issue | [#26432](https://github.com/vllm-project/vllm/issues/26432) |
| 状态 | closed |
| 标签 | documentation;rocm;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: vLLM setup with Triton/ROCm seems to have stale content.

### Issue 正文摘录

### 📚 The doc issue Noticed two issues on the GPU installation page for vLLM https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html?device=cuda#build-wheel-from-source 1. AMD ROCm installation instruction says "Install ROCm's Triton (the default triton-mlir branch) following the instructions from [ROCm/triton](https://github.com/ROCm/triton/blob/triton-mlir/README.md)", but the instruction is using triton-lang/triton ``` git clone https://github.com/triton-lang/triton.git cd triton git checkout e5be006 ``` 2. NVIDIA CUDA instructions uses "uv" but AMD ROCm is not explicitly using "uv", so it adds bit of confusion for user about the instructions to use. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#27603 [ROCm][Docs] Update ROCm installation docs for ROCm 7.0

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: umentation;rocm;stale ### 📚 The doc issue Noticed two issues on the GPU installation page for vLLM https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html?device=cuda#build-wheel-from-source 1. AMD ROCm ins...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Doc]: vLLM setup with Triton/ROCm seems to have stale content. documentation;rocm;stale ### 📚 The doc issue Noticed two issues on the GPU installation page for vLLM https://docs.vllm.ai/en/latest/getting_started/instal...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Doc]: vLLM setup with Triton/ROCm seems to have stale content. documentation;rocm;stale ### 📚 The doc issue Noticed two issues on the GPU installation page for vLLM https://docs.vllm.ai/en/latest/getting_started/instal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: vLLM setup with Triton/ROCm seems to have stale content. documentation;rocm;stale ### 📚 The doc issue Noticed two issues on the GPU installation page for vLLM https://docs.vllm.ai/en/latest/getting_started/instal...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: o issues on the GPU installation page for vLLM https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html?device=cuda#build-wheel-from-source 1. AMD ROCm installation instruction says "Install ROCm's Triton (t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27603](https://github.com/vllm-project/vllm/pull/27603) | closes_keyword | 0.95 | [ROCm][Docs] Update ROCm installation docs for ROCm 7.0 | fixes #26432, #25187 --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [ ] The purpose of the PR, such as "Fix some issue (link exi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
