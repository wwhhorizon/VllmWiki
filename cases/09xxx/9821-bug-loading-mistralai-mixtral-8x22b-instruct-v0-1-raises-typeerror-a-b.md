# vllm-project/vllm#9821: [Bug]: Loading mistralai/Mixtral-8x22B-Instruct-v0.1 raises TypeError: a bytes-like object is required, not 'str'

| 字段 | 值 |
| --- | --- |
| Issue | [#9821](https://github.com/vllm-project/vllm/issues/9821) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Loading mistralai/Mixtral-8x22B-Instruct-v0.1 raises TypeError: a bytes-like object is required, not 'str'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to serve [mistralai/Mixtral-8x22B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) in a single-node with 8 GPUs I get the error below: ```sh VLLM_LOGGING_LEVEL=DEBUG python -m vllm.entrypoints.openai.api_server \ --model mistralai/Mixtral-8x22B-Instruct-v0.1 \ --tensor-parallel-size 8 \ --tokenizer-mode="mistral" ... INFO 10-29 22:43:58 multiproc_worker_utils.py:120] Killing local vLLM worker processes DEBUG 10-29 22:43:58 client.py:170] Waiting for output from MQLLMEngine. Process SpawnProcess-1: Traceback (most recent call last): File "/opt/conda/lib/python3.10/site-packages/vllm/worker/model_runner_base.py", line 116, in _wrapper return func(*args, **kwargs) File "/opt/conda/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 1658, in execute_model hidden_or_intermediate_states = model_executable( File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl return self._call_impl(*args, **kwargs) File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl return forward_call(*args, **kwargs...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r environment) or with the snippet below: ```python from vllm.platforms import current_platform print(current_platform) current_platform.get_device_name().replace(" ", "_") ``` ```python $ python Python 3.10.15 | packag...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ug When trying to serve [mistralai/Mixtral-8x22B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) in a single-node with 8 GPUs I get the error below: ```sh VLLM_LOGGING_LEVEL=DEBUG python -m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: fused_moe/layer.py", line 474, in forward final_hidden_states = self.quant_method.apply( File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/layers/quantization/fp8.py", line 495, in apply return fused_exp...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: /mixtral.py", line 244, in forward hidden_states = self.block_sparse_moe(hidden_states) File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl return self._call_impl(...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tform) >>> name = current_platform.get_device_name() >>> name b'NVIDIA A100-SXM4-80GB' >>> name.replace(" ", "_") Traceback (most recent call last): File " ", line 1, in TypeError: a bytes-like object is required, not '...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
