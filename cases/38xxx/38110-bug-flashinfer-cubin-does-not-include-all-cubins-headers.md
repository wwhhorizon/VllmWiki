# vllm-project/vllm#38110: [Bug]: `flashinfer-cubin` does not include all cubins/headers

| 字段 | 值 |
| --- | --- |
| Issue | [#38110](https://github.com/vllm-project/vllm/issues/38110) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;moe;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `flashinfer-cubin` does not include all cubins/headers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I saw this in CI for `evals/gpt_oss/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-sm100-fi-mxfp4-mxfp8-trtllm]` https://buildkite.com/vllm/ci/builds/57968/steps/canvas?jid=019d2473-3b51-4b05-abd6-6d98fa71d549&tab=output#019d2473-3b51-4b05-abd6-6d98fa71d549/L1413 Log from gpt-oss eval in CI ``` evals/gpt_oss/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-sm100-fi-mxfp4-mxfp8-trtllm] cl100k_base.tiktoken already exists. o200k_base.tiktoken already exists. Starting GPQA evaluation for model: openai/gpt-oss-20b Expected metric threshold: 0.568 Reasoning effort: low Server args: --tensor-parallel-size 2 --trust-remote-code --enforce-eager --disable-uvicorn-access-log Server environment variables: {'TIKTOKEN_ENCODINGS_BASE': '/vllm-workspace/tests/evals/gpt_oss/data', 'VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8': '1'} INFO 03-25 11:53:33 [model.py:541] Resolved architecture: GptOssForCausalLM Parse safetensors files: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00 =12.9 brand=unknown,driver>=535,driver =535,driver =535,driver =535,driver =535,driv...

## 现有链接修复摘要

#38391 [CI Bugfix] Pre-download missing FlashInfer headers in Docker build

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: oss/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-sm100-fi-mxfp4-mxfp8-trtllm]` https://buildkite.com/vllm/ci/builds/57968/steps/canvas?jid=019d2473-3b51-4b05-abd6-6d98fa71d549&tab=output#019d2473-3b51-4b0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: g ### Your current environment ### 🐛 Describe the bug I saw this in CI for `evals/gpt_oss/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-sm100-fi-mxfp4-mxfp8-trtllm]` https://buildkite.com/vllm/ci/builds/57...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: (v0.18.1rc1.dev107+gf118a4e37) with config: model='openai/gpt-oss-20b', speculative_config=None, tokenizer='openai/gpt-oss-20b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, tr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: in CI for `evals/gpt_oss/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-sm100-fi-mxfp4-mxfp8-trtllm]` https://buildkite.com/vllm/ci/builds/57968/steps/canvas?jid=019d2473-3b51-4b05-abd6-6d98fa71d549&tab=out...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ur current environment ### 🐛 Describe the bug I saw this in CI for `evals/gpt_oss/test_gpqa_correctness.py::test_gpqa_correctness[gpt-oss-20b-sm100-fi-mxfp4-mxfp8-trtllm]` https://buildkite.com/vllm/ci/builds/57968/step...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38391](https://github.com/vllm-project/vllm/pull/38391) | closes_keyword | 0.95 | [CI Bugfix] Pre-download missing FlashInfer headers in Docker build | Fixes #38110 ## Test plan - [ ] Docker image builds successfully with this change - [ ] gpt-oss MXFP4 MoE models start without header download attempts - [ ] Air-gapped runti |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
