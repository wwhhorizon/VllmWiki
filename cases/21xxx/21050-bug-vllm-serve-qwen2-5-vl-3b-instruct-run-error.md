# vllm-project/vllm#21050: [Bug]: vllm serve Qwen2.5-VL-3B-Instruct  run error

| 字段 | 值 |
| --- | --- |
| Issue | [#21050](https://github.com/vllm-project/vllm/issues/21050) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;moe;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve Qwen2.5-VL-3B-Instruct  run error

### Issue 正文摘录

### Your current environment vllm==0.9.2 transformers==4.53.2 torch 2.6 ### 🐛 Describe the bug command: vllm serve Qwen2.5-VL-3B-Instruct INFO 07-16 22:41:06 [__init__.py:244] Automatically detected platform cuda. INFO 07-16 22:41:09 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-16 22:41:09 [cli_args.py:325] non-default args: {'model': 'Qwen2.5-VL-3B-Instruct'} ERROR 07-16 22:41:17 [registry.py:379] Error in inspecting model architecture 'Qwen2_5_VLForConditionalGeneration' ERROR 07-16 22:41:17 [registry.py:379] Traceback (most recent call last): ERROR 07-16 22:41:17 [registry.py:379] File "/lib/python3.12/site-packages/vllm/model_executor/models/registry.py", line 610, in _run_in_subprocess ERROR 07-16 22:41:17 [registry.py:379] returned.check_returncode() ERROR 07-16 22:41:17 [registry.py:379] File "/lib/python3.12/subprocess.py", line 502, in check_returncode ERROR 07-16 22:41:17 [registry.py:379] raise CalledProcessError(self.returncode, self.args, self.stdout, ERROR 07-16 22:41:17 [registry.py:379] subprocess.CalledProcessError: Command '['/bin/python', '-m', 'vllm.model_executor.models.registry']' returned non-zero exit status 1. ERROR 07-16 22:41:17 [registry.p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: platform cuda. INFO 07-16 22:41:09 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-16 22:41:09 [cli_args.py:325] non-default args: {'model': 'Qwen2.5-VL-3B-Instruct'} ERROR 07-16 22:41:17 [registry.py:379] Er...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ROR 07-16 22:41:17 [registry.py:379] from vllm.model_executor.layers.quantization.gptq_marlin import ( ERROR 07-16 22:41:17 [registry.py:379] File "/lib/python3.12/site-packages/vllm/model_executor/layers/quantization/g...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vllm serve Qwen2.5-VL-3B-Instruct run error bug;stale ### Your current environment vllm==0.9.2 transformers==4.53.2 torch 2.6 ### 🐛 Describe the bug command: vllm serve Qwen2.5-VL-3B-Instruct INFO 07-16 22:41:06...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ale: Optional[torch.Tensor] = None, bias: Optional[torch.Tensor] = None, cutlass_block_fp8_supported: bool = False, use_aiter_and_is_supported: bool = False) -> torch.Tensor) ERROR 07-16 22:41:17 [registry.py:379] Trace...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ct INFO 07-16 22:41:06 [__init__.py:244] Automatically detected platform cuda. INFO 07-16 22:41:09 [api_server.py:1395] vLLM API server version 0.9.2 INFO 07-16 22:41:09 [cli_args.py:325] non-default args: {'model': 'Qw...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
