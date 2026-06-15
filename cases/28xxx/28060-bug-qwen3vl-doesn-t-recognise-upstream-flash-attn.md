# vllm-project/vllm#28060: [Bug]: Qwen3VL doesn't recognise upstream `flash-attn`

| 字段 | 值 |
| --- | --- |
| Issue | [#28060](https://github.com/vllm-project/vllm/issues/28060) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;gemm;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3VL doesn't recognise upstream `flash-attn`

### Issue 正文摘录

### Your current environment Tested on latest `main` (c9f66da8fdd0a082cd451cecfb7848bb287bf251). ### 🐛 Describe the bug Qwen3VL fails to use upstream `flash-attn` if `VLLM_ATTENTION_BACKEND=FLASH_ATTN` is explicitly set. ``` VLLM_ATTENTION_BACKEND=FLASH_ATTN vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 --limit-mm-per-prompt.video 0 --max-model-len 10000 ``` Fails with the following error despite the fact that upstream `flash-attn` would support `headdim=32` ``` RuntimeError: This flash attention build does not support headdim not being a multiple of 32. ``` This is likely due to the following logic https://github.com/vllm-project/vllm/blob/1fb4217a052189feb8709b67bb3209ab316d13b7/vllm/model_executor/models/qwen3_vl.py#L373-L380 If I manually set `use_upstream_fa = True` everything works as expected. I'm not familiar with the reasoning behind this logic. @DarkLight1337 @Isotr0py @ywang96 Do you know whether this can be changed to prefer upstream `flash-attn` for cases where the builtin one doesn't support the `headdim`? This came up when I tried `VLLM_BATCH_INVARIANT=1` which forces the `FLASH_ATTN` backend. Note: I haven't checked whether other models have similar issues.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: e the bug Qwen3VL fails to use upstream `flash-attn` if `VLLM_ATTENTION_BACKEND=FLASH_ATTN` is explicitly set. ``` VLLM_ATTENTION_BACKEND=FLASH_ATTN vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 --limit-mm-per-prompt.vi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: use upstream `flash-attn` if `VLLM_ATTENTION_BACKEND=FLASH_ATTN` is explicitly set. ``` VLLM_ATTENTION_BACKEND=FLASH_ATTN vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 --limit-mm-per-prompt.video 0 --max-model-len 10000...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: M_ATTENTION_BACKEND=FLASH_ATTN vllm serve Qwen/Qwen3-VL-30B-A3B-Instruct-FP8 --limit-mm-per-prompt.video 0 --max-model-len 10000 ``` Fails with the following error despite the fact that upstream `flash-attn` would suppo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3VL doesn't recognise upstream `flash-attn` bug;stale ### Your current environment Tested on latest `main` (c9f66da8fdd0a082cd451cecfb7848bb287bf251). ### 🐛 Describe the bug Qwen3VL fails to use upstream `fla...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3VL doesn't recognise upstream `flash-attn` bug;stale ### Your current environment Tested on latest `main` (c9f66da8fdd0a082cd451cecfb7848bb287bf251). ### 🐛 Describe the bug Qwen3VL fails to use upstream `fla...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
