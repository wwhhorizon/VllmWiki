# vllm-project/vllm#41094: [Bug]: [GLM-5.1] [MTP] DeepGEMM context_lens.is_contiguous assertion in paged MQA metadata

| 字段 | 值 |
| --- | --- |
| Issue | [#41094](https://github.com/vllm-project/vllm/issues/41094) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cache;fp8;moe |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: [GLM-5.1] [MTP] DeepGEMM context_lens.is_contiguous assertion in paged MQA metadata

### Issue 正文摘录

### Describe the bug `zai-org/GLM-5.1-FP8` crashes under vLLM V1 + MTP speculative decoding with a DeepGEMM paged MQA metadata assertion: ```text RuntimeError: Assertion error (/workspace/.deps/deepgemm-src/csrc/apis/attention.hpp:201): context_lens.is_contiguous() ``` This looks very similar to #40987, but on GLM-5.1-FP8 instead of DeepSeek-V4. It may also be related to #40926, since this is the same GLM-5.1 / DSA / MoE / MLA / MTP serving class. In our deployment, short requests usually work, but a long-context chat request caused the engine to die. The pod restarted cleanly after the fatal EngineCore error. This does not look like OOM: Kubernetes reported the previous container state as `Completed` with exit code `0`, and the first root-cause error was the DeepGEMM assertion above. ### Environment * vLLM image: `vllm/vllm-openai@sha256:46da022ce07aae43e4ffae844aeab467a223437e071abadf566555699fbf16c3` (v0.20.0 image digest) * Model: `zai-org/GLM-5.1-FP8` * Served model name: `zai-org/glm-5.1` * Hardware: 8x NVIDIA B200 * Runtime: Kubernetes/k3s pod, TP=8 * KV cache dtype: `fp8` * Prefix caching: enabled * MTP: enabled, `num_speculative_tokens=3` ### Serve command ```bash vllm se...

## 现有链接修复摘要

#40989 [Bugfix] Ensure DeepGEMM metadata gets contiguous context_lens | #43970 [Bugfix] Align MLA indexer block table with MTP speculative decode

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 5: tarted cleanly after the fatal EngineCore error. This does not look like OOM: Kubernetes reported the previous container state as `Completed` with exit code `0`, and the first root-cause error was the DeepGEMM assertion...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: infer-cubin /tmp/flashinfer-cubin-shadow/flashinfer_cubin printf '%b' '__version__ = "0.6.8.post1"\nCUBIN_DIR = "/tmp/flashinfer-cubin"\ndef get_cubin_dir():\n return CUBIN_DIR\n' > /tmp/flashinfer-cubin-shadow/flashinf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: s assertion in paged MQA metadata ### Describe the bug `zai-org/GLM-5.1-FP8` crashes under vLLM V1 + MTP speculative decoding with a DeepGEMM paged MQA metadata assertion: ```text RuntimeError: Assertion error (/workspa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [Bug]: [GLM-5.1] [MTP] DeepGEMM context_lens.is_contiguous assertion in paged MQA metadata ### Describe the bug `zai-org/GLM-5.1-FP8` crashes under vLLM V1 + MTP speculative decoding with a DeepGEMM paged MQA metadata a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ### Describe the bug `zai-org/GLM-5.1-FP8` crashes under vLLM V1 + MTP speculative decoding with a DeepGEMM paged MQA metadata assertion: ```text RuntimeError: Assertion error (/workspace/.deps/deepgemm-src/csrc/apis/at...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40989](https://github.com/vllm-project/vllm/pull/40989) | mentioned | 0.45 | [Bugfix] Ensure DeepGEMM metadata gets contiguous context_lens | the stack and assertion look aligned with #40987 and the draft fix in #40989, which makes `seq_lens` / `context_lens` contiguous before calling deepgemm metadata code. even if the… |
| [#43970](https://github.com/vllm-project/vllm/pull/43970) | closes_keyword | 0.95 | [Bugfix] Align MLA indexer block table with MTP speculative decode | Fixes #41094 (DeepGEMM contiguous assertion) together with the block table alignment that caused EngineDeadError on high-concurrency MTP. ## Purpose ## Test Plan ## |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
