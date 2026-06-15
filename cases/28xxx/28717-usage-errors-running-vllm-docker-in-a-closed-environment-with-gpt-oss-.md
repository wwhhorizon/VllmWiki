# vllm-project/vllm#28717: [Usage]: Errors running vLLM docker in a closed environment with gpt-oss-120b on RTX 6000 Pro

| 字段 | 值 |
| --- | --- |
| Issue | [#28717](https://github.com/vllm-project/vllm/issues/28717) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Errors running vLLM docker in a closed environment with gpt-oss-120b on RTX 6000 Pro

### Issue 正文摘录

### Your current environment Can't get vLLM to start with the below configuration. Seems to have issues loading in the model .safetensors. Any ideas on what could be causing it? vllm version: 0.11.1 CPU: Intel Xeon w7-2595X GPU: NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition Model: https://huggingface.co/openai/gpt-oss-120b/tree/main Command: docker run --rm --name vllm --gpus=all --runtime=nvidia -p 8000:8000 -e HF_HUB_OFFLINE=1 --ipc=host -v opt/models/cache/:/root/.cache/huggingface/hub vllm/vllm-openai:latest --model openai/gpt-oss-120b Also tried: docker run --rm --name vllm --gpus=all --runtime=nvidia -p 8000:8000 -e HF_HUB_OFFLINE=1 --ipc=host -v opt/models/cache/:/root/.cache/huggingface/hub vllm/vllm-openai:latest --model openai/gpt-oss-120b with the same output. Output: INFO 11-12 06:23:18 [__init__.py:216] Automatically detected platform cuda. [1;36m(APIServer pid=1)[0;0m INFO 11-12 06:23:21 [api_server.py:1839] vLLM API server version 0.11.0 [1;36m(APIServer pid=1)[0;0m INFO 11-12 06:23:21 [utils.py:233] non-default args: {'model': 'openai/gpt-oss-120b'} [1;36m(APIServer pid=1)[0;0m INFO 11-12 06:23:21 [arg_utils.py:504] HF_HUB_OFFLINE is True, replace m...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: e8f754692c1647ca79fbf85e8c1e70f8a] [1;36m(APIServer pid=1)[0;0m `torch_dtype` is deprecated! Use `dtype` instead! [1;36m(APIServer pid=1)[0;0m INFO 11-12 06:23:26 [model.py:547] Resolved architecture: GptOssForCausa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Usage]: Errors running vLLM docker in a closed environment with gpt-oss-120b on RTX 6000 Pro usage;stale ### Your current environment Can't get vLLM to start with the below configuration. Seems to have issues loading i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Usage]: Errors running vLLM docker in a closed environment with gpt-oss-120b on RTX 6000 Pro usage;stale ### Your current environment Can't get vLLM to start with the below configuration. Seems to have issues loading i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: M docker in a closed environment with gpt-oss-120b on RTX 6000 Pro usage;stale ### Your current environment Can't get vLLM to start with the below configuration. Seems to have issues loading in the model .safetensors. A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='openai_gptoss'), obse...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
