# vllm-project/vllm#22376: [Bug]: Model architectures ['GptOssForCausalLM'] failed to be inspected.

| 字段 | 值 |
| --- | --- |
| Issue | [#22376](https://github.com/vllm-project/vllm/issues/22376) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model architectures ['GptOssForCausalLM'] failed to be inspected.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This issue is similar to: https://huggingface.co/openai/gpt-oss-20b/discussions/12 I run the following code: ``` uv pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 \ --index-strategy unsafe-best-match pip install transformers -U vllm serve /root/autodl-tmp/openai/gpt-oss-120b --served-model-name Llama3.3 --gpu-memory-utilization 0.92 --trust-remote-code --max-model-len 65536 --host 0.0.0.0 --port 6006 ``` And I got the following output: INFO 08-07 01:36:04 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=111587) INFO 08-07 01:36:07 [api_server.py:1787] vLLM API server version 0.10.2.dev2+gf5635d62e.d20250806 (APIServer pid=111587) INFO 08-07 01:36:07 [utils.py:326] non-default args: {'model_tag': '/root/autodl-tmp/openai/gpt-oss-120b', 'host': '0.0.0.0', 'port': 6006, 'model': '/root/autodl-tmp/openai/gpt-oss-120b', 'trust_remote_code': True, 'max_model_len': 65536, 'served_model_name': ['Llama3.3'], 'gpu_memory_utilization': 0.92} (APIServer pid=111587) The argument `trust_remote_code` is to be used...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: /openai/gpt-oss-20b/discussions/12 I run the following code: ``` uv pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Model architectures ['GptOssForCausalLM'] failed to be inspected. bug;stale ### Your current environment ### 🐛 Describe the bug This issue is similar to: https://huggingface.co/openai/gpt-oss-20b/discussions/12 I...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: Server pid=111587) ERROR 08-07 01:36:12 [registry.py:415] from ..ops.triton.rotary import apply_rotary # modified from original (APIServer pid=111587) ERROR 08-07 01:36:12 [registry.py:415] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Model architectures ['GptOssForCausalLM'] failed to be inspected. bug;stale ### Your current environment ### 🐛 Describe the bug This issue is similar to: https://huggingface.co/openai/gpt-oss-20b/discussions/12 I...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ls. [type=value_error, input_value=ArgsKwargs((), {'model': ...attention_dtype': None}), input_type=ArgsKwargs] (APIServer pid=111587) For further information visit https://errors.pydantic.dev/2.12/v/value_error ### Bef...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
