# vllm-project/vllm#28572: [Bug]: vllm refuses to serve LLM in the presence of multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#28572](https://github.com/vllm-project/vllm/issues/28572) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm refuses to serve LLM in the presence of multiple GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm fails to serve gpt-oss-20b model on the machine with RTX 3090 (NVIDIA compute capability 8.6), because it is confused by the presence of RTX 2080 TI (NVIDIA compute capability 7.5) and fails with the following error: ``` (vllm) $ uv run --with vllm vllm serve openai/gpt-oss-20b INFO 11-12 17:39:23 [__init__.py:216] Automatically detected platform cuda. WARNING 11-12 17:39:23 [cuda.py:619] Detected different devices in the system: NVIDIA GeForce RTX 2080 Ti, NVIDIA GeForce RTX 3090. Please make sure to set `CUDA_DEVICE_ORDER=PCI_BUS_ID` to avoid unexpected behavior. (APIServer pid=4172) INFO 11-12 17:39:26 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer pid=4172) INFO 11-12 17:39:26 [utils.py:233] non-default args: {'model_tag': 'openai/gpt-oss-20b', 'model': 'openai/gpt-oss-20b'} (APIServer pid=4172) INFO 11-12 17:39:27 [model.py:547] Resolved architecture: GptOssForCausalLM (APIServer pid=4172) `torch_dtype` is deprecated! Use `dtype` instead! Parse safetensors files: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00 (APIServer...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Your current environment ### 🐛 Describe the bug vllm fails to serve gpt-oss-20b model on the machine with RTX 3090 (NVIDIA compute capability 8.6), because it is confused by the presence of RTX 2080 TI (NVIDIA compute c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Ti, NVIDIA GeForce RTX 3090. Please make sure to set `CUDA_DEVICE_ORDER=PCI_BUS_ID` to avoid unexpected behavior. (APIServer pid=4172) INFO 11-12 17:39:26 [api_server.py:1839] vLLM API server version 0.11.0 (APIServer p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 47] Resolved architecture: GptOssForCausalLM (APIServer pid=4172) `torch_dtype` is deprecated! Use `dtype` instead! Parse safetensors files: 100%|█████████████████████████████████████████████████████████████████████████...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: cribe the bug vllm fails to serve gpt-oss-20b model on the machine with RTX 3090 (NVIDIA compute capability 8.6), because it is confused by the presence of RTX 2080 TI (NVIDIA compute capability 7.5) and fails with the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: entrypoints/cli/main.py", line 54, in main (APIServer pid=4172) args.dispatch_function(args) (APIServer pid=4172) File "/home/tigran/vllm/.venv/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 57, in cm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
