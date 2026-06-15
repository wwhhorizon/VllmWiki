# vllm-project/vllm#43163: [Bug]: GLM-5.1-FP8 produces gibberish with RunAI streamer after ac3dac545

| 字段 | 值 |
| --- | --- |
| Issue | [#43163](https://github.com/vllm-project/vllm/issues/43163) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: GLM-5.1-FP8 produces gibberish with RunAI streamer after ac3dac545

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving `zai-org/GLM-5.1-FP8` with vLLM using `--load-format=runai_streamer`, tool-calling chat requests can produce corrupted/gibberish output. The model loads and serves successfully, but streamed output becomes abnormal and often looks like fragments of tool schemas or unrelated text instead of a coherent answer. This reproduces on `v0.20.0` and on the Apr 16 nightly. It does not reproduce on the Apr 15 nightly in the same test setup. The exact first bad commit from source bisection is: ```text ac3dac545b28ea6cf847e0044859e58f33d4f8b9 [Bugfix][Perf] Indexer upcast WK to BF16 for fusion (#38928) ``` PR that caused the issue: https://github.com/vllm-project/vllm/pull/38928 Commit: https://github.com/vllm-project/vllm/commit/ac3dac545b28ea6cf847e0044859e58f33d4f8b9 Immediate bisect boundary: | Commit | Result | | --- | --- | | `39ac640490ee2e8f951d343ae1707dd9bdacaf70` | good | | `ac3dac545b28ea6cf847e0044859e58f33d4f8b9` | bad | ### Minimal reproduction An end-to-end repro script is available here: ```text https://raw.githubusercontent.com/bbartels/vllm_runai_reproduction/main/run-docker-and-repro.sh ``` Run on an 8x H200 h...

## 现有链接修复摘要

#38928 [Bugfix][Perf] Indexer upcast WK to BF16 for fusion

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ps://raw.githubusercontent.com/bbartels/vllm_runai_reproduction/main/run-docker-and-repro.sh ``` Run on an 8x H200 host with Docker/NVIDIA runtime available: ```bash wget https://raw.githubusercontent.com/bbartels/vllm_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: GLM-5.1-FP8 produces gibberish with RunAI streamer after ac3dac545 ### Your current environment ### 🐛 Describe the bug When serving `zai-org/GLM-5.1-FP8` with vLLM using `--load-format=runai_streamer`, tool-calli...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ribe the bug When serving `zai-org/GLM-5.1-FP8` with vLLM using `--load-format=runai_streamer`, tool-calling chat requests can produce corrupted/gibberish output. The model loads and serves successfully, but streamed ou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: p` | good | | `bash`, `edit`, `glob`, `grep`, `question` | bad | So the smallest currently known failing payload is: ```text user message: "hi" tools: bash, edit, glob, grep, question tool_choice: auto stream: true max_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ld;distributed_parallel;frontend_api;model_support;quantization cuda;fp8;triton build_error dtype;env_dependency #38928 [Bugfix][Perf] Indexer upcast WK to BF16 for fusion Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38928](https://github.com/vllm-project/vllm/pull/38928) | mentioned | 0.45 | [Bugfix][Perf] Indexer upcast WK to BF16 for fusion | 4859e58f33d4f8b9 [bugfix][perf] indexer upcast wk to bf16 for fusion (#38928) ``` pr that caused the issue: https://github.com/vllm-project/vllm/pull/38928 commit: https://github.… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
