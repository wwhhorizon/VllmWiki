# vllm-project/vllm#39540: [Bug]: Can't instantiate a local model if importing torch_geometric

| 字段 | 值 |
| --- | --- |
| Issue | [#39540](https://github.com/vllm-project/vllm/issues/39540) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't instantiate a local model if importing torch_geometric

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Importing [pytorch_geometric](https://github.com/pyg-team/pytorch_geometric) causes the engine to fail loading a local model: ```python import vllm import torch_geometric vllm.LLM( model='meta-llama/Llama-3.1-8B-Instruct', max_model_len=2048, # Have to limit this otherwise the model won't fit into my GPU ) ``` I did try changing the order of the imports, but got the same results. I also did set the following variables: ``` export VLLM_LOGGING_LEVEL=DEBUG export VLLM_TRACE_FUNCTION=1 ``` Here's the output: ``` DEBUG 04-10 18:40:08 [plugins/__init__.py:36] No plugins for group vllm.platform_plugins found. DEBUG 04-10 18:40:08 [platforms/__init__.py:37] Checking if TPU platform is available. DEBUG 04-10 18:40:08 [platforms/__init__.py:56] TPU platform is not available because: No module named 'libtpu' DEBUG 04-10 18:40:08 [platforms/__init__.py:62] Checking if CUDA platform is available. DEBUG 04-10 18:40:08 [platforms/__init__.py:85] Confirmed CUDA platform is available. DEBUG 04-10 18:40:08 [platforms/__init__.py:113] Checking if ROCm platform is available. DEBUG 04-10 18:40:08 [platforms/__init__.py:127] ROCm platform is not avai...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Can't instantiate a local model if importing torch_geometric bug ### Your current environment ### 🐛 Describe the bug Importing [pytorch_geometric](https://github.com/pyg-team/pytorch_geometric) causes the engine...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: 04-10 18:40:14 [config/model.py:1743] Generative models support chunked prefill. DEBUG 04-10 18:40:14 [config/model.py:1801] Generative models support prefix caching. DEBUG 04-10 18:40:14 [engine/arg_utils.py:2116] Enab...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Can't instantiate a local model if importing torch_geometric bug ### Your current environment ### 🐛 Describe the bug Importing [pytorch_geometric](https://github.com/pyg-team/pytorch_geometric) causes the engine...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: med 'libtpu' DEBUG 04-10 18:40:08 [platforms/__init__.py:62] Checking if CUDA platform is available. DEBUG 04-10 18:40:08 [platforms/__init__.py:85] Confirmed CUDA platform is available. DEBUG 04-10 18:40:08 [platforms/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
