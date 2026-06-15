# vllm-project/vllm#19502: [Bug]: ValueError: rope_scaling on loading Llama 3.1 AWQ models with vLLM v0.5.1

| 字段 | 值 |
| --- | --- |
| Issue | [#19502](https://github.com/vllm-project/vllm/issues/19502) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: rope_scaling on loading Llama 3.1 AWQ models with vLLM v0.5.1

### Issue 正文摘录

### Your current environment When attempting to load a quantized version of the new meta-llama/Meta-Llama-3.1-70B-Instruct model (e.g., hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4), the server fails during model configuration loading. The config.json for Llama 3.1 uses a new rope_scaling dictionary format that is not understood by the version of transformers library used in the vllm:v0.5.1 release. docker run --rm --runtime=nvidia --gpus all \ -e HUGGING_FACE_HUB_TOKEN= \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ vllm/vllm-openai:v0.5.1 \ --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 \ --trust-remote-code \ --quantization awq \ --tensor-parallel-size 2 Environment: vLLM Version: 0.5.1 (from vllm/vllm-openai:v0.5.1 Docker image) GPU: 2x NVIDIA RTX A6000 NVIDIA Driver Version: 560.35.03 CUDA Version: 12.6 I have tried latest vllm also same error ### 🐛 Describe the bug When attempting to load a quantized version of the new meta-llama/Meta-Llama-3.1-70B-Instruct model (e.g., hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4), the server fails during model configuration loading. The config.json for Llama 3.1 uses a new rope_scaling dictio...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ;stale ### Your current environment When attempting to load a quantized version of the new meta-llama/Meta-Llama-3.1-70B-Instruct model (e.g., hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4), the server fails durin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: ValueError: rope_scaling on loading Llama 3.1 AWQ models with vLLM v0.5.1 bug;stale ### Your current environment When attempting to load a quantized version of the new meta-llama/Meta-Llama-3.1-70B-Instruct model...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: v0.5.1 bug;stale ### Your current environment When attempting to load a quantized version of the new meta-llama/Meta-Llama-3.1-70B-Instruct model (e.g., hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4), the server f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ersion: 0.5.1 (from vllm/vllm-openai:v0.5.1 Docker image) GPU: 2x NVIDIA RTX A6000 NVIDIA Driver Version: 560.35.03 CUDA Version: 12.6 I have tried latest vllm also same error ### 🐛 Describe the bug When attempting to l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Error: rope_scaling on loading Llama 3.1 AWQ models with vLLM v0.5.1 bug;stale ### Your current environment When attempting to load a quantized version of the new meta-llama/Meta-Llama-3.1-70B-Instruct model (e.g., hugg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
