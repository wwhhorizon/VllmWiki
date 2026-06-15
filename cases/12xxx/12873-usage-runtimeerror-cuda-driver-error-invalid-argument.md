# vllm-project/vllm#12873: [Usage]: RuntimeError: CUDA driver error: invalid argument

| 字段 | 值 |
| --- | --- |
| Issue | [#12873](https://github.com/vllm-project/vllm/issues/12873) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;gemm_linear;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;operator |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: RuntimeError: CUDA driver error: invalid argument

### Issue 正文摘录

### Your current environment ```text [rank0]: File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl [rank0]: return forward_call(*args, **kwargs) [rank0]: File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 382, in forward [rank0]: output_parallel = self.quant_method.apply(self, input_, bias) [rank0]: File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 142, in apply [rank0]: return F.linear(x, layer.weight, bias) [rank0]: RuntimeError: CUDA driver error: invalid argument [rank0]:[W207 07:21:42.794850618 ProcessGroupNCCL.cpp:1250] Warning: WARNING: process group has NOT been destroyed before we destruct ProcessGroupNCCL. On normal program exit, the application should call destroy_process_group to ensure that any pending NCCL operations have finished in this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTorch 2.4 (function operator()) ``` load model bash is ```python llm = LLM(model=model_name, dtype...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: y ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched fo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ers/linear.py", line 382, in forward [rank0]: output_parallel = self.quant_method.apply(self, input_, bias) [rank0]: File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 142, in appl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: RuntimeError: CUDA driver error: invalid argument usage ### Your current environment ```text [rank0]: File "/opt/conda/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl [rank0]:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: **kwargs) [rank0]: File "/opt/conda/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 382, in forward [rank0]: output_parallel = self.quant_method.apply(self, input_, bias) [rank0]: File "/opt/con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
