# vllm-project/vllm#42281: [Bug]: EXAONE 4.5 import fails: Exaone4_5_ImageProcessor missing in transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#42281](https://github.com/vllm-project/vllm/issues/42281) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EXAONE 4.5 import fails: Exaone4_5_ImageProcessor missing in transformers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Unable to serve EXAONE-4.5-33B Model due to following error. vLLM tries to import `Exaone4_5_ImageProcessor` from transformers, which does not exist. ``` (APIServer pid=287) ERROR 05-11 14:35:35 [registry.py:912] Error in inspecting model architecture 'Exaone4_5_ForConditionalGeneration' (APIServer pid=287) ERROR 05-11 14:35:35 [registry.py:912] Traceback (most recent call last): (APIServer pid=287) ERROR 05-11 14:35:35 [registry.py:912] File "/usr/local/lib/python3.12/site-packages/vllm/model_executor/models/registry.py", line 1336, in _run_in_subprocess (APIServer pid=287) ERROR 05-11 14:35:35 [registry.py:912] returned.check_returncode() (APIServer pid=287) ERROR 05-11 14:35:35 [registry.py:912] File "/usr/local/lib/python3.12/subprocess.py", line 502, in check_returncode (APIServer pid=287) ERROR 05-11 14:35:35 [registry.py:912] raise CalledProcessError(self.returncode, self.args, self.stdout, (APIServer pid=287) ERROR 05-11 14:35:35 [registry.py:912] subprocess.CalledProcessError: Command '['/usr/local/bin/python3', '-m', 'vllm.model_executor.models.registry']' returned non-zero exit status 1. (APIServer pid=287) ERROR 05-11...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: EXAONE 4.5 import fails: Exaone4_5_ImageProcessor missing in transformers bug ### Your current environment ### 🐛 Describe the bug Unable to serve EXAONE-4.5-33B Model due to following error. vLLM tries to import...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: id=287) ERROR 05-11 14:35:35 [registry.py:912] Error in inspecting model architecture 'Exaone4_5_ForConditionalGeneration' (APIServer pid=287) ERROR 05-11 14:35:35 [registry.py:912] Traceback (most recent call last): (A...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;import_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t environment ### 🐛 Describe the bug Unable to serve EXAONE-4.5-33B Model due to following error. vLLM tries to import `Exaone4_5_ImageProcessor` from transformers, which does not exist. ``` (APIServer pid=287) ERROR 05...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;import_error;nan_in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
