# vllm-project/vllm#15257: [Bug]: tests/v1/tpu/test_sampler.py crashes due to ragged_paged_attention arg mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#15257](https://github.com/vllm-project/vllm/issues/15257) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tests/v1/tpu/test_sampler.py crashes due to ragged_paged_attention arg mismatch

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug To reproduce, run ``` VLLM_USE_V1=1 pytest -s tests/v1/tpu/test_sampler.py ``` Test killed (crashed) due to: ``` ... ERROR 03-21 00:10:17 [core.py:330] File "/root/pytorch/xla/torch_xla/experimental/custom_kernel.py", line 906, in validate_ragged_paged_attention_inputs ERROR 03-21 00:10:17 [core.py:330] _, _, num_kv_heads, head_dim_k = k_pages.shape ERROR 03-21 00:10:17 [core.py:330] ValueError: not enough values to unpack (expected 4, got 3) ... ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling build_error;crash;mismatch;nan_inf e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tests/v1/tpu/test_sampler.py crashes due to ragged_paged_attention arg mismatch bug ### Your current environment ### 🐛 Describe the bug To reproduce, run ``` VLLM_USE_V1=1 pytest -s tests/v1/tpu/test_sampler.py ``` Test...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: : tests/v1/tpu/test_sampler.py crashes due to ragged_paged_attention arg mismatch bug ### Your current environment ### 🐛 Describe the bug To reproduce, run ``` VLLM_USE_V1=1 pytest -s tests/v1/tpu/test_sampler.py ``` Te...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sked questions. correctness attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling build_error;crash;mismatch;nan_inf env_dependency;shape Your c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling build_error;crash;mismatch;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
