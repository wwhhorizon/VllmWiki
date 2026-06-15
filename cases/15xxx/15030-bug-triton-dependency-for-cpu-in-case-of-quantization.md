# vllm-project/vllm#15030: [Bug]: Triton Dependency for CPU in case of Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#15030](https://github.com/vllm-project/vllm/issues/15030) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton Dependency for CPU in case of Quantization

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are in process of implementing w8a8 compressed tensor for IBM Power and during the testing process the following error is encountered ``` INFO 03-18 04:41:03 [__init__.py:256] Automatically detected platform cpu. INFO 03-18 04:41:10 [config.py:583] This model supports multiple tasks: {'embed', 'classify', 'reward', 'score', 'generate'}. Defaulting to 'generate'. INFO 03-18 04:41:10 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available. Traceback (most recent call last): File "/home/akashk/vllm_int8/vllm_latest/vllm/examples/offline_inference/granite_int8.py", line 7, in llm = LLM(model=model_name, tensor_parallel_size=tp_size, max_model_len=max_model_len, trust_remote_code=True) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/akashk/miniconda3/envs/vllm_oob/lib/python3.11/site-packages/vllm-0.8.0rc2.dev3+gdd3b8658.d20250318.cpu-py3.11-linux-ppc64le.egg/vllm/utils.py", line 1031, in inner return fn(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^ File "/home/akashk/miniconda3/envs/vllm_oob/lib/python3.11/site-package...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Triton Dependency for CPU in case of Quantization bug ### Your current environment ### 🐛 Describe the bug We are in process of implementing w8a8 compressed tensor for IBM Power and during the testing process the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Triton Dependency for CPU in case of Quantization bug ### Your current environment ### 🐛 Describe the bug We are in process of implementing w8a8 compressed tensor for IBM Power and during the testing process the...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: zation/gguf.py", line 13, in from vllm.model_executor.layers.fused_moe.fused_moe import moe_align_block_size File "/home/akashk/miniconda3/envs/vllm_oob/lib/python3.11/site-packages/vllm-0.8.0rc2.dev3+gdd3b8658.d2025031...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: init__.py:256] Automatically detected platform cpu. INFO 03-18 04:41:10 [config.py:583] This model supports multiple tasks: {'embed', 'classify', 'reward', 'score', 'generate'}. Defaulting to 'generate'. INFO 03-18 04:4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
