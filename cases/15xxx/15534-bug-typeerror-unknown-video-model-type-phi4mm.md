# vllm-project/vllm#15534: [Bug]: `TypeError: Unknown video model type: phi4mm`

| 字段 | 值 |
| --- | --- |
| Issue | [#15534](https://github.com/vllm-project/vllm/issues/15534) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `TypeError: Unknown video model type: phi4mm`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Step to reproduce ```bash vllm serve microsoft/Phi-4-multimodal-instruct --trust-remote-code ``` Run example ``` cd examples/online_serving python openai_chat_completion_client_for_multimodal.py -c "video" ``` It will throw the error: ``` ... ERROR 03-26 08:20:13 [serving_chat.py:204] File "/app/Quark/aiter-int8-linear/vllm/entrypoints/chat_utils.py", line 461, in _place holder_str ERROR 03-26 08:20:13 [serving_chat.py:204] raise TypeError(f"Unknown {modality} model type: {model_type}") ERROR 03-26 08:20:13 [serving_chat.py:204] TypeError: Unknown video model type: phi4mm /app/Quark/aiter-int8-linear/vllm/entrypoints/openai/serving_chat.py:205: RuntimeWarning: coroutine 'MediaConnector.fetch_video_asyn c' was never awaited return self.create_error_response(str(e)) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization cuda;quantization;triton build_error dtype;env_dependency #43505 B...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: `TypeError: Unknown video model type: phi4mm` bug;stale ### Your current environment ### 🐛 Describe the bug # Step to reproduce ```bash vllm serve microsoft/Phi-4-multimodal-instruct --trust-remote-code ``` Run e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: : ``` ... ERROR 03-26 08:20:13 [serving_chat.py:204] File "/app/Quark/aiter-int8-linear/vllm/entrypoints/chat_utils.py", line 461, in _place holder_str ERROR 03-26 08:2
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: pment ci_build;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization cuda;quantization;triton build_error dtype;env_dependency #43505 Bump the minor-update group across 1 directory with 145 updates | #4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 145 updates | Fix image URLs in <code>index.md</code>. PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15534">#15534</a> by <a href="https://github.com/YuriiMotov"><code>@​YuriiMoto |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 147 updates | Fix image URLs in <code>index.md</code>. PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15534">#15534</a> by <a href="https://github.com/YuriiMotov"><code>@​YuriiMoto |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
