# vllm-project/vllm#33175: [Bug]: Mistral-Small-3.1-24B crashes on startup

| 字段 | 值 |
| --- | --- |
| Issue | [#33175](https://github.com/vllm-project/vllm/issues/33175) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mistral-Small-3.1-24B crashes on startup

### Issue 正文摘录

### Your current environment Current main `492a7983d` ``` uv pip show transformers mistral-common Name: mistral-common Version: 1.8.8 Location: /home/NickLucche/vllm/.venv/lib/python3.12/site-packages Requires: jsonschema, numpy, pillow, pydantic, pydantic-extra-types, requests, tiktoken, typing-extensions Required-by: vllm --- Name: transformers Version: 4.57.1 Location: /home/NickLucche/vllm/.venv/lib/python3.12/site-packages Requires: filelock, huggingface-hub, numpy, packaging, pyyaml, regex, requests, safetensors, tokenizers, tqdm Required-by: compressed-tensors, vllm, vllm-bart-plugin, xgrammar ``` ### 🐛 Describe the bug ```python vllm serve RedHatAI/Mistral-Small-3.1-24B-Instruct-2503-FP8-dynamic --enforce-eager . . . (EngineCore_DP0 pid=937908) File "/home/NickLucche/vllm/vllm/transformers_utils/processor.py", line 128, in get_processor (EngineCore_DP0 pid=937908) processor = processor_cls.from_pretrained( (EngineCore_DP0 pid=937908) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=937908) File "/home/NickLucche/vllm/.venv/lib64/python3.12/site-packages/transformers/processing_utils.py", line 1396, in from_pretrained (EngineCore_DP0 pid=937908) return cls.from_args_and_d...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Mistral-Small-3.1-24B crashes on startup bug ### Your current environment Current main `492a7983d` ``` uv pip show transformers mistral-common Name: mistral-common Version: 1.8.8 Location: /home/NickLucche/vllm/....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e/NickLucche/vllm/.venv/lib/python3.12/site-packages Requires: filelock, huggingface-hub, numpy, packaging, pyyaml, regex, requests, safetensors, tokenizers, tqdm Required-by: compressed-tensors, vllm, vllm-bart-plugin,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ges Requires: jsonschema, numpy, pillow, pydantic, pydantic-extra-types, requests, tiktoken, typing-extensions Required-by: vllm --- Name: transformers Version: 4.57.1 Location: /home/NickLucche/vllm/.venv/lib/python3.1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a7983d` ``` uv pip show transformers mistral-common Name: mistral-common Version: 1.8.8 Location: /home/NickLucche/vllm/.venv/lib/python3.12/site-packages Requires: jsonschema, numpy, pillow, pydantic, pydantic-extra-ty...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: e bug ```python vllm serve RedHatAI/Mistral-Small-3.1-24B-Instruct-2503-FP8-dynamic --enforce-eager . . . (EngineCore_DP0 pid=937908) File "/home/NickLucche/vllm/vllm/transformers_utils/processor.py", line 128, in get_p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
