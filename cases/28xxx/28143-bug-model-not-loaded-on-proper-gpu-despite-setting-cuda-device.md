# vllm-project/vllm#28143: [Bug]: Model not loaded on proper GPU despite setting CUDA device

| 字段 | 值 |
| --- | --- |
| Issue | [#28143](https://github.com/vllm-project/vllm/issues/28143) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model not loaded on proper GPU despite setting CUDA device

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have two GPUs, and vLLM will only attempt to run models via GPU 0 regardless of the command. ```bash CUDA_VISIBLE_DEVICES=0 vllm serve "openai/gpt-oss-120b" --tool-call-parser openai --enable-auto-tool-choice ``` ```bash CUDA_VISIBLE_DEVICES=1 vllm serve "deepseek-ai/DeepSeek-R1-Distill-Llama-70B" --tool-call-parser openai --enable-auto-tool-choice ``` Here is the full error output: ```bash /home/localadmin/Documents/vllm/.venv/lib/python3.10/site-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. import pynvml # type: ignore[import] INFO 11-05 12:19:23 [__init__.py:216] Automatically detected platform cuda. (APIServer pid=12336) INFO 11-05 12:19:25 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=12336) INFO 11-05 12:19:25 [utils.py:233] non-default args: {'model_tag': 'deepseek-ai/DeepSeek-R1-Distill-Llama-70B', 'enable_auto_tool_choice': True, 'tool_call_parser': 'openai', 'model': 'deepseek-ai/DeepSeek-R1-Distill-L...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: /__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 47] Resolved architecture: LlamaForCausalLM (APIServer pid=12336) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=12336) INFO 11-05 12:19:26 [model.py:1510] Using max model len 131072 (APIServer pid=123...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Model not loaded on proper GPU despite setting CUDA device bug;stale ### Your current environment ### 🐛 Describe the bug I have two GPUs, and vLLM will only attempt to run models via GPU 0 regardless of the comma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Model not loaded on proper GPU despite setting CUDA device bug;stale ### Your current environment ### 🐛 Describe the bug I have two GPUs, and vLLM will only attempt to run models via GPU 0 regardless of the comma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
