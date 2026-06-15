# vllm-project/vllm#15345: [Bug]: misleading regex with `--tokenizer-mode mistral` `OSError`

| 字段 | 值 |
| --- | --- |
| Issue | [#15345](https://github.com/vllm-project/vllm/issues/15345) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: misleading regex with `--tokenizer-mode mistral` `OSError`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am hitting this `OSError` with `--tokenizer_mode mistral`: ```none OSError: Found 0 files matching the pattern: re.compile('^tokenizer\\.model\\.v.*$|^tekken\\.json$|^tokenizer\\.mm\\.model\\.v.*$'). Make sure that a Mistral tokenizer is present in ['config.json', 'generation_config.json', 'model-00001-of-00010.safetensors', 'model-00002-of-00010.safetensors', 'model-00003-of-00010.safetensors', 'model-00004-of-00010.safetensors', 'model-00005-of-00010.safetensors', 'model-00006-of-00010.safetensors', 'model-00007-of-00010.safetensors', 'model-00008-of-00010.safetensors', 'model-00009-of-00010.safetensors', 'model-00010-of-00010.safetensors', 'model.safetensors.index.json', 'params.json', 'special_tokens_map.json', 'tokenizer.json', 'tokenizer_config.json']. ``` The [actual regex](https://github.com/vllm-project/vllm/blob/refs/tags/v0.8.1/vllm/transformers_utils/tokenizers/mistral.py#L122-L124) is ```python ^tokenizer\.model\.v.*$|^tekken\.json$|^tokenizer\.mm\.model\.v.*$ ``` But the error message has `\\` in the regex, which means something different. In other words, can we have this `OSError` message to display the correct r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: _mode mistral`: ```none OSError: Found 0 files matching the pattern: re.compile('^tokenizer\\.model\\.v.*$|^tekken\\.json$|^tokenizer\\.mm\\.model\\.v.*$'). Make sure that a Mistral tokenizer is present in ['config.json...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ex? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ne OSError: Found 0 files matching the pattern: re.compile('^tokenizer\\.model\\.v.*$|^tekken\\.json$|^tokenizer\\.mm\\.model\\.v.*$'). Make sure that a Mistral tokenizer is present in ['config.json', 'generation_config...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _parallel;frontend_api;hardware_porting;model_support cuda;gemm;operator;triton build_error env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ld;distributed_parallel;frontend_api;hardware_porting;model_support cuda;gemm;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
